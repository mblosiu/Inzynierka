<template>
  <v-container>
    <nav>
      <v-app-bar fixed app clipped-left dense color="purple">
        <v-app-bar-nav-icon
          color="white darken-1"
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

        <!--<b-nav-form id="logo" class="ml-1 mr-2" v-if="token != null">
        </b-nav-form>-->
        <b-nav-form id="search" @submit.prevent="search" v-if="token != null">
          <b-form-input
            id="search-input"
            size="sm"
            v-model="searchText"
            placeholder="wyszukaj użytkowników"
            name="search"
          />
        </b-nav-form>
        <v-btn
          v-if="token != null"
          icon
          large
          data-toggle="tooltip"
          title="Wyszukaj użytkowników po ich atrybutach i cechach"
        >
          <v-icon @click="search()">mdi-magnify</v-icon>
        </v-btn>

        <v-spacer class="hide-sm-and-down"></v-spacer>

        <b-nav-form v-if="token != null" class="hidden-sm-and-down">
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
        <b-nav-form v-if="token != null" class="hidden-sm-and-down">
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
        <b-nav-form v-if="token != null" class="hidden-sm-and-down">
          <div v-if="messagesFromStrangers.length != 0">
            <v-badge
              overlap
              offset-x="25"
              offset-y="27"
              bottom
              color="blue"
              :content="messagesFromStrangers.length"
            >
              <v-btn
                icon
                color="purple darken-4"
                data-toggle="tooltip"
                title="Konwersacje z nieznajomymi"
                x-large
                class="ml-2 mr-2"
                @click.stop="newMessagesDialog = true"
              >
                <v-icon>mdi-message-text</v-icon>
              </v-btn>
            </v-badge>
          </div>
          <div v-else>
            <v-btn
              icon
              color="purple darken-4"
              data-toggle="tooltip"
              title="Konwersacje z nieznajomymi"
              x-large
              class="ml-2 mr-2"
              @click.stop="newMessagesDialog = true"
            >
              <v-icon>mdi-message-text</v-icon>
            </v-btn>
          </div>
          <v-row justify="center">
            <v-dialog v-model="newMessagesDialog" width="500">
              <v-card>
                <v-card-title flex class="purple">
                  <v-spacer></v-spacer>
                  <span class="headline white--text"
                    >Konwersacje z nieznajomymi.</span
                  >
                  <v-spacer></v-spacer>
                </v-card-title>

                <v-row>
                  <v-col cols="1"></v-col>
                  <v-col cols="10">
                    <div
                      v-for="messagesFromStranger in messagesFromStrangers"
                      v-bind:key="messagesFromStranger.pk"
                    >
                      <b-list-group-item class="d-flex align-items-center">
                        <!--<router-link
                      :to="{
                        name: 'userprofile',
                        params: { pk: messagesFromStranger.sender.pk },
                      }"
                    >
                      <b-avatar
                        rounded
                        variant="info"
                        :src="
                          getUrl(messagesFromStranger.sender.profile_picture)
                        "
                        class="mr-3"
                        size="3rem"
                      ></b-avatar>
                      <span class="mr-auto"
                        ><strong>{{
                          messagesFromStranger.sender.username
                        }}</strong></span
                      >
                    </router-link>-->
                        <div>
                          <v-dialog
                            transition="dialog-bottom-transition"
                            max-width="600"
                            max-height="1000"
                            scrollable
                            origin="bottom center 0"
                          >
                            <template v-slot:activator="{ on, attrs }">
                              <v-spacer></v-spacer>
                              <v-btn
                                depressed
                                x-large
                                flat
                                v-bind="attrs"
                                v-on="on"
                                block
                                @click="
                                  getMessages(
                                    messagesFromStranger.sender.username
                                  )
                                "
                              >
                                <v-avatar size="50" class="mr-1">
                                  <img
                                    :src="
                                      getUrl(
                                        messagesFromStranger.sender
                                          .profile_picture
                                      )
                                    "
                                  />
                                </v-avatar>
                                <span class="ml-2"
                                  ><strong
                                    ><button>
                                      {{ messagesFromStranger.sender.username }}
                                    </button></strong
                                  ></span
                                >
                              </v-btn>
                              <v-spacer></v-spacer>
                            </template>
                            <template v-slot:default="dialog">
                              <v-card>
                                <v-toolbar
                                  class="purple white--text"
                                  @click="
                                    getMessages(
                                      messagesFromStranger.sender.username
                                    ) /*$vuetify.goTo(9999, options)*/
                                  "
                                >
                                  <router-link
                                    :to="{
                                      name: 'userprofile',
                                      params: {
                                        pk: messagesFromStranger.sender.pk,
                                      },
                                    }"
                                  >
                                    <v-avatar class="mr-3">
                                      <img
                                        :src="
                                          getUrl(
                                            messagesFromStranger.sender
                                              .profile_picture
                                          )
                                        "
                                      />
                                    </v-avatar>
                                  </router-link>
                                  <button bold>
                                    Rozmowa z
                                    {{ messagesFromStranger.sender.username }}
                                  </button>

                                  <v-spacer></v-spacer
                                  ><v-icon
                                    large
                                    @click="
                                      getMessages(
                                        messagesFromStranger.sender.username
                                      )
                                    "
                                    data-toggle="tooltip"
                                    data-placement="bottom"
                                    title="Nie jesteście znajomymi"
                                    color="white"
                                    >mdi-alert-circle-outline</v-icon
                                  ></v-toolbar
                                >

                                <v-card-text
                                  class="purple lighten-5"
                                  @click="
                                    getMessages(
                                      messagesFromStranger.sender.username
                                    )
                                  "
                                >
                                  <!--<div v-if="newMessages">-->
                                  <div
                                    v-for="message in messages"
                                    v-bind:key="message.pk"
                                  >
                                    <div
                                      v-if="
                                        message.sender.username ==
                                        user_data.username
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
                                              'Wysłano ' +
                                              extractDate(message.created)
                                            "
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
                                              :src="
                                                getUrl(
                                                  message.sender.profile_picture
                                                )
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
                                              'Wysłano ' +
                                              extractDate(message.created)
                                            "
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
                                  @click="
                                    getMessages(
                                      messagesFromStranger.sender.username
                                    )
                                  "
                                >
                                  <v-form>
                                    <v-container>
                                      <v-text-field
                                        @click="
                                          getMessages(
                                            messagesFromStranger.sender.username
                                          )
                                        "
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
                                          sendMessage(
                                            message,
                                            messagesFromStranger.sender.username
                                          );
                                          getMessages(
                                            messagesFromStranger.sender.username
                                          );
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
                  </v-col>
                  <v-col cols="1"></v-col>
                </v-row>

                <v-card-actions>
                  <v-spacer></v-spacer>

                  <v-btn
                    color="purple darken-1"
                    text
                    @click="newMessagesDialog = false"
                  >
                    Zamknij
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-row>
          <b-modal
            id="messages"
            scrollable
            title="Nowe wiadomości od nieznajomych: "
            hide-footer
          >
            <v-row>
              <v-col cols="1"></v-col>
              <v-col cols="10">
                <div
                  v-for="messagesFromStranger in messagesFromStrangers"
                  v-bind:key="messagesFromStranger.pk"
                >
                  <b-list-group-item class="d-flex align-items-center">
                    <!--<router-link
                      :to="{
                        name: 'userprofile',
                        params: { pk: messagesFromStranger.sender.pk },
                      }"
                    >
                      <b-avatar
                        rounded
                        variant="info"
                        :src="
                          getUrl(messagesFromStranger.sender.profile_picture)
                        "
                        class="mr-3"
                        size="3rem"
                      ></b-avatar>
                      <span class="mr-auto"
                        ><strong>{{
                          messagesFromStranger.sender.username
                        }}</strong></span
                      >
                    </router-link>-->
                    <div>
                      <v-dialog
                        transition="dialog-bottom-transition"
                        max-width="600"
                        max-height="1000"
                        scrollable
                        origin="bottom center 0"
                      >
                        <template v-slot:activator="{ on, attrs }">
                          <v-btn
                            depressed
                            x-large
                            flat
                            v-bind="attrs"
                            v-on="on"
                            block
                            @click="
                              getMessages(messagesFromStranger.sender.username);
                              v - b - modal.messages.close;
                            "
                          >
                            <v-avatar size="50" class="mr-1">
                              <img
                                :src="
                                  getUrl(
                                    messagesFromStranger.sender.profile_picture
                                  )
                                "
                              />
                            </v-avatar>
                            <span class="ml-2"
                              ><strong
                                ><button>
                                  {{ messagesFromStranger.sender.username }}
                                </button></strong
                              ></span
                            >
                          </v-btn>
                        </template>
                        <template v-slot:default="dialog">
                          <v-card>
                            <v-toolbar
                              class="purple white--text"
                              @click="
                                getMessages(
                                  messagesFromStranger.sender.username
                                ) /*$vuetify.goTo(9999, options)*/
                              "
                            >
                              <router-link
                                :to="{
                                  name: 'userprofile',
                                  params: {
                                    pk: messagesFromStranger.sender.pk,
                                  },
                                }"
                              >
                                <v-avatar class="mr-3">
                                  <img
                                    :src="
                                      getUrl(
                                        messagesFromStranger.sender
                                          .profile_picture
                                      )
                                    "
                                  />
                                </v-avatar>
                              </router-link>
                              <button bold>
                                Rozmowa z
                                {{ messagesFromStranger.sender.username }}
                              </button>

                              <v-spacer></v-spacer
                              ><v-icon
                                large
                                @click="
                                  getMessages(
                                    messagesFromStranger.sender.username
                                  )
                                "
                                data-toggle="tooltip"
                                data-placement="bottom"
                                title="Nie jesteście znajomymi"
                                color="white"
                                >mdi-alert-circle-outline</v-icon
                              ></v-toolbar
                            >

                            <v-card-text
                              class="purple lighten-5"
                              @click="
                                getMessages(
                                  messagesFromStranger.sender.username
                                )
                              "
                            >
                              <!--<div v-if="newMessages">-->
                              <div
                                v-for="message in messages"
                                v-bind:key="message.pk"
                              >
                                <div
                                  v-if="
                                    message.sender.username ==
                                    user_data.username
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
                                          'Wysłano ' +
                                          extractDate(message.created)
                                        "
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
                                          :src="
                                            getUrl(
                                              message.sender.profile_picture
                                            )
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
                                          'Wysłano ' +
                                          extractDate(message.created)
                                        "
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
                              @click="
                                getMessages(
                                  messagesFromStranger.sender.username
                                )
                              "
                            >
                              <v-form>
                                <v-container>
                                  <v-text-field
                                    @click="
                                      getMessages(
                                        messagesFromStranger.sender.username
                                      )
                                    "
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
                                      sendMessage(
                                        message,
                                        messagesFromStranger.sender.username
                                      );
                                      getMessages(
                                        messagesFromStranger.sender.username
                                      );
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
              </v-col>
              <v-col cols="1"></v-col>
            </v-row>
          </b-modal>
        </b-nav-form>

        <b-nav-form v-if="token != null" class="hidden-sm-and-down">
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
              color="purple darken-4"
              data-toggle="tooltip"
              title="Polubienia"
              x-large
              v-b-modal.likes
              class="ml-2 mr-2"
            >
              <v-icon>mdi-account-heart</v-icon>
            </v-btn>
          </div>

          <div v-if="userCouples.length != 0">
            <v-badge
              overlap
              offset-x="25"
              offset-y="27"
              bottom
              color="pink"
              :content="userCouples.length"
            >
              <v-btn
                icon
                color="red darken"
                data-toggle="tooltip"
                title="Pary"
                x-large
                v-b-modal.couples
                class="ml-2 mr-2"
              >
                <v-icon>mdi-heart</v-icon>
              </v-btn>
            </v-badge>
          </div>
          <div v-else>
            <v-btn
              icon
              color="purple darken-4"
              data-toggle="tooltip"
              title="Pary"
              x-large
              v-b-modal.couples
              class="ml-2 mr-2"
            >
              <v-icon>mdi-heart</v-icon>
            </v-btn>
          </div>

          <b-modal
            id="likes"
            scrollable
            title="Otrzymane polubienia"
            hide-footer
          >
            <v-row>
              <v-col cols="1"></v-col>
              <v-col cols="10">
                <b-list-group style="max-width: 600px">
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
              </v-col>
              <v-col cols="1"></v-col>
            </v-row>
          </b-modal>

          <b-modal id="couples" scrollable title="Pary" hide-footer>
            <v-row>
              <v-col cols="1"></v-col>
              <v-col cols="10">
                <b-list-group style="max-width: 600px">
                  <div
                    v-for="userCouple in userCouples"
                    v-bind:key="userCouple.pk"
                  >
                    <router-link
                      :to="{
                        name: 'userprofile',
                        params: { pk: userCouple.liked_by.pk },
                      }"
                    >
                      <b-list-group-item class="d-flex align-items-center">
                        <b-avatar
                          rounded
                          variant="info"
                          :src="getUrl(userCouple.liked_by.profile_picture)"
                          class="mr-3"
                          size="3rem"
                        ></b-avatar>
                        <span class="mr-auto">{{
                          userCouple.liked_by.username
                        }}</span>
                      </b-list-group-item>
                    </router-link>
                  </div>
                </b-list-group>
              </v-col>
              <v-col cols="1"></v-col>
            </v-row>
          </b-modal>

          <b-modal
            id="notifications"
            scrollable
            title="Otrzymane zaproszenia do grona znajomych: "
            hide-footer
          >
            <v-row>
              <v-col cols="1"></v-col>
              <v-col cols="10">
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
                        ><strong>{{
                          user_friend.friend.username
                        }}</strong></span
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
              </v-col>
              <v-col cols="1"></v-col>
            </v-row>
          </b-modal>
        </b-nav-form>

        <div v-if="token == null">
          <v-alert
            v-model="valert"
            class="mr-3 ml-3 hidden-sm-and-down"
            dense
            :type="alertType"
            transition="fade-transition"
          >
            {{ alertMsg }}
          </v-alert>
          <!--<b-alert
            :show="dismissCountDown"
            fade
            class="mr-sm-2"
            variant="danger"
            @dismissed="dismissCountDown = 0"
            @dismiss-count-down="countDownChanged"
            >{{ msg }}</b-alert
          >-->
        </div>
        <b-nav-form
          @submit.prevent="login"
          v-if="token == null"
          class="hidden-sm-and-down"
        >
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

        <v-menu transition="scroll-y-transition">
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              v-bind="attrs"
              v-on="on"
              v-if="token != null"
              color="purple lighten-2"
              medium
              class="ml-5 hidden-md-and-up"
            >
              <v-icon class="mr-2">mdi-account-details</v-icon
              ><button class="font-weight-bold">Menu</button>
            </v-btn>
          </template>
          <v-list class="purple">
            <v-list-item>
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
            </v-list-item>
          </v-list>
          <v-list class="purple">
            <v-list-item>
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
            </v-list-item>
          </v-list>
          <v-list class="purple">
            <v-list-item>
              <div v-if="messagesFromStrangers.length != 0">
                <v-badge
                  overlap
                  offset-x="25"
                  offset-y="27"
                  bottom
                  color="blue"
                  :content="messagesFromStrangers.length"
                >
                  <v-btn
                    icon
                    color="purple darken-4"
                    data-toggle="tooltip"
                    title="Nowe wiadomości od nieznajomych"
                    x-large
                    class="ml-2 mr-2"
                    @click.stop="newMessagesDialog = true"
                  >
                    <v-icon>mdi-message-text</v-icon>
                  </v-btn>
                </v-badge>
              </div>
              <div v-else>
                <v-btn
                  icon
                  color="purple darken-4"
                  data-toggle="tooltip"
                  title="Nowe wiadomości od nieznajomych"
                  x-large
                  class="ml-2 mr-2"
                  @click.stop="newMessagesDialog = true"
                >
                  <v-icon>mdi-message-text</v-icon>
                </v-btn>
              </div>
            </v-list-item>
          </v-list>
          <v-list class="purple">
            <v-list-item>
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
                  color="purple darken-4"
                  data-toggle="tooltip"
                  title="Polubienia"
                  x-large
                  v-b-modal.likes
                  class="ml-2 mr-2"
                >
                  <v-icon>mdi-account-heart</v-icon>
                </v-btn>
              </div>
            </v-list-item>
          </v-list>
          <v-list class="purple">
            <v-list-item>
              <div v-if="userCouples.length != 0">
                <v-badge
                  overlap
                  offset-x="25"
                  offset-y="27"
                  bottom
                  color="pink"
                  :content="userCouples.length"
                >
                  <v-btn
                    icon
                    color="red darken"
                    data-toggle="tooltip"
                    title="Pary"
                    x-large
                    v-b-modal.couples
                    class="ml-2 mr-2"
                  >
                    <v-icon>mdi-heart</v-icon>
                  </v-btn>
                </v-badge>
              </div>
              <div v-else>
                <v-btn
                  icon
                  color="purple darken-4"
                  data-toggle="tooltip"
                  title="Pary"
                  x-large
                  v-b-modal.couples
                  class="ml-2 mr-2"
                >
                  <v-icon>mdi-heart</v-icon>
                </v-btn>
              </div>
            </v-list-item>
          </v-list>
          <v-list class="purple">
            <v-list-item>
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
            </v-list-item>
          </v-list>
        </v-menu>

        <b-nav-form
          @submit.prevent="logout"
          v-if="token != null"
          class="hidden-sm-and-down"
        >
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

        <v-dialog transition="dialog-top-transition" max-width="400">
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              v-bind="attrs"
              v-on="on"
              v-if="token == null"
              color="purple lighten-3"
              elevation="4"
              small
              class="my-2 ml-2 hidden-md-and-up"
              ><button class="font-weight-bold">Logowanie</button></v-btn
            >
          </template>
          <template v-slot:default="dialog">
            <v-card>
              <v-card-title flex class="purple">
                <v-spacer></v-spacer>
                <span class="headline white--text">Logowanie</span>
                <v-spacer></v-spacer>
              </v-card-title>

              <v-card-actions>
                <v-card flat>
                  <v-form @submit.prevent="login" v-if="token == null">
                    <v-container>
                      <v-row>
                        <v-col cols="12" md="6">
                          <v-text-field
                            id="username"
                            class="mr-sm-2"
                            v-model="username"
                            name="username"
                            label="Nazwa użytkownika"
                            required
                          ></v-text-field>
                        </v-col>

                        <v-col cols="12" md="6">
                          <v-text-field
                            label="Hasło"
                            id="password"
                            class="mr-sm-2"
                            type="password"
                            v-model="password"
                            name="password"
                            required
                          ></v-text-field>
                        </v-col>
                      </v-row>
                      <v-row>
                        <v-spacer></v-spacer>
                        <v-alert
                          v-model="valert"
                          class="mr-3 ml-3"
                          dense
                          :type="alertType"
                          transition="fade-transition"
                        >
                          {{ alertMsg }}
                        </v-alert>
                        <v-spacer></v-spacer>
                      </v-row>
                      <v-row>
                        <v-btn
                          color="red darken-1"
                          text
                          @click="dialog.value = false"
                        >
                          Zamknij
                        </v-btn>
                        <v-spacer></v-spacer>
                        <v-btn
                          color="purple darken-1"
                          text
                          v-on:click="login"
                          type="submit"
                          >Zaloguj</v-btn
                        >
                      </v-row>
                    </v-container>
                  </v-form>
                </v-card>
              </v-card-actions>
            </v-card>
          </template>
        </v-dialog>
      </v-app-bar>

      <v-navigation-drawer
        v-model="drawer"
        temporary
        class="purple"
        width="300"
        style="position: fixed; top: 0; left: 0"
      >
        <v-row>
          <v-col cols="2"></v-col>
          <v-col cols="8">
            <v-list-item-avatar size="150">
              <v-img :src="getUrl(user_data.profile_picture)"></v-img>
            </v-list-item-avatar>
          </v-col>
          <v-col cols="2"></v-col>
        </v-row>
        <v-row>
          <v-col cols="1"></v-col>
          <v-col cols="10">
            <button class="text-lg-h6 white--text">
              {{ user_data.username }}
            </button>
          </v-col>
          <v-col cols="1"></v-col>
        </v-row>

        <v-divider></v-divider>

        <v-list class="d-flex flex-row mb-6">
          <div>
            <v-btn block x-large depressed class="purple" href="/mainuser">
              <div>
                <v-icon x-large class="ml-0" color="white"
                  >mdi-card-account-details</v-icon
                >
              </div>

              <div class="white--text ml-10 mr-5">
                <button class="text-lg-h6">Mój profil</button>
              </div>
            </v-btn>
          </div>
        </v-list>
        <br />
        <v-list class="d-flex flex-row mb-6">
          <div>
            <v-btn
              block
              x-large
              depressed
              class="purple"
              href="/mainuser/search"
            >
              <div>
                <v-icon x-large class="ml-0" color="white"
                  >mdi-account-heart</v-icon
                >
              </div>

              <div class="white--text ml-10 mr-5">
                <button class="text-lg-h6">Szukaj par</button>
              </div>
            </v-btn>
          </div>
        </v-list>
        <br />
        <v-list class="d-flex flex-row mb-6">
          <div>
            <v-dialog v-model="interactionsDialog" width="1000px">
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  block
                  x-large
                  depressed
                  v-bind="attrs"
                  v-on="on"
                  class="purple"
                >
                  <v-icon x-large class="ml-0" color="white"
                    >mdi-account-switch</v-icon
                  >

                  <div class="white--text ml-5 mr-5">
                    <button class="text-lg-h6">Interakcje</button>
                  </div>
                </v-btn>
              </template>
              <v-card>
                <v-card-title>
                  <v-spacer></v-spacer>
                  <span class="headline">Interakcje</span>
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
                                      getUrl(
                                        user_liking.liked_by.profile_picture
                                      )
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
                                    :src="
                                      getUrl(user_like.liked.profile_picture)
                                    "
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
          </div>
        </v-list>
        <br />
        <v-list class="d-flex flex-row mb-6">
          <div>
            <v-btn
              block
              x-large
              depressed
              class="purple"
              href="/mainuser/gallery"
            >
              <div>
                <v-icon x-large class="ml-0" color="white"
                  >mdi-image-multiple</v-icon
                >
              </div>

              <div class="white--text ml-10 mr-5">
                <button class="text-lg-h6">Galeria</button>
              </div>
            </v-btn>
          </div>
        </v-list>
        <br />
        <v-list class="d-flex flex-row mb-6">
          <div>
            <v-btn
              block
              x-large
              depressed
              class="purple"
              href="/mainuser/settings"
            >
              <div>
                <v-icon x-large class="ml-0" color="white">mdi-cogs</v-icon>
              </div>

              <div class="white--text ml-10 mr-5">
                <button class="text-lg-h6">Ustawienia</button>
              </div>
            </v-btn>
          </div>
        </v-list>
        <br />
      </v-navigation-drawer>

      <v-navigation-drawer
        v-model="friendlist"
        right
        temporary
        width="250"
        style="position: fixed; top: 0; right: 0"
      >
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
                origin="bottom center 0"
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
                    <!--<div
                    v-if="getLastMessage(user_friend.friend.username) == true"
                  >
                    <v-icon class="ml-2" color="purple darken-1"
                      >mdi-chat-alert</v-icon
                    >
                  </div>
                  <div v-else>
                    <v-icon class="ml-2" color="grey">mdi-chat-alert</v-icon>
                  </div>-->
                  </v-btn>
                </template>
                <template v-slot:default="dialog">
                  <v-card>
                    <v-toolbar
                      class="purple white--text"
                      @click="
                        getMessages(
                          user_friend.friend.username
                        ) /*$vuetify.goTo(9999, options)*/
                      "
                    >
                      <router-link
                        :to="{
                          name: 'userprofile',
                          params: { pk: user_friend.friend.pk },
                        }"
                      >
                        <v-avatar class="mr-3">
                          <img
                            :src="getUrl(user_friend.friend.profile_picture)"
                          />
                        </v-avatar>
                      </router-link>
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
                    <v-dialog
                      v-model="historyDialog"
                      max-width="600"
                      scrollable
                    >
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
                                      'Wysłano ' +
                                      extractDate(allMessage.created)
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
                                        getUrl(
                                          allMessage.sender.profile_picture
                                        )
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
                                      'Wysłano ' +
                                      extractDate(allMessage.created)
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
                        <div
                          v-if="message.sender.username == user_data.username"
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
                                  'Wysłano ' + extractDate(message.created)
                                "
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
                                :title="
                                  'Wysłano ' + extractDate(message.created)
                                "
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
    <!--<v-row justify="center">
      <v-dialog v-model="loginDialog" min-width="250" max-width="370">
        <v-card>
          <v-card-title flex class="purple">
            <v-spacer></v-spacer>
            <span class="headline white--text">Logowanie</span>
            <v-spacer></v-spacer>
          </v-card-title>

          <v-card-actions>
            <v-card flat>
              <v-form @submit.prevent="login" v-if="token == null">
                <v-container>
                  <v-row>
                    <v-col cols="12" md="6">
                      <v-text-field
                        id="username"
                        class="mr-sm-2"
                        v-model="username"
                        name="username"
                        label="Nazwa użytkownika"
                        required
                      ></v-text-field>
                    </v-col>

                    <v-col cols="12" md="6">
                      <v-text-field
                        label="Hasło"
                        id="password"
                        class="mr-sm-2"
                        type="password"
                        v-model="password"
                        name="password"
                        required
                      ></v-text-field>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-spacer></v-spacer>
                    <v-alert
                      v-model="valert"
                      class="mr-3 ml-3"
                      dense
                      :type="alertType"
                      transition="fade-transition"
                    >
                      {{ alertMsg }}
                    </v-alert>
                    <v-spacer></v-spacer>
                  </v-row>
                  <v-row>
                    <v-btn
                      color="red darken-1"
                      text
                      @click="loginDialog = false"
                    >
                      Zamknij
                    </v-btn>
                    <v-spacer></v-spacer>
                    <v-btn
                      color="purple darken-1"
                      text
                      v-on:click="login"
                      type="submit"
                      >Zaloguj</v-btn
                    >
                  </v-row>
                </v-container>
              </v-form>
            </v-card>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>-->
  </v-container>
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
      usersFriendsNames: [],
      usersWaiting: 0,
      userCouples: [],
      likingsUsers: [],
      likesUsers: [],
      drawer: false,
      friendlist: false,
      interactionsDialog: false,
      message: "",
      messages: [],
      allMessages: [],
      //lastMessage: [],
      userMessages: [],
      messagesFromFriends: [],
      messagesFromStrangers: [],
      lastmessages: 10,
      historyDialog: false,
      target: 9999,
      oneMessage: 1,
      newMessagesDialog: false,
      valert: false,
      alertType: null,
      alertMsg: null,
    };
  },
  methods: {
    clearMessage() {
      this.message = "";
    },
    extractDate(date) {
      var y = date.slice(0, 10);
      var t = date.slice(11, 19);
      var ty = t + ", " + y;
      return ty;
    },
    /*showMsg() {
      this.dismissCountDown = this.dismissSecs;
    },*/
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
            "https://elove.ml:8000/api/chat/" + username + "/send-msg",
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
          "https://elove.ml:8000/api/chat/" + username + "/get-last-x-msgs",
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
    /*getLastMessage(name) {
      const config = {
        headers: {
          Authorization: "Token " + localStorage.getItem("user-token"),
        },
      };
      var lastMessage = [];
      axios
        .get("http://127.0.0.1:8000/api/chat/" + name + "/get-last-x-msgs", {
          x: this.oneMessage,

          headers: {
            Authorization: "Token " + localStorage.getItem("user-token"),
          },
        })
        .then((response) => {
          console.log("lastMessage " + name);
          console.log(response), (this.lastMessage = response.data);
          console.log(this.lastMessage);
          if (this.lastMessage[0].receiver.username != name) {
            console.log("true");
            return true;
          } else {
            console.log("false");
            return false;
          }
        })
        .catch((errors) => console.log(errors));
    },*/
    getConversation(username) {
      const config = {
        headers: {
          Authorization: "Token " + localStorage.getItem("user-token"),
        },
      };
      return axios
        .get("https://elove.ml:8000/api/chat/" + username + "/get-all-msgs", {
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
    async getUserMessages() {
      await this.getUserFriends();
      return axios
        .get(
          "https://elove.ml:8000/api/chat/get-all-messages-received-by-user-pk",
          {
            params: {},
            headers: {
              Authorization: "Token " + localStorage.getItem("user-token"),
            },
          }
        )
        .then((response) => {
          //console.log("getuserMessages");
          console.log(response), (this.userMessages = response.data);

          var strangersNames = [];

          for (var i = 0; i < this.userMessages.length; i = i + 1) {
            if (
              this.usersFriendsNames.includes(
                this.userMessages[i].sender.username
              ) == false
            ) {
              if (
                false ==
                strangersNames.includes(this.userMessages[i].sender.username)
              ) {
                this.messagesFromStrangers.push(this.userMessages[i]);
                strangersNames.push(this.userMessages[i].sender.username);
              }
            }
          }
          //console.log("this.messagesFromStrangers");
          console.log(this.messagesFromStrangers);
        })
        .catch((errors) => console.log(errors));
    },
    getUserData() {
      return axios
        .get("https://elove.ml:8000/api/user/properties", {
          params: {},
          headers: {
            Authorization: "Token " + localStorage.getItem("user-token"),
          },
        })
        .then((response) => {
          console.log("getuserdata");
          console.log(response), (this.user_data = response.data);
        })
        .catch((errors) => console.log(errors));
    },
    //to jest routing aby dostać lajki które otrzymał przeglądany user
    async getUserLikes() {
      //console.log(this.user_data['pk']);
      return axios
        .get("https://elove.ml:8000/api/user/get-user-are-liked", {
          params: {},
          headers: {
            Authorization: "Token " + localStorage.getItem("user-token"),
          },
        })
        .then((response) => {
          console.log("userdata");
          console.log(response),
            (this.user_likes = response.data),
            console.log(this.user_likes);
        })
        .catch((errors) => console.log(errors));
    },
    //to jest routing do lajków które current user rozdał
    async getUserLiking() {
      await this.getUserLikes();
      return axios
        .get("https://elove.ml:8000/api/user/get-user-liked", {
          params: {},
          headers: {
            Authorization: "Token " + localStorage.getItem("user-token"),
          },
        })
        .then((response) => {
          console.log(response),
            (this.user_likings = response.data),
            console.log(this.user_likings);

          for (var i = 0; i < this.user_likings.length; i = i + 1) {
            //console.log(this.user_likings[i].liked_by.username);
            for (var j = 0; j < this.user_likes.length; j = j + 1) {
              if (
                this.user_likings[i].liked_by.username ==
                this.user_likes[j].liked.username
              ) {
                //console.log(this.user_likings[i].liked_by.username);
                this.userCouples.push(this.user_likings[i]);
              }
            }
          }
          //console.log(this.likingsUsers);
        })
        .catch((errors) => console.log(errors));
    },

    getUrl(pic) {
      if (pic != null) return "https://elove.ml" + pic;
    },
    login() {
      axios
        .post("https://elove.ml:8000/api/user/login", {
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
            //this.showMsg(),
            if (errors.response.data.detail == "account is not verified") {
              this.alertType = "warning";
              this.alertMsg = "Użytkownik niezweryfikowany.";
            } else {
              this.alertType = "error";
              this.alertMsg = "Błędny login lub hasło!";
            }

            (this.valert = true),
              setTimeout(() => {
                this.valert = false;
              }, 5000);
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
        .post("https://elove.ml:8000/api/user/logout", {}, config)
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
      if (pic != null) return "https://elove.ml" + pic;
      else
        return "https://www.manufacturingusa.com/sites/manufacturingusa.com/files/default.png";
    },
    async getUserFriends() {
      await this.getUserData();

      return axios
        .get(
          "https://elove.ml:8000/api/user/friendlist",

          {
            params: { pk: this.user_data.pk },
            headers: {
              Authorization: "Token " + localStorage.getItem("user-token"),
            },
          }
        )
        .then((response) => {
          console.log(response),
            (this.user_friends =
              response.data) /*, console.log(this.usersFriends = response.data.filter(element => element.status == 'friend'))*/;
          this.usersFriends = this.user_friends.filter((element) => {
            return element.status == "accepted";
          });
          this.usersWaiting = this.user_friends.filter((element) => {
            return element.status == "waiting for your accept";
          });
          this.usersFriendsNames = this.usersFriends.map(
            (a) => a.friend.username
          );
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
      let config = {
        headers: {
          Authorization: "Token " + localStorage.getItem("user-token"),
        },
      };
      axios
        .patch(
          "https://elove.ml:8000/api/user/friendlist",
          {
            pk: pk,
          },
          config
        )
        .then((response) => {
          console.log(response);
        })
        .catch((errors) => console.log(errors));
    },
    rejectUser(pk) {
      axios
        .delete(
          "https://elove.ml:8000/api/user/friendlist",

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
          console.log(response);
        })
        .catch((errors) => console.log(errors));
      this.$router.go();
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
      this.getUserMessages();
      //this.getMessages();
    }
    setTimeout(() => {
      this.valert = false;
    }, 5000);
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
.v-alert {
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
.scroll {
  height: 100%;
  overflow-y: scroll;
  height: 100vh;
}
.v-card__text,
.v-card__title {
  word-break: normal; /* maybe !important  */
}
</style>
