<template>
  <div class="row justify-content-start">
    <!-- Фильтр: сортировка по цене -->
    <div class="col-lg-4 col-md-4 col-sm-4 d-flex flex-row-reverse mt-2 mb-5">
      <select id="sortOrder" class="form-select form-select-sm custom-select-width" aria-label="sort"
              v-model="sortOrder" @change="sortProducts">
        <option disabled value="">Sort by Price</option>
        <option value="asc">Ascending</option>
        <option value="desc">Descending</option>
      </select>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Filter',
    props: {
      products: Array,
    },
    data() {
      return {
        sortOrder: '',
      }
    },
    methods: {
      sortProducts() {
        if (this.sortOrder === 'asc') {
          this.sortByPriceAscending()
        } else {
          this.sortByPriceDescending()
        }
      },
      sortByPriceAscending() {
        if (Array.isArray(this.products)) {
          this.products.sort((a, b) => parseFloat(a.price) - parseFloat(b.price))
        }
      },
      sortByPriceDescending() {
        if (Array.isArray(this.products)) {
          this.products.sort((a, b) => parseFloat(b.price) - parseFloat(a.price))
        }
      },
    },
  }
</script>

<style>
  @media (max-width: 576px) {
    .custom-select-width {
      width: 100px;
    }
  }
</style>