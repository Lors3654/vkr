<template>
  <div class="container" >
    <div class="row">
      <div class="col-lg-4">
        <navigation-main />
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
  import NavigationMain from '@/components/NavigationMain.vue';

  export default {
    name: 'Categories',
    components: {
      NavigationMain
    }
  } 
</script>