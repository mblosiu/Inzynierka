<template>
  <div class="images">
    <div id="app">
      <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand" href="/">e-Love</a>
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
          <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
              <router-link class="nav-link" to="/login">Logowanie</router-link>
            </li>
          </ul>
          <form class="form-inline my-2 my-lg-0">
            <router-link class="btn btn-outline-info my-2 my-sm-0" type="submit" to="/register">Rejestracja</router-link>
          </form>
        </div>
      </nav>
      <br />
      <router-view />
    </div>
  </div>
</template>

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
