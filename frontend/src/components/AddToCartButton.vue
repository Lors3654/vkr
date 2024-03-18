<template>
  <button class="position-absolute bottom-0 m-3 ms-1 btn-sm btn-lg custom-button" type="button" @click="addToCart">
    <svg class="icon">
      <use xlink:href="@/assets/styles/sprite.svg#bag"></use>
    </svg>
  </button>
</template>

<script>
export default {
  name: 'AddToCartButton',
  methods: {
    addToCart() {
      // Logic to add product to cart
    },
  },
};
</script>