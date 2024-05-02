<template>
  <div class="container">
    <div class="row">
      <div class="col-lg-4">
        <NavigationMain />
      </div>
      <div class="col-lg-8 mt-5">
        <div class="container">
          <div class="row">
            <hr class="mt-4">
            <div class="text-center lh-base mt-5 mb-5">
              <p class="title-h4">Dear customer, We are delighted to inform you that we have received your order and it has been accepted for processing. </p>
              <p class="title-h4">We will contact you shortly to confirm the details of your order. </p> 
              <p class="title-h4">Thank you for choosing our products and services. We look forward to serving you. </p>
              <p class="title-h4">Best regards, Bohemin!</p>
            </div>  
            <hr>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
  
<script>
  import NavigationMain from '@/components/NavigationMain.vue';

  export default {
    name: 'Success',
    components: {
      NavigationMain
    },
  }
</script>

<style>
.footer {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
}
</style>