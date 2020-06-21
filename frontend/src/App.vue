<template>
  <div class="images">
    <div id="app">
      <Header/>
      <router-view />
    </div>
  </div>
</template>


<script>

import Header from '@/components/Header.vue'

export default {
  name: "App",
  components: {
    Header
  },
};
</script>


<style>
.images {
  background-image: url("../public/img/ecouple3.jpg");
  background-repeat: no-repeat;
  background-size: auto;
}

#app {
  height: 1400px;
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
