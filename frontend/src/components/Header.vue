<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <a v-if="token == null" class="navbar-brand" href="/">e-Love</a>
    <a v-else class="navbar-brand" href="/mainuser">e-Love</a>
    <button
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#navbarSupportedContent"
      aria-controls="navbarSupportedContent"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>

    <div v-if="token == null" class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <router-link class="btn btn-outline-primary my-2 my-sm-0" to="/login">Logowanie</router-link>
        </li>
      </ul>
      <form class="form-inline my-2 my-lg-0">
        <router-link
          class="btn btn-outline-success my-2 my-sm-0"
          type="submit"
          to="/register"
        >Rejestracja</router-link>
      </form>
    </div>
    <div v-else class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto"></ul>
      <b-nav-form @submit.prevent="logout">
        <b-button type="submit" size="sm" class="Primary">Wyloguj</b-button>
      </b-nav-form>
    </div>
  </nav>
</template>

<script>

import axios from 'axios';
//import { mapState } from 'vuex';

export default {
    name: 'Header',
    components: {

    },
    /*computed: {
      ...mapState(['currentUser'])
    },*/
    data() {
    return {
      token: localStorage.getItem("user-token") || null
      
    };
  },
  methods: {
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
  }

}
</script>

<style>
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>