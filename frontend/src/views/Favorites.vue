<template>
  <div class="container" >
    <div class="row">
      <div class="col-lg-4">
        <NavigationCartFav />
      </div>
      <div class="col-lg-8 mt-5">
        <div class="row row-cols-2">
          <div class="col">
            <div class="text-center my-auto">
              <router-link class="nav-link" to="/Cart" aria-label="Cart page" style="color: gray;">CART</router-link>
            </div>
          </div>
          <div class="col">
            <div class="text-center my-auto">
              <router-link class="nav-link" to="/favorites" aria-label="Favorites page">FAVORITES</router-link>
            </div>
          </div>
        </div>
        <hr class="wishlist-line" style="margin-top: 5px;">
      </div>
    </div>
  </div>
</template>

<script>
  import NavigationCartFav from '@/components/NavigationCartFav.vue';
  
  export default {
    name: 'Favorites',
    components: {
      NavigationCartFav
    },
    methods: {
      isCurrentRoute(route) {
        return this.$route.path === route;
    }
  }
} 
</script>