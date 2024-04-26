<template>
  <div class="card mb-3">
    <div :id="carouselId" class="carousel slide carousel-fade">
      <div class="carousel-inner">
        <!-- Основное изображение -->
        <div class="carousel-item active">
          <img :src="product.image" class="d-block w-100" :alt="product.product_name">
          <div>
            <!-- кнопка добавления в корзину -->
            <button class="position-absolute bottom-0 m-3 ms-1 btn-sm btn-lg custom-button" aria-label="cart_bottom" type="button" @click="addToCart()">
              <svg class="icon">
                <use xlink:href="@/assets/styles/sprite.svg#bag"></use>
              </svg>
            </button>
            <!-- кнопка добавления в избранное -->
            <button class="position-absolute top-0 end-0 m-2 ms-1 btn-sm btn-lg custom-button" aria-label="favorite_bottom" type="button" @click="addToFavorites()">
              <svg class="icon">
                <use xlink:href="../assets/styles/sprite.svg#heart"></use>
              </svg>
            </button>
          </div>
        </div>
        <!-- Дополнительные изображения из product_images -->
        <div v-for="(image, imageIndex) in product.product_images" :key="imageIndex" class="carousel-item">
          <img :src="image.images" class="d-block w-100" :alt="'Image ' + (imageIndex + 1)">
          <div>
            <!-- кнопка добавления в корзину -->
            <button class="position-absolute bottom-0 m-3 ms-1 btn-sm btn-lg custom-button" aria-label="cart_bottom" type="button" @click="addToCart()">
              <svg class="icon">
                <use xlink:href="@/assets/styles/sprite.svg#bag"></use>
              </svg>
            </button>
            <!-- кнопка добавления в избранное -->
            <button class="position-absolute top-0 end-0 m-2 ms-1 btn-sm btn-lg custom-button" aria-label="favorite_bottom" type="button" @click="addToFavorites()">
              <svg class="icon">
                <use xlink:href="../assets/styles/sprite.svg#heart"></use>
              </svg>
            </button>
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
    <div class="card-body">
      <h5 class="title-h6 text-center">{{ product.description }}</h5>
      <p class="title-carddes card-text text-center">{{ product.price }} AED</p>
    </div>
  </div>
</template>


<script>
export default {
  name: 'ProductBox',
  props: {
    product: {
      type: Object,
      required: true
    },
  },
  computed: {
    carouselId() {
      return `carousel-${this.product.id}`
    },
  },
  methods: {
    addToCart() {
      // Вызываем событие для добавления в корзину
      this.$emit('add-to-cart', { product: this.product, quantity: 1 });
    }
  }
}
</script>
