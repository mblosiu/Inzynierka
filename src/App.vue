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
    Footer,
  },
};
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #343a40;
  background-image: url("../public/img/ecouple3.jpg");
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

#content {
  color: #343a40;
  min-height: 100vh;
  margin-left: 2cm;
  margin-right: 2cm;
  margin-top: 1cm;
  margin-bottom: 1cm;
}

#footer {
  background-color: #343a40;
  color: whitesmoke;
  bottom: 0;
  width: 100%;
}
</style>
