<template>
  <div class="register-form">
    <form @submit.prevent="register">
      <p>
        <label for="username">
          <h5>Nazwa konta</h5>
        </label>
        <br />
        <input type="text" name="username" id="username" v-model="username" />
        <br />
        <br />
      </p>
      <p>
        <label for="email">
          <h5>Email</h5>
        </label>
        <br />
        <input type="email" name="email" id="email" v-model="email" />
        <br />
        <br />
      </p>
      <p>
        <label for="birthday">
          <h5>Data urodzenia</h5>
        </label>
        <br />
        <input type="date" name="birthday" id="birthday" v-model="birthday" />
        <br />
        <br />
      </p>
      <p>
        <label for="Location">
          <h5>Lokacja</h5>
        </label>
        <br />
        <input type="text" name="Location" id="Locatiom" v-model="location" />
        <br />
        <br />
      </p>
      <p>
        <label for="sex">
          <h5>Płeć</h5>
        </label>
        <br />
        <select class="ml-2" name="Sex" id="Sex" v-model="sex">
          <br />
          <option>mężczyzna</option>
          <option>kobieta</option>
          <option>inna</option>
        </select>
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
      <p>
        <label for="password2">
          <h5>Powtórz hasło</h5>
        </label>
        <br />
        <input type="password" name="password2" id="password2" v-model="password2" />
        <br />
        <br />
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
</template>

<script>
import axios from "axios";

export default {
  name: "Register",
  components: {},
  data() {
    return {
      username: '',
      email: '',
      location: '',
      birthday: '',
      sex: '',
      password: ''
    };
  },

  methods: {
    register() {
      if (this.password !== this.password2) {
        console.log('Podane hasła muszą być identyczne!');
      }
      axios
        .post("http://127.0.0.1:8000/api/account/register", {
          username: this.username,
          email: this.email,
          location: this.location,
          birthday: this.birthday,
          sex: this.sex,
          password: this.password
        })
        .then(Response => console.log(Response))
        .catch(err => console.log(err));
      this.$router.push("/");
    }
  }
};
</script>

<style>
h5 {
  color: gold;
}
</style>