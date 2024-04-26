<template>
    <div class="row d-none d-lg-block">
      <!-- Наваигация -->
      <ul class="nav flex-column">
        <li class="nav-item" style="margin-top:50px;">
          <router-link class="nav-link" to="/profile" aria-label="Profile page">MY ACCOUNT
            <svg class="icon">
              <use xlink:href="../assets/styles/sprite.svg#profile"></use>
            </svg>
          </router-link>
        </li>
        <li class="nav-item" >
          <router-link class="nav-link" to="/cart" aria-label="Cart page">CART</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" to="/favorites" aria-label="Favorites page">FAVORITES</router-link>
        </li>
        <li class="nav-item" style="margin-top:30px;">
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
    name: 'NavigationAuth',
  }
</script>