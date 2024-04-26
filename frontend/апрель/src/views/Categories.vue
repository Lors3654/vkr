<template>
  <div class="container" >
    <div class="row">
      <div class="col-lg-4">
        <navigation-main />
      </div>
      <div class="col-lg-8 mt-5">
        <!-- карточки с каталогом одежды -->
        <div class="row row-cols-2 row-cols-lg-3">
          <div class="col mb-4" v-for="category in categories" :key="category.id">
            <div class="card">
              <img v-bind:src="category.image" class="card-img-top" :alt="category.name">
              <div class="card-body title-h6 text-center">
                <router-link :to="'/categories' + category.get_absolute_url" aria-label="Category page" class="nav-link">{{ category.name }}</router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
    
<script>
  import axios from 'axios'
  import NavigationMain from '@/components/NavigationMain.vue';

  export default {
    name: 'Categories',
    components: {
      NavigationMain
    },
    data() {
      return {
        categories: {},
      }
    },
    mounted() {
      this.getCategories()
    },
    watch: {
      $route(to, from) {
        if (to.name === 'Category') {
          this.getCategories()
        }
      }
    },
    methods: {
      async getCategories() {
        const categorySlug = this.$route.params.category_slug
        console.log('Category Slug:', categorySlug)
        try {
          const response = await axios.get(`/api/v1/${categorySlug}/`)
          this.categories = response.data
        } catch (error) {
          console.error('Error fetching categories:', error);
        }
      }
    }
  } 
</script>
