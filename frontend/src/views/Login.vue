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
            <form @submit.prevent="loginUser">
              <p>
                <label for="username">
                  Nazwa użytkownika
                  <input type="text" name="username" id="username" v-model="username" />
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
                  v-on:click="loginUser"
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
//import axios from "axios";
//import Api from "../service/api";

export default {
  name: "Login",
  components: {},
  data() {
    return {
      username: "",
      password: "",
      token: null,
      status: "",
      user: ""
    };
  },

  methods: {
    async loginUser() {
      let user = await this.$store.dispatch('loginUser', {username: this.username, password: this.password});
      console.log(user);
      if(user.status=="200"){
        this.$router.push("/mainuser");
      } else {
        console.log("error")
      }
      /*if(this.user.error){
        alert(user.error)
      } else {
          alert('Udane logowanie użytkownika' + user.name);
          this.$router.push("/mainuser");
      }*/

      /*Api()
        .post("/account/login", {
          username: this.username,
          password: this.password
        })
        .then(Response => {
          this.status = Response.status;
          this.token = Response.data.token;
          console.log(this.token);
          console.log(Response.status);
          localStorage.setItem("user-token", Response.data.token);
          //localStorage.setItem("username", this.username);
        })
        .catch(Error => {
          console.log(Error);
          localStorage.removeItem("user-token");
        });*/
      //this.$store.dispatch("loginUser", user);
      //tu pushnac na strone usera

      //history.go();
    }
  }
};
</script>

<style>
</style>