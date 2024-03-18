<template>
  <div class="container" >
    <div class="row">
      <div class="col-lg-4">
        <NavigationCategory />
      </div>
      <div class="col-lg-8 mt-5">
        <div class="row row-cols-2 row-cols-sm-2 row-cols-md-2 row-cols-lg-2 g-5">
          <div class="col" v-for="(product, index) in products" :key="index">
            <div class="card mb-3">              
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

  import { toast } from 'bulma-toast'
  
  export default {
    name: 'Dresses',
    components: {
      NavigationCategory,
      ProductCarousel,
      AddToCartButton,
      AddToFavoritesButton,
    },
    methods: {
      addToCart() {
        const item = {
          product: this.product,
        }
        this.$store.commit('addToCart', item)
        toast({
          message: 'The product was added to the cart',
          type: 'is-success',
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: 'bottom-right',
        })
      }
    },
    data() {
      return {
        products: [
          {
            name: 'Silk Maxi Dress with Long Flared Sleeves',
            price: '1270 AED',
            images: [
              require('@/assets/images/prof/images for page with dresses/photo_2022-10-08_00-46-16.jpg'),
              require('@//assets/images/prof/images for page with dresses/silk_grey_dress2.jpg'),
            ],
          },
          {
            name: 'Maxi Sleeveless Milk Dress',
            price: '890 AED',
            images: [
              require('@/assets/images/prof/images for page with dresses/photo_2022-10-08_00-46-13.jpg'),
              require('@/assets/IMG_1.gif'),
            ],
          },
          {
            name: 'Purple Dress',
            price: '1300 AED',
            images: [
              require('@/assets/images/prof/images for page with dresses/photo_2022-10-08_00-46-28.jpg'),
              require('@/assets/images/prof/images for page with dresses/perple_dress_2.jpg'),
              require('@/assets/images/prof/images for page with dresses/perple_dress_3.jpg'),
            ],
          },
          {
            name: 'Midnight Blue Knitted Fabric Dress',
            price: '1500 AED',
            images: [
              require('@/assets/images/prof/images for page with dresses/photo_2022-10-08_00-46-34 — копия.jpg'),
              require('@/assets/images/prof/images for page with dresses/blue_dress2.jpg'),
            ],
          },
          {
            name: 'Grey Sillk Dress',
            price: '1450 AED',
            images: [
              require('@/assets/images/prof/images for page with dresses/photo_2022-10-08_00-46-14.jpg'),
              require('@/assets/images/prof/images for page with dresses/maxi_grey_dress2.jpg'),
              require('@/assets/images/prof/images for page with dresses/maxi_grey_dress3.jpg'),
            ],
          },
          {
            name: 'Sleeveless Dress',
            price: '760 AED',
            images: [
              require('@/assets/images/prof/images for page with dresses/photo_2022-10-08_00-46-37 — копия.jpg'),
              require('@/assets/images/prof/images for page with dresses/sleeveless_dress2.jpg'),
              require('@/assets/images/prof/images for page with dresses/sleeveless_dress3.jpg'),
            ],
          },
        ]
      }
    },
  }

</script>