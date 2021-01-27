<template>
  <v-container>
    <!--polubiony: {{ isUserLiked() }}
    user.data - user przeglądający
    user - user podglądany
    -->
    <br />
    <v-container>
      <b-sidebar id="sidebar-footer" aria-label="Okno chatu" no-header shadow>
        <template v-slot:footer="{ hide }">
          <div class="d-flex bg-dark text-light align-items-center px-3 py-2">
            <strong class="mr-auto"></strong>
            <b-button size="sm" @click="hide">Zamknij</b-button>
          </div>
        </template>
        <div class="px-3 py-2">
          <h3>Okienko chatu</h3>
        </div>
        <p>
          Początek rozmowy między {{ user_data.username }} a
          {{ user.username }}
        </p>
      </b-sidebar>
      <b-row>
        <b-col cols="1"> </b-col>
        <b-col cols="5">
          <div>
            <v-card
              outlined
              rounded
              class="mx-auto"
              max-width="500"
              height="700"
              color="purple"
            >
              <v-img
                class="white--text align-end"
                :src="getUrl(user.profile_picture)"
                aspect-ratio="1"
              >
                <v-app-bar flat color="rgba(0, 0, 0, 0)">
                  <v-menu
                    :close-on-content-click="false"
                    :nudge-width="200"
                    offset-x
                    left
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-btn fab small class="purple" v-bind="attrs" v-on="on"
                        ><v-app-bar-nav-icon color="white"></v-app-bar-nav-icon
                      ></v-btn>
                    </template>

                    <v-card>
                      <v-list>
                        <v-list-item>
                          <v-list-item-avatar>
                            <img :src="getUrl(user.profile_picture)" />
                          </v-list-item-avatar>

                          <v-list-item-content>
                            <v-list-item-title>{{
                              user.username
                            }}</v-list-item-title>
                            <v-list-item-subtitle
                              >({{ user.location }})</v-list-item-subtitle
                            >
                          </v-list-item-content>
                        </v-list-item>
                      </v-list>

                      <v-divider></v-divider>

                      <v-list>
                        <v-list-item>
                          <div v-if="isUserLiked() == false">
                            <v-btn
                              icon
                              x-large
                              @click="
                                likeUser();
                                toast(
                                  'b-toaster-bottom-right',
                                  'success',
                                  'Polubiono użytkownika!'
                                );
                              "
                              data-toggle="tooltip"
                              data-placement="bottom"
                              title="Polub"
                            >
                              <v-icon>mdi-heart</v-icon>
                            </v-btn>
                          </div>
                          <div v-else>
                            <v-btn
                              icon
                              x-large
                              @click="
                                dislikeUser();
                                toast(
                                  'b-toaster-bottom-right',
                                  'danger',
                                  'Usunięto polubienie.'
                                );
                              "
                              data-toggle="tooltip"
                              data-placement="bottom"
                              title="Usuń polubienie"
                            >
                              <v-icon color="red">mdi-heart</v-icon>
                            </v-btn>
                          </div>

                          <v-divider vertical></v-divider>

                          <v-dialog
                            transition="dialog-bottom-transition"
                            max-width="600"
                            max-height="1000"
                            scrollable
                          >
                            <template v-slot:activator="{ on, attrs }">
                              <v-btn
                                icon
                                x-large
                                data-toggle="tooltip"
                                data-placement="bottom"
                                title="Wyślij wiadomość"
                                v-bind="attrs"
                                v-on="on"
                                @click="getMessages(user.username)"
                              >
                                <v-icon color="purple"
                                  >mdi-message-processing</v-icon
                                >
                              </v-btn>
                            </template>
                            <template v-slot:default="dialog">
                              <v-card>
                                <v-toolbar
                                  class="purple white--text"
                                  @click="getMessages(user.username)"
                                >
                                  <v-avatar class="mr-3">
                                    <img :src="getUrl(user.profile_picture)" />
                                  </v-avatar>
                                  <button bold>
                                    Rozmowa z {{ user.username }}
                                  </button>
                                  <v-spacer></v-spacer>
                                  <v-icon
                                    large
                                    color="white"
                                    data-toggle="tooltip"
                                    data-placement="bottom"
                                    title="Aby czatować bez ograniczeń zaproś użytkownika do grona znajomych."
                                    >mdi-chat-question</v-icon
                                  >
                                </v-toolbar>
                                <v-card-text
                                  class="purple lighten-5"
                                  @click="getMessages(user.username)"
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
                                  @click="getMessages(user.username)"
                                >
                                  <v-form>
                                    <v-container>
                                      <div v-if="iAmSender == false">
                                        <v-text-field
                                          @click="getMessages(user.username)"
                                          v-model="message"
                                          prepend-icon="mdi-chat-processing"
                                          :rules="[
                                            (v) =>
                                              (v || '').length <= 199 ||
                                              'Maksymalna długość wiadomości to 200 znaków!',
                                          ]"
                                          :append-outer-icon="
                                            message
                                              ? 'mdi-send'
                                              : 'mdi-send-lock'
                                          "
                                          filled
                                          clear-icon="mdi-close-circle"
                                          clearable
                                          label="Wiadomość"
                                          type="text"
                                          @click:append-outer="
                                            sendMessage(message, user.username);
                                            getMessages(user.username);
                                          "
                                          @click:clear="clearMessage"
                                        ></v-text-field>
                                      </div>
                                      <div v-else>
                                        <v-text-field
                                          @click="getMessages(user.username)"
                                          prepend-icon="mdi-chat-processing"
                                          @click:append-outer="
                                            getMessages(user.username)
                                          "
                                          value="Wysłano wiadomość, czekaj na odpowiedź"
                                          label="Info"
                                          disabled
                                        ></v-text-field>
                                      </div>
                                    </v-container>
                                  </v-form>
                                </v-card-actions>
                              </v-card>
                            </template>
                          </v-dialog>
                          <v-divider vertical></v-divider>
                          <div v-if="userStatus() == 'none'">
                            <v-btn
                              :class="inv ? 'blue--text' : ''"
                              icon
                              x-large
                              @click="
                                inviteUser();
                                toast(
                                  'b-toaster-bottom-right',
                                  'info',
                                  'Wysłano zaproszenie do grona znajomych.'
                                );
                              "
                              data-toggle="tooltip"
                              data-placement="bottom"
                              title="Zaproś do grona znajomych"
                            >
                              <v-icon>mdi-account-plus</v-icon>
                            </v-btn>
                          </div>
                          <div v-else-if="userStatus() == 'friend'">
                            <v-btn
                              icon
                              x-large
                              data-toggle="tooltip"
                              data-placement="bottom"
                              title="Usuń z grona znajomych"
                              @click="removeFriend(user.pk)"
                            >
                              <v-icon color="green">mdi-account-check</v-icon>
                            </v-btn>
                          </div>
                          <div v-else-if="userStatus() == 'waiting'">
                            <v-btn
                              icon
                              x-large
                              data-toggle="tooltip"
                              data-placement="bottom"
                              title="Oczekiwanie na akceptację"
                              @click="
                                toast(
                                  'b-toaster-bottom-right',
                                  'info',
                                  'Użytkownik czeka na akceptację w twoich powiadomieniach!'
                                )
                              "
                            >
                              <v-icon color="blue">mdi-account-question</v-icon>
                            </v-btn>
                          </div>
                          <v-divider vertical></v-divider>
                          <v-btn
                            icon
                            x-large
                            @click="$bvModal.show('user_gallery')"
                            data-toggle="tooltip"
                            data-placement="bottom"
                            title="Zobacz galerię"
                          >
                            <v-icon color="purple">mdi-image-search</v-icon>
                          </v-btn>
                          <v-divider vertical></v-divider>
                          <div v-if="isUserLiked() == false">
                            <v-btn
                              icon
                              x-large
                              @click="blockUser()"
                              data-toggle="tooltip"
                              data-placement="bottom"
                              title="Zablokuj użytkownika"
                            >
                              <v-icon>mdi-lock</v-icon>
                            </v-btn>
                          </div>
                          <div v-else>
                            <v-btn
                              icon
                              x-large
                              @click="
                                toast(
                                  'b-toaster-bottom-right',
                                  'danger',
                                  'Nie możesz zablokować polubionego użytkownika.'
                                )
                              "
                              data-toggle="tooltip"
                              data-placement="bottom"
                              title="Nie możesz zablokować polubionego użytkownika."
                            >
                              <v-icon>mdi-lock-off</v-icon>
                            </v-btn>
                          </div>
                        </v-list-item>
                      </v-list>
                    </v-card>
                  </v-menu>
                  <div v-if="user.profile_picture == null">
                    <v-card-title class="black--text"
                      >{{ user.username }} ({{
                        getAge(user.birthday)
                      }})</v-card-title
                    >
                  </div>
                  <div v-else>
                    <v-card-title class="white--text"
                      >{{ user.username }} ({{
                        getAge(user.birthday)
                      }})</v-card-title
                    >
                  </div>
                </v-app-bar>
              </v-img>

              <v-card-text class="white--text">
                <h4 v-if="user.description != null">
                  <p class="font-italic">{{ user.description }}</p>
                </h4>
                <h4 v-else>
                  <p class="font-italic">Brak opisu.</p>
                </h4>
                <br />

                <b-modal
                  id="user_gallery"
                  size="lg"
                  title="Galeria użytkownika"
                  hide-footer
                >
                  <div v-if="images != []">
                    <div>
                      <b-carousel
                        id="carousel-1"
                        :interval="40000"
                        controls
                        indicators
                        background="#ababab"
                        img-width="100%"
                        img-height="100%"
                        style="text-shadow: 1px 1px 2px #333"
                      >
                        <div
                          v-for="image in images"
                          v-bind:key="image.id"
                          style="padding-bottom: 2px; img-height: 50%"
                        >
                          <b-carousel-slide
                            :img-src="getUrl(image.image)"
                          ></b-carousel-slide>
                        </div>
                      </b-carousel>
                    </div>
                    <footer>
                      <b-row>
                        <b-col cols="10"></b-col>
                        <b-col cols="2">
                          <b-button
                            class="mt-3"
                            block
                            @click="$bvModal.hide('bv-modal-example')"
                            >Zamknij</b-button
                          >
                        </b-col>
                      </b-row>
                      <b-row>
                        <b-col cols="1"></b-col>
                        <b-col cols="10"></b-col>
                        <div class="comments">
                          <br />
                        </div>
                        <b-col cols="1"></b-col>
                      </b-row>
                    </footer>
                  </div>
                  <div v-else>
                    <footer>
                      <b-row>
                        <b-col cols="1"></b-col>
                        <b-col cols="10"></b-col>
                        <div class="comments">
                          <h2>
                            Użytkownik nie posiada w swojej galerii żadnego
                            zdjęcia :(
                          </h2>
                          <br />
                        </div>
                        <b-col cols="1"></b-col>
                      </b-row>
                      <b-row>
                        <b-col cols="10"></b-col>
                        <b-col cols="2">
                          <b-button
                            class="mt-3"
                            block
                            @click="$bvModal.hide('bv-modal-example')"
                            >Zamknij</b-button
                          >
                        </b-col>
                      </b-row>
                    </footer>
                  </div>
                </b-modal>
              </v-card-text>
            </v-card>
          </div>
          <br />
        </b-col>
        <b-col cols="5">
          <div>
            <v-card>
              <v-toolbar flat color="purple" dark>
                <v-toolbar-title
                  >Profil użytkownika {{ user.username }}</v-toolbar-title
                >
              </v-toolbar>
              <v-tabs vertical color="purple">
                <v-tab> O mnie </v-tab>
                <v-tab> Mój wygląd </v-tab>
                <v-tab> Preferencje </v-tab>

                <v-tab-item color="purple">
                  <v-card flat>
                    <v-card-text>
                      <ul class="list-group list-group-flush">
                        <li class="list-group-item">
                          Imię i nazwisko:
                          <div class="oneline">
                            <p class="font-weight-bold">
                              {{ user.name }} {{ user.surname }}
                            </p>
                          </div>
                        </li>
                        <li class="list-group-item">
                          Płeć:
                          <div class="oneline">
                            <p class="font-weight-bold">{{ user.sex }}</p>
                          </div>
                        </li>
                        <li class="list-group-item">
                          Wiek:
                          <div class="oneline">
                            <p class="font-weight-bold">
                              {{ getAge(user.birthday) }}
                            </p>
                          </div>
                        </li>
                        <li class="list-group-item">
                          Mieszkam w:
                          <div class="oneline">
                            <p class="font-weight-bold">
                              {{ user.location }}
                            </p>
                          </div>
                        </li>
                        <li class="list-group-item">
                          Urodziny:
                          <div class="oneline">
                            <p class="font-weight-bold">
                              {{ user.birthday }}
                            </p>
                          </div>
                        </li>
                        <li class="list-group-item">
                          Status:
                          <div class="oneline">
                            <p class="font-weight-bold">
                              {{ user.status }}
                            </p>
                          </div>
                        </li>
                        <li class="list-group-item">
                          Wykształcenie:
                          <div class="oneline">
                            <p class="font-weight-bold">
                              {{ user.education }}
                            </p>
                          </div>
                        </li>

                        <li class="list-group-item">
                          <div v-if="user.is_smoking == 0">
                            Papierosy:
                            <div class="oneline">
                              <p class="font-weight-bold">nie palę</p>
                            </div>
                          </div>
                          <div v-else-if="user.is_smoking == 1">
                            Papierosy:
                            <div class="oneline">
                              <p class="font-weight-bold">okazjonalnie</p>
                            </div>
                          </div>
                          <div v-else-if="user.is_smoking == 2">
                            Papierosy:
                            <div class="oneline">
                              <p class="font-weight-bold">często</p>
                            </div>
                          </div>
                          <div v-else-if="user.is_smoking == 3">
                            Papierosy:
                            <div class="oneline">
                              <p class="font-weight-bold">codziennie</p>
                            </div>
                          </div>
                          <div v-else-if="user.is_smoking == 4">
                            Papierosy:
                            <div class="oneline">
                              <p class="font-weight-bold">nałogowo</p>
                            </div>
                          </div>
                          <div v-else>
                            Papierosy:
                            <div class="oneline">
                              <p class="font-weight-bold"></p>
                            </div>
                          </div>
                        </li>

                        <li class="list-group-item">
                          <div v-if="user.is_drinking_alcohol == 0">
                            Alkohol:
                            <div class="oneline">
                              <p class="font-weight-bold">nie piję</p>
                            </div>
                          </div>
                          <div v-else-if="user.is_drinking_alcohol == 1">
                            Alkohol:
                            <div class="oneline">
                              <p class="font-weight-bold">okazjonalnie</p>
                            </div>
                          </div>
                          <div v-else-if="user.is_drinking_alcohol == 2">
                            Alkohol:
                            <div class="oneline">
                              <p class="font-weight-bold">często</p>
                            </div>
                          </div>
                          <div v-else-if="user.is_drinking_alcohol == 3">
                            Alkohol:
                            <div class="oneline">
                              <p class="font-weight-bold">codziennie</p>
                            </div>
                          </div>
                          <div v-else-if="user.is_drinking_alcohol == 4">
                            Alkohol:
                            <div class="oneline">
                              <p class="font-weight-bold">nałogowo</p>
                            </div>
                          </div>
                          <div v-else>
                            Alkohol:
                            <div class="oneline">
                              <p class="font-weight-bold"></p>
                            </div>
                          </div>
                        </li>
                      </ul>
                    </v-card-text>
                  </v-card>
                </v-tab-item>
                <v-tab-item color="purple">
                  <v-card flat>
                    <v-card-text>
                      <ul class="list-group list-group-flush">
                        <li class="list-group-item">
                          Wzrost:
                          <div class="oneline" v-if="user.growth != null">
                            <p class="font-weight-bold">{{ user.growth }} cm</p>
                          </div>
                        </li>
                        <li class="list-group-item">
                          Waga:
                          <div class="oneline" v-if="user.weight != null">
                            <p class="font-weight-bold">{{ user.weight }} kg</p>
                          </div>
                        </li>

                        <li class="list-group-item">
                          Włosy:
                          <div class="oneline">
                            <p class="font-weight-bold">
                              {{ user.hair_length }}
                              {{ user.hair_color }}
                            </p>
                          </div>
                        </li>
                        <li class="list-group-item">
                          Kolor oczu:
                          <div class="oneline">
                            <p class="font-weight-bold">
                              {{ user.eye_color }}
                            </p>
                          </div>
                        </li>
                        <li class="list-group-item">
                          Sylwetka:
                          <div class="oneline">
                            <p class="font-weight-bold">
                              {{ user.body_type }}
                            </p>
                          </div>
                        </li>
                      </ul>
                    </v-card-text>
                  </v-card>
                </v-tab-item>
                <v-tab-item color="purple">
                  <v-card flat>
                    <v-card-text>
                      <ul class="list-group list-group-flush">
                        <li class="list-group-item">
                          Przedział wiekowy:
                          <div
                            class="oneline"
                            v-if="user_preferences.age_preference_min != null"
                          >
                            <p class="font-weight-bold">
                              od {{ user_preferences.age_preference_min }}
                            </p>
                          </div>

                          <div
                            class="oneline"
                            v-if="user_preferences.age_preference_max != null"
                          >
                            <p class="font-weight-bold">
                              do {{ user_preferences.age_preference_max }}
                            </p>
                          </div>
                        </li>

                        <li class="list-group-item">
                          Waga:
                          <div
                            class="oneline"
                            v-if="user_preferences.weight_preference != null"
                          >
                            <p class="font-weight-bold">
                              do {{ user_preferences.weight_preference }} kg
                            </p>
                          </div>
                        </li>
                        <li class="list-group-item">
                          Sylwetka:
                          <div class="oneline">
                            <p class="font-weight-bold">
                              {{ user_preferences.body_type_preference }}
                            </p>
                          </div>
                        </li>
                        <li class="list-group-item">
                          Moja orientacja:
                          <div class="oneline">
                            <p class="font-weight-bold">
                              {{ user.orientation }}
                            </p>
                          </div>
                        </li>

                        <li class="list-group-item">
                          <div
                            v-if="user_preferences.is_smoking_preference == 0"
                          >
                            Papierosy:
                            <div class="oneline">
                              <p class="font-weight-bold">nie pali</p>
                            </div>
                          </div>

                          <div
                            v-else-if="
                              user_preferences.is_smoking_preference == 1
                            "
                          >
                            Papierosy:
                            <div class="oneline">
                              <p class="font-weight-bold">okazjonalnie</p>
                            </div>
                          </div>
                          <div
                            v-else-if="
                              user_preferences.is_smoking_preference == 2
                            "
                          >
                            Papierosy:
                            <div class="oneline">
                              <p class="font-weight-bold">często</p>
                            </div>
                          </div>
                          <div
                            v-else-if="
                              user_preferences.is_smoking_preference == 3
                            "
                          >
                            Papierosy:
                            <div class="oneline">
                              <p class="font-weight-bold">codziennie</p>
                            </div>
                          </div>
                          <div
                            v-else-if="
                              user_preferences.is_smoking_preference == 4
                            "
                          >
                            Papierosy:
                            <div class="oneline">
                              <p class="font-weight-bold">nałogowo</p>
                            </div>
                          </div>
                          <div v-else>
                            Papierosy:
                            <div class="oneline">
                              <p class="font-weight-bold">obojętne</p>
                            </div>
                          </div>
                        </li>

                        <li class="list-group-item">
                          <div
                            v-if="
                              user_preferences.is_drinking_alcohol_preference ==
                              0
                            "
                          >
                            Alkohol:
                            <div class="oneline">
                              <p class="font-weight-bold">nie pije</p>
                            </div>
                          </div>
                          <div
                            v-else-if="
                              user_preferences.is_drinking_alcohol_preference ==
                              1
                            "
                          >
                            Alkohol:
                            <div class="oneline">
                              <p class="font-weight-bold">okazjonalnie</p>
                            </div>
                          </div>
                          <div
                            v-else-if="
                              user_preferences.is_drinking_alcohol_preference ==
                              2
                            "
                          >
                            Alkohol:
                            <div class="oneline">
                              <p class="font-weight-bold">często</p>
                            </div>
                          </div>
                          <div
                            v-else-if="
                              user_preferences.is_drinking_alcohol_preference ==
                              3
                            "
                          >
                            Alkohol:
                            <div class="oneline">
                              <p class="font-weight-bold">codziennie</p>
                            </div>
                          </div>
                          <div
                            v-else-if="
                              user_preferences.is_drinking_alcohol_preference ==
                              4
                            "
                          >
                            Alkohol:
                            <div class="oneline">
                              <p class="font-weight-bold">nałogowo</p>
                            </div>
                          </div>
                          <div v-else>
                            Alkohol:
                            <div class="oneline">
                              <p class="font-weight-bold">obojętnie</p>
                            </div>
                          </div>
                        </li>
                      </ul>
                    </v-card-text>
                  </v-card>
                </v-tab-item>
              </v-tabs>
            </v-card>
          </div>
        </b-col>
        <b-col cols="1"></b-col>
      </b-row>
    </v-container>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      user_data: {},
      user: {},
      user_preferences: {},
      images: {},
      like: "like",
      liked_user: {},
      user_likes: [],
      liked: false,
      blocked: false,
      user_blacklist: [],
      user_friendlist: [],
      user_friends: [],
      friends: [],
      fav: false,
      inv: false,
      message: "",
      messages: [],
      //allMessages: [],
      lastmessages: 10,
      iAmSender: false,
    };
  },
  methods: {
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
            "http://46.101.213.106:8000/api/chat/" + username + "/send-msg",
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
          "http://46.101.213.106:8000/api/chat/" +
            username +
            "/get-last-x-msgs",
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
    checkMessage() {
      var lastMessage = this.messages.pop();
      console.log(lastMessage.sender.username);
      if (lastMessage.sender.username == this.user_data.username) {
        this.iAmSender = true;
      } else {
        this.iAmSender = false;
      }
    },
    getUserData() {
      return axios
        .get("http://46.101.213.106:8000/api/user/properties", {
          params: {},
          headers: {
            Authorization: "Token " + localStorage.getItem("user-token"),
          },
        })
        .then((response) => {
          //console.log("current_user_data:")
          console.log(response), (this.user_data = response.data);
        })
        .catch((errors) => console.log(errors));
      //return this.user.data.pk;
    },
    async getUsers() {
      return axios
        .get(
          "http://46.101.213.106:8000/api/user/users/" + this.$route.params.pk,
          {
            params: {},
            headers: {
              Authorization: "Token " + localStorage.getItem("user-token"),
            },
          }
        )
        .then((response) => {
          console.log(response),
            (this.user = response.data),
            (this.user_preferences = this.user.preferences);
        })
        .catch((errors) => console.log(errors));
    },
    getUserImages() {
      axios
        .get(
          "http://46.101.213.106:8000/api/user/users/" +
            this.$route.params.pk +
            "/images",
          {
            headers: {
              Authorization: "Token " + localStorage.getItem("user-token"),
            },
          }
        )
        .then((response) => {
          this.images = response.data;
          //console.log(this.images[0]);
        })
        .catch((errors) => console.log(errors));
    },
    likeUser() {
      const config = {
        headers: {
          Authorization: "Token " + localStorage.getItem("user-token"),
        },
      };

      axios
        .post(
          "http://46.101.213.106:8000/api/user/create-like",
          { value: "like", pk: this.$route.params.pk },
          config
        )
        .then((response) => {
          console.log(response);
          this.$router.go();
        })
        .catch((errors) => console.log(errors));
      //this.$forceUpdate();
    },

    dislikeUser() {
      const config = {};
      axios
        .delete("http://46.101.213.106:8000/api/user/delete-like", {
          headers: {
            Authorization: "Token " + localStorage.getItem("user-token"),
          },
          data: {
            pk: this.getLikePK(),
          },
        })
        .then((response) => {
          console.log(response);
          this.$router.go();
        })
        .catch((errors) => console.log(errors));
    },
    getUserLikes() {
      axios
        .get(
          "http://46.101.213.106:8000/api/user/get-users-are-liked/" +
            this.$route.params.pk,
          {
            params: {},
            headers: {
              Authorization: "Token " + localStorage.getItem("user-token"),
            },
          }
        )
        .then((response) => {
          console.log(response),
            (this.user_likes = response.data),
            console.log(this.user_likes);
        })
        .catch((errors) => console.log(errors));
    },
    isUserLiked() {
      var liked = false;
      for (var i = 0; i < this.user_likes.length; i++) {
        if (this.user_likes[i].liked_by["pk"] == this.$route.params.pk) {
          return true;
        }
      }
      return false;
    },
    getLikePK() {
      var pk = -1;
      for (var i = 0; i < this.user_likes.length; i++) {
        if (this.user_likes[i].liked_by["pk"] == this.$route.params.pk) {
          pk = this.user_likes[i].pk;
        }
      }
      return pk;
    },
    blockUser() {
      const config = {
        headers: {
          Authorization: "Token " + localStorage.getItem("user-token"),
        },
      };
      if (this.userStatus() == "waiting" || this.userStatus() == "friend") {
        this.removeFriend(this.user.pk);
      }
      axios
        .post(
          "http://46.101.213.106:8000/api/user/blacklist",
          { pk: this.$route.params.pk },
          config
        )
        .then((response) => {
          console.log("blocked");
          console.log(response);
          this.$router.go(-1);
        })
        .catch((errors) => console.log(errors));
    },

    getAge(dateString) {
      var today = new Date();
      var birthDate = new Date(dateString);
      var age = today.getFullYear() - birthDate.getFullYear();
      var m = today.getMonth() - birthDate.getMonth();
      if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
        age--;
      }
      return age;
    },
    toast(toaster, variant = null, msg) {
      this.$bvToast.toast(msg, {
        title: `Info`,
        toaster: toaster,
        solid: true,
        variant: variant,
      });
    },
    getUrl(pic) {
      if (pic != null) return "http://elove.ml" + pic;
      else
        return "https://www.manufacturingusa.com/sites/manufacturingusa.com/files/default.png";
    },
    inviteUser() {
      //console.log("invite user");
      const config = {
        headers: {
          Authorization: "Token " + localStorage.getItem("user-token"),
        },
      };

      axios
        .post(
          "http://46.101.213.106:8000/api/user/friendlist",
          { pk: this.$route.params.pk },
          config
        )
        .then((response) => {
          //console.log("invited");
          console.log(response);
          //this.$router.go();
        })
        .catch((errors) => {
          if (errors.response.status == 400) {
            this.toast(
              "b-toaster-bottom-right",
              "danger",
              "Użytkownik już jest na liście zaproszonych! Czekaj na akceptację."
            );
          }
          //console.log(errors)
        });
    },
    removeFriend(pk) {
      //console.log("removeFriend");
      //console.log(pk);
      axios
        .delete(
          "http://46.101.213.106:8000/api/user/friendlist",

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
      //this.$router.go();
      this.toast(
        "b-toaster-bottom-right",
        "info",
        "Usunięto z grona znajomych."
      );
    },
    async getUserFriends() {
      await this.getUserData();
      console.log(this.user_data.pk);
      axios
        .get(
          "http://46.101.213.106:8000/api/user/friendlist",

          {
            params: { pk: this.user_data.pk },
            headers: {
              Authorization: "Token " + localStorage.getItem("user-token"),
            },
          }
        )
        .then((response) => {
          console.log(response), (this.user_friendlist = response.data);
        })
        .catch((errors) => console.log(errors));
    },
    userStatus() {
      var status = "none";
      for (var i = 0; i < this.user_friendlist.length; i++) {
        if (
          this.user_friendlist[i].status == "accepted" &&
          this.user_friendlist[i].friend.pk == this.user.pk
        ) {
          status = "friend";
          return status;
        } else if (
          this.user_friendlist[i].status == "waiting for your accept" &&
          this.user_friendlist[i].friend.pk == this.user.pk
        ) {
          status = "waiting";

          return status;
        }
      }
      console.log("none");
      return status;
    },
  },
  created() {
    this.getUsers();
    this.getUserImages();
    this.getUserData();
    this.getUserLikes();
    this.getUserFriends();
    //this.getUserBlacklist();
  },
  mounted() {
    this.getUserFriends();
  },
  //computed() {},
};
</script>

<style scoped>
.card-header {
  color: white;
}
.mainuser {
  margin: auto;
  width: 100%;
}
.card-img-top {
  /*height: 300px;*/
  object-fit: scale-down;
}
.card-text {
  font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;
  text-align: left;
  font-size: 20px;
}
.user-card {
  background: #a01818;
  color: white;
}
.sidebar {
  width: 300px;
  background-color: #a01818;
}
.svg {
  align-content: flex-start;
}

.tabs {
  background: #ff9292d5;
  border-radius: 12px;
  border-style: solid;
  border-width: 2px;
  border-color: #aa1d37;
}
.card-header {
  background: #df4040;
}
.oneline {
  display: inline-block;
}
.v-text-field {
  width: 490px;
}
</style>
