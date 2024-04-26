<template>
  <div class="container">
    <div class="row">
      <div class="col-lg-4">
        <NavigationMain />
      </div>
      <div class="col-lg-8 mt-5">
        <form class="d-flex mt-3" @submit.prevent="performSearch">
          <input class="input" type="text" placeholder="SEARCH" aria-label="Search" autocomplete="off" v-model="query" style="width: 100%;">
          <button class="btn btn-outline-dark rectangular-button" type="submit">
            <svg class="icon">
              <use xlink:href="../assets/styles/sprite.svg#search"></use>
            </svg>
          </button>
        </form>
        <div class="container mt-5" v-if="products.length > 0">
          <h4 class="title-h4 mb-4">Were you looking for "{{ query }}"?</h4>
          <div class="row row-cols-2 row-cols-sm-2 row-cols-md-2 row-cols-lg-2 g-5">
            <div class="col" v-for="(product, index) in products" :key="product.id">
              <product-box :product="product"/>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
      
<script>
import NavigationMain from '@/components/NavigationMain.vue';
import ProductBox from '@/components/ProductBox.vue';
import axios from 'axios';

export default {
  name: 'Search',
  components: {
    NavigationMain,
    ProductBox
  },
  data() {
    return {
      products: [],
      query: '',
    }
  },
  methods: {
    async performSearch() {
      try {
        const response = await axios.get('/api/v1/search/', { params: { q: this.query } })
        console.log('Search API response:', response.data)
        this.products = response.data.flatMap(category => category.products)
                                        .filter(product => product.product_name.toLowerCase().includes(this.query.toLowerCase()) || 
                                                          product.description.toLowerCase().includes(this.query.toLowerCase()))
        console.log('Filtered products:', this.products)
      } catch (error) {
        console.error('Error fetching search results:', error)
        this.products = []
      }
    }
  },
}
</script>
