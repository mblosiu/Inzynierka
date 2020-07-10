<template>
  <div class>

    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand class="text-white" href="#">Tytuł strony</b-navbar-brand>

      <div class="search-wrapper">
        <input type="text" v-model="search" placeholder="Search..." />
      </div>

      <b-navbar-nav class="ml-auto">
        <b-nav-form @submit.prevent="users" v-if="token != null">
          <b-button :to="{name:'Users'}" type="submit" size="sm" class="my-2 ml-2">Look for partner</b-button>
        </b-nav-form>
        <b-nav-form @submit.prevent="profile" v-if="token != null">
          <b-button :to="{name:'Profile'}" type="submit" size="sm" class="my-2 ml-2">Profile</b-button>
        </b-nav-form>
        <b-nav-form @submit.prevent="settings" v-if="token != null">
          <b-button :to="{name:'Settings'}" type="submit" size="sm" class="my-2 ml-2">Settings</b-button>
        </b-nav-form>
        <b-nav-form @submit.prevent="login" v-if="token==null">
          <b-form-input
            id="username"
            size="sm"
            class="mr-sm-2"
            v-model="username"
            placeholder="username"
            name="username"
          />
          <b-form-input
            id="password"
            size="sm"
            class="mr-sm-2"
            placeholder="password"
            type="password"
            v-model="password"
            name="password"
          />

          <b-button size="sm" class="my-2 my-sm-0" type="submit">Login</b-button>
        </b-nav-form>
        <b-nav-form @submit.prevent="logout" v-if="token !== null">
          <b-button type="submit" size="sm" class="my-2 ml-2">Logout</b-button>
        </b-nav-form>
        <b-nav-form @submit.prevent="register" v-if="token === null">
          <b-button :to="{name:'Register'}" type="submit" size="sm" class="my-2 ml-2">Register</b-button>
        </b-nav-form>
      </b-navbar-nav>
    </b-navbar>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Header",
  components: {},
  data() {
    return {
      username: "",
      password: "",
      token: localStorage.getItem("user-token") || null,
      search: [],
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
            this.token = response.data.token,
            localStorage.setItem("user-token", response.data.token);
            this.$router.go();
        })
        .catch(errors => console.log(errors));
    },
    logout() {
      let config = {
        headers: {
          Authorization: "Token " + localStorage.getItem("user-token")
        }
      };

      axios
        .post("http://127.0.0.1:8000/api/user/logout", {}, config)
        .then(
          response => console.log(response),
          localStorage.removeItem("user-token"),
          (this.token = null),
          this.$router.push("/")
        )
        .catch(errors => console.log(errors));
    },
    register() {
      console.log("Router");
    },
    settings() {
      console.log("Router");
    },
    profile() {
      console.log("Router");
    },
    users() {
      console.log("Router");
    }
  }
};
</script>