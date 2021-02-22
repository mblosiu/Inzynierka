<template>
  <div class="page">
    <v-container style="height: 100%">
      <br />
      <v-card color="purple">
        <v-card-title class="text-center justify-center py-6">
          <v-icon x-large color="white">mdi-cogs</v-icon>
          <h1 class="font-weight-bold display-5 white--text">
            Ustawienia konta
          </h1>
        </v-card-title>

        <v-tabs v-model="tab" color="purple" grow>
          <v-tab> Podstawowe informacje </v-tab>
          <v-tab> Wygląd </v-tab>
          <!--<v-tab> Zainteresowania </v-tab>-->
          <v-tab> Preferencje </v-tab>
          <v-tab> Opis profilu </v-tab>
          <v-tab> Prywatność </v-tab>
        </v-tabs>

        <v-tabs-items v-model="tab">
          <v-tab-item>
            <v-card flat>
              <v-row>
                <v-col cols="1"></v-col>
                <v-col cols="10">
                  <v-card-text>
                    <form @submit.prevent="editUserData">
                      <ul class="list-group list-group-flush">
                        <li class="list-group-item">
                          <b-row>
                            <b-col cols="6">
                              <label for="name" class="white-text">Imię</label>
                              <input
                                type="text"
                                id="name"
                                v-model="user_data.name"
                                class="form-control"
                              />
                            </b-col>
                            <b-col cols="6">
                              <label for="surname" class="grey-text"
                                >Nazwisko</label
                              >
                              <input
                                type="text"
                                id="surname"
                                v-model="user_data.surname"
                                class="form-control"
                              />
                            </b-col>
                          </b-row>
                        </li>
                        <ul class="list-group-item">
                          <b-row>
                            <b-col cols="6">
                              <label for="location" class="grey-text"
                                >Miejsce zamieszkania</label
                              >
                              <input
                                type="text"
                                id="location"
                                v-model="user_data.location"
                                class="form-control"
                              />
                            </b-col>
                            <b-col cols="6">
                              <label for="sex" class="grey-text">Płeć</label>
                              <b-form-select
                                class="form-control"
                                id="sex"
                                v-model="user_data.sex"
                                :options="sex_options"
                              ></b-form-select>
                            </b-col>
                          </b-row>
                        </ul>

                        <ul class="list-group-item">
                          <b-row>
                            <b-col cols="6">
                              <label for="is_smoking" class="grey-text"
                                >Papierosy</label
                              >
                              <b-form-select
                                class="form-control"
                                id="is_smoking"
                                v-model="user_data.is_smoking"
                                :options="smoking_options"
                              ></b-form-select>
                            </b-col>
                            <b-col cols="6">
                              <label for="is_drinking" class="grey-text"
                                >Alkohol</label
                              >
                              <b-form-select
                                class="form-control"
                                id="is_drinking"
                                v-model="user_data.is_drinking_alcohol"
                                :options="alcohol_options"
                              ></b-form-select>
                            </b-col>
                          </b-row>
                        </ul>

                        <ul class="list-group-item">
                          <b-row>
                            <b-col cols="6">
                              <label for="status" class="grey-text"
                                >Status</label
                              >
                              <b-form-select
                                class="form-control"
                                id="status"
                                v-model="user_data.status"
                                :options="status_options"
                              ></b-form-select>
                            </b-col>
                            <b-col cols="6">
                              <label for="education" class="grey-text"
                                >Edukacja</label
                              >
                              <b-form-select
                                class="form-control"
                                id="education"
                                v-model="user_data.education"
                                :options="education_options"
                              ></b-form-select>
                            </b-col>
                          </b-row>
                        </ul>

                        <ul class="list-group-item">
                          <b-row>
                            <b-col cols="3"></b-col>
                            <b-col cols="6">
                              <label for="status" class="grey-text"
                                >Orientacja</label
                              >
                              <b-form-select
                                class="form-control"
                                id="orientation"
                                v-model="user_data.orientation"
                                :options="orientation_options"
                              ></b-form-select>
                            </b-col>
                            <b-col cols="3"></b-col>
                          </b-row>
                        </ul>
                      </ul>

                      <div class="text-center mt-4">
                        <button type="submit" class="btn btn-success">
                          Zapisz
                        </button>
                      </div>
                      <p></p>
                    </form>
                  </v-card-text>
                </v-col>
                <v-col cols="1"></v-col>
              </v-row>
            </v-card>
          </v-tab-item>

          <v-tab-item>
            <v-card flat>
              <v-row>
                <v-col cols="1"></v-col>
                <v-col cols="10">
                  <v-card-text>
                    <form class="card" @submit.prevent="editUserData">
                      <ul class="list-group list-group-flush">
                        <ul class="list-group-item">
                          <b-row>
                            <b-col cols="6">
                              <label for="growth" class="white-text"
                                >Wzrost</label
                              >
                              <input
                                type="number"
                                id="growth"
                                v-model="user_data.growth"
                                class="form-control"
                                placeholder="Wzrost w cm"
                              />
                            </b-col>
                            <b-col cols="6">
                              <label for="weight" class="white-text"
                                >Waga</label
                              >
                              <input
                                type="text"
                                id="weight"
                                v-model="user_data.weight"
                                class="form-control"
                                placeholder="Waga w kg"
                              />
                            </b-col>
                          </b-row>
                        </ul>
                        <ul class="list-group-item">
                          <b-row>
                            <b-col cols="6">
                              <label for="hair_length" class="grey-text"
                                >Długość włosów</label
                              >
                              <b-form-select
                                class="form-control"
                                id="hair_length"
                                v-model="user_data.hair_length"
                                :options="hair_length_options"
                              ></b-form-select>
                            </b-col>
                            <b-col cols="6">
                              <label for="hair_color" class="grey-text"
                                >Kolor włosów</label
                              >
                              <b-form-select
                                class="form-control"
                                id="hair_color"
                                v-model="user_data.hair_color"
                                :options="hair_color_options"
                              ></b-form-select>
                            </b-col>
                          </b-row>
                        </ul>
                        <ul class="list-group-item">
                          <b-row>
                            <b-col cols="6">
                              <label for="body_type" class="grey-text"
                                >Sylwetka</label
                              >
                              <b-form-select
                                class="form-control"
                                id="body_type"
                                v-model="user_data.body_type"
                                :options="body_type_options"
                              ></b-form-select>
                            </b-col>
                            <b-col cols="6">
                              <label for="eye_color" class="grey-text"
                                >Kolor oczu</label
                              >
                              <b-form-select
                                class="form-control"
                                id="eye_color"
                                v-model="user_data.eye_color"
                                :options="eye_color_options"
                              ></b-form-select>
                            </b-col>
                          </b-row>
                          <br />
                          <b-row>
                            <br />
                            <b-col cols="12"> </b-col>
                          </b-row>
                        </ul>
                      </ul>

                      <div class="text-center mt-4">
                        <button type="submit" class="btn btn-success">
                          Zapisz
                        </button>
                      </div>
                      <p></p>
                    </form>
                  </v-card-text>
                </v-col>
                <v-col cols="1"></v-col>
              </v-row>
            </v-card>
          </v-tab-item>

          <v-tab-item>
            <v-card flat>
              <v-row>
                <v-col cols="1"></v-col>
                <v-col cols="10">
                  <v-card-text>
                    <form class="card" @submit.prevent="editUserPreferences">
                      <div class="card text-black">
                        <ul class="list-group list-group-flush">
                          <ul class="list-group-item">
                            <b-row>
                              <b-col cols="12">
                                <label
                                  for="age_preference_min"
                                  class="white-text"
                                  >Przedział wiekowy</label
                                >
                                <b-row>
                                  <b-col cols="3"></b-col>
                                  <b-col cols="3">
                                    <div>
                                      <div class="mt-2">
                                        Wiek minimalny:
                                        {{
                                          user_preferences.age_preference_min
                                        }}
                                      </div>
                                      <b-form-input
                                        id="user_preferences.age_preference_min"
                                        v-model="
                                          user_preferences.age_preference_min
                                        "
                                        type="range"
                                        min="18"
                                        :max="
                                          user_preferences.age_preference_max
                                        "
                                      ></b-form-input>
                                    </div>
                                  </b-col>
                                  <b-col cols="3">
                                    <div>
                                      <div class="mt-2">
                                        Wiek maksymalny:
                                        {{
                                          user_preferences.age_preference_max
                                        }}
                                      </div>
                                      <b-form-input
                                        id="age_preference_max"
                                        v-model="
                                          user_preferences.age_preference_max
                                        "
                                        type="range"
                                        :min="
                                          user_preferences.age_preference_min
                                        "
                                        max="100"
                                      ></b-form-input>
                                    </div>
                                  </b-col>
                                  <b-col cols="3"></b-col>
                                </b-row>
                              </b-col>
                            </b-row>
                          </ul>
                          <ul class="list-group-item">
                            <b-row>
                              <b-col cols="6">
                                <label
                                  for="body_type_preference"
                                  class="grey-text"
                                  >Sylwetka</label
                                >
                                <b-form-select
                                  class="form-control"
                                  id="body_type_preference"
                                  v-model="
                                    user_preferences.body_type_preference
                                  "
                                  :options="body_type_options"
                                ></b-form-select>
                              </b-col>
                              <b-col cols="6">
                                <label
                                  for="weight_preference"
                                  class="white-text"
                                  >Waga maks:
                                  {{
                                    user_preferences.weight_preference
                                  }}</label
                                >
                                <b-row>
                                  <b-col cols="2"></b-col>
                                  <b-col cols="8">
                                    <b-form-input
                                      id="weight_preference"
                                      v-model="
                                        user_preferences.weight_preference
                                      "
                                      type="range"
                                      min="40"
                                      max="200"
                                    ></b-form-input>
                                  </b-col>
                                  <b-col cols="2"></b-col>
                                </b-row>
                              </b-col>
                            </b-row>
                          </ul>

                          <ul class="list-group-item">
                            <b-row>
                              <b-col cols="6">
                                <label
                                  for="is_smoking_preference"
                                  class="grey-text"
                                  >Papierosy</label
                                >
                                <b-form-select
                                  class="form-control"
                                  id="is_smoking_preference"
                                  v-model="
                                    user_preferences.is_smoking_preference
                                  "
                                  :options="smoking_options2"
                                ></b-form-select>
                              </b-col>
                              <b-col cols="6">
                                <label
                                  for="is_drinking_preference"
                                  class="grey-text"
                                  >Alkohol</label
                                >
                                <b-form-select
                                  class="form-control"
                                  id="is_drinking_preference"
                                  v-model="
                                    user_preferences.is_drinking_alcohol_preference
                                  "
                                  :options="alcohol_options2"
                                ></b-form-select>
                              </b-col>
                            </b-row>
                          </ul>
                        </ul>

                        <div class="text-center mt-4">
                          <button type="submit" class="btn btn-success">
                            Zapisz
                          </button>
                        </div>
                        <p></p>
                      </div>
                    </form>
                  </v-card-text>
                </v-col>
                <v-col cols="1"></v-col>
              </v-row>
            </v-card>
          </v-tab-item>
          <v-tab-item>
            <v-card flat>
              <v-row>
                <v-col cols="1"></v-col>
                <v-col cols="10">
                  <v-card-text>
                    <form
                      class="description"
                      @submit.prevent="editUserDescription"
                    >
                      <b-row class="mt-2">
                        <b-col cols="2"></b-col>
                        <b-col sm="8">
                          <b-form-textarea
                            id="textarea-large"
                            size="lg"
                            v-model="user_data.description"
                            maxlength="200"
                            rows="4"
                            placeholder="Aktualnie nie posiadasz opisu. Napisz coś o sobie!"
                          ></b-form-textarea>
                          <small>
                            <strong>Maks 200 znaków.</strong>
                          </small>
                        </b-col>
                        <b-col cols="2"></b-col>
                      </b-row>
                      <div class="text-center mt-4">
                        <button type="submit" class="btn btn-success">
                          Zapisz
                        </button>
                        <p></p>
                      </div>
                    </form>
                    <br />
                    <br />
                    <br />
                    <br />
                    <br />
                  </v-card-text>
                </v-col>
                <v-col cols="1"></v-col>
              </v-row>
            </v-card>
          </v-tab-item>
          <v-tab-item>
            <v-card flat>
              <v-row>
                <v-col cols="1"></v-col>
                <v-col cols="10">
                  <v-card-text>
                    <form class="card" @submit.prevent="editUserSettings">
                      <ul class="list-group list-group-flush">
                        <ul class="list-group-item">
                          <b-row>
                            <b-col cols="6">
                              <label for="messages_privacy" class="grey-text"
                                >Otrzymywanie wiadomości:</label
                              >

                              <b-form-select
                                class="form-control"
                                id="messages_privacy"
                                v-model="user_data.settings.messages_privacy"
                                :options="messages_privacy"
                              ></b-form-select>
                              <!--<b-form-select
                                class="form-control"
                                id="msg_option"
                                v-model="msg_option"
                                :options="msgoptions"
                              ></b-form-select>-->
                            </b-col>
                            <b-col cols="6">
                              <label for="search_privacy" class="grey-text"
                                >Kto może mnie wyszukać:</label
                              >
                              <b-form-select
                                class="form-control"
                                id="search_privacy"
                                v-model="user_data.settings.search_privacy"
                                :options="search_privacy"
                              ></b-form-select>
                            </b-col>
                          </b-row>
                        </ul>

                        <ul class="list-group-item">
                          <b-row>
                            <b-col cols="3"></b-col>
                            <b-col cols="6">
                              <label for="hide_age" class="grey-text"
                                >Ukrywanie wieku:</label
                              >
                              <b-form-select
                                class="form-control"
                                id="hide_age"
                                v-model="user_data.settings.hide_age"
                                :options="hide_age"
                              ></b-form-select>
                            </b-col>
                            <b-col cols="3"> </b-col>
                          </b-row>
                        </ul>
                      </ul>
                      <div class="text-center mt-4">
                        <button type="submit" class="btn btn-success">
                          Zapisz
                        </button>
                      </div>
                      <p></p>
                    </form>
                    <br />
                    <br />
                    <br />
                    <b-row>
                      <v-spacer></v-spacer>

                      <v-btn
                        color="black"
                        elevation="5"
                        v-b-modal.modal-blacklist
                        @click="getUserBlacklist()"
                        ><button class="white--text font-weight-black">
                          Czarna lista</button
                        ><v-icon color="white" class="ml-2"
                          >mdi-account-cancel</v-icon
                        ></v-btn
                      >
                      <b-modal
                        id="modal-blacklist"
                        scrollable
                        title="Czarna lista"
                        hide-footer
                      >
                        <h5>
                          Zablokowani:
                          {{ blacklisted_users.length }}
                        </h5>
                        <b-list-group style="max-width: 470px">
                          <div
                            class="my-3"
                            v-for="blacklisted_user in blacklisted_users"
                            v-bind:key="blacklisted_user.pk"
                          >
                            <b-list-group-item
                              class="d-flex align-items-center"
                            >
                              <b-avatar
                                rounded
                                :src="
                                  getUrl(
                                    blacklisted_user.blacklisted.profile_picture
                                  )
                                "
                                class="mr-3"
                                size="4rem"
                              ></b-avatar>
                              <span class="mr-auto"
                                ><strong>{{
                                  blacklisted_user.blacklisted.username
                                }}</strong>
                              </span>
                              <b-button
                                squared
                                variant="outline-success"
                                @click="
                                  unblockUser(blacklisted_user.blacklisted.pk)
                                "
                                >Odblokuj</b-button
                              >
                            </b-list-group-item>
                          </div>
                        </b-list-group>
                      </b-modal>
                      <v-spacer></v-spacer>
                      <v-btn
                        color="red darken-1"
                        elevation="5"
                        @click.stop="deleteDialog = true"
                        ><button class="white--text font-weight-black">
                          Usuwanie konta
                        </button>
                        <v-icon class="ml-2" color="white"
                          >mdi-delete-empty</v-icon
                        ></v-btn
                      >
                      <v-dialog v-model="deleteDialog" max-width="450">
                        <v-card>
                          <v-card-title class="headline">
                            Czy jesteś pewien?
                          </v-card-title>
                          <v-divider></v-divider>
                          <v-card-text class="text-left">
                            Czy na pewno chcesz usunąć swoje konto z portalu
                            e-Love? Historia konta i wszystkie przypisane do
                            niego dane zostaną usunięte bezpowrotnie!
                            <v-divider></v-divider>

                            Aby kontynuować wpisz swoje hasło.
                          </v-card-text>
                          <v-row>
                            <v-col cols="3"> </v-col>
                            <v-col cols="6">
                              <v-text-field
                                label="Hasło*"
                                type="password"
                                required
                                name="password"
                                id="password"
                                v-model="password"
                              ></v-text-field>
                            </v-col>
                            <v-col cols="3"> </v-col>
                          </v-row>

                          <v-card-actions>
                            <v-btn
                              color="green darken-1"
                              x-large
                              text
                              @click="deleteDialog = false"
                              ><button class="font-weight-black">Powrót</button>
                            </v-btn>
                            <v-spacer></v-spacer>
                            <v-btn
                              color="red darken-1"
                              x-large
                              text
                              @click="deleteAccount()"
                              ><button class="font-weight-black">
                                Usuń konto
                              </button>
                            </v-btn>
                          </v-card-actions>
                        </v-card>
                      </v-dialog>
                      <v-spacer></v-spacer>
                    </b-row>

                    <br />
                    <br />
                  </v-card-text>
                </v-col>
                <v-col cols="1"></v-col>
              </v-row>
            </v-card>
          </v-tab-item>
        </v-tabs-items>
      </v-card>
      <br />
    </v-container>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "UsersProfile",
  components: {},
  data() {
    return {
      placeholder: null,
      active: "",
      tab: null,
      checkedNames: [],
      special_options: [],
      user_data: {},
      user_preferences: {},
      calculated: 0,
      deleteDialog: false,
      password: "",
      //hide_age: 'everybody',
      //msg_option: "od wszystkich",
      messages_privacy: [
        { text: "", value: null },
        { text: "od wszystkich", value: "everybody" },
        { text: "od płci przeciwnej", value: "oppSex" },
        { text: "od znajomych", value: "friends" },
      ],
      hide_age: [
        { text: "", value: null },
        { text: "ukryj mój wiek", value: "everybody" },
        { text: "pokaż mój wiek", value: "nobody" },
      ],
      comm_option: "od wszystkich",
      search_option: "wszyscy",
      search_privacy: [
        { text: "", value: null },
        { text: "wszyscy", value: "everybody" },
        { text: "płeć przeciwna", value: "oppSex" },
        { text: "ukrycie konta", value: "nobody" },
      ],
      new_likes: true,
      new_messages: true,
      new_comments: true,
      blacklisted_users: [],

      sex_options: [
        { value: null, text: "" },
        { value: "Mężczyzna", text: "mężczyzna" },
        { value: "Kobieta", text: "kobieta" },
        //{ value: "Inna", text: "inna" },
      ],
      orientation_options: [
        { value: null, text: "" },
        { value: "Hetero", text: "heteroseksualna" },
        { value: "Homo", text: "homoseksualna" },
        { value: "Bi", text: "biseksualna" },
      ],
      body_type_options: [
        { value: null, text: "" },
        { value: "Normalna", text: "normalna" },
        { value: "Szczupła", text: "szczupła" },
        { value: "Wysportowana", text: "wysportowana" },
        { value: "Puszysta", text: "puszysta" },
      ],
      eye_color_options: [
        { value: null, text: "" },
        { value: "Szare", text: "szare" },
        { value: "Niebieskie", text: "niebieskie" },
        { value: "Brązowe", text: "brązowe" },
        { value: "Piwne", text: "piwne" },
        { value: "Zielone", text: "zielone" },
      ],
      hair_color_options: [
        { value: null, text: "" },
        { value: "Blond", text: "blond" },
        { value: "Ciemny blond", text: "ciemny blond" },
        { value: "Jasny blond", text: "jasny blond" },
        { value: "Brązowe", text: "brązowe" },
        { value: "Ciemny brąz", text: "ciemny brąz" },
        { value: "Jasny brąz", text: "jasny brąz" },
        { value: "Czarne", text: "czarne" },
        { value: "Siwe", text: "siwe" },
        { value: "Inny", text: "inny" },
      ],
      hair_length_options: [
        { value: null, text: "" },
        { value: "Bardzo krótkie", text: "bardzo krótkie" },
        { value: "Krótkie", text: "krótkie" },
        { value: "Średnie", text: "średnie (do barków)" },
        { value: "Dłuższe", text: "dłuższe (do łopatek)" },
        { value: "Długie", text: "długie" },
        { value: "Bardzo długie", text: "bardzo długie (do pasa+)" },
        { value: "Łysy", text: "brak (łysy)" },
      ],
      status_options: [
        { value: null, text: "" },
        { value: "Uczeń", text: "uczeń" },
        { value: "Student", text: "student" },
        { value: "Pracuję", text: "pracuję" },
        { value: "Nie pracuję", text: "nie pracuję" },
        { value: "Emeryt", text: "emeryt" },
      ],
      education_options: [
        { value: null, text: "brak" },
        { value: "Podstawowe", text: "podstawowe" },
        { value: "Gimnazjalne", text: "gimnazjalne" },
        { value: "Zawodowe", text: "zawodowe" },
        { value: "Średnie", text: "średnie" },
        { value: "Wyższe", text: "wyższe" },
      ],
      smoking_options: [
        { value: null, text: "" },
        { value: "0", text: "nie palę" },
        { value: "1", text: "okazjonalnie" },
        { value: "2", text: "często" },
        { value: "3", text: "codziennie" },
        { value: "4", text: "nałogowo" },
      ],
      smoking_options2: [
        { value: null, text: "" },
        { value: "0", text: "nie pali" },
        { value: "1", text: "okazjonalnie" },
        { value: "2", text: "często" },
        { value: "3", text: "codziennie" },
        { value: "4", text: "nałogowo" },
      ],
      alcohol_options: [
        { value: null, text: "" },
        { value: "0", text: "nie piję" },
        { value: "1", text: "okazjonalnie" },
        { value: "2", text: "często" },
        { value: "3", text: "codziennie" },
        { value: "4", text: "nałogowo" },
      ],
      alcohol_options2: [
        { value: null, text: "" },
        { value: "0", text: "nie pije" },
        { value: "1", text: "okazjonalnie" },
        { value: "2", text: "często" },
        { value: "3", text: "codziennie" },
        { value: "4", text: "nałogowo" },
      ],
    };
  },
  methods: {
    deleteAccount() {
      //console.log("usuwanie konta");
      axios
        .delete("https://elove.ml:8000/api/user/delete", {
          headers: {
            Authorization: "Token " + localStorage.getItem("user-token"),
          },
          data: {
            password: this.password,
          },
        })
        .then((response) => {
          //console.log("unblocked:");
          console.log(response);
          if (response.status == 200) {
            localStorage.removeItem("user-token");
            this.$router.go();
          } else {
            this.toast(
              "b-toaster-bottom-right",
              "danger",
              "Podano nieprawidłowe hasło!"
            );
          }
        })
        .catch((errors) => console.log(errors));
    },

    getUserBlacklist() {
      //console.log("getblacklist");
      axios
        .get(
          "https://elove.ml:8000/api/user/blacklist",

          {
            params: { pk: this.user_data.pk },
            headers: {
              Authorization: "Token " + localStorage.getItem("user-token"),
            },
          }
        )
        .then((response) => {
          //console.log("userblacklist:");
          console.log(response),
            (this.blacklisted_users =
              response.data); /*,
            console.log(this.blacklisted_users);*/
        })
        .catch((errors) => console.log(errors));
    },
    unblockUser(pk) {
      axios
        .delete(
          "https://elove.ml:8000/api/user/blacklist",

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
          //console.log("unblocked:");
          //console.log(response);
        })
        .catch((errors) => console.log(errors));
      this.$router.go();
    },
    getUserData() {
      axios
        .get("https://elove.ml:8000/api/user/properties", {
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
    editUserData() {
      let config = {
        headers: {
          Authorization: "Token " + localStorage.getItem("user-token"),
        },
      };
      axios
        .patch(
          "https://elove.ml:8000/api/user/properties",
          {
            surname: this.user_data.surname,
            name: this.user_data.name,
            location: this.user_data.location,
            sex: this.user_data.sex,
            is_smoking: this.user_data.is_smoking,
            is_drinking_alcohol: this.user_data.is_drinking_alcohol,
            status: this.user_data.status,
            education: this.user_data.education,
            growth: this.user_data.growth,
            weight: this.user_data.weight,
            hair_length: this.user_data.hair_length,
            hair_color: this.user_data.hair_color,
            eye_color: this.user_data.eye_color,
            body_type: this.user_data.body_type,
            favourite_place: this.user_data.favourite_place,
            passion: this.user_data.passion,
            orientation: this.user_data.orientation,
          },
          config
        )
        .then((response) => {
          if (response.status == 200) {
            this.toast(
              "b-toaster-bottom-right",
              "success",
              "Zapisano zmiany profilu."
            );
          }
          console.log(response);
        })
        .catch((errors) => {
          if (errors.response.status != 200) {
            this.toast(
              "b-toaster-bottom-right",
              "danger",
              "Formularz zawiera błędy!"
            );
          }
          console.log(errors);
        });
    },
    editUserSettings() {
      let config = {
        headers: {
          Authorization: "Token " + localStorage.getItem("user-token"),
        },
      };
      axios
        .patch(
          "https://elove.ml:8000/api/user/settings",
          {
            messages_privacy: this.user_data.settings.messages_privacy,
            hide_age: this.user_data.settings.hide_age,
            search_privacy: this.user_data.settings.search_privacy,
          },
          config
        )
        .then((response) => {
          if (response.status == 200) {
            this.toast(
              "b-toaster-bottom-right",
              "success",
              "Zapisano zmiany ustawień."
            );
          }
          console.log(response);
        })
        .catch((errors) => {
          if (errors.response.status != 200) {
            this.toast(
              "b-toaster-bottom-right",
              "danger",
              "Formularz zawiera błędy!"
            );
          }
          console.log(errors);
        });
    },
    editUserDescription() {
      let config = {
        headers: {
          Authorization: "Token " + localStorage.getItem("user-token"),
        },
      };
      axios
        .patch(
          "https://elove.ml:8000/api/user/properties",
          {
            description: this.user_data.description,
          },
          config
        )
        .then((response) => {
          console.log(response);
          if (response.status == 200) {
            this.toast(
              "b-toaster-bottom-right",
              "success",
              "Zaktualizowano opis profilu!"
            );
          }
        })
        .catch((errors) => console.log(errors));
    },
    editUserPrivate() {
      this.toast(
        "b-toaster-bottom-right",
        "success",
        "Zaktualizowano ustawienia prywatności!"
      );
    },
    getUserPreferences() {
      axios
        .get("https://elove.ml:8000/api/user/preferences", {
          params: {},
          headers: {
            Authorization: "Token " + localStorage.getItem("user-token"),
          },
        })
        .then((response) => {
          console.log(response), (this.user_preferences = response.data);
        })
        .catch((errors) => console.log(errors));
    },
    editUserPreferences() {
      let config = {
        headers: {
          Authorization: "Token " + localStorage.getItem("user-token"),
        },
      };
      axios
        .patch(
          "https://elove.ml:8000/api/user/preferences",
          {
            orientation: this.user_preferences.orientation,
            is_drinking_alcohol_preference: this.user_preferences
              .is_drinking_alcohol_preference,
            is_smoking_preference: this.user_preferences.is_smoking_preference,
            age_preference_min: this.user_preferences.age_preference_min,
            age_preference_max: this.user_preferences.age_preference_max,
            body_type_preference: this.user_preferences.body_type_preference,
            weight_preference: this.user_preferences.weight_preference,
            education_preference: this.user_preferences.education_preference,
            eye_color_preference: this.user_preferences.eye_color_preference,
            hair_length_preference: this.user_preferences
              .hair_length_preference,
            hair_color_preference: this.user_preferences.hair_color_preference,
          },
          config
        )
        .then((response) => {
          if (response.status == 200) {
            this.toast(
              "b-toaster-bottom-right",
              "success",
              "Zapisano zmiany profilu!"
            );
          }
          console.log(response);
        })
        .catch((errors) => {
          if (errors.response.status != 200) {
            this.toast(
              "b-toaster-bottom-right",
              "danger",
              "Formularz zawiera błędy!"
            );
          }
          console.log(errors);
        });
    },
    getUrl(pic) {
      if (pic != null) return "https://elove.ml" + pic;
      else
        return "https://www.manufacturingusa.com/sites/manufacturingusa.com/files/default.png";
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
    this.getUserData();
    this.getUserPreferences();
    this.getUserBlacklist();
  },
  //computed() {},
};
</script>

<style scoped>
.profile {
  width: 300px;
  min-height: 500px;
  margin-left: auto;
  margin-right: auto;
  border-radius: 25px;
  padding: 0.5cm;
  background: #fadbdb;
  color: white;
}
.preferences {
  width: 300px;
  min-height: 500px;
  margin-left: auto;
  margin-right: auto;

  border-radius: 25px;
  padding: 0.5cm;
  background: #fadbdb;
  color: white;
}
.settings {
  width: 300px;
  min-height: 500px;
  margin-left: auto;
  margin-right: auto;
  border-radius: 25px;
  padding: 0.5cm;
  background: #fadbdb;
  color: white;
}
table {
  margin-left: auto;
  margin-right: auto;
  width: 80%;
  position: relative;
}

.tabs {
  background: #db4460;
  border-radius: 12px;
  border-style: solid;
  border-width: 2px;
  border-color: #9a3f66;
}

.textarea {
  height: 100%;
  width: 100%;
  background-color: #e9bac2;
}
.card-text {
  font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;
  text-align: left;
  font-size: 60px;
}

.nav-link {
  color: white;
}
</style>
