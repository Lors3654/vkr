<template>
  <div class="container" >
    <div class="row">
      <div class="col-lg-4">
        <navigation-main />
      </div>
      <div class="col-lg-8 mt-5">
        <form @submit.prevent="submitForm">
          <div class="row">
            <div class="form-outline mb-4">
              <label for="name">USERNAME</label>
              <input type="usename" class="form-control" id="usename" name="username" placeholder="Your UserName" required v-model="username">
            </div>
            <div class="form-outline mb-4">
              <label class="form-label" for="password">PASSWORD</label>
              <input type="password" id="password" class="form-control" name="password" placeholder="Password" required v-model="password">
            </div>
            <div class="alert alert-danger" role="alert" v-if="errors.length">
              <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div>
            <div class="justify-content">
              <button type="submit" class="w-100 btn btn-dark btn-sm mb-5">SIGN IN</button>
            </div>
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
        password: '',
        errors: []
      }
    },
    methods: {
      async submitForm() {
        axios.defaults.headers.common['Authorization'] = ''
        localStorage.removeItem('token')
        const formData = {
          username: this.username,
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
      }
    }
  } 
</script>