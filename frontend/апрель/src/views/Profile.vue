<template>
  <div class="container" >
    <div class="row">
      <div class="col-lg-4">
        <NavAuth />
      </div>
      <div class="col-lg-8 mt-5">
        <div class="row row-cols-2">
          <div class="col">
            <div class="text-center my-auto">
              <router-link class="nav-link" to="/profile" aria-label="Profile page"><b>PERSONAL INFORMATION</b></router-link>
            </div>
          </div>
          <div class="col">
            <div class="text-center my-auto">
              <router-link class="nav-link" to="/orders" aria-label="Orders page"style="color: gray;">MY ORDERS</router-link>
            </div>
          </div>
        </div>
        <hr style="margin-top: 5px;">
        <form>
          <div class="row" id="myData">
            <div class="form-group mt-4 mb-3">
              <label for="name">USERNAME</label>
              <input type="username" class="form-control" id="username" name="username" v-model="user.username" :disabled="!isEditing">
            </div>
            <div class="form-group mb-4">
              <label for="name">NAME</label>
              <input type="name" class="form-control" id="name" name="name" v-model="user.name" :disabled="!isEditing">
            </div>
            <div class="form-outline mb-4">
              <label for="name">LASTNAME</label>
              <input type="lastname" class="form-control" id="lastname" name="lastname" v-model="user.lastname" :disabled="!isEditing">
            </div>
            <div class="form-outline mb-4">
              <label for="phone">PHONE NUMBER </label>
              <input type="tel" class="form-control" id="phone" name="phone" v-model="user.phone" :disabled="!isEditing">
            </div>
            <div class="justify-content" id="toastContainer">
                <button @click.prevent="toggleEdit" type="submit" class="w-100 btn btn-dark btn-sm mb-5"><small>{{ isEditing ? 'UPDATE' : 'EDIT' }}</small></button>
            </div>
            <div class="justify-content mt-5">
              <button @click="logout()" type="button" class="w-100 btn btn-dark btn-sm mb-5"><small>LOG OUT</small></button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
  
<script>
  import axios from 'axios'
  import NavAuth from '@/components/NavAuth.vue'

  export default {
    name: 'Profile',
    components: {
      NavAuth
    },
    data() {
      return {
        user: {},
        isEditing: false
      }
    },
    mounted() {
      this.fetchUserData()
    },
    methods: {
      async toggleEdit() {
        if (this.isEditing) {
          await this.saveUserData()
        } else {
          this.isEditing = true
        }
      },
      async saveUserData() {
        try {
          await axios.put(`/api/v1/users/${this.user.id}/`, this.user)

          this.isEditing = false

          // Bootstrap toast
          this.showToast('Your personal information was updated', 'bg-dark-subtle')
        } catch (error) {
          console.error('Error saving user data:', error)
          this.showToast('Error saving user data', 'bg-danger')
        }
      },
      async fetchUserData() {
        try {
          const response = await axios.get('/api/v1/current-user/')
          
          this.user = response.data

        } catch (error) {
          console.error('Error fetching user data:', error)
        }
      },
      async logout() {
        await axios
          .post('/api/v1/token/logout/')
          .then(response => {
            console.log('Logged out')
          })
          .catch(error => {
            if (error.response) {
              console.log(JSON.stringify(error.response.data))
            } else if (error.message) {
              console.log(JSON.stringify(error.message))
            } else {
              console.log(JSON.stringify(error))
            }
          })  
        axios.defaults.headers.common['Authorization'] = ''

        localStorage.removeItem('token')

        this.$store.commit('removeToken')

        this.$router.push('/')     
      },
      showToast(message, backgroundColor) {
        // Bootstrap toast
        const toastElement = document.createElement('div');
        toastElement.className = `toast show text-white ${backgroundColor}`;
        toastElement.setAttribute('role', 'alert');
        toastElement.setAttribute('aria-live', 'assertive');
        toastElement.setAttribute('aria-atomic', 'true');
        toastElement.innerHTML = `
          <div class="toast-body">${message}</div>
        `;
        // Append toast to container
        const toastContainer = document.getElementById('toastContainer');
        toastContainer.appendChild(toastElement);
        // Show toast
        setTimeout(() => {
          toastElement.classList.remove('show');
          setTimeout(() => {
            toastContainer.removeChild(toastElement);
          }, 1000);
        }, 2000);
      },
    }
  } 
</script>

