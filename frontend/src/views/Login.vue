<template>
  <div class="container">
    <div class="row">
      <div class="col-md-3"></div>
      <div class="col-md-6">
        <form>
          <p>
          <label for="el"><h5>Email</h5></label> <br />
          <input type="email" name="el" id="el" v-model="email"> <br /> <br />
          </p>
          <p>
          <label for="pwr"><h5>Hasło</h5></label> <br />
          <input type="password" name="pwr" id="pwr" v-model="password"> <br /> <br />
          </p>
        </form>
      </div>
      <div class="col-md-3"></div>
    </div>
  </div>
</template>

<script>

import axios from 'axios'

export default {
  name: 'Login',
  components: {

  },

  methods: {
    login() {
      axios.post()
    }
  }
}
</script>

<style>
</style>