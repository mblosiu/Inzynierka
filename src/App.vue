<template>
  <div id="app">
    <div id="nav">
      <Header />
    </div>

    <div id="content">
      <router-view />
    </div>

    <div id="footer">
      <Footer />
    </div>
  </div>
</template>


<script>
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";
export default {
  name: "",
  components: {
    Header,
    Footer
  }
};
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #343a40;
  background-color: whitesmoke;
}

#nav {
  padding: 0px;
}

#nav a {
  color: whitesmoke;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

#footer {
  background-color: #343a40;
  color: whitesmoke;
  padding: 0px;
}

#content {
  background-color: whitesmoke;
  color: #343a40;
  padding: 0px;
  min-height: 70vh;
  padding-bottom: 10px;
  padding-top: 10px;
}
</style>
