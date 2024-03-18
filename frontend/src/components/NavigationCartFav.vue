<template>
  <div class="row d-none d-lg-block">
    <!-- Наваигация -->
    <ul class="nav flex-column">
      <li v-if="isCurrentRoute('/Cart')" class="nav-item" style="margin-top:30px;">
        <router-link class="nav-link" to="/cart" aria-label="Cart page"><strong>CART</strong></router-link>
      </li>
      <li v-if="isCurrentRoute('/favorites')" class="nav-item" style="margin-top:30px;">
        <router-link class="nav-link" to="/favorites" aria-label="Favorites page"><strong>FAVORITES</strong></router-link>
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
</template>

<script>
  export default {
    name: 'NavigationCartFav',
    methods: {
      isCurrentRoute(route) {
        return this.$route.path === route;
      }
    }
  }
</script>
