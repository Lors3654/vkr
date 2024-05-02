<template>
  <div class="row d-none d-lg-block">
    <!-- Наваигация -->
    <ul class="nav flex-column">
      <li class="nav-item" style="margin-top:50px;">
        <router-link 
          :class="{'nav-link':true, 'sidebar-link': true, 'active': isCurrentRoute('/categories') }" 
          to="/categories" aria-label="Categories page">
          <strong v-if="isCurrentRoute('/categories')">BOHEMIN COLLECTION</strong>
          <span v-else>BOHEMIN COLLECTION</span>
        </router-link>
      </li>
      <template v-if="!$store.state.isAuthenticated">
        <li class="nav-item" style="margin-top:50px;">
          <router-link 
            :class="{'nav-link': true, 'sidebar-link': true, 'active': isCurrentRoute('/sign-up') }" 
            to="/sign-up" aria-label="SignUp page">
            <strong v-if="isCurrentRoute('/sign-up')">SIGN IN/REGISTER</strong>
            <span v-else>SIGN IN/REGISTER</span>
          </router-link>
        </li>
      </template>
      <template v-else >
        <li class="nav-item mt-3">
          <router-link class="nav-link" to="/cart" aria-label="Cart page">CART</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" to="/favorites" aria-label="Favorites page">FAVORITES</router-link>
        </li>
        <li class="nav-item mt-3">
        <router-link class="nav-link" to="/profile" aria-label="Profile page">MY ACCOUNT
          <svg class="icon">
            <use xlink:href="../assets/styles/sprite.svg#profile"></use>
          </svg>
        </router-link>
      </li>
      </template>
      <li class="nav-item mt-3">
        <router-link 
          :class="{'nav-link': true, 'sidebar-link': true, 'active': isCurrentRoute('/search') }" 
          to="/search" aria-label="Search page">
          <strong v-if="isCurrentRoute('/search')">SEARCH</strong>
          <span v-else>SEARCH</span>
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
    name: 'NavigationMain',
    methods: {
      isCurrentRoute(route) {
        return this.$route.path === route;
      }
    }
  }
</script>

<!-- <style>
  .nav-pills .nav-link.active{
    color: initial;
    background-color: initial;
  }
</style> -->