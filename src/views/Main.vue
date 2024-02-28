<template>
  <main class="container">
    <div class="row">
      <div class="col-lg-4">
        <!-- Прячем колонку с навигацией для маленького экрана -->
        <div class="row d-none d-lg-block">
          <!-- Наваигация -->
          <ul class="nav flex-column">
            <li class="nav-item" style="margin-top:30px;">
              <router-link class="nav-link" to="/categories" aria-label="Categories page">BOHEMIN COLLECTION</router-link>
            </li>
            <li class="nav-item" style="margin-top:50px;">
              <router-link class="nav-link" to="/sign-up" aria-label="SignUp page">SIGN IN/REGISTER</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/search" aria-label="Search page">SEARCH   
                <svg class="icon">
                  <use xlink:href="../assets/styles/sprite.svg#search"></use>
                </svg></router-link> 
            </li>
          </ul>
        </div>
      </div>
      <div class="col-lg-8">
        <div class="container">
          <div class="row">
            <div class="col mt-3 text-center">
              <img src="../assets/IMG_1148.gif" class="img-fluid img-thumbnail" alt="main">
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
  export default {
    name: 'Main'
  } 
</script>