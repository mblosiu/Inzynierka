<template>
  <div class="container">
    <div class="row">
      <div class="col-md-3"></div>
      <div class="col-md-6">
        <form @submit.prevent="login">
          <p>
            <label for="username">
              <h5>Nazwa użytkownika</h5>
            </label>
            <br />
            <input type="text" name="username" id="username" v-model="usernaeme" />
            <br />
            <br />
          </p>
          <p>
            <label for="password">
              <h5>Hasło</h5>
            </label>
            <br />
            <input type="password" name="password" id="password" v-model="password" />
            <br />
            <br />
          </p>
          <br />
          <p>
            <input v-on:click="login" class="btn btn-outline-success" type="submit" value="Zaloguj" />
          </p>
        </form>
      </div>
      <div class="col-md-3"></div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Login",
  components: {},
  data() {
    return {
      username: "",
      password: "",
      token: null
    };
  },

  methods: {
    login() {
      axios
        .post("http://127.0.0.1:8000/api/account/login", {
          email: this.username,
          password: this.password
        })
        .then(Response => console.log(Response))
        .catch(err => console.log(err));
        //tu pushnac do profilu usera
        this.$router.push("/");
    }
  }
};
</script>

<style>
</style>