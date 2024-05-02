<template>
  <div class="container">
    <div class="row">
      <div class="col-lg-4">
        <NavigationMain />
      </div>
      <div class="col-lg-8 mt-5">
        <div class="container mt-2">
          <div class="row">
            <h4 class="title-h4 my-auto">MY ORDERS</h4>  
            <hr>
          </div>
          <div class="card text-center mb-5" v-for="order in orders" :key="order.id">
            <div class="card-header">
              <h4 class="title-h4 text-center align-middle mt-4">Order #{{ order.id }} </h4>
            </div>
            <div class="card-body">
              <table class="table table-hover">
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
                  v-for="item in order.items" :key="item.product.id">
                    <td class="product-inf text-center">{{ item.product.description }}</td>
                    <td class="product-inf text-center">{{ item.unit_price }}</td>
                    <td class="product-quantity text-center">{{ item.quantity }}</td>
                    <td class="product-total-price text-center">{{ item.total_amount }} AED</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div class="card-footer text-body-secondary">
              <h4 class="title-h4 ext-center my-auto">{{ order.formattedOrderDate }}</h4>
            </div>
          </div>
          <!-- <div v-for="order in orders" :key="order.id">
            <h4 class="title-h4 mt-4">Order #{{ order.id }}</h4>
            <h4 class="title-h4">{{ order.formattedOrderDate }}</h4>
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
                v-for="item in order.items" :key="item.product.id">
                  <td class="product-inf text-center">{{ item.product.description }}</td>
                  <td class="product-inf text-center">{{ item.unit_price }}</td>
                  <td class="product-quantity text-center">{{ item.quantity }}</td>
                  <td class="product-total-price text-center">{{ item.total_amount }} AED</td>
                </tr>
              </tbody>
            </table>
            <hr class="mt-4">
          </div> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  import NavigationMain from '@/components/NavigationMain.vue';

  export default {
    name: 'Orders',
    components: {
      NavigationMain
    },
    data() {
      return {
        orders: []
      }
    },
    mounted() {
      this.getMyOrders()
    },
    methods: {
      async getMyOrders() {
        await axios
          .get('/api/v1/my-orders/')
          .then(response => {
            console.log("Orders:", response.data)
            this.orders = response.data.map(order => {
              order.formattedOrderDate = this.formatDate(order.order_date)
              return order
            })
          })
          .catch(error => {
            console.error('Error fetching orders:', error.response ? error.response.data : error)
          })
      },
      formatDate(dateString) {
        const date = new Date(dateString);
        return date.toLocaleDateString("en-US", { 
          year: 'numeric', 
          month: 'long', 
          day: 'numeric', 
          hour: '2-digit', 
          minute: '2-digit'
        })
      },
    },
  } 
</script>