<template>
  <v-app>
    <Header />

    <div id="user" v-if="token != null">
      <v-content>
        <router-view />
      </v-content>

      <div id="footer">
        <Footer />
      </div>
    </div>
    <div id="guest" v-if="token == null">
      <v-content>
        <v-row>
          <v-col cols="12"></v-col>
        </v-row>
        <v-row>
          <v-col cols="1"></v-col>
          <v-col cols="10">
            <router-view />
          </v-col>
          <v-col cols="1"></v-col>
        </v-row>
        <v-row>
          <v-col cols="12"></v-col>
        </v-row>
      </v-content>

      <div id="footer">
        <Footer />
      </div>
    </div>
  </v-app>
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
  data() {
    return {
      token: localStorage.getItem("user-token"),
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
  background-color: rgba(128, 0, 128, 0.288);
  background-blend-mode: overlay;
  background-repeat: no-repeat;
  background-size: cover;
}
#guest {
  background-image: url("../public/img/2.jpeg");
  background-color: rgba(255, 255, 255, 0.1);
  background-blend-mode: overlay;
  background-repeat: no-repeat;
  background-size: cover;
}
#nav {
  top: 0px;
}
#v-content {
  min-height: 73.2vh;
}

#footer a:hover {
  color: #0275d8;
  width: fit-content;
}
</style>