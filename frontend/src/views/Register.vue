<template>
  <div>
    <br />
    <div class="register-form d-flex justify-content-center">
      <div class="card bg-dark text-white text-center p-3 rounded" style="max-width: 18rem;">
        <div class="card-header">
          <h5>Rejestracja</h5>
        </div>
        <div class="card-body">
          <p class="card-text"></p>
          <form @submit.prevent="register">
            <p>
              <label for="username">
                Nazwa konta
                <input type="text" name="username" id="username" v-model="username" />
              </label>
              <br />
            </p>
            <p>
              <label for="email">
                Email
                <input type="email" name="email" id="email" v-model="email" />
              </label>
              <br />
            </p>
            <p>
              <label for="Location">
                Lokacja
                <input type="text" name="Location" id="Locatiom" v-model="location" />
              </label>
              <br />
            </p>
            <p>
              <label for="birthday">
                Data urodzenia
                <input type="date" name="birthday" id="birthday" v-model="birthday" />
              </label>
              <br />
            </p>
            <p>
              <label for="sex">
                Płeć
                <select class="ml-2" name="Sex" id="Sex" v-model="sex">
                  <br />
                  <option>mężczyzna</option>
                  <option>kobieta</option>
                  <option>inna</option>
                </select>
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
            <p>
              <label for="password2">
                Powtórz hasło
                <input type="password" name="password2" id="password2" v-model="password2" />
              </label>
              <br />
            </p>
            <p>
              <input
                v-on:click="register"
                class="btn btn-outline-success"
                type="submit"
                value="Zarejestruj"
              />
            </p>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
//import axios from "axios";
import Api from "../service/api";

export default {
  name: "Register",
  components: {},
  data() {
    return {
      username: "",
      email: "",
      location: "",
      birthday: "",
      sex: "",
      password: "",
      password2: ""
    };
  },

  methods: {
    register() {
      if (this.password !== this.password2) {
        console.log("Podane hasła muszą być identyczne!");
        this.$router.push("/register");
      } else {
        Api()
          .post("/account/register", {
            username: this.username,
            email: this.email,
            location: this.location,
            birthday: this.birthday,
            sex: this.sex,
            password: this.password,
            password2: this.password2
          })
          .then(Response => console.log(Response))
          .catch(err => console.log(err));
        this.$router.push("/");
      }
    }
  }
};
</script>

<style>
h5 {
  color: gold;
}
</style>