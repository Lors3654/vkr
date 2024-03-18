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
              <router-link class="nav-link" to="/cart" aria-label="Cart page">CART</router-link>
            </div>
          </div>
          <div class="col">
            <div class="text-center my-auto">
              <router-link class="nav-link" to="/favorites" aria-label="Favorites page"style="color: gray;">FAVORITES</router-link>
            </div>
          </div>
        </div>
        <hr style="margin-top: 5px;">
        <div class="table-responsive mt-5">
          <table class="table table-hover">
            <thead>
              <tr>
                <th scope="col" class="product-thumb text-center">IMAGE</th>
                <th scope="col" class="product-inf text-center">INFORMATION</th>
                <th scope="col" class="product-quantity text-center">QUANTITY</th>
                <th scope="col" class="product-total-price text-center">TOTAL PRICE</th>
                <th scope="col" class="product-action text-center">ACTION</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in cartItems" :key="item.id">
                <th scope="row">{{ item.images }}</th>
                <td class="product-thumb">{{ item.name }}</td>
                <td class="product-quantity">
                  <div class="input-group justify-content-center">
                    <button type="button" class="btn btn-outline-secondary btn-sm sub">-</button>
                    <div class="col-md-4">
                      <input type="text" class="form-control" value="1">
                    </div>
                    <button type="button" class="btn btn-outline-secondary btn-sm add">+</button>
                  </div>
                </td>
                <td class="product-total-price">{{ item.price }}</td>
                <td class="product-action">
                  <div class="input-group justify-content-center">
                    <button class="btn mx-auto justify-content-center" type="button">
                      <svg class="icon">
                        <use xlink:href="../assets/styles/sprite.svg#remove"></use>
                      </svg>
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
  </template>

  <script>
  import NavigationCartFav from '@/components/NavigationCartFav.vue';
  
  export default {
    name: 'Cart',
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