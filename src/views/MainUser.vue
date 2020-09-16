<template>
  <div class="container-fluid">
    <b-row>
      <b-col cols="2">
        <div class="nav">
          <b-nav vertical class="w-11">
            <b-nav-item active>Active</b-nav-item>
            <b-nav-item>Link</b-nav-item>
            <b-nav-item>Another Link</b-nav-item>
            <b-nav-item disabled>Disabled</b-nav-item>
          </b-nav>
        </div>
      </b-col>
      <b-col cols="5">
        <div>
          <b-card
            :img-src="getUrl(user_data.profile_picture)"
            img-alt="Card image"
            img-top
            class="user-card"
          >
            <b-card-title>
              <h2>{{user_data.username}} ({{getAge(user_data.birthday)}})</h2>
            </b-card-title>
            <b-card-text>
              <div>
                <form class="description" @submit.prevent="editUserData">
                  <textarea
                    v-model="user_data.description"
                    placeholder="Aktualnie nie posiadasz opisu. Napisz coś o sobie!"
                  ></textarea>
                  <button type="submit" class="btn btn-secondary">Zapisz</button>
                  <b-alert
                  :show="dismissCountDown"
                  fade
                  variant="success"
                  @dismissed="dismissCountDown=0"
                  @dismiss-count-down="countDownChanged"
                >{{msg}}</b-alert>
                </form>
              </div>
            </b-card-text>
          </b-card>
        </div>
        <br />
      </b-col>
      <b-col cols="5">
        <div>
          <b-tabs pills card vertical>
            <b-tab title="O mnie" active>
              <div class="card text-black bg-dark mb-3">
                <ul class="list-group list-group-flush">
                  <li
                    class="list-group-item"
                  >Imię i nazwisko: {{user_data.name}} {{user_data.surname}}</li>
                  <li class="list-group-item">Płeć: {{user_data.sex}}</li>
                  <li class="list-group-item">Wiek: {{getAge(user_data.birthday)}}</li>
                  <li class="list-group-item">Mieszkam w: {{user_data.location}}</li>
                  <li class="list-group-item">Urodziny: {{user_data.birthday}}</li>
                  <li class="list-group-item">Status: {{user_data.status}}</li>
                  <li class="list-group-item">Wykształcenie:{{user_data.education}}</li>
                  <div smoking>
                    <div v-if="user_data.is_smoking==0">
                      <li class="list-group-item">Papierosy: nie palę</li>
                    </div>
                    <div v-else-if="user_data.is_smoking==1">
                      <li class="list-group-item">Papierosy: okazjonalnie</li>
                    </div>
                    <div v-else-if="user_data.is_smoking==2">
                      <li class="list-group-item">Papierosy: często</li>
                    </div>
                    <div v-else-if="user_data.is_smoking==3">
                      <li class="list-group-item">Papierosy: codziennie</li>
                    </div>
                    <div v-else-if="user_data.is_smoking==4">
                      <li class="list-group-item">Papierosy: nałogowo</li>
                    </div>
                    <div v-else>
                      <li class="list-group-item">Papierosy: {{user_data.is_smoking}}</li>
                    </div>
                  </div>
                  <div v-if="user_data.is_drinking_alcohol==0">
                    <li class="list-group-item">Alkohol: nie piję</li>
                  </div>
                  <div v-else-if="user_data.is_drinking_alcohol==1">
                    <li class="list-group-item">Alkohol: okazjonalnie</li>
                  </div>
                  <div v-else-if="user_data.is_drinking_alcohol==2">
                    <li class="list-group-item">Alkohol: często</li>
                  </div>
                  <div v-else-if="user_data.is_drinking_alcohol==3">
                    <li class="list-group-item">Alkohol: codziennie</li>
                  </div>
                  <div v-else-if="user_data.is_drinking_alcohol==4">
                    <li class="list-group-item">Alkohol: nałogowo</li>
                  </div>
                  <div v-else>
                    <li class="list-group-item">Alkohol: {{user_data.is_drinking_alcohol}}</li>
                  </div>
                </ul>
              </div>
            </b-tab>
            <b-tab title="Mój wygląd">
              <div class="card text-black bg-dark mb-3">
                <ul class="list-group list-group-flush">
                  <li class="list-group-item">Wzrost: {{user_data.growth}}</li>
                  <li class="list-group-item">Waga: {{user_data.weight}}</li>
                  <li
                    class="list-group-item"
                  >Włosy: {{user_data.hair_length}} {{user_data.hair_color}}</li>
                  <li class="list-group-item">Kolor oczu: {{user_data.eye_color}}</li>
                  <li class="list-group-item">Sylwetka: {{user_data.body_type}}</li>
                  <li class="list-group-item">
                    Znaki szczególne:
                    <p v-if="user_data.freckles!=false">mam piegi</p>
                    <p v-if="user_data.glasses!=false">noszę okulary</p>
                  </li>
                  <li class="list-group-item"></li>
                </ul>
              </div>
            </b-tab>
            <b-tab title="Zainteresowania">
              <div class="card text-black bg-dark mb-3">
                <ul class="list-group list-group-flush">
                  <li class="list-group-item">Rozrywka i hobby: {{user_data.hobbies}}</li>
                  <li class="list-group-item">Sport: {{user_data.sport}}</li>
                  <li class="list-group-item">Muzyka: {{user_data.music}}</li>
                  <li class="list-group-item">Kuchnia: {{user_data.cooking}}</li>
                  <li class="list-group-item">Ulubione miejsce: {{user_data.favourite_place}}</li>
                  <li class="list-group-item">Największa pasja: {{user_data.passion}}</li>
                </ul>
              </div>
            </b-tab>
            <b-tab title="Moje preferencje">
              <div class="card text-black bg-dark mb-3">
                <ul class="list-group list-group-flush">
                  <li class="list-group-item">Orientacja: {{user_preferences.orientation}}</li>
                  <li
                    class="list-group-item"
                  >Przedział wiekowy: {{user_preferences.age_preference_min}} - {{user_preferences.age_preference_max}}</li>
                  <li class="list-group-item">Edukacja: {{user_preferences.education_preference}}</li>
                  <li class="list-group-item">Waga: do {{user_preferences.weight_preference}} kg</li>
                  <li class="list-group-item">Sylwetka: {{user_preferences.body_type_preference}}</li>
                  <li class="list-group-item">Włosy:</li>
                  <li class="list-group-item">Kolor oczu: {{user_preferences.eye_color_preference}}</li>
                  <li class="list-group-item">
                    Znaki szczególne:
                    <p v-if="user_preferences.freckles_preference!=false">piegi</p>
                    <p v-if="user_preferences.glasses_preference!=false">okulary</p>
                  </li>

                  <div v-if="user_preferences.is_smoking_preference==0">
                    <li class="list-group-item">Papierosy: nie pali</li>
                  </div>
                  <div v-else-if="user_preferences.is_smoking_preference==1">
                    <li class="list-group-item">Papierosy: okazjonalnie</li>
                  </div>
                  <div v-else-if="user_preferences.is_smoking_preference==2">
                    <li class="list-group-item">Papierosy: często</li>
                  </div>
                  <div v-else-if="user_preferences.is_smoking_preference==3">
                    <li class="list-group-item">Papierosy: codziennie</li>
                  </div>
                  <div v-else-if="user_preferences.is_smoking_preference==4">
                    <li class="list-group-item">Papierosy: nałogowo</li>
                  </div>

                  <div v-if="user_preferences.is_drinking_alcohol_preference==0">
                    <li class="list-group-item">Alkohol: nie pije</li>
                  </div>
                  <div v-else-if="user_preferences.is_drinking_alcohol_preference==1">
                    <li class="list-group-item">Alkohol: okazjonalnie</li>
                  </div>
                  <div v-else-if="user_preferences.is_drinking_alcohol_preference==2">
                    <li class="list-group-item">Alkohol: często</li>
                  </div>
                  <div v-else-if="user_preferences.is_drinking_alcohol_preference==3">
                    <li class="list-group-item">Alkohol: codziennie</li>
                  </div>
                  <div v-else-if="user_preferences.is_drinking_alcohol_preference==4">
                    <li class="list-group-item">Alkohol: nałogowo</li>
                  </div>
                  <div v-else>
                    <li class="list-group-item">Alkohol: {{user_data.is_drinking_alcohol}}</li>
                  </div>
                </ul>
              </div>
            </b-tab>
            <b-tab title="Cechy charakteru">
              <div class="card text-black bg-dark mb-3">
                <ul class="list-group list-group-flush">
                  <li class="list-group-item">Pewność siebie: {{user_data.assertiveness}}</li>
                  <li class="list-group-item">Szczerość: {{user_data.sincerity}}</li>
                  <li class="list-group-item">Empatia: {{user_data.empathy}}</li>
                  <li class="list-group-item">Komunikatywność: {{user_data.communication}}</li>
                  <li class="list-group-item">Bezinteresowność: {{user_data.selflessness}}</li>
                  <li class="list-group-item">Uczciwość: {{user_data.honesty}}</li>
                  <li class="list-group-item">Sumienność: {{user_data.scrupulousness}}</li>
                  <li class="list-group-item">Pracowitość: {{user_data.diligence}}</li>
                  <li class="list-group-item">Życzliwość: {{user_data.kindness}}</li>
                  <li class="list-group-item">Romantyczność: (?)</li>
                </ul>
              </div>
            </b-tab>
          </b-tabs>
        </div>
      </b-col>
      
    </b-row>
  </div>
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
      if (pic != null) return "http://127.0.0.1:8000" + pic;
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
  height: 300px;
  object-fit:cover;
}
.card-text {
  font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;
  text-align: left;
  font-size: 20px;
}
.user-card {
  background: #8d1515;
  color: white;
  border-style: solid;
  border-width: 2px;
  border-color: #aa1d37;
}
textarea {
  height: 100%;
  width: 100%;
  background-color: #ffc5c5;
}
.alert {
  width: 265px;
  margin-left: 100px;
  padding-block: inherit;
  margin-block: inherit;
  align-content: inherit;
}
.list-group-item {
  background: #fadbdb;
}
.tabs {
  background: #eb6767;
  border-radius: 12px;
  border-style: solid;
  border-width: 2px;
  border-color: #aa1d37;
}
.nav {
  background: #eb6767;
  height: 100%;
  width: 100%;
  padding-left: 0mm;
  margin-left: 0mm;
}
</style>