<template>
  <div class="container">
    <div class="row">
      <div class="col-lg-4">
        <NavigationMain />
      </div>
      <div class="col-lg-8">
        <div class="container">
          <div class="row">
            
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