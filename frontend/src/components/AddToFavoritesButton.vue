<template>
  <button class="position-absolute top-0 end-0 m-2 ms-1 btn-sm btn-lg custom-button" type="button" @click="addToFavorites">
    <svg class="icon">
      <use xlink:href="../assets/styles/sprite.svg#heart"></use>
    </svg>
  </button>
</template>
  
<script>
export default {
  name: 'AddToFavoritesButton',
  methods: {
    addToFavorites() {
      // Logic to add product to favorites
    },
  },
};
</script>