<template>
  <v-container>
    <br />
    <v-row>
      <v-col lg="1" md="1" sm="0" xs="0" > </v-col>
      <v-col lg="5" md="5" sm="12" xs="12">
        <div>
          <v-card
            outlined
            rounded
            max-width="500"
            min-height="500"
            class="mx-auto hidden-sm-and-down"
            color="purple"
          >
            <v-img
              class="white--text align-end"
              :src="getUrl(user_data.profile_picture)"
              aspect-ratio="1"
            >
              <div v-if="user_data.profile_picture == null">
                <v-card-title class="black--text"
                  >{{ user_data.username }} ({{
                    getAge(user_data.birthday)
                  }})</v-card-title
                >
              </div>
              <div v-else>
                <v-card-title
                  >{{ user_data.username }} ({{
                    getAge(user_data.birthday)
                  }})</v-card-title
                >
              </div>
            </v-img>

            <v-card-text class="white--text text-left">
              <h4 v-if="user_data.description != null">
                <p class="font-italic">{{ user_data.description }}</p>
              </h4>
              <h4 v-else>
                <p class="font-italic text-center">Brak opisu.</p>
              </h4>
            </v-card-text>
          </v-card>
          <v-card
            outlined
            rounded
            max-width="500"
            class="mx-auto hidden-md-and-up"
            color="purple"
          >
            
              <v-row>
                <v-col cols="8">
                  <div>
                    <v-card-title class="white--text"
                      >{{ user_data.username }} ({{
                        getAge(user_data.birthday)
                      }})</v-card-title
                    >

                    <v-card-text class="white--text text-left">
                      <h4 v-if="user_data.description != null">
                        <p class="font-italic">{{ user_data.description }}</p>
                      </h4>
                      <h4 v-else>
                        <p class="font-italic text-center">Brak opisu.</p>
                      </h4>
                    </v-card-text>
                  </div>
                </v-col>
                <v-col cols="4">
                  <v-avatar class="ma-3" size="125" tile>
                    <v-img
                      class="white--text align-end"
                      :src="getUrl(user_data.profile_picture)"
                      aspect-ratio="1"
                    >
                    </v-img>
                  </v-avatar>
                </v-col>
              </v-row>
            
          </v-card>
        </div>
        <br />
      </v-col>

      <v-col lg="5" md="12" sm="12" xs="12">
        <div>
          <v-card>
            <v-toolbar flat color="purple" dark>
              <v-toolbar-title>Profil</v-toolbar-title>
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
                            {{ user_data.name }} {{ user_data.surname }}
                          </p>
                        </div>
                      </li>
                      <li class="list-group-item">
                        Płeć:
                        <div class="oneline">
                          <p class="font-weight-bold">{{ user_data.sex }}</p>
                        </div>
                      </li>
                      <li class="list-group-item">
                        Wiek:
                        <div class="oneline">
                          <p class="font-weight-bold">
                            {{ getAge(user_data.birthday) }}
                          </p>
                        </div>
                      </li>
                      <li class="list-group-item">
                        Mieszkam w:
                        <div class="oneline">
                          <p class="font-weight-bold">
                            {{ user_data.location }}
                          </p>
                        </div>
                      </li>
                      <li class="list-group-item">
                        Urodziny:
                        <div class="oneline">
                          <p class="font-weight-bold">
                            {{ user_data.birthday }}
                          </p>
                        </div>
                      </li>
                      <li class="list-group-item">
                        Status:
                        <div class="oneline">
                          <p class="font-weight-bold">{{ user_data.status }}</p>
                        </div>
                      </li>
                      <li class="list-group-item">
                        Wykształcenie:
                        <div class="oneline">
                          <p class="font-weight-bold">
                            {{ user_data.education }}
                          </p>
                        </div>
                      </li>

                      <li class="list-group-item">
                        <div v-if="user_data.is_smoking == 0">
                          Papierosy:
                          <div class="oneline">
                            <p class="font-weight-bold">nie palę</p>
                          </div>
                        </div>
                        <div v-else-if="user_data.is_smoking == 1">
                          Papierosy:
                          <div class="oneline">
                            <p class="font-weight-bold">okazjonalnie</p>
                          </div>
                        </div>
                        <div v-else-if="user_data.is_smoking == 2">
                          Papierosy:
                          <div class="oneline">
                            <p class="font-weight-bold">często</p>
                          </div>
                        </div>
                        <div v-else-if="user_data.is_smoking == 3">
                          Papierosy:
                          <div class="oneline">
                            <p class="font-weight-bold">codziennie</p>
                          </div>
                        </div>
                        <div v-else-if="user_data.is_smoking == 4">
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
                        <div v-if="user_data.is_drinking_alcohol == 0">
                          Alkohol:
                          <div class="oneline">
                            <p class="font-weight-bold">nie piję</p>
                          </div>
                        </div>
                        <div v-else-if="user_data.is_drinking_alcohol == 1">
                          Alkohol:
                          <div class="oneline">
                            <p class="font-weight-bold">okazjonalnie</p>
                          </div>
                        </div>
                        <div v-else-if="user_data.is_drinking_alcohol == 2">
                          Alkohol:
                          <div class="oneline">
                            <p class="font-weight-bold">często</p>
                          </div>
                        </div>
                        <div v-else-if="user_data.is_drinking_alcohol == 3">
                          Alkohol:
                          <div class="oneline">
                            <p class="font-weight-bold">codziennie</p>
                          </div>
                        </div>
                        <div v-else-if="user_data.is_drinking_alcohol == 4">
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
                        <div class="oneline" v-if="user_data.growth != null">
                          <p class="font-weight-bold">
                            {{ user_data.growth }} cm
                          </p>
                        </div>
                      </li>
                      <li class="list-group-item">
                        Waga:
                        <div class="oneline" v-if="user_data.weight != null">
                          <p class="font-weight-bold">
                            {{ user_data.weight }} kg
                          </p>
                        </div>
                      </li>

                      <li class="list-group-item">
                        Włosy:
                        <div class="oneline">
                          <p class="font-weight-bold">
                            {{ user_data.hair_length }}
                            {{ user_data.hair_color }}
                          </p>
                        </div>
                      </li>
                      <li class="list-group-item">
                        Kolor oczu:
                        <div class="oneline">
                          <p class="font-weight-bold">
                            {{ user_data.eye_color }}
                          </p>
                        </div>
                      </li>
                      <li class="list-group-item">
                        Sylwetka:
                        <div class="oneline">
                          <p class="font-weight-bold">
                            {{ user_data.body_type }}
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
                      <!--<li
                    class="list-group-item"
                  >Przedział wiekowy: {{user_preferences.age_preference_min}} - {{user_preferences.age_preference_max}}</li>-->
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
                            {{ user_data.orientation }}
                          </p>
                        </div>
                      </li>

                      <li class="list-group-item">
                        <div v-if="user_preferences.is_smoking_preference == 0">
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
                            user_preferences.is_drinking_alcohol_preference == 0
                          "
                        >
                          Alkohol:
                          <div class="oneline">
                            <p class="font-weight-bold">nie pije</p>
                          </div>
                        </div>
                        <div
                          v-else-if="
                            user_preferences.is_drinking_alcohol_preference == 1
                          "
                        >
                          Alkohol:
                          <div class="oneline">
                            <p class="font-weight-bold">okazjonalnie</p>
                          </div>
                        </div>
                        <div
                          v-else-if="
                            user_preferences.is_drinking_alcohol_preference == 2
                          "
                        >
                          Alkohol:
                          <div class="oneline">
                            <p class="font-weight-bold">często</p>
                          </div>
                        </div>
                        <div
                          v-else-if="
                            user_preferences.is_drinking_alcohol_preference == 3
                          "
                        >
                          Alkohol:
                          <div class="oneline">
                            <p class="font-weight-bold">codziennie</p>
                          </div>
                        </div>
                        <div
                          v-else-if="
                            user_preferences.is_drinking_alcohol_preference == 4
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
      </v-col>
      <v-col lg="1"></v-col>
    </v-row>
    <br />
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  name: "MainUser",
  components: {},
  data() {
    return {
      user_data: {},
      profile_picture: null,
      user_preferences: {},
      today: new Date(),
      birthDate: "",
      age: "",
      m: "",
      description: [],
      msg: "",
      dismissSecs: 5,
      dismissCountDown: 0,
      whitespace: " ",
    };
  },
  methods: {
    countDownChanged(dismissCountDown) {
      this.dismissCountDown = dismissCountDown;
    },
    showMsg() {
      this.dismissCountDown = this.dismissSecs;
    },
    //pobieranie danych zalogowanego użytkownika
    getUserData() {
      axios
        .get("https://elove.ml:8000/api/user/properties", {
          params: {},
          headers: {
            Authorization: "Token " + localStorage.getItem("user-token"),
          },
        })
        .then((response) => {
          //console.log("getUserData");
          console.log(response), (this.user_data = response.data);
        })
        .catch((errors) => console.log(errors));
    },
    //pobieranie preferencji zalogowanego użytkownika
    getUserPreferences() {
      axios
        .get("https://elove.ml:8000/api/user/preferences", {
          params: {},
          headers: {
            Authorization: "Token " + localStorage.getItem("user-token"),
          },
        })
        .then((response) => {
          console.log("getUserPreferences");
          console.log(response), (this.user_preferences = response.data);
        })
        .catch((errors) => console.log(errors));
    },
    //funkcja nie używana w aktualnej wersji
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
            description: this.user_data.description,
          },
          config
        )
        .then((response) => {
          console.log(response);
          if (response.status == 200) {
            this.showMsg(), (this.msg = "Zaktualizowano opis profilu");
          }
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
    getUrl(pic) {
      if (pic != null) return "https://elove.ml" + pic;
      else
        return "https://www.manufacturingusa.com/sites/manufacturingusa.com/files/default.png";
    },
  },
  created() {
    this.getUserData();
    this.getUserPreferences();
  },
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
  object-fit: cover;
  /*object-fit: scale-down;*/
  width: auto;
  max-height: 400px;
  border-radius: 10px;
}
.card-text {
  font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;
  text-align: left;
  font-size: 20px;
}
.user-card {
  height: 700px;
  background: #be3636;
  color: white;
  padding: 2px;
  border-radius: 12px;
  border-style: solid;
  border-width: 2px;
  border-color: #9a3f66;
  object-fit: scale-down;
}
textarea {
  height: 100%;
  width: 100%;
  background-color: #e9bac2;
}
.alert {
  width: 265px;
  margin-left: 100px;
  padding-block: inherit;
  margin-block: inherit;
  align-content: inherit;
}
.list-group-item {
  background: white;
}
.tabs {
  height: 700px;
  width: 100%;
  margin-left: 0;
  background: #ecb2b2d5;
  border-radius: 12px;
  border-style: solid;
  border-width: 2px;
  border-color: #9a3f66;
}
.nav {
  background: #ecb2b2d5;
  height: 700px;
  width: 100%;
  border-radius: 12px;
  border-style: solid;
  border-width: 1px;
  border-color: #9a3f66;
}
.oneline {
  display: inline-block;
}
.h4 {
  color: wheat;
}
.h6 {
  align-content: left;
}
.v-card__text, .v-card__title {
  word-break: normal; /* maybe !important  */
}
</style>
