<template>
  <div class="container">
    <div class="row">
      <div class="col-lg-3">
        <NavigationMain />
      </div>
      <div class="col-lg-9 mt-5 main-content">
        <img src="../assets/IMG_1148.gif" class="background-image" alt="main">
      </div>
    </div>
  </div>
</template>

<script>
  import NavigationMain from '@/components/NavigationMain.vue';

  export default {
    name: 'Main',
    components: {
      NavigationMain
    }
  } 
</script>


<style scoped>
  .container {
    position: relative; 
  }

  .main-content {
    min-height: 100vh; 
  }

  .background-image {
    width: 100%;
    height: 900px;
    object-fit: cover;
  }
</style>