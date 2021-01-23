<template>
  <nav>
    <v-app-bar app clipped-left dense color="purple">
      <v-app-bar-nav-icon
        v-if="token != null"
        class="mr-2"
        @click="drawer = !drawer"
      >
      </v-app-bar-nav-icon>

      <a v-if="token == null" id="logo" class="navbar-brand ml-0" href="/">
        <v-img
          max-height="150"
          max-width="150"
          contain
          :src="require('../../public/img/eloveLogo.png')"
        ></v-img>
      </a>

      <a id="logo" v-else class="navbar-brand" href="/mainuser">
        <v-img
          max-height="150"
          max-width="150"
          contain
          :src="require('../../public/img/eloveLogo.png')"
        ></v-img>
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
              color="purple darken-4"
              data-toggle="tooltip"
              title="Polubienia"
              x-large
              v-b-modal.likes
              class="ml-2 mr-2"
            >
              <v-icon>mdi-account-heart</v-icon>
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
              color="purple darken-4"
              data-toggle="tooltip"
              title="Pary"
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
            title="Pary"
            x-large
            v-b-modal.likes
            class="ml-2 mr-2"
          >
            <v-icon>mdi-heart</v-icon>
          </v-btn>
        </div>

        <b-modal id="likes" scrollable title="Otrzymane polubienia" hide-footer>
          <b-row>
            <b-col cols="1"></b-col>
            <b-col cols="10">
              <b-list-group style="max-width: 600px">
                <div v-for="user_like in user_likes" v-bind:key="user_like.pk">
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
            <b-col cols="1"></b-col>
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
                  @click="
                    acceptUser(user_friend.friend.pk);
                    toast(
                      'b-toaster-bottom-right',
                      'success',
                      'Zaakceptowano zaproszenie użytkownika.'
                    );
                  "
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
    </v-app-bar>

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
      <div class="purple">
        <b-list-group-item class="purple rounded">
          <h5 class="white--text">Znajomi</h5>
        </b-list-group-item>
      </div>
      <div
        v-for="user_friend in user_friends"
        v-bind:key="user_friend.friend.pk"
      >
        <b-list-group-item
          class="d-flex align-items-right"
          v-if="user_friend.status == 'accepted'"
        >
          <div>
            <v-dialog
              transition="dialog-bottom-transition"
              max-width="600"
              max-height="1000"
              scrollable
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  depressed
                  x-large
                  v-bind="attrs"
                  v-on="on"
                  block
                  @click="
                    getMessages(user_friend.friend.username);
                    getConversation(user_friend.friend.username);
                  "
                >
                  <v-avatar size="50" class="mr-1">
                    <img :src="getUrl(user_friend.friend.profile_picture)" />
                  </v-avatar>
                  <span class="ml-2"
                    ><strong
                      ><button>
                        {{ user_friend.friend.username }}
                      </button></strong
                    ></span
                  >
                </v-btn>
              </template>
              <template v-slot:default="dialog">
                <v-card>
                  <v-toolbar
                    class="purple white--text"
                    @click="getMessages(user_friend.friend.username)"
                  >
                    <v-avatar class="mr-3">
                      <img :src="getUrl(user_friend.friend.profile_picture)" />
                    </v-avatar>
                    <button bold>
                      Rozmowa z {{ user_friend.friend.username }}
                    </button>
                    <v-spacer></v-spacer
                    ><v-icon
                      large
                      @click="
                        getConversation(user_friend.friend.username);
                        getMessages(user_friend.friend.username);
                        historyDialog = true;
                      "
                      data-toggle="tooltip"
                      data-placement="bottom"
                      title="Historia rozmowy"
                      color="white"
                      >mdi-history</v-icon
                    ></v-toolbar
                  >
                  <v-dialog v-model="historyDialog" max-width="600" scrollable>
                    <v-card>
                      <v-toolbar class="purple white--text">
                        <h5>Historia rozmowy</h5>
                        <v-spacer></v-spacer
                        ><v-icon
                          large
                          @click="
                            getMessages(user_friend.friend.username);
                            historyDialog = false;
                          "
                          data-toggle="tooltip"
                          data-placement="bottom"
                          title="Zamknij"
                          color="white"
                          >mdi-close</v-icon
                        ></v-toolbar
                      >

                      <v-card-text class="purple lighten-5">
                        <br />
                        Początek rozmowy.
                        <v-divider></v-divider>
                        <div
                          v-for="allMessage in allMessages"
                          v-bind:key="allMessage.pk"
                        >
                          <div
                            v-if="
                              allMessage.sender.username == user_data.username
                            "
                          >
                            <v-row>
                              <v-col cols="4"></v-col>
                              <v-col cols="8">
                                <v-card
                                  elevation="5"
                                  class="mx-auto my-auto"
                                  outlined
                                  rounded
                                  data-toggle="tooltip"
                                  data-placement="bottom"
                                  :title="
                                    'Wysłano ' + extractDate(allMessage.created)
                                  "
                                >
                                  <v-card-text
                                    class="text-left text-body-1 font-weight-medium"
                                  >
                                    {{ allMessage.message }}
                                  </v-card-text>
                                </v-card>
                              </v-col>
                            </v-row>
                            <br />
                          </div>
                          <div v-else>
                            <v-row>
                              <v-col cols="1">
                                <v-avatar>
                                  <img
                                    :src="
                                      getUrl(allMessage.sender.profile_picture)
                                    "
                                  />
                                </v-avatar>
                              </v-col>
                              <v-col cols="8">
                                <v-card
                                  elevation="5"
                                  outlined
                                  class="ml-1 my-auto"
                                  rounded
                                  data-toggle="tooltip"
                                  data-placement="bottom"
                                  :title="
                                    'Wysłano ' + extractDate(allMessage.created)
                                  "
                                >
                                  <v-card-text
                                    class="text-left text-body-1 font-weight-medium"
                                  >
                                    {{ allMessage.message }}
                                  </v-card-text>
                                </v-card>
                              </v-col>
                              <v-col cols="3"></v-col>
                            </v-row>
                          </div>
                        </div>
                        <br />
                      </v-card-text>
                    </v-card>
                  </v-dialog>
                  <v-card-text
                    class="purple lighten-5"
                    @click="getMessages(user_friend.friend.username)"
                  >
                    <!--<div v-if="newMessages">-->
                    <div v-for="message in messages" v-bind:key="message.pk">
                      <div v-if="message.sender.username == user_data.username">
                        <v-row>
                          <v-col cols="4"></v-col>
                          <v-col cols="8">
                            <v-card
                              elevation="5"
                              class="mx-auto my-auto"
                              outlined
                              rounded
                              data-toggle="tooltip"
                              data-placement="bottom"
                              :title="'Wysłano ' + extractDate(message.created)"
                            >
                              <v-card-text
                                class="text-left text-body-1 font-weight-medium"
                              >
                                {{ message.message }}
                              </v-card-text>
                            </v-card>
                          </v-col>
                        </v-row>
                        <br />
                      </div>
                      <div v-else>
                        <v-row>
                          <v-col cols="1">
                            <v-avatar>
                              <img
                                :src="getUrl(message.sender.profile_picture)"
                              />
                            </v-avatar>
                          </v-col>
                          <v-col cols="8">
                            <v-card
                              elevation="5"
                              outlined
                              class="ml-1 my-auto"
                              rounded
                              data-toggle="tooltip"
                              data-placement="bottom"
                              :title="'Wysłano ' + extractDate(message.created)"
                            >
                              <v-card-text
                                class="text-left text-body-1 font-weight-medium"
                              >
                                {{ message.message }}
                              </v-card-text>
                            </v-card>
                          </v-col>
                          <v-col cols="3"></v-col>
                        </v-row>
                      </div>
                    </div>
                    <!--</div>-->
                  </v-card-text>

                  <v-card-actions
                    class="purple lighten-5"
                    @click="getMessages(user_friend.friend.username)"
                  >
                    <v-form>
                      <v-container>
                        <v-text-field
                          @click="getMessages(user_friend.friend.username)"
                          v-model="message"
                          prepend-icon="mdi-chat-processing"
                          :rules="[
                            (v) =>
                              (v || '').length <= 199 ||
                              'Maksymalna długość wiadomości to 200 znaków!',
                          ]"
                          :append-outer-icon="
                            message ? 'mdi-send' : 'mdi-send-lock'
                          "
                          filled
                          clear-icon="mdi-close-circle"
                          clearable
                          label="Wiadomość"
                          type="text"
                          @click:append-outer="
                            sendMessage(message, user_friend.friend.username);
                            getMessages(user_friend.friend.username);
                          "
                          @click:clear="clearMessage"
                        ></v-text-field>
                      </v-container>
                    </v-form>
                  </v-card-actions>
                </v-card>
              </template>
            </v-dialog>
          </div>
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
      userCouples: [],
      //newMessages: 0,
      drawer: false,
      friendlist: false,
      interactionsDialog: false,
      message: "",
      messages: [],
      allMessages: [],
      lastmessages: 10,
      historyDialog: false,
    };
  },
  methods: {
    //rerender(){
    //},
    clearMessage() {
      this.message = "";
    },
    extractDate(date) {
      var y = date.slice(0, 10);
      var t = date.slice(12, 19);
      var ty = t + ", " + y;
      return ty;
    },
    sendMessage(message, username) {
      console.log(message + " -> " + username);
      if (message.length > 200 || message.length == 0) {
        this.toast(
          "b-toaster-bottom-right",
          "danger",
          "Wiadomość nie może być pusta, lub dłuższa niż 200 znaków!"
        );
      } else {
        const config = {
          headers: {
            Authorization: "Token " + localStorage.getItem("user-token"),
          },
        };
        axios
          .post(
            "http://127.0.0.1:8000/api/chat/" + username + "/send-msg",
            { message: message },
            config
          )
          .then((response) => {
            if (response.status == 201) {
              console.log(response);
              this.clearMessage();
            }
          })
          .catch((errors) => {
            if (errors.response.status != 201) {
              console.log(errors);
            }
          });
      }
    },
    getMessages(username) {
      const config = {
        headers: {
          Authorization: "Token " + localStorage.getItem("user-token"),
        },
      };
      return axios
        .get(
          "http://127.0.0.1:8000/api/chat/" + username + "/get-last-x-msgs",
          {
            x: this.lastmessages,

            headers: {
              Authorization: "Token " + localStorage.getItem("user-token"),
            },
          }
        )
        .then((response) => {
          console.log(response), (this.messages = response.data);
        })
        .catch((errors) => console.log(errors));
    },
    getConversation(username) {
      const config = {
        headers: {
          Authorization: "Token " + localStorage.getItem("user-token"),
        },
      };
      return axios
        .get("http://127.0.0.1:8000/api/chat/" + username + "/get-all-msgs", {
          x: this.lastmessages,

          headers: {
            Authorization: "Token " + localStorage.getItem("user-token"),
          },
        })
        .then((response) => {
          console.log(response), (this.allMessages = response.data);
        })
        .catch((errors) => console.log(errors));
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
    async couples() {
      await this.getUserLikes();
      await this.getUserLiking();
      for (var i = 0; i < this.user_likes.length; i += 1) {
        for (var j = 0; j < this.user_likings.length; j += 1) {
          if (this.user_likes[i].liked.pk == this.user_likings[j].liked_by.pk) {
            this.couples.push(user_likes[i]);
          }
        }
      }
      console.log(this.couples.length);
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

    toast(toaster, variant = null, msg) {
      this.$bvToast.toast(msg, {
        title: `Info`,
        toaster: toaster,
        solid: true,
        variant: variant,
      });
    },
  },
  created() {
    if (this.token != null) {
      this.getUserData(),
        this.getUserLikes(),
        this.getUserLiking(),
        this.getUserFriends();
      //this.getMessages();
    }
  },
  watch: {},
  /*computed: {
    updatedMessages() {
      return this.getMessages(this.username);
    }
  },*/
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

.list-group-item {
  border-radius: 12px;
}
.v-text-field {
  width: 490px;
}
#search {
  margin-left: 100px;
  margin-right: 10px;
}
</style>
