<template>
  <div class>
    <b-navbar class="navbar" toggleable="lg">
      <a v-if="token == null" class="navbar-brand" href="/">
        e
        <svg
          width="0.85em"
          height="0.85em"
          viewBox="0 0 16 16"
          class="bi bi-heart"
          fill="currentColor"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            fill-rule="evenodd"
            d="M8 2.748l-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"
          />
        </svg>
        Love
      </a>
      <a v-else class="navbar-brand" href="/mainuser">
        e
        <svg
          width="0.85em"
          height="0.85em"
          viewBox="0 0 16 16"
          class="bi bi-heart"
          fill="currentColor"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            fill-rule="evenodd"
            d="M8 2.748l-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"
          />
        </svg>
        Love
      </a>

      <div v-if="token!=null" href="/mainuser">
        <b-avatar href="/mainuser" :src="getUrl(user_data.profile_picture)"></b-avatar>
        {{user_data.username}}
      </div>
      <!--<b-nav-form @submit.prevent="search" v-if="token != null">
        <b-form-input size="sm" class="mr-sm-2" placeholder="Search" v-model="searchText"></b-form-input>
        <b-button size="sm" class="my-2 my-sm-0" type="submit">Szukaj</b-button>
      </b-nav-form>-->

      <b-navbar-nav class="ml-auto">
        <b-nav-form v-if="token != null">
          <b-button class="my-2 ml-2" type="button" size="sm" to="/mainuser">Twój profil</b-button>
        </b-nav-form>

        <b-nav-form v-if="token != null">
          <b-button class="my-2 ml-2" type="button" size="sm" to="/mainuser/search">Szukaj par</b-button>
        </b-nav-form>

        <b-nav-form v-if="token != null">
          <b-button class="my-2 ml-2" type="button" size="sm">Dopasuj</b-button>
          <b-nav-form v-if="token != null">
            <b-button class="my-2 ml-2" type="button" size="sm">
              Polubienia
              <span class="badge badge-light">0</span>
            </b-button>
          </b-nav-form>

          <b-nav-form v-if="token != null">
            <b-button class="my-2 ml-2" type="button" size="sm">
              Wiadomości
              <span class="badge badge-light">0</span>
            </b-button>
          </b-nav-form>

          <b-nav-form v-if="token != null">
            <b-button class="my-2 ml-2" type="button" size="sm">
              Kontakty
              <span class="badge badge-light">0</span>
            </b-button>
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
        <div v-if="token == null">
          <b-alert
            :show="dismissCountDown"
            fade
            class="mr-sm-2"
            variant="danger"
            @dismissed="dismissCountDown = 0"
            @dismiss-count-down="countDownChanged"
          >{{ msg }}</b-alert>
        </div>
        <b-nav-form @submit.prevent="login" v-if="token == null">
          <b-form-input
            id="username"
            size="sm"
            class="mr-sm-2"
            v-model="username"
            placeholder="nazwa użytkownika"
            name="username"
          />
          <b-form-input
            id="password"
            size="sm"
            class="mr-sm-2"
            placeholder="hasło"
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
      user_data: {},
    };
  },
  methods: {
    countDownChanged(dismissCountDown) {
      this.dismissCountDown = dismissCountDown;
    },
    showMsg() {
      this.dismissCountDown = this.dismissSecs;
    },
    getUserData() {
      axios
        .get("http://127.0.0.1:8000/api/user/properties", {
          params: {},
          headers: {
            Authorization: "Token " + localStorage.getItem("user-token"),
          },
        })
        .then((response) => {
          console.log(response), (this.user_data = response.data);
        })
        .catch((errors) => console.log(errors));
    },
    getUrl(pic) {
      if (pic != null) return "http://127.0.0.1:8000" + pic;
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
    },
    search() {
      localStorage.setItem("search-text", this.searchText);
      if (this.$route.name == "search") this.$router.go();
      else this.$router.push({ name: "search" });
    },
  },
  created() {
    this.getUserData();
  },
};
</script>

<style scoped>
.alert {
  padding-block: inherit;
  margin-block: inherit;
  align-content: inherit;
}
.navbar {
  background-color: #344d72;
}
.b-avatar {
  margin-left: 10px;
}
</style>
