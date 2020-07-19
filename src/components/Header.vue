<template>
  <div class>
    <b-alert v-model="showDismissibleAlert" variant="danger" dismissible>{{error_message}}</b-alert>

    <b-navbar toggleable="lg" type="dark" variant="dark">
      <b-navbar-brand class="text-white" href="/">e-love</b-navbar-brand>
 
      <b-nav-form @submit.prevent="search">
        <b-form-input size="sm" class="mr-sm-2" placeholder="Search" v-model="searchText"></b-form-input>
        <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
      </b-nav-form>

      <b-navbar-nav class="ml-auto">
        <b-nav-form @submit.prevent="users" v-if="token != null">
          <b-button :to="{name:'Users'}" type="button" size="sm" class="my-2 ml-2">Look for partner</b-button>
        </b-nav-form>
        <b-nav-form @submit.prevent="profile" v-if="token != null">
          <b-button :to="{name:'Profile'}" type="button" size="sm" class="my-2 ml-2">Profile</b-button>
        </b-nav-form>
        <b-nav-form @submit.prevent="settings" v-if="token != null">
          <b-button :to="{name:'Settings'}" type="button" size="sm" class="my-2 ml-2">Settings</b-button>
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
        <b-nav-form @submit.prevent="register" v-if="token == null">
          <b-button :to="{name:'Register'}" type="button" size="sm" class="my-2 ml-2">Register</b-button>
        </b-nav-form>
        <b-nav-form @submit.prevent="logout" v-if="token != null">
          <b-button size="sm" type="submit" class="my-2 ml-2">Logout</b-button>
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
      searchText: "",
      showDismissibleAlert: false,
      error_message: "xd"
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
          (this.status = response.status),
            (this.token = response.data.token),
            localStorage.setItem("user-token", this.token);
          if (response.status == 200) {
            this.error_message = "";
            this.showDismissibleAlert = false;
          }
        })
        .catch(errors => {
          if (errors.response.status != 200) {
            this.error_message = "Błędny login lub hasło!";
            this.showDismissibleAlert = true;
          }
        });
      //this.$router.go()
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
          this.$router.push('/')
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
    },
    search() {
      console.log(this.searchText);
      this.$store.dispatch("search", { text: this.searchText });
    }
  }
};
</script>