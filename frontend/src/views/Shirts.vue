<template>
  <div class="container" >
    <div class="row">
      <div class="col-lg-4">
        <NavigationCategory />
      </div>
      <div class="col-lg-8 mt-5">
        <div class="row row-cols-2 row-cols-2 row-cols-md-2 row-cols-lg-2 g-5">
          <div class="col" v-for="(product, index) in products" :key="index">
            <div class="card position-relative mb-3">
              <add-to-cart-button @click="addToCart(product)" />
              <add-to-favorites-button @click="addToFavorites(product)" />
              <product-carousel :images="product.images">
              </product-carousel>
              <div class="card-body">
                <h5 class="title-h6 text-center">{{ product.name }}</h5>
                <p class="title-carddes card-text text-center">{{ product.price }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
      
<script>
  import NavigationCategory from '@/components/NavigationCategory.vue';
  import ProductCarousel from '@/components/ProductCarousel.vue';
  import AddToCartButton from '@/components/AddToCartButton.vue';
  import AddToFavoritesButton from '@/components/AddToFavoritesButton.vue';

  export default {
    name: 'Shirts',
    components: {
      NavigationCategory,
      ProductCarousel,
      AddToCartButton,
      AddToFavoritesButton,
    },
    data() {
      return {
        products: [
          {
            name: 'Accent Shoulder Shirt',
            price: '540 AED',
            images: [
              require('@/assets/images/prof/images for page with shirts/photo_2022-10-08_00-46-35 — копия.jpg'),
              require('@/assets/images/prof/images for page with shirts/photo_2022-10-08_00-46-30.jpg'),
            ],
          },
        ]
      }
    }
  } 
</script>