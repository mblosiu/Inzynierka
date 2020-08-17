<template>
  <div id="app">
    <div id="user" v-if="token != null">
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
    <div id="guest" v-if="token == null">
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
  </div>
</template>

<script>
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';
export default {
  name: '',
  components: {
    Header,
    Footer,
  },
  data() {
    return {
      token: localStorage.getItem('user-token'),
    };
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
}
#user {
  background-image: url('../public/img/3.jpeg');
  background-color: rgba(255, 255, 255, 0.4);
  background-blend-mode: overlay;
  background-repeat: no-repeat;
  background-size: cover;
}
#guest {
  background-image: url('../public/img/2.jpeg');
  background-color: rgba(255, 255, 255, 0.1);
  background-blend-mode: overlay;
  background-repeat: no-repeat;
  background-size: cover;
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
  min-height: 73.2vh;
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
