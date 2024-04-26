<template>
  <div class="container">
    <div class="row">
      <div class="col-lg-4">
        <NavigationCategory />
      </div>
      <div class="col-lg-8 mt-5">
        <Filter :products="products" />
        <div class="row row-cols-2 row-cols-sm-2 row-cols-md-2 row-cols-lg-2 g-5">
          <div class="col" v-for="product in products" :key="product.id">
            <product-box :product="product" @add-to-cart="addToCart" />
          </div>
        </div>
        <div v-if="showAlert" class="alert alert-secondary cart-notification" role="alert">
          The product was added to the cart!
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavigationCategory from '@/components/NavigationCategory.vue';
import Filter from '@/components/Filter.vue';
import ProductBox from '@/components/ProductBox.vue';
import axios from 'axios';

export default {
  name: 'Products',
  components: {
    NavigationCategory,
    Filter,
    ProductBox
  },
  data() {
    return {
      products: [],
      quantity: 1,
      showAlert: false
    }
  },
  mounted() {
    this.getProducts(),
    console.log('Product:', this.products)
  },
  watch: {
    $route(to, from) {
      if (to.name === 'Product') {
        this.getProducts()
      }
    }
  },
  methods: {
    async getProducts() {
      const category_slug = this.$route.params.category_slug;

      try {
        const response = await axios.get(`/api/v1/categories/${category_slug}/`);
        this.products = response.data;
        console.log('Products:', this.products);
      } catch (error) {
        console.log('Error fetching products:', error);
      }
    },
    addToCart(product) {
      console.log("Received product:", product);
      if (isNaN(this.quantity) || this.quantity < 1) {
        this.quantity = 1
      }

      const item = {
        product: product,
        quantity: this.quantity
      }

      this.$store.commit('addToCart', item)

      this.showAlert = true

      setTimeout(() => {
        this.showAlert = false
      }, 3000)

      console.log("Product:", JSON.stringify(product));
      console.log('Quantity:', this.quantity)
    },
    addToFavorites(product) {
      const item = { product: product };
      this.$store.commit('addToFavorites', item)
    },
  },
}
</script>
