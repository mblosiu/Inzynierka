<template>
  <div class>
    <b-navbar class="navbar" toggleable="lg">
      <a v-if="token == null" id="logo" class="navbar-brand" href="/">
        e
        <svg
          width="0.85em"
          height="0.85em"
          viewBox="0 0 16 16"
          class="bi bi-heart-fill"
          fill="red"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z" />
        </svg>
        Love
      </a>
      <a id="logo" v-else class="navbar-brand" href="/mainuser">
        e
        <svg
          width="0.85em"
          height="0.85em"
          viewBox="0 0 16 16"
          class="bi bi-heart-fill"
          fill="red"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z" />
        </svg>
        Love
      </a>

      <b-nav-form id="search" @submit.prevent="search" v-if="token != null">
        <b-form-input
          id="search-input"
          size="sm"
          class="mr-sm-2"
          v-model="searchText"
          placeholder="wyszukaj użytkownika"
          name="search"
        />
      </b-nav-form>

      <b-navbar-nav class="ml-auto">
        <!--<b-dropdown text="Lista 1" size="sm">
          <b-dropdown-item href="/mainuser">Twój profil</b-dropdown-item>
          <b-dropdown-item href="/mainuser/gallery">Galeria</b-dropdown-item>
          <b-dropdown-item href="/mainuser/settings">Ustawienia</b-dropdown-item>
          <b-dropdown-item href="/#">Premium</b-dropdown-item>
        </b-dropdown>
        <div id="dropdown" v-if="token != null">
          <b-dropdown id="dropdown" text="Dropdown1" variant="own" size="md" class="ml-2 mr-2">
            <b-dropdown-item href="/mainuser">Twój profil</b-dropdown-item>
            <b-dropdown-item href="/mainuser/gallery">Galeria</b-dropdown-item>
            <b-dropdown-item href="/mainuser/settings">Ustawienia</b-dropdown-item>
            <b-dropdown-item href="/#">Premium</b-dropdown-item>
          </b-dropdown>
        </div>
-->
        <b-nav-form id="logo" v-if="token != null" href="/mainuser">
          <b-avatar href="/mainuser" :src="getUrl(user_data.profile_picture)"></b-avatar>
          <div style="margin-left:5px;">{{ user_data.username }}</div>
        </b-nav-form>
        <!--
        <b-nav-form v-if="token != null">
          <b-button class="my-2 ml-2" type="button" size="sm" to="/mainuser">Twój profil</b-button>
        </b-nav-form>

        <b-nav-form v-if="token != null">
          <b-button class="my-2 ml-2" type="button" size="sm" to="/mainuser/search">Szukaj par</b-button>
        </b-nav-form>

        <b-nav-form v-if="token != null">
          <b-button class="my-2 ml-2" type="button" size="sm">Dopasuj</b-button>
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
        -->
        <b-nav-form v-if="token != null">
          <b-button class="my-2 ml-2" type="button" size="sm" to="/mainuser/gallery">Galeria</b-button>
        </b-nav-form>
        <b-nav-form v-if="token != null">
          <b-button class="my-2 ml-2" type="button" size="sm" v-b-modal.modal-scrollable>
            Polubienia
            <span class="badge badge-light">{{ user_likes.length }}</span>
          </b-button>
          <b-modal id="modal-scrollable" scrollable title="Polubienia" hide-footer>
            <b-row>
              <b-col cols="6">
                <b-row>
                  <b-col cols="12">
                    <h5>Polubiłeś: {{ user_liking.length }}</h5>
                  </b-col>
                </b-row>
              </b-col>

              <b-col cols="6">
                <b-row>
                  <b-col cols="12">
                    <h5>Lubią mnie: {{ user_likes.length }}</h5>
                  </b-col>
                </b-row>
              </b-col>
            </b-row>
          </b-modal>
        </b-nav-form>
        <b-nav-form v-if="token != null">
          <b-button class="my-2 ml-2" type="button" size="sm" to="/mainuser/settings">Ustawienia</b-button>
        </b-nav-form>
        <!-- zbedny button -->
        <!--<b-nav-form v-if="token != null">
          <b-button class="my-2 ml-2" type="button" size="sm" to="/#">Premium</b-button>
        </b-nav-form>-->
        <div v-if="token == null">
          <b-alert
            :show="dismissCountDown"
            fade
            class="mr-sm-2"
            variant="danger"
            @dismissed="dismissCountDown = 0"
            @dismiss-count-down="countDownChanged"
            >{{ msg }}</b-alert
          >
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
          <b-button v-on:click="login" type="submit" size="sm" class="my-2 ml-2">Zaloguj</b-button>
        </b-nav-form>

        <b-nav-form @submit.prevent="logout" v-if="token != null">
          <b-button type="submit" size="sm" class="my-2 ml-2">Wyloguj</b-button>
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
import axios from 'axios';
export default {
  name: 'Header',
  components: {},
  data() {
    return {
      token: localStorage.getItem('user-token') || null,
      username: '',
      password: '',
      searchText: '',
      pk: 0,
      dismissSecs: 5,
      dismissCountDown: 0,
      user_data: {},
      user_likes: [],
      user_liking: [],
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
        .get('http://127.0.0.1:8000/api/user/properties', {
          params: {},
          headers: {
            Authorization: 'Token ' + localStorage.getItem('user-token'),
          },
        })
        .then((response) => {
          console.log(response), (this.user_data = response.data);
        })
        .catch((errors) => console.log(errors));
    },
    getUserLikes() {
      console.log(this.user_data['pk']);
      axios
        .get('http://127.0.0.1:8000/api/user/get-user-are-liked', {
          params: {},
          headers: {
            Authorization: 'Token ' + localStorage.getItem('user-token'),
          },
        })
        .then((response) => {
          console.log(response), (this.user_likes = response.data);
        })
        .catch((errors) => console.log(errors));
    },
    getUserLiking() {
      axios
        .get('http://127.0.0.1:8000/api/user/get-user-liked', {
          params: {},
          headers: {
            Authorization: 'Token ' + localStorage.getItem('user-token'),
          },
        })
        .then((response) => {
          console.log(response), (this.user_liking = response.data);
        })
        .catch((errors) => console.log(errors));
    },
    getUrl(pic) {
      if (pic != null) return 'http://127.0.0.1:8000' + pic;
    },
    login() {
      axios
        .post('http://127.0.0.1:8000/api/user/login', {
          username: this.username,
          password: this.password,
        })
        .then((response) => {
          if (response.status == 200) {
            (this.error_message = ''),
              (this.showDismissibleAlert = false),
              (this.token = response.data.token),
              localStorage.setItem('user-token', response.data.token),
              this.$router.go();
          }
        })
        .catch((errors) => {
          if (errors.response.status != 200) {
            this.showMsg(), (this.msg = 'Błędny login lub hasło!');
          }
        });
    },
    logout() {
      let config = {
        headers: {
          Authorization: 'Token ' + localStorage.getItem('user-token'),
        },
      };

      axios
        .post('http://127.0.0.1:8000/api/user/logout', {}, config)
        .then((response) => {})
        .catch((errors) => {});
      localStorage.removeItem('user-token'), (this.token = null), this.$router.go();
    },
    search() {
      localStorage.setItem('search-text', this.searchText);
      if (this.$route.name == 'search') this.$router.go();
      else this.$router.push({ name: 'search' });
    },
  },
  created() {
    this.getUserData();
    this.getUserLikes();
    this.getUserLiking();
  },
};
</script>

<style scoped>
.alert {
  padding-block: 5px;
  margin-block: 5px;
  align-content: inherit;
}
.navbar {
  background-color: #9a3f66;
  /*background-color: #ce3854a1;*/
}
.b-avatar {
  margin-left: 10px;
}
.btn-secondary {
  background-color: #cdb7c0;
  color: #501c4c;
  font-weight: 600;
}

.btn-secondary:hover,
.btn-secondary:active {
  background-color: #0275d8;
  color: white;
  font-weight: 600;
}

#nav a.router-link-exact-active {
  background-color: #0275d8;
  color: white;
  font-weight: 600;
}
#logo {
  color: whitesmoke;
  font-weight: 600;
}
.dropdown {
  border: solid 1px rgba(82, 82, 82, 100);
  border-radius: 5px;
  background: blue !important;
  background-color: #cdb7c0 !important;
  color: #501c4c !important;
  font-weight: 600;
  width: 160px;
  height: 35px;
  position: flex;
  margin-block: 5px;
}
.dropdown:hover {
  background-color: #0275d8 !important;
  color: #ffffff !important;
}
.dropdown-text {
  color: #501c4c !important;
}

/*
.btn {
  background-color: #cdb7c0;
  color: #501c4c;
  font-weight: 600;
}
.my-dropdown .dropdown-menu .dropdown-item {
  background-color: #cdb7c0;
  color: #501c4c;
  font-weight: 600;
}
#__BVID__8__BV_toggle_ {
  background-color: #cdb7c0 !important;
  color: #501c4c !important;
  font-weight: 600 !important;
}
*/
#search {
  margin-left: 30px;
  margin-right: 10px;
}
</style>
