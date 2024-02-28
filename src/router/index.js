import { createRouter, createWebHistory } from 'vue-router'
import SignUp from '@/views/SignUp.vue'
import Main from '@/views/Main.vue'
import SignIn from '@/views/SignIn.vue'
import Categories from '@/views/Categories.vue'
import Dresses from '@/views/Dresses.vue'
import Shirts from '@/views/Shirts.vue'
import Skirts from '@/views/Skirts.vue'

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
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
