<template>
  <nav>
    <v-toolbar app clipped-left dense color="purple">
      <v-app-bar-nav-icon v-if="token != null" class="mr-2" @click="drawer = !drawer">
      </v-app-bar-nav-icon>

      <a v-if="token == null" id="logo" class="navbar-brand" href="/">
        e

        <v-icon color="red">mdi-heart</v-icon>

        Love
      </a>
      <a id="logo" v-else class="navbar-brand" href="/mainuser">
        e

        <v-icon color="red">mdi-heart</v-icon>

        Love
      </a>

      <b-nav-form id="logo" class="ml-1 mr-2" v-if="token != null">
      </b-nav-form>
      <b-nav-form id="search" @submit.prevent="search" v-if="token != null">
        <v-btn icon large>
          <v-icon>mdi-magnify</v-icon>
        </v-btn>
        <b-form-input
          id="search-input"
          size="sm"
          class="mr-sm-2"
          v-model="searchText"
          placeholder="wyszukaj użytkownika"
          name="search"
        />
      </b-nav-form>

      <v-spacer></v-spacer>

      <b-nav-form v-if="token != null">
        <div v-if="usersFriends.length != 0">
          <v-badge
            overlap
            offset-x="25"
            offset-y="27"
            bottom
            color="green"
            :content="usersFriends.length"
          >
            <v-btn
              icon
              color="purple darken-4"
              data-toggle="tooltip"
              title="Znajomi"
              x-large
              class="ml-2 mr-2"
              @click="friendlist = !friendlist"
            >
              <v-icon>mdi-account-group</v-icon>
            </v-btn>
          </v-badge>
        </div>
        <div v-else>
          <v-btn
            icon
            color="purple darken-4"
            data-toggle="tooltip"
            title="Znajomi"
            x-large
            class="ml-2 mr-2"
            @click="friendlist = !friendlist"
          >
            <v-icon>mdi-account-group</v-icon>
          </v-btn>
        </div>
      </b-nav-form>
      <b-nav-form v-if="token != null">
        <div v-if="usersWaiting.length != 0">
          <v-badge
            overlap
            offset-x="25"
            offset-y="27"
            bottom
            color="blue"
            :content="usersWaiting.length"
          >
            <v-btn
              icon
              color="purple darken-4"
              data-toggle="tooltip"
              title="Zaproszenia do znajomych"
              v-b-modal.notifications
              x-large
              class="ml-2 mr-2"
            >
              <v-icon>mdi-account-plus</v-icon>
            </v-btn>
          </v-badge>
        </div>
        <div v-else>
          <v-btn
            icon
            color="purple darken-4"
            data-toggle="tooltip"
            title="Zaproszenia do znajomych"
            v-b-modal.notifications
            x-large
            class="ml-2 mr-2"
          >
            <v-icon>mdi-account-plus</v-icon>
          </v-btn>
        </div>
      </b-nav-form>
      <b-nav-form v-if="token != null">
        <v-badge
          overlap
          offset-x="25"
          offset-y="27"
          bottom
          color="blue"
          content="0"
        >
          <v-btn
            icon
            color="purple darken-4"
            data-toggle="tooltip"
            title="Nowe wiadomości"
            v-b-modal.notifications
            x-large
            class="ml-2 mr-2"
          >
            <v-icon>mdi-message-text</v-icon>
          </v-btn>
        </v-badge>
      </b-nav-form>

      <b-nav-form v-if="token != null">
        <div v-if="user_likes.length != 0">
          <v-badge
            overlap
            offset-x="25"
            offset-y="27"
            bottom
            color="green"
            :content="user_likes.length"
          >
            <v-btn
              icon
              color="red lighten"
              data-toggle="tooltip"
              title="Polubienia"
              x-large
              v-b-modal.likes
              class="ml-2 mr-2"
            >
              <v-icon>mdi-heart</v-icon>
            </v-btn>
          </v-badge>
        </div>
        <div v-else>
          <v-btn
            icon
            color="red lighten"
            data-toggle="tooltip"
            title="Polubienia"
            x-large
            v-b-modal.likes
            class="ml-2 mr-2"
          >
            <v-icon>mdi-heart</v-icon>
          </v-btn>
        </div>

        <b-modal id="likes" scrollable title="Polubienia" hide-footer>
          <b-row>
            <b-col cols="6">
              <b-row>
                <b-col cols="12">
                  <h5>Polubieni: {{ user_likings.length }}</h5>
                  <b-list-group style="max-width: 300px">
                    <div
                      v-for="user_liking in user_likings"
                      v-bind:key="user_liking.pk"
                    >
                      <router-link
                        :to="{
                          name: 'userprofile',
                          params: { pk: user_liking.liked_by.pk },
                        }"
                      >
                        <b-list-group-item class="d-flex align-items-center">
                          <b-avatar
                            rounded
                            variant="info"
                            :src="getUrl(user_liking.liked_by.profile_picture)"
                            class="mr-3"
                            size="3rem"
                          ></b-avatar>
                          <span class="mr-auto">{{
                            user_liking.liked_by.username
                          }}</span>
                        </b-list-group-item>
                      </router-link>
                    </div>
                  </b-list-group>
                </b-col>
              </b-row>
            </b-col>

            <b-col cols="6">
              <b-row>
                <b-col cols="12">
                  <h5>Lubią mnie: {{ user_likes.length }}</h5>
                  <b-list-group style="max-width: 300px">
                    <div
                      v-for="user_like in user_likes"
                      v-bind:key="user_like.pk"
                    >
                      <router-link
                        :to="{
                          name: 'userprofile',
                          params: { pk: user_like.liked.pk },
                        }"
                      >
                        <b-list-group-item class="d-flex align-items-center">
                          <b-avatar
                            rounded
                            variant="info"
                            :src="getUrl(user_like.liked.profile_picture)"
                            class="mr-3"
                            size="3rem"
                          ></b-avatar>
                          <span class="mr-auto">{{
                            user_like.liked.username
                          }}</span>
                        </b-list-group-item>
                      </router-link>
                    </div>
                  </b-list-group>
                </b-col>
              </b-row>
            </b-col>
          </b-row>
        </b-modal>

        <b-modal
          id="notifications"
          scrollable
          title="Otrzymane zaproszenia do grona znajomych: "
          hide-footer
        >
          <b-row>
            <div
              v-for="user_friend in user_friends"
              v-bind:key="user_friend.friend.pk"
            >
              <b-list-group-item
                class="d-flex align-items-center"
                v-if="user_friend.status == 'waiting for your accept'"
              >
                <router-link
                  :to="{
                    name: 'userprofile',
                    params: { pk: user_friend.friend.pk },
                  }"
                >
                  <b-avatar
                    rounded
                    variant="info"
                    :src="getUrl(user_friend.friend.profile_picture)"
                    class="mr-3"
                    size="3rem"
                  ></b-avatar>
                  <span class="mr-auto"
                    ><strong>{{ user_friend.friend.username }}</strong></span
                  >
                </router-link>
                <b-button
                  class="ml-5 mr-1"
                  size="sm"
                  variant="success"
                  @click="acceptUser(user_friend.friend.pk)"
                  >Akceptuj</b-button
                >
                <b-button
                  class="ml-1"
                  size="sm"
                  variant="danger"
                  @click="rejectUser(user_friend.friend.pk)"
                  >Odrzuć</b-button
                >
              </b-list-group-item>
            </div>
          </b-row>
        </b-modal>
      </b-nav-form>

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
        <v-btn
          color="purple lighten-3"
          elevation="4"
          small
          v-on:click="login"
          type="submit"
          size="sm"
          class="my-2 ml-2"
          ><button class="font-weight-bold">Zaloguj</button></v-btn
        >
      </b-nav-form>

      <v-btn icon v-if="token != null">
        <b-avatar
          class="ml-5 mr-2"
          :src="getUrl(user_data.profile_picture)"
        ></b-avatar>
      </v-btn>
      <b-nav-form @submit.prevent="logout" v-if="token != null">
        <v-btn
          data-toggle="tooltip"
          title="Wyloguj"
          color="purple"
          medium
          type="submit"
          class="my-2 ml-2 mx-2"
          depressed
          ><v-icon large color="purple darken-4"
            >mdi-logout-variant</v-icon
          ></v-btn
        >
      </b-nav-form>
    </v-toolbar>

    <v-navigation-drawer v-model="drawer" absolute temporary class="purple">
      <v-list-item>
        <v-list-item-avatar size="95">
          <v-img :src="getUrl(user_data.profile_picture)"></v-img>
        </v-list-item-avatar>

        <v-list-item-content>
          <button class="text-lg-h6 white--text">
            {{ user_data.username }}
          </button>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list class="d-flex flex-row mb-6">
        <v-list-tile>
          <v-btn block x-large fixed depressed class="purple" href="/mainuser">
            <v-list-tile-action>
              <v-icon x-large class="ml-0" color="white"
                >mdi-card-account-details</v-icon
              >
            </v-list-tile-action>

            <v-list-tile-title class="white--text ml-10 mr-5"
              ><button class="text-lg-h6">Mój profil</button></v-list-tile-title
            >
          </v-btn>
        </v-list-tile>
      </v-list>
      <br />
      <v-list class="d-flex flex-row mb-6">
        <v-list-tile>
          <v-btn
            block
            x-large
            fixed
            depressed
            class="purple"
            href="/mainuser/search"
          >
            <v-list-tile-action>
              <v-icon x-large class="ml-0" color="white"
                >mdi-account-heart</v-icon
              >
            </v-list-tile-action>

            <v-list-tile-title class="white--text ml-10 mr-5"
              ><button class="text-lg-h6">Szukaj par</button></v-list-tile-title
            >
          </v-btn>
        </v-list-tile>
      </v-list>
      <br />
      <v-list class="d-flex flex-row mb-6">
        <v-list-tile>
          <v-dialog v-model="interactionsDialog" width="1000px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                block
                x-large
                fixed
                depressed
                v-bind="attrs"
                v-on="on"
                class="purple"
              >
                <v-icon x-large class="ml-0" color="white"
                  >mdi-account-switch</v-icon
                >

                <v-list-tile-title class="white--text ml-5 mr-5"
                  ><button class="text-lg-h6">
                    Powiadomienia
                  </button></v-list-tile-title
                >
              </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <v-spacer></v-spacer>
                <span class="headline">Powiadomienia</span>
                <v-spacer></v-spacer>
              </v-card-title>
              <v-card-text>
                <b-row>
                  <b-col cols="4">
                    <b-row>
                      <b-col cols="12">
                        <h5>Wysłane zaproszenia:</h5>

                        <div
                          v-for="user_friend in user_friends"
                          v-bind:key="user_friend.friend.pk"
                        >
                          <b-list-group-item
                            class="d-flex align-items-center"
                            v-if="user_friend.status == 'waiting'"
                          >
                            <router-link
                              :to="{
                                name: 'userprofile',
                                params: { pk: user_friend.friend.pk },
                              }"
                            >
                              <b-avatar
                                rounded
                                variant="info"
                                :src="
                                  getUrl(user_friend.friend.profile_picture)
                                "
                                class="mr-3"
                                size="3rem"
                              ></b-avatar>
                              <span class="mr-auto"
                                ><strong>{{
                                  user_friend.friend.username
                                }}</strong></span
                              >
                            </router-link>
                          </b-list-group-item>
                        </div>
                      </b-col>
                    </b-row>
                  </b-col>
                  <b-col cols="4">
                    <b-row>
                      <b-col cols="12">
                        <h5>Polubieni: {{ user_likings.length }}</h5>
                        <b-list-group style="max-width: 300px">
                          <div
                            v-for="user_liking in user_likings"
                            v-bind:key="user_liking.pk"
                          >
                            <router-link
                              :to="{
                                name: 'userprofile',
                                params: { pk: user_liking.liked_by.pk },
                              }"
                            >
                              <b-list-group-item
                                class="d-flex align-items-center"
                              >
                                <b-avatar
                                  rounded
                                  variant="info"
                                  :src="
                                    getUrl(user_liking.liked_by.profile_picture)
                                  "
                                  class="mr-3"
                                  size="3rem"
                                ></b-avatar>
                                <span class="mr-auto">{{
                                  user_liking.liked_by.username
                                }}</span>
                              </b-list-group-item>
                            </router-link>
                          </div>
                        </b-list-group>
                      </b-col>
                    </b-row>
                  </b-col>
                  <b-col cols="4">
                    <b-row>
                      <b-col cols="12">
                        <h5>Lubią mnie: {{ user_likes.length }}</h5>
                        <b-list-group style="max-width: 300px">
                          <div
                            v-for="user_like in user_likes"
                            v-bind:key="user_like.pk"
                          >
                            <router-link
                              :to="{
                                name: 'userprofile',
                                params: { pk: user_like.liked.pk },
                              }"
                            >
                              <b-list-group-item
                                class="d-flex align-items-center"
                              >
                                <b-avatar
                                  rounded
                                  variant="info"
                                  :src="getUrl(user_like.liked.profile_picture)"
                                  class="mr-3"
                                  size="3rem"
                                ></b-avatar>
                                <span class="mr-auto">{{
                                  user_like.liked.username
                                }}</span>
                              </b-list-group-item>
                            </router-link>
                          </div>
                        </b-list-group>
                      </b-col>
                    </b-row>
                  </b-col>
                </b-row>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>

                <v-btn
                  color="purple darken-1"
                  text
                  @click="interactionsDialog = false"
                >
                  Zamknij
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-list-tile>
      </v-list>
      <br />
      <v-list class="d-flex flex-row mb-6">
        <v-list-tile>
          <v-btn
            block
            x-large
            fixed
            depressed
            class="purple"
            href="/mainuser/gallery"
          >
            <v-list-tile-action>
              <v-icon x-large class="ml-0" color="white"
                >mdi-image-multiple</v-icon
              >
            </v-list-tile-action>

            <v-list-tile-title class="white--text ml-10 mr-5"
              ><button class="text-lg-h6">Galeria</button></v-list-tile-title
            >
          </v-btn>
        </v-list-tile>
      </v-list>
      <br />
      <v-list class="d-flex flex-row mb-6">
        <v-list-tile>
          <v-btn
            block
            x-large
            fixed
            depressed
            class="purple"
            href="/mainuser/settings"
          >
            <v-list-tile-action>
              <v-icon x-large class="ml-0" color="white">mdi-cogs</v-icon>
            </v-list-tile-action>

            <v-list-tile-title class="white--text ml-10 mr-5"
              ><button class="text-lg-h6">Ustawienia</button></v-list-tile-title
            >
          </v-btn>
        </v-list-tile>
      </v-list>
      <br />
    </v-navigation-drawer>

    <v-navigation-drawer v-model="friendlist" absolute right temporary>
      <br />
      <h5>Znajomi</h5>
      <div
        v-for="user_friend in user_friends"
        v-bind:key="user_friend.friend.pk"
      >
        <b-list-group-item
          class="d-flex align-items-right"
          v-if="user_friend.status == 'accepted'"
        >
          <router-link
            :to="{
              name: 'userprofile',
              params: { pk: user_friend.friend.pk },
            }"
          >
            <b-avatar
              badge
              badge-variant="dark"
              variant="info"
              :src="getUrl(user_friend.friend.profile_picture)"
              class="ml-1 mr-1"
              size="4rem"
            ></b-avatar>
            <span class="ml-2"
              ><strong>{{ user_friend.friend.username }}</strong></span
            >
          </router-link>
        </b-list-group-item>
      </div>
    </v-navigation-drawer>
  </nav>
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
      pk: 0,
      dismissSecs: 5,
      dismissCountDown: 0,
      user_data: {},
      user_likes: [],
      user_likings: [],
      user_friends: [],
      usersFriends: 0,
      usersWaiting: 0,
      newMessages: 0,
      drawer: false,
      friendlist: false,
      interactionsDialog: false,
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
      return axios
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
    //to jest routing aby dostać lajki które otrzymał przeglądany user
    getUserLikes() {
      //console.log(this.user_data['pk']);
      axios
        .get("http://127.0.0.1:8000/api/user/get-user-are-liked", {
          params: {},
          headers: {
            Authorization: "Token " + localStorage.getItem("user-token"),
          },
        })
        .then((response) => {
          console.log(response),
            (this.user_likes = response.data),
            console.log(this.user_likes);
        })
        .catch((errors) => console.log(errors));
    },
    //to jest routing do lajków które current user rozdał
    getUserLiking() {
      axios
        .get("http://127.0.0.1:8000/api/user/get-user-liked", {
          params: {},
          headers: {
            Authorization: "Token " + localStorage.getItem("user-token"),
          },
        })
        .then((response) => {
          console.log(response),
            (this.user_likings = response.data),
            console.log(this.user_likings);
        })
        .catch((errors) => console.log(errors));
    },
    getUrl(pic) {
      if (pic != null) return "http://127.0.0.1:8000" + pic;
    },
    login() {
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
    getUrl(pic) {
      if (pic != null) return "http://127.0.0.1:8000" + pic;
      else
        return "https://www.manufacturingusa.com/sites/manufacturingusa.com/files/default.png";
    },
    async getUserFriends() {
      await this.getUserData();
      //console.log("getFriends");
      return axios
        .get(
          "http://127.0.0.1:8000/api/user/friendlist",

          {
            params: { pk: this.user_data.pk },
            headers: {
              Authorization: "Token " + localStorage.getItem("user-token"),
            },
          }
        )
        .then((response) => {
          //console.log("userfriendlist:");
          console.log(response),
            (this.user_friends =
              response.data) /*, console.log(this.usersFriends = response.data.filter(element => element.status == 'friend'))*/;
          this.usersFriends = this.user_friends.filter((element) => {
            return element.status == "accepted";
          });
          this.usersWaiting = this.user_friends.filter((element) => {
            return element.status == "waiting for your accept";
          });
        })
        .catch((errors) => console.log(errors));
    },
    async counter() {
      await this.getUserFriends();
      console.log("onlyfriends");
      var onlyFriends = this.user_friends.filter((element) => {
        return element.status == "friend";
      });
      console.log(onlyFriends);
      this.usersFriends = onlyFriends.length;
    },
    acceptUser(pk) {
      //console.log("acceptuser");
      //console.log(pk);
      let config = {
        headers: {
          Authorization: "Token " + localStorage.getItem("user-token"),
        },
      };
      axios
        .patch(
          "http://127.0.0.1:8000/api/user/friendlist",
          {
            pk: pk,
          },
          config
        )
        .then((response) => {
          //console.log("user accepted");
          console.log(response);
        })
        .catch((errors) => console.log(errors));
    },
    rejectUser(pk) {
      //console.log("rejectUser");
      //console.log(pk);
      axios
        .delete(
          "http://127.0.0.1:8000/api/user/friendlist",

          {
            headers: {
              Authorization: "Token " + localStorage.getItem("user-token"),
            },
            data: {
              pk: pk,
            },
          }
        )
        .then((response) => {
          //console.log("rejected:");
          console.log(response);
        })
        .catch((errors) => console.log(errors));
      this.$router.go();
      //this.$forceUpdate();
    },
  },
  created() {
    if (this.token != null) {
      this.getUserData(),
        this.getUserLikes(),
        this.getUserLiking(),
        this.getUserFriends();
    }
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
  background-color: #9a3f66c2;
  /*background-color: #ce3854a1;*/
}
.b-avatar {
  margin-left: 10px;
}
.btn-secondary {
  background-color: #cdb7c0;
  color: #501c4c;
  font-weight: 600;
  border-radius: 8px;
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
.list-group-item {
  border-radius: 12px;
}

#search {
  margin-left: 100px;
  margin-right: 10px;
}
</style>
