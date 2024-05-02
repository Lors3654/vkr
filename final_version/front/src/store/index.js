import { createStore } from 'vuex'

export default createStore({
  state: {
    isLoading: false,
    isAuthenticated: false,
    token: '',
    cart: {
      items: []
    },
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('cart')) {
        state.cart = JSON.parse(localStorage.getItem('cart'))
      } else {
        localStorage.setItem('cart', JSON.stringify(state.cart))
      }

      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
      } else {
        state.token = ''
        state.isAuthenticated = false
      }
    },
    addToCart(state, item) {
      console.log('Received item:', item)
      console.log(item.product);
      console.log(state.cart.items)
      console.log(item.product.product.id)
      if (item && item.product && item.product.product && item.product.product.id !== undefined) {
        const exists = state.cart.items.find(i => i.product && i.product.id === item.product.product.id);
        if (exists) {
          exists.quantity += parseInt(item.quantity);
        } else {
          state.cart.items.push(item);
        }
        localStorage.setItem('cart', JSON.stringify(state.cart));
      } else {
        if (state.cart.items.indexOf(item) !== 0) {
          console.warn('The item does not have the required "product" property. Skipping.');
        }
      }
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state) {
      state.token = ''
      state.isAuthenticated = false
    },
    clearCart(state) {
      state.cart = { items: [] }

      localStorage.setItem('cart', JSON.stringify(state.cart))
    },
  },
  getters: {
    cartTotalLength(state) {
      return state.cart.items.reduce((acc, item) => acc + item.quantity, 0);
    }
  },
  actions: {
    clearCart({ commit }) {
      commit('clearCart')
    },
  },
  modules: {
  }
})
