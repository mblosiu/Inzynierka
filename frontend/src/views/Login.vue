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
            <input type="text" name="username" id="username" v-model="username" />
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
          username: this.username,
          password: this.password
        })
        .then(Response => {
          this.token = Response.data.token;
          console.log(this.token);
          localStorage.setItem("user-token", Response.data.token);
        })
        .catch(Error => {
          console.log(Error);
          localStorage.removeItem("user-token");
        });
      //tu pushnac na strone usera
      this.$router.push("/userpage");
      //history.go();
      //vm.$forceUpdate();
    }
  }
};
</script>

<style>
</style>