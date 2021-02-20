<template>
  <v-content>
    <v-container>
      <br />
      <v-card class="mx-auto purple" elevation="5" max-width="1500">
        <v-row>
          <v-col cols="1">
            <v-icon
              medium
              color="purple lighten-3"
              data-toggle="tooltip"
              data-placement="left"
              title="Wyszukaj użytkowników za pomocą nałożonych filtrów, bądź konkretnego z nich po nazwie"
              >mdi-help-circle</v-icon
            >
          </v-col>
          <v-col cols="11"></v-col>
        </v-row>
        <form id="filters" @submit.prevent="getPageUsers">
          <v-row>
            <v-col cols="1"></v-col>
            <v-col cols="10">
              <!--form-->
              <v-row>
                <v-col md="2" lg="2" sm="6" xs="6">
                  <b-form-select
                    :options="sex_options"
                    class="ml-2"
                    id="sex"
                    v-model="sex"
                    size="md"
                    value="sex"
                    placeholder="Płeć"
                  ></b-form-select>
                </v-col>
                <v-col md="2" lg="2" sm="6" xs="6">
                  <input
                    class="form-control ml-2"
                    type="text"
                    placeholder="Lokacja"
                    id="location"
                    v-model="location"
                  />
                </v-col>
                <v-col cols="6" class="hidden-sm-and-down">
                  <v-card flat color="transparent">
                    <h5 class="white--text">
                      Przedział wiekowy: {{ age_min }} - {{ age_max }}
                    </h5>

                    <v-card-text>
                      <v-row>
                        <v-col cols="1"></v-col>
                        <v-col cols="5">
                          <div>
                            <b-form-input
                              id="age_min"
                              v-model="age_min"
                              type="range"
                              min="18"
                              :max="age_max"
                            ></b-form-input>
                          </div>
                        </v-col>
                        <v-col cols="5">
                          <div>
                            <b-form-input
                              id="age_max"
                              v-model="age_max"
                              type="range"
                              :min="age_min"
                              max="100"
                            ></b-form-input>
                          </div>
                        </v-col>
                        <v-col cols="1"></v-col>
                      </v-row>
                    </v-card-text>
                  </v-card>
                </v-col>

                <v-col cols="1" class="hidden-sm-and-down">
                  <button type="submit" @click="page = 1">
                    <v-btn x-large block color="purple lighten-2">
                      <b class="white--text">Filtruj</b>
                    </v-btn>
                  </button>
                </v-col>
              </v-row>
            </v-col>
            <v-col cols="1"></v-col>
          </v-row>
          <v-row class="hidden-md-and-up">
            <v-spacer></v-spacer>
            <v-card flat color="transparent">
              <h5 class="white--text">
                Przedział wiekowy: {{ age_min }} - {{ age_max }}
              </h5>

              <v-card-text>
                <v-row>
                  <v-col cols="1"></v-col>
                  <v-col cols="5">
                    <div>
                      <b-form-input
                        id="age_min"
                        v-model="age_min"
                        type="range"
                        min="18"
                        :max="age_max"
                      ></b-form-input>
                    </div>
                  </v-col>
                  <v-col cols="5">
                    <div>
                      <b-form-input
                        id="age_max"
                        v-model="age_max"
                        type="range"
                        :min="age_min"
                        max="100"
                      ></b-form-input>
                    </div>
                  </v-col>
                  <v-col cols="1"></v-col>
                </v-row>
              </v-card-text>
            </v-card>
            <v-spacer></v-spacer>
          </v-row>
          <v-row class="hidden-md-and-up">
            <v-spacer></v-spacer>
            <button type="submit" @click="page = 1">
              <v-btn x-large block color="purple lighten-2">
                <b class="white--text">Filtruj</b>
              </v-btn>
            </button>
            <v-spacer></v-spacer>
          </v-row>
        </form>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            @click="show = !show"
            flat
            block
            depressed
            color="purple lighten-0"
          >
            <b class="mr-2 white--text">Więcej filtrów</b>

            <v-btn icon class="purple lighten-1" small>
              <v-icon color="white">{{
                show ? "mdi-chevron-up" : "mdi-chevron-down"
              }}</v-icon>
            </v-btn>
          </v-btn>
        </v-card-actions>

        <v-expand-transition>
          <div v-show="show">
            <v-divider></v-divider>
            <v-row>
              <v-col cols="1"></v-col>
              <v-col>
                <th>
                  <b-form-select
                    :options="orientation_options"
                    class="ml-2"
                    id="orientation"
                    v-model="orientation"
                    size="md"
                    value="orientation"
                    placeholder="Orientacja"
                  ></b-form-select>
                </th>
              </v-col>
              <v-col>
                <th>
                  <b-form-select
                    :options="hair_color_options"
                    class="ml-2"
                    id="hair_color"
                    v-model="hair_color"
                    size="md"
                    value="hair_color"
                    placeholder="Kolor włosów"
                  ></b-form-select>
                </th>
              </v-col>
              <v-col>
                <th>
                  <b-form-select
                    :options="hair_length_options"
                    class="ml-2"
                    id="hair_length"
                    v-model="hair_length"
                    size="md"
                    value="hair_length"
                    placeholder="Długość włosów"
                  ></b-form-select>
                </th>
              </v-col>
              <!--<v-col>
                <th>
                  <b-form-select
                    :options="eye_color_options"
                    class="ml-2"
                    id="eye_color"
                    v-model="eye_color"
                    size="md"
                    value="eye_color"
                    placeholder="Kolor oczu"
                  ></b-form-select>
                </th>
              </v-col>-->
              <v-col>
                <th>
                  <b-form-select
                    :options="body_type_options"
                    class="ml-2"
                    id="body_type"
                    v-model="body_type"
                    size="md"
                    value="body_type"
                    placeholder="Sylwetka"
                  ></b-form-select>
                </th>
              </v-col>
              <v-col cols="1"></v-col>
            </v-row>
          </div>
        </v-expand-transition>
      </v-card>

      <v-row flex>
        <v-col cols="3"></v-col>

        <v-col cols="6">
          <div v-if="searchText">
            <div class="oneline">
              <h2 class="purple--text">Wyniki wyszukiwania dla frazy</h2>
            </div>
            <div class="oneline">
              <h2>
                <p class="font-italic text-primary">{{ searchText }}</p>
              </h2>
            </div>
          </div>
          <div v-else>
            <h2 class="purple--text">Wyniki wyszukiwania:</h2>
          </div>
        </v-col>

        <v-col cols="3"></v-col>
      </v-row>
      <v-row>
        <v-row>
          <v-spacer></v-spacer>
          <div class="text-center" @click="getPageUsers()">
            <v-pagination
              color="purple darken-1"
              v-model="page"
              :length="totalPages"
              :total-visible="7"
              prev-icon="mdi-menu-left"
              next-icon="mdi-menu-right"
            ></v-pagination>
          </div>
          <v-spacer></v-spacer>
        </v-row>
        <v-col cols="12" align-self="start" class="scroll">
          <v-row v-for="i in Math.ceil(users.length / 4)" v-bind:key="i">
            <v-col
              cols="3"
              v-for="user in users.slice((i - 1) * 4, i * 4)"
              v-bind:key="user.id"
              style="ml-2 mr-2"
            >
              <div v-if="user.settings.search_privacy == 'everybody'">
                <v-card
                  outlined
                  rounded
                  class="mx-auto"
                  max-width="500"
                  max-height="700"
                  color="purple"
                >
                  <router-link
                    :to="{ name: 'userprofile', params: { pk: user.pk } }"
                  >
                    <v-img
                      class="white--text align-end"
                      :src="getUrl(user.profile_picture)"
                      aspect-ratio="1"
                    >
                      <v-app-bar flat color="rgba(0, 0, 0, 0)" height="45">
                        <v-tooltip bottom>
                          <template v-slot:activator="{ on, attrs }">
                            <v-btn
                              fab
                              x-small
                              class="purple"
                              v-bind="attrs"
                              v-on="on"
                              ><v-icon color="white"
                                >mdi-information-variant</v-icon
                              ></v-btn
                            >
                          </template>

                          <v-card width="300" color="grey">
                            <v-list class="purple lighten-5">
                              <v-list-item>
                                <v-list-item-avatar size="70">
                                  <img :src="getUrl(user.profile_picture)" />
                                </v-list-item-avatar>

                                <v-list-item-content>
                                  <v-list-item-title
                                    ><h5>
                                      {{ user.username }}
                                    </h5></v-list-item-title
                                  >
                                  <v-list-item-subtitle
                                    ><h6>
                                      ({{ user.location }})
                                    </h6></v-list-item-subtitle
                                  >
                                </v-list-item-content>
                              </v-list-item>
                              <v-divider></v-divider>
                              <div v-if="user.description != null">
                                <v-list-item
                                  ><h6 class="font--italic text-left">
                                    {{ user.description }}
                                  </h6></v-list-item
                                >
                              </div>
                              <div v-else><h6>Brak opisu.</h6></div>
                            </v-list>
                          </v-card>
                        </v-tooltip>
                        <div
                          v-if="user.settings.hide_age == 'nobody'"
                          class="oneline"
                        >
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
                        </div>
                        <div v-else>
                          <div v-if="user.profile_picture == null">
                            <v-card-title class="black--text">{{
                              user.username
                            }}</v-card-title>
                          </div>
                          <div v-else>
                            <v-card-title class="white--text"
                              >{{ user.username }}
                            </v-card-title>
                          </div>
                        </div>
                      </v-app-bar>
                    </v-img>
                  </router-link>
                </v-card>
              </div>
              <div v-else-if="user.settings.search_privacy == 'oppSex'">
                <div v-if="user_data.sex != user.sex">
                  <v-card
                    outlined
                    rounded
                    class="mx-auto"
                    max-width="500"
                    max-height="700"
                    color="purple"
                  >
                    <router-link
                      :to="{ name: 'userprofile', params: { pk: user.pk } }"
                    >
                      <v-img
                        class="white--text align-end"
                        :src="getUrl(user.profile_picture)"
                        aspect-ratio="1"
                      >
                        <v-app-bar flat color="rgba(0, 0, 0, 0)" height="45">
                          <v-tooltip bottom>
                            <template v-slot:activator="{ on, attrs }">
                              <v-btn
                                fab
                                x-small
                                class="purple"
                                v-bind="attrs"
                                v-on="on"
                                ><v-icon color="white"
                                  >mdi-information-variant</v-icon
                                ></v-btn
                              >
                            </template>

                            <v-card width="300" color="grey">
                              <v-list class="purple lighten-5">
                                <v-list-item>
                                  <v-list-item-avatar size="70">
                                    <img :src="getUrl(user.profile_picture)" />
                                  </v-list-item-avatar>

                                  <v-list-item-content>
                                    <v-list-item-title
                                      ><h5>
                                        {{ user.username }}
                                      </h5></v-list-item-title
                                    >
                                    <v-list-item-subtitle
                                      ><h6>
                                        ({{ user.location }})
                                      </h6></v-list-item-subtitle
                                    >
                                  </v-list-item-content>
                                </v-list-item>
                                <v-divider></v-divider>
                                <div v-if="user.description != null">
                                  <v-list-item
                                    ><h6 class="font--italic text-left">
                                      {{ user.description }}
                                    </h6></v-list-item
                                  >
                                </div>
                                <div v-else><h6>Brak opisu.</h6></div>
                              </v-list>
                            </v-card>
                          </v-tooltip>
                          <div
                            v-if="user.settings.hide_age == 'nobody'"
                            class="oneline"
                          >
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
                          </div>
                          <div v-else>
                            <div v-if="user.profile_picture == null">
                              <v-card-title class="black--text">{{
                                user.username
                              }}</v-card-title>
                            </div>
                            <div v-else>
                              <v-card-title class="white--text"
                                >{{ user.username }}
                              </v-card-title>
                            </div>
                          </div>
                        </v-app-bar>
                      </v-img>
                    </router-link>
                  </v-card>
                </div>
              </div>
            </v-col>
          </v-row>
          <br />
        </v-col>
      </v-row>
    </v-container>
  </v-content>
</template>

<script>
import axios from "axios";
export default {
  name: "UsersList",
  components: {},
  data() {
    return {
      page: 1,
      itemsPerPage: 2,
      resultCount: 0,
      more_filters: false,
      searchText: null,
      birthday: null,
      sex: null,
      orientation: null,
      location: null,
      hair_color: null,
      hair_length: null,
      eye_color: null,
      body_type: null,
      users: [],
      users_count: "",
      profileImage: null,
      is_smoking: null,
      today: new Date(),
      birthDate: "",
      age: "",
      age_min: 18,
      age_max: 100,
      min: 18,
      max: 100,
      range: [18, 100],
      m: "",
      show: false,
      description: null,
      sex_options: [
        { value: null, text: "płeć" },
        { value: "Mężczyzna", text: "mężczyzna" },
        { value: "Kobieta", text: "kobieta" },
        //{ value: "Inna", text: "inna" },
      ],
      orientation_options: [
        { value: null, text: "orientacja" },
        { value: "Hetero", text: "heteroseksualna" },
        { value: "Homo", text: "homoseksualna" },
        { value: "Bi", text: "biseksualna" },
      ],
      location_options: [
        { value: null, text: "lokalizacja" },
        { value: "Poznań", text: "Poznań" },
        { value: "Warszawa", text: "Warszawa" },
      ],
      body_type_options: [
        { value: null, text: "Sylwetka" },
        { value: "Normalna", text: "normalna" },
        { value: "Szczupła", text: "szczupła" },
        { value: "Wysportowana", text: "wysportowana" },
        { value: "Puszysta", text: "puszysta" },
      ],
      eye_color_options: [
        { value: null, text: "Kolor oczu" },
        { value: "Szare", text: "szare" },
        { value: "Niebieskie", text: "niebieskie" },
        { value: "Brązowe", text: "brązowe" },
        { value: "Piwne", text: "piwne" },
        { value: "Szare", text: "zieone" },
      ],
      hair_color_options: [
        { value: null, text: "Kolor włosów" },
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
        { value: null, text: "Długość włosów" },
        { value: "Bardzo krótkie", text: "bardzo krótkie" },
        { value: "Krótkie", text: "krótkie" },
        { value: "Średnie", text: "średnie (do barków)" },
        { value: "Dłuższe", text: "dłuższe (do łopatek)" },
        { value: "Długie", text: "długie" },
        { value: "Bardzo długie", text: "bardzo długie (do pasa+)" },
        { value: "Łysy", text: "brak (łysy)" },
      ],
      smoking_options: [
        { value: null, text: "" },
        { value: "0", text: "nie palę" },
        { value: "1", text: "okazjonalnie" },
        { value: "2", text: "często" },
        { value: "3", text: "codziennie" },
        { value: "4", text: "nałogowo" },
      ],
      fields: ["location", "sex", "birthday"],
    };
  },
  methods: {
    /*getAllUsers() {
      axios
        .get("http://127.0.0.1:8000/api/user/users", {
          params: {
            search: localStorage.getItem("search-text"),
            sex: this.sex,
            location: this.location,
            birthday: this.birthday,
            hair_length: this.hair_length,
            hair_color: this.hair_color,
            eye_color: this.eye_color,
            body_type: this.body_type,
            is_smoking: this.is_smoking,
            orientation: this.orientation,
            age_preference_min: this.age_min,
            age_preference_max: this.age_max,
          },
          headers: {
            Authorization: "Token " + localStorage.getItem("user-token"),
          },
        })
        .then((response) => {
          console.log("getallusers");
          console.log(response), (this.allUsers = response.data);
        })
        .catch((errors) => console.log(errors));
      this.searchText = localStorage.getItem("search-text");
      localStorage.removeItem("search-text");
    },*/
    getPageUsers() {
      axios
        .get("https://elove.ml:8000/api/user/users?page=" + this.page, {
          params: {
            search: localStorage.getItem("search-text"),
            sex: this.sex,
            location: this.location,
            birthday: this.birthday,
            hair_length: this.hair_length,
            hair_color: this.hair_color,
            eye_color: this.eye_color,
            body_type: this.body_type,
            is_smoking: this.is_smoking,
            orientation: this.orientation,
            age_preference_min: this.age_min,
            age_preference_max: this.age_max,
          },
          headers: {
            Authorization: "Token " + localStorage.getItem("user-token"),
          },
        })
        .then((response) => {
          console.log("pageusers"),
            console.log(response),
            (this.users = response.data.users);
            (this.users_count = response.data.users_count);
        })
        .catch((errors) => console.log(errors));
      this.searchText = localStorage.getItem("search-text");
      localStorage.removeItem("search-text");
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
    getUrl(pic) {
      if (pic != null) return "https://elove.ml" + pic;
      else
        return "https://www.manufacturingusa.com/sites/manufacturingusa.com/files/default.png";
    },
  },
  created() {
    this.getPageUsers();
    //this.getAllUsers();
  },
  computed: {
    totalPages: function () {
      return Math.ceil(this.users_count / 20);
    },
    pageUsers: function () {
      return this.paginate(this.users);
    },
  },
  /*filters: {
        paginate: function(list) {
            this.resultCount = list.length
            
            var index = this.currentPage * this.itemsPerPage
            return list.slice(index, index + this.itemsPerPage)
        }
    },*/
};
</script>

<style scoped>
.page {
  margin: auto;
  width: 100%;
}

#filters {
  margin: auto;
  width: 100%;
}
#filter {
  margin: auto;
  width: 100%;
  padding-left: 20px;
}
#title {
  padding: 1cm;
  color: white;
  color: #ad1717;
  text-shadow: 1px 1px #000000;
}
.card {
  margin-bottom: 15px;
  width: 100%;
  height: 300px;
  padding-block: 1px;
}
td {
  padding-left: 2.1cm;
  padding-right: 2.1cm;
  padding-bottom: 1cm;
}
.card-img-left {
  max-height: 300px;
  object-fit: cover;
  max-width: 300px;
}
.card-text {
  font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;
  text-align: left;
  font-size: 5px;
  color: white;
  width: 375px;
}
.user-card {
  background: #8d1515;
  color: white;
  border-style: solid;
  border-width: 2px;
  border-color: #aa1d37;
}
.user-card:hover {
  background: #aa1a1a;
}
.scroll {
  height: 100%;
  overflow-y: scroll;
  height: 100vh;
  background: rgba(128, 0, 128, 0.199);
  border-radius: 12px;
}
.navbar {
  border-radius: 17px;
  background-color: #db4460;
}
.oneline {
  display: inline-block;
}
.h1 {
  color: #ad1717;
  text-shadow: 1px 1px #ff0202;
}
.btn {
  border-radius: 12px;
}
.h6 {
  color: rgb(255, 255, 255);
}
.v-card__text, .v-card__title {
  word-break: normal; /* maybe !important  */
}
</style>
