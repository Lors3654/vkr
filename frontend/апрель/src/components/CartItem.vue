<template>
  <tr>
    <!-- Изображение -->
    <td>
      <div class="card mb-3" v-if="item.product && item.product.product">
        <img :src="item.product.product.image" class="d-block w-100" style="max-width: 200px; max-height: 200px;">
        <div class="card-body">
          <h5 class="title-h6 text-center">{{ item.product.product.product_name }}</h5>
          <p class="title-carddes card-text text-center">{{ item.product.product.price }} AED</p>
        </div>
      </div>
    </td>
    <!-- Описание -->
    <td class="product-thumb text-center" v-if="item.product && item.product.product">{{ item.product.product.description }}</td>
    <!-- Увеличение/уменьшение -->
    <td class="product-quantity">
      <div class="input-group justify-content-center">
        <button type="button" @click="decrementQuantity(item)" class="btn btn-outline-secondary btn-sm sub">-</button>
        <div class="col-md-5">
          <input type="text" class="form-control text-center" v-model="item.quantity">
        </div>
        <button type="button" @click="incrementQuantity(item)" class="btn btn-outline-secondary btn-sm add">+</button>
      </div>
    </td>
    <!-- Общая стоимость товаров в корзине -->
    <td class="product-total-price text-center" v-if="item.product && item.product.product">{{ getItemTotal(item).toFixed(2) }} AED</td>
    <!-- Удаление товара -->
    <td class="product-action">
      <div class="input-group justify-content-center">
        <button type="button" @click="removeFromCart(item)" class="delete btn mx-auto justify-content-center">
          <svg class="icon">
            <use xlink:href="../assets/styles/sprite.svg#remove"></use>
          </svg>
        </button>
      </div>
    </td>
  </tr>
</template>

<script>
export default {
  name: 'CartItem',
  emits: ['removeFromCart'],
  props: {
    initialItem: Object,
    index: Number
  },
  data() {
    return {
      item: this.initialItem || {}, // добавляем проверку на существование объекта
      quantity: 1,
    }
  },
  methods: {
    getItemTotal(item) {
      if (item.product && item.product.product) {
        return item.quantity * item.product.product.price
      }
      return 0
    },
    decrementQuantity(item) {
      if (item.quantity > 0) {
        item.quantity -= 1
        if (item.quantity === 0) {
          this.$emit('removeFromCart', item)
        }
        this.updateCart()
      }
    },
    incrementQuantity(item) {
      item.quantity += 1
      this.updateCart()
    },
    updateCart() {
      localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
    },
    removeFromCart(item) {
      this.$emit('removeFromCart', item)
      this.updateCart()
    },
  },
}
</script>
