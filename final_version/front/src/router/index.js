import { createRouter, createWebHistory } from 'vue-router'
import store from '@/store'

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Main',
      component: () => import('../views/Main.vue')
    },
    {
      path: '/sign-up/',
      name: 'SignUp',
      component: () => import('../views/SignUp.vue')
    },
    {
      path: '/sign-in/',
      name: 'SignIn',
      component: () => import('../views/SignIn.vue')
    },
    {
      path: '/:category_slug',
      name: 'Categories',
      component: () => import('../views/Categories.vue')
    },
    {
      path: '/categories/:category_slug',
      name: 'Products',
      component: () => import('../views/Products.vue')
    },
    {
      path: '/search/',
      name: 'Search',
      component: () => import('../views/Search.vue')
    },
    {
      path: '/profile/',
      name: 'Profile',
      component: () => import('../views/Profile.vue'),
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/cart/',
      name: 'Cart',
      component: () => import('../views/Cart.vue'),
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/cart/checkout/',
      name: 'Checkout',
      component: () => import('../views/Checkout.vue'),
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/cart/checkout/success/',
      name: 'Success',
      component: () => import('../views/Success.vue'),
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/my-orders/',
      name: 'Orders',
      component: () => import('../views/Orders.vue'),
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/favorites/',
      name: 'Favorites',
      component: () => import('../views/Favorites.vue'),
      meta: {
        requireLogin: true
      }
    },
  ]
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next('/sign-in/')
  } else {
    next()
  }
}) 

export default router
