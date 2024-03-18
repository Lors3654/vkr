<template>
    <div class="row d-none d-lg-block">
      <!-- Наваигация -->
      <ul class="nav nav-pills flex-column" style="margin-top:30px;" id="menu">
        <li class="sidebar-item">
          <router-link class="nav-link sidebar-link collapsed has-dropdown" to="/categories" data-bs-toggle="collapse" data-bs-target="#categories" aria-label="Categories page" aria-expanded="false"><strong>BOHEMIN COLLECTION/</strong></router-link>         
          <ul id="categories" class="sidebar-dropdown list-unstyled collapse"  data-bs-parent="#sidebar">
            <li class="sidebar-item">
              <router-link 
                :class="{ 'nav-link': true, 'sidebar-link': true, 'active': isCurrentRoute('/dresses') }" 
                to="/dresses" aria-label="Dresses page">
                <strong v-if="isCurrentRoute('/dresses')">/DRESSES/</strong>
                <span v-else>/DRESSES/</span>
              </router-link>
            </li>
            <li>
              <router-link 
                :class="{ 'nav-link': true, 'sidebar-link': true, 'active': isCurrentRoute('/shirts') }" 
                to="/shirts" aria-label="Shirts page">
                <strong v-if="isCurrentRoute('/shirts')">/SHIRTS/</strong>
                <span v-else>/SHIRTS/</span>
              </router-link>
            </li>
            <li>
              <router-link 
                :class="{ 'nav-link': true, 'sidebar-link': true, 'active': isCurrentRoute('/skirts') }" 
                to="/skirts" aria-label="Skirts page">
                <strong v-if="isCurrentRoute('/skirts')">/SKIRTS/</strong>
                <span v-else>/SKIRTS/</span>
              </router-link>
            </li>
          </ul>
        </li>
        <li class="nav-item" style="margin-top:50px;">
          <router-link class="nav-link" to="/sign-in" aria-label="SignIn page">SIGN IN/REGISTER</router-link>
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
    name: 'NavigationCategory',
    methods: {
      isCurrentRoute(route) {
        return this.$route.path === route;
      }
    }
  }
</script>
  
<style>
  .nav-pills .nav-link.active{
    color: initial;
    background-color: initial;
  }
</style>