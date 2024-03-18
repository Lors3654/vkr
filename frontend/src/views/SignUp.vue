<template>
  <div class="container" >
    <div class="row">
      <div class="col-lg-4">
        <navigation-main />
      </div>
      <div class="col-lg-8 mt-5">
        <!-- Typical sign up form with additional buttons -->
        <form @submit.prevent="submitForm">
          <div class="form-outline mb-4">
            <label for="name">NAME</label>
            <input type="name" class="form-control" id="name" name="name" placeholder="Your Name" required v-model="username">
          </div>
          <div class="form-outline mb-4">
            <label for="latname">LAST NAME</label>
            <input type="lastname" class="form-control" id="lastname" name="lastname" placeholder="Your Last Name" required v-model="lastname">
          </div>
          <div class="form-outline mb-4">
            <label for="birthday">BIRTHDAY</label>
            <input type="birthday" class="form-control" id="birthday" name="birthday" placeholder="DATE OF BIRTH (MM/DD/YYYY)" required v-model="birthday">
          </div>
          <div class="form-outline mb-4">
            <label for="phone">PHONE NUMBER</label>
            <input type="tel" class="form-control" id="phone" name="phone" placeholder="Enter your phone" required v-model="phone">
          </div>  
          <div class="form-outline mb-4">
            <label for="password">PASSWORD</label>
            <input type="password" class="form-control" id="password1" name="password1" placeholder="Password" required v-model="password1">
          </div> 
          <div class="form-outline mb-4">
            <label for="password">REPEAT PASSWORD</label>
            <input type="password" class="form-control" id="password2" name="password2" placeholder="Confirm password" required v-model="password2">
          </div> 
          <div class="alert alert-danger" role="alert" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>
          <div class="form-outline mb-2">
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="" id="example" checked>
              <label class="form-check-label" for="example"><p>I agree to the processing of personal data</p></label>
            </div>
          </div>
          <div class="justify-content">
            <button type="submit" class="w-100 btn btn-dark btn-sm mb-5"><small>REGISTER</small></button>
          </div>
          <!-- Register buttons -->
          <div class="text-center mb-5">
            <p>Are you a member?<router-link class="nav-link" to="/sign-in" aria-label="SignIn page"><u>Sig in</u></router-link></p>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
  import NavigationMain from '@/components/NavigationMain.vue'
  import axios from 'axios'
  import {toast} from 'bulma-toast'

  export default {
    name: 'SignUp',
    components: {
      NavigationMain
    },
    data() {
      return {
        username: '',
        lastname: '',
        birthday: '',
        phone: '',
        password1: '',
        password2: '',
        errors: []
      }
    },
    methods: {
      validatePhoneNumber(phone) {
        // Регулярное выражение для проверки номера телефона
        const phoneRegex = /^\+?\d{1,3}[- ]?\d{1,14}$/;
        return phoneRegex.test(phone);
      },
      async submitForm() {
        this.$store.commit('setIsLoading', true)
        this.errors = []

        if (!this.validatePhoneNumber(this.phone)) {
          this.errors.push('Invalid phone number');
        }

        if (this.password1 !== this.password2) {
          this.errors.push('The password are not matching')
        }
      
        if (!this.errors.length) {

          this.$store.commit('setIsLoading', true)

          const formData = {
            username: this.username,
            lastname: this.lastname,
            birthday: this.birthday,
            phone: this.phone,
            password: this.password1
          }
          
          axios
            .post('/api/v1/users/', formData)
            .then(response => {
              toast({
                message: 'Account was created, please sign in',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
              })

              this.$router.push('/sign-in')
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
  } 
</script>