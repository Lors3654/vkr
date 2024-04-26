<template>
  <header>
    <div class="container-lg mt-3">
      <div class="row">
        <!-- Navbar для маленького экрана -->
        <nav class="navbar navbar-expand-lg">
          <div class="container-fluid">
            <div class="d-flex justify-content-between align-items-center w-100">
              <router-link style="text-decoration: none; color: inherit" to="/" aria-label="Log">
                <h1 class="title-h1">BOHEMIN</h1>
              </router-link>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <i class="bi bi-list"></i>
              </button>
            </div>
          </div>
        </nav>
        <div class="collapse navbar-collapse mt-3 bg-body-tertiary" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link style="text-decoration: none; color: inherit" to="/categories" aria-label="Categories page">BOHEMIN COLLECTION</router-link>
          </li>
          <li class="nav-item pt-3">
            <template v-if="$store.state.isAuthenticated">
              <router-link class="nav-link" to="/cart" aria-label="Cart page">CART</router-link>
              <router-link class="nav-link" to="/favorites" aria-label="Favorites page">FAVORITES</router-link>
              <router-link class="nav-link" to="/profile" aria-label="Profile page">MY ACCOUNT
                <svg class="icon">
                  <use xlink:href="../assets/styles/sprite.svg#profile"></use>
                </svg>
              </router-link>
            </template>
            <template v-else>
              <router-link class="nav-link" to="/sign-up" aria-label="SignUp page">SIGN IN/REGISTER</router-link>
            </template>
          </li>
          <li class="nav-item mt-3">
            <router-link style="text-decoration: none; color: inherit" to="/search" aria-label="Search page">SEARCH
              <svg class="icon">
                <use xlink:href="../assets/styles/sprite.svg#search"></use>
              </svg>
            </router-link>
          </li>
        </ul>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
  import { onMounted } from 'vue';
  import { useRouter } from 'vue-router';

  export default {
    name: 'Navbar',
    setup() {
      const router = useRouter();
      // Закрывать меню при переходе по маршруту
      router.afterEach(() => {
        const navbar = document.querySelector('.navbar-collapse');
        if (navbar.classList.contains('show')) {
          navbar.classList.remove('show');
        } 
      });

      return {
        router
      };
    },
    mounted() {
      // Добавляем обработчик события для всех ссылок в меню
      const links = document.querySelectorAll('.navbar-nav .nav-link');
      links.forEach(link => {
        link.addEventListener('click', this.closeNavbar);
      });
    }
};
</script>