<template>
  <div class="container">
    <div class="row">
      <div class="col-lg-4">
        <NavigationMain />
      </div>
      <div class="col-lg-8 mt-5">
        <div class="container mt-2">
          <div class="row">
            <h4 class="title-h4 text-center my-auto">CHECKOUT</h4>  
            <hr>
          </div>
          <table class="table table-hover mt-3">
            <thead class="table-dark">
              <tr>
                <th scope="col" class="product-inf text-center align-middle">PRODUCT</th>
                <th scope="col" class="product-price text-center align-middle">PRICE</th>
                <th scope="col" class="product-quantity text-center align-middle">QUANTITY</th>
                <th scope="col" class="product-total-price text-center align-middle">TOTAL PRICE</th>
              </tr>
            </thead>
            <tbody>
              <tr 
                v-for="(item, index) in $store.state.cart.items" :key="index">
                <td class="product-inf text-center" v-if="item.product && item.product.product">{{ item.product.product.description }}</td>
                <td class="product-price text-center" v-if="item.product && item.product.product">{{ item.product.product.price }}</td>
                <td class="product-quantity text-center">{{ item.quantity }}</td>
                <td class="product-total-price text-center">{{ getItemTotal(item).toFixed(2) }} AED</td>
              </tr>
            </tbody>
          </table>
          <div class="row">
            <div class="col-6"></div>
            <div class="col-6">
              <table class="table table-dark table-borderless mt-3">
                <tbody>
                  <tr>
                    <td colspan="2" class="text-center align-middle"><strong>TOTAL:</strong></td>
                    <td class="text-center align-middle"><strong>{{ cartTotalLength }} ITEMS</strong></td>
                    <td class="text-center align-middle"><strong>{{ cartTotalPrice.toFixed(2) }} AED</strong></td>
                  </tr>
                </tbody>
              </table>           
            </div>
          </div>
          <div class="row">
            <h4 class="title-h4 text-center mt-5">ORDER DETAILS</h4>  
            <hr>
          </div>
          <form>
            <div class="row" id="OrderDetails">
              <div class="form-group mb-3">
                <label for="name">FIRST NAME*</label>
                <input type="name" class="form-control" id="name" name="name" v-model="user.name" disabled>
              </div>
              <div class="form-outline mb-4">
                <label for="lastname">LASTNAME*</label>
                <input type="lastname" class="form-control" id="lastname" name="lastname" v-model="user.lastname" disabled>
              </div>
              <div class="form-outline mb-4">
                <label for="phone">PHONE NUMBER*</label>
                <input type="tel" class="form-control" id="phone" name="phone" v-model="user.phone" disabled>
              </div>
              <div class="justify-content">
                <p class="text-center">If you would like to update your registration information, please do so before submitting your order
                  <div class="text-center">
                    <router-link class="nav-link" to="/profile" aria-label="Profile page"><b>PERSONAL INFORMATION</b></router-link>
                  </div> 
                </p>
              </div>
            </div>
          </form>
          <div class="justify-content mt-3">
            <button type="submit" class="w-100 btn btn-dark btn-sm mb-5" @click="submitForm"><small>PLACE AN ORDER</small></button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
  
<script>
  import axios from 'axios';
  import NavigationMain from '@/components/NavigationMain.vue';


  export default {
    name: 'Checkout',
    components: {
      NavigationMain,
    },
    data() {
      return {
        cart: {
          items: []
        },
        user: {}
      }
    },
    mounted() {
      this.cart = this.$store.state.cart;
      this.fetchUserData()
    },
    methods: {
      async fetchUserData() {
        try {
          const response = await axios.get('/api/v1/current-user/')
          
          this.user = response.data
          
        } catch (error) {
          console.error('Error fetching user data:', error)
        }
      },
      async submitForm() {
        await this.fetchUserData();
        if (!this.user || !this.user.id) {
          alert("Please log in to proceed with the checkout.")
          return;
        }
        // Проверяем, существует ли orderId в localStorage
        let orderId = localStorage.getItem('orderId')
        if (!orderId) {
          // Если orderId нет, создаем новый заказ.
          try {
            const orderResponse = await axios.post('/api/v1/orders/', {
              user: this.user.id,
              product_status: "process", 
            });
            orderId = orderResponse.data.id;
            // Сохраняем новый orderId в localStorage
            localStorage.setItem('orderId', orderId)
          } catch (error) {
            console.error('Error creating order:', error.response ? error.response.data : error)
            return;
          }
        }

        const items = this.cart.items.map(item => ({
          product: item.product.product.id,
          quantity: item.quantity,
          unit_price: parseFloat(item.product.product.price),
          total_amount: parseFloat(item.product.product.price) * parseInt(item.quantity, 10),
          order: orderId
        }))

        // Отправляем детали заказа с существующим orderId
        const checkoutData = {
          order: orderId,
          items: items
        }

        try {
          const checkoutResponse = await axios.post('/api/v1/checkout/', checkoutData)
          console.log("Server response:", checkoutResponse.data)
          this.$store.commit('clearCart')
          this.$router.push('/cart/checkout/success')
          // Очищаем orderId из localStorage после успешного создания заказа
          localStorage.removeItem('orderId')
        } catch (error) {
          console.error('Error during checkout:', error.response ? error.response.data : error)
        }
      },
      getItemTotal(item) {
        if (item.product && item.product.product) {
          return item.quantity * item.product.product.price
        }
        return 0
      },
    },
    computed: {
      orderId() {
        const id = localStorage.getItem('orderId');
        return id ? parseInt(id, 10) : null;
      },
      cartTotalLength() {
        return this.cart.items.reduce((acc, curVal) => {
          return acc += curVal.quantity
        }, 0)
      },
      cartTotalPrice() {
        return this.cart.items.reduce((acc, curVal) => {
          if (curVal.product && curVal.product.product.price) {
            return acc += curVal.product.product.price * curVal.quantity
          } else {
            return acc
          }
        }, 0)
      },
    },

  }
</script>
