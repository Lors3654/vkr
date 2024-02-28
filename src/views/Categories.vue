<template>
  <div class="container" >
    <div class="row">
      <div class="col-lg-4">
        <!-- Прячем колонку с навигацией для маленького экрана -->
        <div class="row d-none d-lg-block">
          <!-- Наваигация -->
          <ul class="nav flex-column">
            <li class="nav-item" style="margin-top:30px;">
              <router-link class="nav-link" to="/categories" aria-label="Categories page"><strong>BOHEMIN COLLECTION</strong></router-link>
            </li>
            <li class="nav-item" style="margin-top:50px;">
              <router-link class="nav-link" to="/sign-in" aria-label="SignIn page">SIGN IN/REGISTER</router-link>
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
      <div class="col-lg-8 mt-5">
        <!-- карточки с каталогом одежды -->
        <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3">
          <div class="col">
            <div class="card mb-4">
              <img src="../assets/images/prof/images for main page/photo_2022-10-08_00-46-11.jpg" class="card-img-top" alt="dress">
              <div class="card-body title-h6 text-center">
                <router-link class="nav-link" to="/dresses" aria-label="Dress page">Dresses</router-link>
              </div>
            </div>
          </div>
          <div class="col mb-4">
            <div class="card">
              <img src="../assets/images/prof/images for main page/photo_2022-10-08_00-46-26.jpg" class="card-img-top" alt="skirt">
              <div class="card-body title-h6 text-center">
                <router-link class="nav-link" to="/skirts" aria-label="Skirts page">Skirts</router-link>
              </div>
            </div>
          </div>
          <div class="col mb-4">
            <div class="card">
              <img src="../assets/images/prof/images for main page/photo_2022-10-08_00-46-35 — копия.jpg" class="card-img-top" alt="shirt">
              <div class="card-body title-h6 text-center">
                <router-link class="nav-link" to="/shirts" aria-label="Shirts page">Shirts</router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
    
<script>
  export default {
    name: 'Categories'
  } 
</script>