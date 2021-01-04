<template>
  <div class="page">
    <v-container>
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
          <v-tab> Zainteresowania </v-tab>
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
                            <b-col cols="12">
                              <!--<label for="special_options" class="grey-text">Znaki szczególne</label>
                          <br />
                          <input
                            type="checkbox"
                            id="glasses"
                            value="okulary"
                            v-model="special_options"
                          />
                          <label for="glasses">Okulary</label>
                          <input
                            type="checkbox"
                            id="freckles"
                            value="piegi"
                            v-model="special_options"
                          />
                          <label for="freckles">Piegi</label>
                          <input
                            type="checkbox"
                            id="scars"
                            value="blizny"
                            v-model="special_options"
                          />
                          <label for="scars">Blizny</label>
                          <input
                            type="checkbox"
                            id="body_piercing"
                            value="body piercing"
                            v-model="special_options"
                          />
                          <label for="body_piercing">Body piercing</label>
                          <input
                            type="checkbox"
                            id="tattoos"
                            value="tatuaże"
                            v-model="special_options"
                          />
                          <label for="tattoos">Tatuaże</label>
                          <br />
                        <span>Zaznaczono: {{ special_options }}</span>-->
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
                      <!--<ul class="list-group list-group-flush">
                        <ul class="list-group-item">
                          <b-row>
                            <b-col cols="6">
                          <label for="entertainment" class="grey-text">Rozrywka i hobby:</label>
                          <br />
                          <input type="checkbox" id="jack" value="Shopping" v-model="checkedNames" />
                          <label for="jack">Shopping</label>
                          <input type="checkbox" id="john" value="Netflix" v-model="checkedNames" />
                          <label for="john">Netflix</label>
                          <input type="checkbox" id="mike" value="Książki" v-model="checkedNames" />
                          <label for="mike">Książki</label>
                        </b-col>
                        <b-col cols="6">
                          <label for="sport" class="grey-text">Sport:</label>
                          <br />
                          <input
                            type="checkbox"
                            id="jack"
                            value="Piłka nożna"
                            v-model="checkedNames"
                          />
                          <label for="jack">Piłka nożna</label>
                          <input
                            type="checkbox"
                            id="john"
                            value="Koszykówka"
                            v-model="checkedNames"
                          />
                          <label for="john">Koszykówka</label>
                          <input type="checkbox" id="mike" value="Pływactwo" v-model="checkedNames" />
                          <label for="mike">Pływactwo</label>
                      </b-col>
                          </b-row>
                        </ul>
                        <ul class="list-group-item">
                          <b-row>
                            <b-col cols="6">
                              <label for="music" class="grey-text">Muzyka:</label>
                          <br />
                          <input type="checkbox" id="jack" value="Rock" v-model="checkedNames" />
                          <label for="jack">Rock</label>
                          <input type="checkbox" id="john" value="Jazz" v-model="checkedNames" />
                          <label for="john">Jazz</label>
                          <input type="checkbox" id="mike" value="Pop" v-model="checkedNames" />
                        <label for="mike">Pop</label>
                            </b-col>
                            <b-col cols="6">
                              <label for="cooking" class="grey-text">Kuchnia:</label>
                          <br />
                          <input type="checkbox" id="jack" value="Polska" v-model="checkedNames" />
                          <label for="jack">Polska</label>
                          <input
                            type="checkbox"
                            id="john"
                            value="Orientalna"
                            v-model="checkedNames"
                          />
                          <label for="john">Orientalna</label>
                          <input type="checkbox" id="mike" value="Studencka" v-model="checkedNames" />
                        <label for="mike">Studencka</label>
                            </b-col>
                          </b-row>
                        </ul>-->
                      <ul class="list-group-item">
                        <b-row>
                          <b-col cols="6">
                            <label for="favourite_place" class="white-text"
                              >Ulubione miejsce:</label
                            >
                            <input
                              type="text"
                              id="favourite_place"
                              v-model="user_data.favourite_place"
                              class="form-control"
                            />
                          </b-col>
                          <b-col cols="6">
                            <label for="passion" class="white-text"
                              >Największa pasja:</label
                            >
                            <input
                              type="text"
                              id="passion"
                              v-model="user_data.passion"
                              class="form-control"
                            />
                          </b-col>
                        </b-row>
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
                                <!--<input
                            type="number"
                            id="weight_preference"
                            placeholder="maksymalna waga"
                            v-model="user_preferences.weight_preference"
                            class="form-control"
                          />-->
                              </b-col>
                            </b-row>
                          </ul>
                          <ul class="list-group-item">
                            <b-row>
                              <b-col cols="6">
                                <label
                                  for="education_preference"
                                  class="white-text"
                                  >Edukacja</label
                                >
                                <b-form-select
                                  class="form-control"
                                  id="education_preference"
                                  v-model="
                                    user_preferences.education_preference
                                  "
                                  :options="education_options"
                                ></b-form-select>
                              </b-col>
                              <b-col cols="6">
                                <label
                                  for="eye_color_preference"
                                  class="grey-text"
                                  >Kolor oczu</label
                                >
                                <b-form-select
                                  class="form-control"
                                  id="eye_color_preference"
                                  v-model="
                                    user_preferences.eye_color_preference
                                  "
                                  :options="eye_color_options"
                                ></b-form-select>
                              </b-col>
                            </b-row>
                          </ul>
                          <ul class="list-group-item">
                            <b-row>
                              <b-col cols="6">
                                <label
                                  for="hair_length_preference"
                                  class="grey-text"
                                  >Długość włosów</label
                                >
                                <b-form-select
                                  class="form-control"
                                  id="hair_length_preference"
                                  v-model="
                                    user_preferences.hair_length_preference
                                  "
                                  :options="hair_length_options"
                                ></b-form-select>
                              </b-col>
                              <b-col cols="6">
                                <label
                                  for="hair_color_preference"
                                  class="grey-text"
                                  >Kolor włosów</label
                                >
                                <b-form-select
                                  class="form-control"
                                  id="hair_color_preference"
                                  v-model="
                                    user_preferences.hair_color_preference
                                  "
                                  :options="hair_color_options"
                                ></b-form-select>
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
                    <form class="card" @submit.prevent="editUserPrivate">
                      <ul class="list-group list-group-flush">
                        <ul class="list-group-item">
                          <b-row>
                            <b-col cols="6">
                              <label for="msg_option" class="grey-text"
                                >Otrzymywanie wiadomości:</label
                              >
                              <b-form-select
                                class="form-control"
                                id="msg_option"
                                v-model="msg_option"
                                :options="msgoptions"
                              ></b-form-select>
                            </b-col>
                            <b-col cols="6">
                              <label for="comm_option" class="grey-text"
                                >Otrzymywanie komentarzy:</label
                              >
                              <b-form-select
                                class="form-control"
                                id="comm_option"
                                v-model="comm_option"
                                :options="msgoptions"
                              ></b-form-select>
                            </b-col>
                          </b-row>
                        </ul>
                        <ul class="list-group-item">
                          <b-row>
                            <b-col cols="6">
                              <label for="search_option" class="grey-text"
                                >Kto może mnie wyszukać:</label
                              >
                              <b-form-select
                                class="form-control"
                                id="search_option"
                                v-model="search_option"
                                :options="searchoptions"
                              ></b-form-select>
                            </b-col>
                            <b-col cols="6">
                              <strong>Otrzymywanie powiadomień:</strong><br />
                              <b-form-checkbox
                                id="new_likes"
                                v-model="new_likes"
                                name="checkbox-1"
                                value="true"
                                unchecked-value="false"
                              >
                                Polubienia od innych użytkowników
                              </b-form-checkbox>
                              <b-form-checkbox
                                id="new_messages"
                                v-model="new_messages"
                                name="checkbox-1"
                                value="true"
                                unchecked-value="false"
                              >
                                Wiadomości prywatne
                              </b-form-checkbox>
                              <b-form-checkbox
                                id="new_comments"
                                v-model="new_comments"
                                name="checkbox-1"
                                value="true"
                                unchecked-value="false"
                              >
                                Komentarze pod moimi zdjęciami
                              </b-form-checkbox>
                            </b-col>
                          </b-row>
                        </ul>
                        <ul class="list-group-item">
                          <b-row>
                            <b-col cols="6">
                              <b-form-checkbox
                                id="hideage"
                                v-model="hideage"
                                name="checkbox-1"
                                value="true"
                                unchecked-value="false"
                              >
                                Ukryj mój wiek dla innych użytkowników
                              </b-form-checkbox>
                            </b-col>
                            <b-col cols="6">
                              <b-row>
                                <b-col cols="4"></b-col>
                                <b-col cols="4">
                                  <b-button
                                    v-b-modal.modal-blacklist
                                    @click="getUserBlacklist()"
                                    variant="dark"
                                    size="md"
                                    >Czarna lista</b-button
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
                                                blacklisted_user.blacklisted
                                                  .profile_picture
                                              )
                                            "
                                            class="mr-3"
                                            size="4rem"
                                          ></b-avatar>
                                          <span class="mr-auto"
                                            ><strong>{{
                                              blacklisted_user.blacklisted
                                                .username
                                            }}</strong>
                                          </span>
                                          <b-button
                                            squared
                                            variant="outline-success"
                                            @click="
                                              unblockUser(
                                                blacklisted_user.blacklisted.pk
                                              )
                                            "
                                            >Odblokuj</b-button
                                          >
                                        </b-list-group-item>
                                      </div>
                                    </b-list-group>
                                  </b-modal>
                                </b-col>
                                <b-col cols="4"></b-col>
                              </b-row>
                            </b-col>
                          </b-row>
                        </ul>
                        <ul class="list-group-item">
                          <b-row>
                            <b-col cols="4"></b-col>
                            <b-col cols="4">
                              <b-button
                                variant="danger"
                                size="lg"
                                @click="$bvModal.show('modal-scoped')"
                                >Usuń konto</b-button
                              >
                              <b-modal id="modal-scoped">
                                <template v-slot:modal-header="{ close }">
                                  <h5>Czy jesteś pewien?</h5>
                                </template>

                                <h6>
                                  Czy na pewno chcesz usunąć swoje konto z
                                  portalu e-Love? Konto zostanie usunięte
                                  bezpowrotnie!
                                </h6>

                                <template v-slot:modal-footer="{ cancel }">
                                  <b-button
                                    size="md"
                                    variant="secondary"
                                    class="mr-20 ml-20"
                                    @click="cancel()"
                                    >Nie</b-button
                                  >
                                  <b-button
                                    size="md"
                                    variant="danger"
                                    @click="deleteAccount"
                                    >Tak</b-button
                                  >
                                </template>
                              </b-modal>
                            </b-col>
                            <b-col cols="4"></b-col>
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
        </v-tabs-items>
      </v-card>
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
      hideage: false,
      msg_option: "od wszystkich",
      msgoptions: [
        { text: "od wszystkich", value: "od wszystkich" },
        { text: "od płci przeciwnej", value: "od płci przeciwnej" },
        { text: "od znajomych", value: "od znajomych" },
        { text: "od nikogo", value: "od nikogo" },
      ],
      comm_option: "od wszystkich",
      search_option: "wszyscy",
      searchoptions: [
        { text: "wszyscy", value: "wszyscy" },
        { text: "płeć przeciwna", value: "płeć przeciwna" },
        { text: "ukrycie konta", value: "ukrycie konta" },
      ],
      new_likes: true,
      new_messages: true,
      new_comments: true,
      blacklisted_users: [],

      sex_options: [
        { value: null, text: "" },
        { value: "Mężczyzna", text: "mężczyzna" },
        { value: "Kobieta", text: "kobieta" },
        { value: "Inna", text: "inna" },
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
        { value: "Szare", text: "zieone" },
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
      axios.delete("http://127.0.0.1:8000/api/user/delete", {
        headers: {
          Authorization: "Token " + localStorage.getItem("user-token"),
        },
      });
      localStorage.removeItem("user-token");
      this.$router.go();
    },

    getUserBlacklist() {
      //console.log("getblacklist");
      axios
        .get(
          "http://127.0.0.1:8000/api/user/blacklist",

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
      //console.log("unblockUser");
      //console.log(pk);
      axios
        .delete(
          "http://127.0.0.1:8000/api/user/blacklist",

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
    editUserData() {
      let config = {
        headers: {
          Authorization: "Token " + localStorage.getItem("user-token"),
        },
      };
      axios
        .patch(
          "http://127.0.0.1:8000/api/user/properties",
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
    editUserDescription() {
      let config = {
        headers: {
          Authorization: "Token " + localStorage.getItem("user-token"),
        },
      };
      axios
        .patch(
          "http://127.0.0.1:8000/api/user/properties",
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
        .get("http://127.0.0.1:8000/api/user/preferences", {
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
          "http://127.0.0.1:8000/api/user/preferences",
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
      if (pic != null) return "http://127.0.0.1:8000" + pic;
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
    getUserSettings() {},
    editUserSetting() {},
  },
  created() {
    this.getUserData();
    this.getUserPreferences();
    this.getUserSettings();
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
