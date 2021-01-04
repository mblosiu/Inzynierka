<template>
  <v-content>
    <v-container>
      <br />
      <v-expansion-panels color="purple">
        <v-expansion-panel class="purple">
          <v-toolbar extended extension-height="50" class="purple">
            <v-icon
              medium
              color="purple lighten-3"
              data-toggle="tooltip"
              data-placement="left"
              title="Wyszukaj użytkowników za pomocą nałożonych filtrów, bądź konkretnego z nich po nazwie"
              >mdi-help-circle</v-icon
            >
            <form id="filters" @submit.prevent="getUsers">
              <table>
                <tr>
                  <th>
                    <div id="filter">
                      <b-form-select
                        :options="sex_options"
                        class="ml-2"
                        id="sex"
                        v-model="sex"
                        size="md"
                        value="sex"
                        placeholder="Płeć"
                      ></b-form-select>
                    </div>
                  </th>

                  <th>
                    <div id="filter">
                      <input
                        class="form-control ml-2"
                        type="text"
                        placeholder="Lokacja"
                        id="location"
                        v-model="location"
                      />
                    </div>
                  </th>
                  <th>
                    <b-row>
                      <b-col cols="2"></b-col>
                      <b-col cols="8">
                        <div class="p-1 text-white text-i">
                          <h6>
                            Przedział wiekowy: {{ age_min }} - {{ age_max }}
                          </h6>
                        </div>
                      </b-col>
                      <b-col cols="2"></b-col>
                    </b-row>
                    <b-row>
                      <b-col cols="1"></b-col>
                      <b-col cols="5">
                        <div>
                          <b-form-input
                            id="age_min"
                            v-model="age_min"
                            type="range"
                            min="18"
                            :max="age_max"
                          ></b-form-input>
                        </div>
                      </b-col>
                      <b-col cols="5">
                        <div>
                          <b-form-input
                            id="age_max"
                            v-model="age_max"
                            type="range"
                            :min="age_min"
                            max="100"
                          ></b-form-input>
                        </div>
                      </b-col>
                      <b-col cols="1"></b-col>
                    </b-row>
                  </th>

                  <th>
                    <div id="filter">
                      <v-btn x-large block color="purple lighten-2">
                        <button type="submit">
                          <b class="white--text">Filtruj</b>
                        </button>
                      </v-btn>
                    </div>
                  </th>
                </tr>
              </table>
            </form>
          </v-toolbar>

          <v-expansion-panel-header class="purple" extended>
            <h5 class="white--text centre">Więcej filtrów</h5>
          </v-expansion-panel-header>
          <v-expansion-panel-content class="purple">
            <v-row>
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
              <v-col>
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
              </v-col>
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
            </v-row>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>

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
        <v-col cols="12" align-self="start" class="scroll">
          <b-row v-for="i in Math.ceil(users.length / 2)" v-bind:key="i">
            <b-col
              cols="6"
              v-for="user in users.slice((i - 1) * 2, i * 2)"
              v-bind:key="user.id"
              style="ml-2 mr-2"
            >
              <v-hover>
                <router-link
                  :to="{ name: 'userprofile', params: { pk: user.pk } }"
                >
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
                          v-model="menu"
                          :close-on-content-click="false"
                          :nudge-width="200"
                          offset-x
                          left
                        >
                          <template v-slot:activator="{ on, attrs }">
                            <v-btn
                              fab
                              small
                              class="purple"
                              v-bind="attrs"
                              v-on="on"
                              ><v-app-bar-nav-icon
                                color="white"
                              ></v-app-bar-nav-icon
                            ></v-btn>
                          </template>

                          <v-card> </v-card>
                        </v-menu>
                        <div v-if="user.profile_picture==null">
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
                    </v-card-text>
                  </v-card>
                </router-link>
              </v-hover>
            </b-col>
          </b-row>
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
      profileImage: null,
      is_smoking: null,
      today: new Date(),
      birthDate: "",
      age: "",
      age_min: 18,
      age_max: 100,
      m: "",
      description: null,
      sex_options: [
        { value: null, text: "płeć" },
        { value: "Mężczyzna", text: "mężczyzna" },
        { value: "Kobieta", text: "kobieta" },
        { value: "Inna", text: "inna" },
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
    getUsers() {
      this.users = [];
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
          console.log(response), (this.users = response.data);
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
      if (pic != null) return "http://127.0.0.1:8000" + pic;
      else
        return "https://www.manufacturingusa.com/sites/manufacturingusa.com/files/default.png";
    },
  },
  created() {
    this.getUsers();
  },
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

</style>
