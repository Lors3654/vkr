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
              <router-link class="nav-link" to="/cart" aria-label="Cart page" style="color: gray;">CART ({{ cartTotalLength }})</router-link>
            </div>
          </div>
          <div class="col">
            <div class="text-center my-auto">
              <router-link class="nav-link" to="/favorites" aria-label="Favorites page">FAVORITES</router-link>
            </div>
          </div>
        </div>
        <hr class="wishlist-line" style="margin-top: 5px;">
        <div class="row row-cols-2 row-cols-sm-2 row-cols-md-2 row-cols-lg-3 g-5">
          <div class="col" v-for="favorite in favorites" :key="favorite.id">
            <div class="card mt-3 mb-3">
              <img :src="getFullImagePath(favorite.product.image)" class="d-block w-100" :alt="favorite.product.product_name || 'Product Image'">
              <button class="position-absolute bottom-0 end-0 mb-6 btn-sm btn-lg custom-button" aria-label="favorite_bottom" type="button" @click="removeFromFavorites(favorite.id)">
                <svg class="icon">
                  <use xlink:href="../assets/styles/sprite.svg#remove"></use>
                </svg>
              </button>
              <div class="card-body">
                <h5 class="title-h6 text-center">{{ favorite.product.description }}</h5>
                <p class="title-carddes card-text text-center">{{ favorite.product.price }} AED</p>
              </div>
            </div>
          </div>
        </div>
        <div v-if="showAlert" class="alert alert-secondary cart-notification" role="alert">
          The product hass been removed!
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import NavigationCartFav from '@/components/NavigationCartFav.vue';
  import axios from 'axios';
  import { mapGetters } from 'vuex';

  export default {
    name: 'Favorites',
    components: {
      NavigationCartFav,
    },
    data() {
      return {
        favorites: [],
        showAlert: false
      }
    },
    computed: {
      ...mapGetters({
        cartTotalLength: 'cartTotalLength'
      })
    },
    mounted() {
      this.getFavoritesProducts()
    },
    methods: {
      async getFavoritesProducts() {
        axios.get('/api/v1/favorites/')
        .then(response => {
          console.log("Favorites data received:", response.data)
          this.favorites = response.data
        })
        .catch(error => {
          console.error('Error getting favorites:', error)
        })
      },
      getFullImagePath(relativePath) {
        const baseUrl = 'http://127.0.0.1:8000'
        return `${baseUrl}${relativePath}`
      },
      removeFromFavorites(favoriteId) {
        axios.delete(`/api/v1/favorites/${favoriteId}/`)
        .then(() => {
          this.favorites = this.favorites.filter(f => f.id !== favoriteId)
          
          this.showAlert = true

          setTimeout(() => {
            this.showAlert = false
          }, 3000)

        })
        .catch(error => {
          console.error('Error removing from favorites:', error)
          alert('Failed to remove from favorites')
        })
      },
      isCurrentRoute(route) {
        return this.$route.path === route
      },
    }
  } 
</script>
