<template>
  <div class="container">
    <div class="row">
      <div class="col-lg-4">
        <NavigationMain />
      </div>
      <div class="col-lg-8">
        <div class="container">
          <div class="row">
            <div class="col mt-5 text-center">
              <img src="../assets/IMG_1148.gif" class="img-fluid img-thumbnail" alt="main">
            </div>
          </div>
        </div>
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

<!-- <style>
.footer {
  position: fixed; 
  bottom: 0; 
  left: 0; 
  width: 100%; 
}
</style> -->