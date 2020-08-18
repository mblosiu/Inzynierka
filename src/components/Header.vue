<template>
  <div class>
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <a v-if="token == null" class="navbar-brand" href="/">e-Love</a>
      <a v-else class="navbar-brand" href="/mainuser">e-Love</a>

      <b-nav-form @submit.prevent="search">
        <b-form-input size="sm" class="mr-sm-2" placeholder="Search" v-model="searchText"></b-form-input>
        <b-button size="sm" class="my-2 my-sm-0" type="submit">Szukaj</b-button>
      </b-nav-form>

      <b-navbar-nav class="ml-auto">
        <b-nav-form v-if="token != null">
          <b-button class="my-2 ml-2" type="button" size="sm" to="/mainuser">Twój profil</b-button>
        </b-nav-form>

        <b-nav-form v-if="token != null">
          <b-button class="my-2 ml-2" type="button" size="sm" to="/mainuser/search">Szukaj par</b-button>
        </b-nav-form>

        <b-nav-form v-if="token != null">
          <b-button class="my-2 ml-2" type="button" size="sm" to="/#">Dopasuj</b-button>
          <b-nav-form v-if="token != null">
            <b-button class="my-2 ml-2" type="button" size="sm" to="/#">Polubienia</b-button>
          </b-nav-form>

          <b-nav-form v-if="token != null">
            <b-button class="my-2 ml-2" type="button" size="sm" to="/#">Wiadomości</b-button>
          </b-nav-form>

          <b-nav-form v-if="token != null">
            <b-button class="my-2 ml-2" type="button" size="sm" to="/#">Kontakty</b-button>
          </b-nav-form>

          <b-nav-form v-if="token != null">
            <b-button class="my-2 ml-2" type="button" size="sm" to="/mainuser/gallery">Galeria</b-button>
          </b-nav-form>
        </b-nav-form>

        <b-nav-form v-if="token != null">
          <b-button
            class="my-2 ml-2 mr-1"
            type="button"
            size="sm"
            to="/mainuser/settings"
          >Ustawienia</b-button>
        </b-nav-form>

        <b-nav-form v-if="token != null">
          <b-button class="btn btn-warning mr-1" type="button" size="sm" to="/#">Premium</b-button>
        </b-nav-form>
        <div v-if="token==null">
          <b-alert
            :show="dismissCountDown"
            fade
            class="mr-sm-2"
            variant="danger"
            @dismissed="dismissCountDown=0"
            @dismiss-count-down="countDownChanged"
          >{{msg}}</b-alert>
        </div>
        <b-nav-form @submit.prevent="login" v-if="token == null">
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
          <b-button v-on:click="login" type="submit" size="sm" class="btn btn-success mr-2">Zaloguj</b-button>
        </b-nav-form>

        <!--<b-nav-form @submit.prevent="register" v-if="token == null">
          <router-link class="btn btn-outline-warning" type="submit" to="/register">Rejestracja</router-link>
        </b-nav-form>-->

        <b-nav-form @submit.prevent="logout" v-if="token != null">
          <b-button type="submit" size="sm" class="btn btn-danger mr-1">Wyloguj</b-button>
        </b-nav-form>
      </b-navbar-nav>
    </b-navbar>
    <!--<b-row>
      <b-col cols="12">
        <b-alert
          :show="dismissCountDown"
          dismissible
          fade
          variant="danger"
          @dismissed="dismissCountDown=0"
          @dismiss-count-down="countDownChanged"
        >{{msg}}</b-alert>
      </b-col>
    </b-row>-->
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Header",
  components: {},
  data() {
    return {
      token: localStorage.getItem("user-token") || null,
      username: "",
      password: "",
      searchText: "",
      dismissSecs: 5,
      dismissCountDown: 0,
    };
  },
  methods: {
    countDownChanged(dismissCountDown) {
      this.dismissCountDown = dismissCountDown;
    },
    showMsg() {
      this.dismissCountDown = this.dismissSecs;
    },
    login() {
      //this.showMsg(), (this.msg = "Błędny login lub hasło!");
      axios
        .post("http://127.0.0.1:8000/api/user/login", {
          username: this.username,
          password: this.password,
        })
        .then((response) => {
          if (response.status == 200) {
            (this.error_message = ""),
              (this.showDismissibleAlert = false),
              (this.token = response.data.token),
              localStorage.setItem("user-token", response.data.token),
              this.$router.push("mainuser");
            this.$router.go();
          }
        })
        .catch((errors) => {
          if (errors.response.status != 200) {
            this.showMsg(), (this.msg = "Błędny login lub hasło!");
          }
        });
    },
    logout() {
      let config = {
        headers: {
          Authorization: "Token " + localStorage.getItem("user-token"),
        },
      };

      axios
        .post("http://127.0.0.1:8000/api/user/logout", {}, config)
        .then((response) => {})
        .catch((errors) => {});
      localStorage.removeItem("user-token"),
        (this.token = null),
        this.$router.go();
      ł;
    },
    search() {
      localStorage.setItem("search-text", this.searchText);
      if (this.$route.name == "search") this.$router.go();
      else this.$router.push({ name: "search" });
    },
  },
};
</script>

<style scoped>
.navbar-brand {
}

.alert {
 padding-block:inherit;
 margin-block:inherit;
 align-content: inherit;
}

</style>
