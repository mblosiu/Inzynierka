<template>
  <div class="images">
    <div id="app">
      <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <a v-if="token==null" class="navbar-brand" href="/">e-Love</a>
        <a v-else class="navbar-brand" href="/userpage">e-Love</a>
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

        <div v-if="token==null" class="collapse navbar-collapse" id="navbarSupportedContent">
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
      <br />
      <router-view />
    </div>
  </div>
</template>


<script>
export default {
  name: "App",
  components: {},
  data() {
    return {
      token: localStorage.getItem("user-token") || null
    };
  },
  methods: {
    logout() {
      localStorage.removeItem('user-token');
      this.token = null;
      this.$router.push("/");
      history.go()
    }
  }
};
</script>


<style>
.images {
  background-image: url("../public/img/ecouple3.jpg");
  background-repeat: no-repeat;
  background-size: auto;
}

#app {
  height: 1200px;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

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
