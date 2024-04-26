<template>
  <div class="container" >
    <div class="row">
      <div class="col-lg-4">
        <navigation-main />
      </div>
      <div class="col-lg-8 mt-5">
        <form @submit.prevent="submitForm">
          <div class="form-outline mb-4">
            <label for="username">USERNAME</label>
            <input type="username" class="form-control" id="username" name="username" placeholder="Your UserName" v-model="username">
          </div>
          <div class="form-outline mb-4">
            <label for="name">NAME</label>
            <input type="name" class="form-control" id="name" name="name" placeholder="Your Name" v-model="name">
          </div>
          <div class="form-outline mb-4">
            <label for="latname">LAST NAME</label>
            <input type="lastname" class="form-control" id="lastname" name="lastname" placeholder="Your Last Name" v-model="lastname">
          </div>
          <div class="form-outline mb-4">
            <label for="phone">PHONE NUMBER</label>
            <input type="tel" class="form-control" id="phone" name="phone" placeholder="Enter your phone" v-model="phone">
          </div>
          <div class="form-outline mb-4">
            <label for="password">PASSWORD</label>
            <input type="password" class="form-control" id="password1" name="password1" placeholder="Password" v-model="password1">
          </div> 
          <div class="form-outline mb-4">
            <label for="password">REPEAT PASSWORD</label>
            <input type="password" class="form-control" id="password2" name="password2" placeholder="Confirm password" v-model="password2">
          </div> 
          <div class="alert alert-danger" role="alert" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>
          <div class="form-outline mb-2">
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="" id="checkbox" checked>
              <label class="form-check-label" for="checkbox"><p>I agree to the processing of personal data</p></label>
            </div>
          </div>
          <div class="justify-content">
            <button type="submit" class="w-100 btn btn-dark btn-sm mb-5"><small>REGISTER</small></button>
          </div>
          <div class="text-center mb-5">
            <p>Are you a member?<router-link class="nav-link" to="/sign-in" aria-label="SignIn page"><u>Sig in</u></router-link></p>
          </div>
          <div v-if="successMessage" class="alert alert-success" role="alert">
            {{ successMessage }}
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
  import NavigationMain from '@/components/NavigationMain.vue'
  import axios from 'axios'
  import { parsePhoneNumber } from 'libphonenumber-js'

  export default {
    name: 'SignUp',
    components: {
      NavigationMain
    },
    data() {
      return {
        username: '',
        name: '',
        lastname: '',
        phone: '',
        password1: '',
        password2: '',
        errors: [],
        successMessage: ''
      }
    },
    methods: {
      validatePhoneNumber(phone) {
        try {
          const phoneNumber = parsePhoneNumber(phone)
          return phoneNumber.isValid()
        } catch (error) {
          console.error('Error parsing phone number:', error)
          return false
        }
      },
      async submitForm() {    
        this.errors = []
        if (!document.getElementById('checkbox').checked) {
          this.errors.push('You must agree to the processing of personal data');
        }
        if (!this.validatePhoneNumber(this.phone)) {
          this.errors.push('Invalid phone number');
        }
        if (this.password1 !== this.password2) {
          this.errors.push('The password are not matching')
        }
        if (!this.errors.length) {
          const formData = {
            username: this.username,
            name: this.name,
            lastname: this.lastname,
            phone: this.phone,
            password: this.password1
          }
          axios
            .post('/api/v1/users/', formData)
            .then(response => {
              this.successMessage = 'Account was created, please sign in'
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
        }
      }
    }
  } 
</script>