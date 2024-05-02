<template>
  <div class="container">
    <div class="row">
      <div class="col-lg-4">
        <NavigationCartFav />
      </div>
      <div class="col-lg-8 mt-5">
        <div class="row row-cols-2">
          <div class="col">
            <div class="text-center my-auto">
              <router-link class="nav-link" to="/cart" aria-label="Cart page">CART ({{ cartTotalLength }})</router-link>
            </div>
          </div>
          <div class="col">
            <div class="text-center my-auto">
              <router-link class="nav-link" to="/favorites" aria-label="Favorites page" style="color: gray;">FAVORITES</router-link>
            </div>
          </div>
        </div>
        <hr style="margin-top: 5px;">
        <div class="table-responsive mt-5">
          <table class="table table-hover" v-if="cartTotalLength">
            <thead>
              <tr>
                <th scope="col" class="product-thumb text-center">IMAGE</th>
                <th scope="col" class="product-inf text-center">INFORMATION</th>
                <th scope="col" class="product-quantity text-center">QUANTITY</th>
                <th scope="col" class="product-total-price text-center">TOTAL PRICE</th>
                <th scope="col" class="product-action text-center">ACTION</th>
              </tr>
            </thead>
            <tbody v-for="(item, index) in $store.state.cart.items" :key="index">
              <CartItem
                :initialItem="item"
                :index="index"
                @removeFromCart="removeFromCart"
              />
            </tbody>
            <tfoot>
              <tr>
                <td colspan="1" class="text-center"><strong>SUMMARY</strong></td>
                <td colspan="2" class="text-center"><strong>{{ cartTotalPrice.toFixed(2) }} AED</strong>, {{ cartTotalLength }} ITEMS</td>
                <td colspan="2" class="text-center"><router-link to="/cart/checkout" class="btn btn-dark btn-sm mt-3 mb-3">Proceed to checkout</router-link></td>
              </tr>
            </tfoot>
          </table>
          <h4 class="title-h4" v-else>
            YOU DON'T HAVE ANY PRODUCTS IN YOUR CART
          </h4>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavigationCartFav from '@/components/NavigationCartFav.vue';
import CartItem from '@/components/CartItem.vue';
import { mapGetters } from 'vuex';

export default {
  name: 'Cart',
  components: {
    NavigationCartFav,
    CartItem
  },
  props: {
    initialItem: Object
  },
  data() {
    return {
      cart: {
        items: []
      }
    }
  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  computed: {
    ...mapGetters([
      'cartTotalLength'
    ]),
    cartTotalPrice() {
      return this.cart.items.reduce((acc, curVal) => {
        if (curVal.product && curVal.product.product.price) {
          return acc += curVal.product.product.price * curVal.quantity
        } else {
          return acc
        }
      }, 0)
    },
  },
  methods: {
    removeFromCart(item) {
      if (item.product && item.product.product) {
        const itemId = item.product.product.id
        this.cart.items = this.cart.items.filter(i => i.product && i.product.product && i.product.product.id !== itemId)
      }
    },
    clearCart() {
      this.$store.commit('clearCart')
      window.location.reload() // Обновить страницу
    },
  },
}
</script>
