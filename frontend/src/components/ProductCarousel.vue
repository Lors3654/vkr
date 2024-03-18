<template>
  <div class="card">
    <div :id="carouselId" class="carousel slide carousel-fade">
      <div class="carousel-inner">
        <div v-for="(image, index) in images" :key="index" :class="{ 'carousel-item': true, active: index === 0 }">
          <img :src="image" class="card-img-top d-block w-100" :alt="'Image ' + (index + 1)">
          <div>
            <add-to-cart-button @click="addToCart" />
          </div>
          <div>
            <add-to-favorites-button @click="addToFavorites" />
          </div>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" :data-bs-target="`#${carouselId}`" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" :data-bs-target="`#${carouselId}`" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>
</template>

<script>
import AddToCartButton from '@/components/AddToCartButton.vue';
import AddToFavoritesButton from '@/components/AddToFavoritesButton.vue';

export default {
  name: 'ProductCarousel',
  components: {
    AddToCartButton,
    AddToFavoritesButton,
  },
  props: {
    images: {
      type: Array,
      required: true,
    },
  },
  computed: {
    carouselId() {
      return `carousel-${Math.random().toString(36).substr(2, 9)}`;
    },
  },
  methods: {
    addToCart() {
      // Логика добавления в корзину
    },
    addToFavorites() {
      // Логика добавления в избранное
    },
  },
};
</script>
