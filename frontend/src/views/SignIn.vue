<template>
  <div class="container" >
    <div class="row">
      <div class="col-lg-4">
        <navigation-main />
      </div>
      <div class="col-lg-8 mt-5">
        <!-- Typical sign in / login form with additional register buttons -->
        <form @submit.prevent="submitForm">
          <div class="row">
            <div class="form-outline mb-4">
              <label for="name">NAME</label>
              <input type="name" class="form-control" id="name" name="name" placeholder="Your Name" required v-model="username">
            </div>
            <!-- <div class="form-outline mb-4">
              <label class="form-label" for="phone">PHONE NUMBER</label>
              <input type="tel" id="phone" class="form-control" name="phone" placeholder="Enter your phone" required v-model="phone">
            </div> -->
            <div class="form-outline mb-4">
              <label class="form-label" for="password">PASSWORD</label>
              <input type="password" id="password" class="form-control" name="password" placeholder="Password" required v-model="password">
            </div>
            <div class="alert alert-danger" role="alert" v-if="errors.length">
              <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div>
            <!-- Submit button -->
            <div class="justify-content">
              <button type="submit" class="w-100 btn btn-dark btn-sm mb-5">SIGN IN</button>
            </div>
            <!-- Register buttons -->
            <div class="text-center mb-5">
              <p>Not a member?<router-link class="nav-link" to="/sign-up" aria-label="SignUp page"><u>Register</u></router-link></p>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
  
<script>
  import NavigationMain from '@/components/NavigationMain.vue'
  import axios from 'axios'

  export default {
    name: 'SignIn',
    components: {
      NavigationMain
    },
    data() {
      return {
        username: '',
        // phone: '',
        password: '',
        errors: []
      }
    },
    methods: {
      // validatePhoneNumber(phone) {
      //   // Регулярное выражение для проверки номера телефона
      //   const phoneRegex = /^\+?\d{1,3}[- ]?\d{1,14}$/;
      //   return phoneRegex.test(phone);
      // },

      async submitForm() {
        this.$store.commit('setIsLoading', true)

        // if (!this.validatePhoneNumber(this.phone)) {
        //   this.errors.push('Invalid phone number');
        // }

        axios.defaults.headers.common['Authorization'] = ''
        localStorage.removeItem('token')

        const formData = {
          username: this.username,
          // phone: this.phone,
          password: this.password
        }

        await axios
          .post('/api/v1/token/login/', formData)
          .then(response => {
            const token = response.data.auth_token

            this.$store.commit('setToken', token)

            axios.defaults.headers.common['Authorization'] = 'Token ' + token
            
            localStorage.setItem('token', token)
            
            this.$router.push('/profile')
          })
          .catch(error => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(`${property}: ${error.response.data[property]}`)
              }
            } else if (error.message) {
                this.errors.push('Something went wrong. Please try again!')
            }
          })
      
        this.$store.commit('setIsLoading', false)
      }
    }
  } 
</script>