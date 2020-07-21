<template>
  <div class="container">
    <br />
    <div class="row">
      <div class="col-md-3"></div>
      <div class="col-md-6 d-flex justify-content-center">
        <div
          class="card bg-dark text-white text-center p-3"
          style="width: 18rem;"
          background="black"
        >
          <div class="card-body">
            <h5 class="card-header">Logowanie</h5>
            <br />
            <p class="card-text"></p>
            <form @submit.prevent="login">
              <p>
                <label for="username">
                  Nazwa użytkownika
                  <input
                    type="text"
                    name="username"
                    id="username"
                    v-model="username"
                  />
                </label>
                <br />
              </p>
              <p>
                <label for="password">
                  Hasło
                  <input type="password" name="password" id="password" v-model="password" />
                </label>
                <br />
              </p>
              <br />
              <p>
                <input
                  v-on:click="login"
                  class="btn btn-outline-success"
                  type="submit"
                  value="Zaloguj"
                />
              </p>
            </form>
          </div>
        </div>
      </div>
      <div class="col-md-3"></div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
//import Api from "../service/api";

export default {
  name: "Login",
  components: {},
  data() {
    return {
      username: "",
      password: "",
      token: localStorage.getItem("user-token") || null,
      //search: [],
      errors: []
    };
  },

  methods: {
    login() {
      axios
        .post("http://127.0.0.1:8000/api/user/login", {
          username: this.username,
          password: this.password
        })
        .then(response => {
          console.log(response),
            (this.token = response.data.token),
            localStorage.setItem("user-token", response.data.token);
          this.$router.go();
        })
        .catch(errors => console.log(errors));
      this.$router.push("/mainuser");
    }
  }
};
</script>

<style>
</style>