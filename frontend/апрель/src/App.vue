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
  import axios from 'axios';
  import Navbar from '@/components/Navbar.vue';
  import Footer from '@/components/Footer.vue';
  
  export default {
    name: 'App',
    components: {
      Navbar,
      Footer
    },
    beforeCreate() {
      this.$store.commit('initializeStore')
      
      if (this.$store.state.token) {
        axios.defaults.headers.common['Authorization'] = "Token " + this.$store.state.token
      } else {
        axios.defaults.headers.common['Authorization'] = ""
      }
    },
  }
</script>

<style lang="scss">
@import '../node_modules/bootstrap/scss/bootstrap.scss';
@import '../src/assets/styles/style.css';
@import '../node_modules/bootstrap-icons/font/bootstrap-icons.css';
</style>
