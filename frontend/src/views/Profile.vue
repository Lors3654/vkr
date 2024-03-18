<template>
  <div class="container" >
    <div class="row">
      <div class="col-lg-4">
        <!-- Прячем колонку с навигацией для маленького экрана -->
        <div class="row d-none d-lg-block">
          <!-- Наваигация -->
          <ul class="nav flex-column">
            <li class="nav-item" style="margin-top:30px;">
              <router-link class="nav-link" to="/profile" aria-label="Profile page">MY ACCOUNT
                <svg class="icon">
                  <use xlink:href="../assets/styles/sprite.svg#profile"></use>
                </svg>
              </router-link>
            </li>
            <li class="nav-item" style="margin-top:50px;">
              <router-link class="nav-link" to="/categories" aria-label="Categories page">BOHEMIN COLLECTION</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/search" aria-label="Search page">SEARCH   
                <svg class="icon">
                  <use xlink:href="../assets/styles/sprite.svg#search"></use>
                </svg>
              </router-link> 
            </li>
          </ul>
        </div>
      </div>
      <div class="col-lg-8 mt-5">
        <form>
          <div class="row pb-5" id="myData">
            <b>MY INFORMATION</b>
            <div class="form-group mt-4 mb-3">
              <label for="name">NAME</label>
              <input type="name" class="form-control" id="name" name="name" disabled>
            </div>
            <div class="form-outline mb-3">
              <label for="name">LASTNAME</label>
              <input type="lastname" class="form-control" id="lastname" name="lastname" disabled>
            </div>
            <div class="form-outline mb-3">
              <label for="birthday">BIRTHDAY</label>
              <input type="birthday" class="form-control" id="birthday" name="birthday" disabled>
            </div>
            <div class="form-outline mb-3">
              <label for="phone">PHONE NUMBER </label>
              <input type="tel" class="form-control" id="phone" name="phone" disabled>
            </div>
            <div class="form-outline mb-4">
              <label for="password">PASSWORD</label>
              <input type="password" class="form-control" id="password1" name="password1" placeholder="Password" required v-model="password1">
            </div> 
            <div class="justify-content">
              <button type="submit" class="w-100 btn btn-dark btn-sm mb-5"><small>EDIT</small></button>
            </div>
            <div class="justify-content mt-5">
              <button @click="logout()" type="submit" class="w-100 btn btn-dark btn-sm mb-5"><small>LOG OUT</small></button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
  
<script>
  import axios from 'axios'

  export default {
    name: 'Profile',
    methods: {
      async logout() {
        await axios
          .post('/auth/token/logout/')
          .then(response => {
            console.log('Logged out')
          })
          .catch(error => {
            console.log(JSON.stringify(error))
          })  

        axios.defaults.headers.common['Authorization'] = ''
        localStorage.removeItem('token')
        this.$store.commit('removeToken')
        
        this.$router.push('/')
      }
    }
  } 
</script>