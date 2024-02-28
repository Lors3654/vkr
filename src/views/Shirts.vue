<template>
  <div class="container" >
    <div class="row">
      <div class="col-lg-4">
        <!-- Прячем колонку с навигацией для маленького экрана -->
        <div class="row d-none d-lg-block">
          <!-- Наваигация -->
          <ul class="nav nav-pills flex-column" style="margin-top:30px;" id="menu">
            <li class="sidebar-item">
              <router-link class="nav-link sidebar-link collapsed has-dropdown" to="/categories" data-bs-toggle="collapse" data-bs-target="#categories" aria-label="Categories page" aria-expanded="false"><strong>BOHEMIN COLLECTION/</strong></router-link>         
              <ul id="categories" class="sidebar-dropdown list-unstyled collapse"  data-bs-parent="#sidebar">
                <li class="sidebar-item"><router-link class="nav-link" to="/Dresses" aria-label="Dresses page"><strong>/SHIRTS/</strong></router-link></li>
                <li><router-link class="nav-link sidebar-link" to="/Shirts" aria-label="Shirts page">/DRESSES/</router-link></li>
                <li><router-link class="nav-link sidebar-link" to="/Skirts" aria-label="Skirts page">/SKIRTS/</router-link></li>
              </ul>
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
        <div class="row row-cols-1 row-cols-md-2 row-cols-lg-2 g-5">
          <div class="col">
            <div class="card mb-3">
              <img src="../assets/images/prof/images for page with shirts/photo_2022-10-08_00-46-35 — копия.jpg" class="card-img-top" alt="shoulder shirt">
              <div class="card-body">
                <h5 class="title-h6 text-center">Accent Shoulder Shirt</h5>
                <p class="title-carddes card-text text-center">540 AED</p>
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
    name: 'Shirts'
  } 
</script>