import { createRouter, createWebHistory } from 'vue-router'
import store from '@/store'
import SignUp from '@/views/SignUp.vue'
import Main from '@/views/Main.vue'
import SignIn from '@/views/SignIn.vue'
import Categories from '@/views/Categories.vue'
import Dresses from '@/views/Dresses.vue'
import Shirts from '@/views/Shirts.vue'
import Skirts from '@/views/Skirts.vue'
import Search from '@/views/Search.vue'
import Profile from '@/views/Profile.vue'
import Cart from '@/views/Cart.vue'
import Favorites from '@/views/Favorites.vue'


const routes = [
  {
    path: '/',
    name: 'Main',
    component: Main
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/sign-in',
    name: 'SignIn',
    component: SignIn
  },
  {
    path: '/categories',
    name: 'Categories',
    component: Categories
  },
  {
    path: '/dresses',
    name: 'Dresses',
    component: Dresses
  },
  {
    path: '/shirts',
    name: 'Shirts',
    component: Shirts
  },
  {
    path: '/skirts',
    name: 'Skirts',
    component: Skirts
  },
  {
    path: '/search',
    name: 'Search',
    component: Search
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/cart',
    name: 'Cart',
    component: Cart,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/favorites',
    name: 'Favorites',
    component: Favorites,
    meta: {
      requireLogin: true
    }
  },
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next('/sign-in')
  } else {
    next()
  }
}) 

export default router
