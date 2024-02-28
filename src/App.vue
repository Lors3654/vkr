<template>
  <div>
    <Navbar />
    <section class="section">
      <router-view/>
    </section>
    <Footer />
  </div>
</template>

<script>
  import Navbar from '@/components/Navbar.vue';
  import Footer from '@/components/Footer.vue';
  export default {
    name: 'App',
    components: {
      Navbar,
      Footer
    }
  }
</script>

<style lang="scss">
@import '../node_modules/bootstrap/scss/bootstrap.scss';
@import '../src/assets/styles/style.css';
@import '../node_modules/bootstrap-icons/font/bootstrap-icons.css';
</style>
