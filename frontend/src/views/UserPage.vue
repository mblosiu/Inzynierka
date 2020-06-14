<template>
    <div id="userpage">
      <!--<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand" href="/userpage">e-Love</a>
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

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav mr-auto"></ul>
          <b-nav-form @submit.prevent="logout">
            <b-button type="submit" size="sm" class="Primary">Wyloguj</b-button>
          </b-nav-form>
        </div>
      </nav>
      <br />
      <router-view />-->
    </div>
</template>


<script>
export default {
  name: "UserPage",
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

#userpage {
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