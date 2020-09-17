<template>
  <div class="container-fluid">
    <b-row>
      <b-col cols="2">
        <div class="nav">
          <b-nav vertical>
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
                  <li class="list-group-item">
                    Imię i nazwisko:
                    <div class="oneline">
                      <p class="font-weight-bold">{{user_data.name}} {{user_data.surname}}</p>
                    </div>
                  </li>
                  <li class="list-group-item">
                    Płeć:
                    <div class="oneline">
                      <p class="font-weight-bold">{{user_data.sex}}</p>
                    </div>
                  </li>
                  <li class="list-group-item">
                    Wiek:
                    <div class="oneline">
                      <p class="font-weight-bold">{{getAge(user_data.birthday)}}</p>
                    </div>
                  </li>
                  <li class="list-group-item">
                    Mieszkam w:
                    <div class="oneline">
                      <p class="font-weight-bold">{{user_data.location}}</p>
                    </div>
                  </li>
                  <li class="list-group-item">
                    Urodziny:
                    <div class="oneline">
                      <p class="font-weight-bold">{{user_data.birthday}}</p>
                    </div>
                  </li>
                  <li class="list-group-item">
                    Status:
                    <div class="oneline">
                      <p class="font-weight-bold">{{user_data.status}}</p>
                    </div>
                  </li>
                  <li class="list-group-item">
                    Wykształcenie:
                    <div class="oneline">
                      <p class="font-weight-bold">{{user_data.education}}</p>
                    </div>
                  </li>

                  <!--<li class="list-group-item">
                    <div class="oneline">
                      <p class="font-weight-bold"></p>
                    </div>
                  </li>-->
                  <div v-if="user_data.is_smoking==0">
                    <li class="list-group-item">
                      Papierosy:
                      <div class="oneline">
                        <p class="font-weight-bold">nie palę</p>
                      </div>
                    </li>
                  </div>
                  <div v-else-if="user_data.is_smoking==1">
                    <li class="list-group-item">
                      Papierosy:
                      <div class="oneline">
                        <p class="font-weight-bold">okazjonalnie</p>
                      </div>
                    </li>
                  </div>
                  <div v-else-if="user_data.is_smoking==2">
                    <li class="list-group-item">
                      Papierosy:
                      <div class="oneline">
                        <p class="font-weight-bold">często</p>
                      </div>
                    </li>
                  </div>
                  <div v-else-if="user_data.is_smoking==3">
                    <li class="list-group-item">
                      Papierosy:
                      <div class="oneline">
                        <p class="font-weight-bold">codziennie</p>
                      </div>
                    </li>
                  </div>
                  <div v-else-if="user_data.is_smoking==4">
                    <li class="list-group-item">
                      Papierosy:
                      <div class="oneline">
                        <p class="font-weight-bold">nałogowo</p>
                      </div>
                    </li>
                  </div>
                  <div v-else>
                    <li class="list-group-item">
                      Papierosy:
                      <div class="oneline">
                        <p class="font-weight-bold">?</p>
                      </div>
                    </li>
                  </div>

                  <div v-if="user_data.is_drinking_alcohol==0">
                    <li class="list-group-item">
                      Alkohol:
                      <div class="oneline">
                        <p class="font-weight-bold">nie piję</p>
                      </div>
                    </li>
                  </div>
                  <div v-else-if="user_data.is_drinking_alcohol==1">
                    <li class="list-group-item">
                      Alkohol:
                      <div class="oneline">
                        <p class="font-weight-bold">okazjonalnie</p>
                      </div>
                    </li>
                  </div>
                  <div v-else-if="user_data.is_drinking_alcohol==2">
                    <li class="list-group-item">
                      Alkohol:
                      <div class="oneline">
                        <p class="font-weight-bold">często</p>
                      </div>
                    </li>
                  </div>
                  <div v-else-if="user_data.is_drinking_alcohol==3">
                    <li class="list-group-item">
                      Alkohol:
                      <div class="oneline">
                        <p class="font-weight-bold">codziennie</p>
                      </div>
                    </li>
                  </div>
                  <div v-else-if="user_data.is_drinking_alcohol==4">
                    <li class="list-group-item">
                      Alkohol:
                      <div class="oneline">
                        <p class="font-weight-bold">nałogowo</p>
                      </div>
                    </li>
                  </div>
                  <div v-else>
                    <li class="list-group-item">
                      Alkohol:
                      <div class="oneline">
                        <p class="font-weight-bold">?</p>
                      </div>
                    </li>
                  </div>
                </ul>
              </div>
            </b-tab>
            <b-tab title="Mój wygląd">
              <div class="card text-black bg-dark mb-3">
                <ul class="list-group list-group-flush">
                  <li class="list-group-item">
                    Wzrost:
                    <div class="oneline">
                      <p class="font-weight-bold">{{user_data.growth}}</p>
                    </div>
                  </li>
                  <li class="list-group-item">
                    Waga:
                    <div class="oneline">
                      <p class="font-weight-bold">{{user_data.weight}}</p>
                    </div>
                  </li>

                  <li class="list-group-item">
                    Włosy:
                    <div class="oneline">
                      <p class="font-weight-bold">{{user_data.hair_length}} {{user_data.hair_color}}</p>
                    </div>
                  </li>
                  <li class="list-group-item">
                    Kolor oczu:
                    <div class="oneline">
                      <p class="font-weight-bold">{{user_data.eye_color}}</p>
                    </div>
                  </li>
                  <li class="list-group-item">
                    Sylwetka:
                    <div class="oneline">
                      <p class="font-weight-bold">{{user_data.body_type}}</p>
                    </div>
                  </li>

                  <li class="list-group-item">
                    Znaki szczególne:
                    <div class="oneline" v-if="user_data.freckles!=false">
                      <p class="font-weight-bold">mam piegi</p>
                    </div>
                    <div class="oneline" v-if="user_data.glasses!=false">
                      <p class="font-weight-bold">noszę okulary</p>
                    </div>
                  </li>
                </ul>
              </div>
            </b-tab>
            <b-tab title="Zainteresowania">
              <div class="card text-black bg-dark mb-3">
                <ul class="list-group list-group-flush">
                  <li class="list-group-item">
                    Rozrywka i hobby:
                    <div class="oneline">
                      <p class="font-weight-bold">{{user_data.hobbies}}</p>
                    </div>
                  </li>
                  <li class="list-group-item">
                    Sport:
                    <div class="oneline">
                      <p class="font-weight-bold">{{user_data.sport}}</p>
                    </div>
                  </li>
                  <li class="list-group-item">
                    Muzyka:
                    <div class="oneline">
                      <p class="font-weight-bold">{{user_data.music}}</p>
                    </div>
                  </li>
                  <li class="list-group-item">
                    Kuchnia:
                    <div class="oneline">
                      <p class="font-weight-bold">{{user_data.cooking}}</p>
                    </div>
                  </li>
                  <li class="list-group-item">
                    Ulubione miejsce:
                    <div class="oneline">
                      <p class="font-weight-bold">{{user_data.favourite_place}}</p>
                    </div>
                  </li>
                  <li class="list-group-item">
                    Największa pasja:
                    <div class="oneline">
                      <p class="font-weight-bold">{{user_data.passion}}</p>
                    </div>
                  </li>
                </ul>
              </div>
            </b-tab>
            <b-tab title="Moje preferencje">
              <div class="card text-black">
                <ul class="list-group list-group-flush">
                  <li class="list-group-item">
                    Orientacja:
                    <div class="oneline">
                      <p class="font-weight-bold">{{user_preferences.orientation}}</p>
                    </div>
                  </li>
                  <!--<li
                    class="list-group-item"
                  >Przedział wiekowy: {{user_preferences.age_preference_min}} - {{user_preferences.age_preference_max}}</li>-->
                  <li class="list-group-item">
                    Przedział wiekowy:
                    <div class="oneline" v-if="user_preferences.age_preference_min!=null">
                      <p class="font-weight-bold">od {{user_preferences.age_preference_min}}</p>
                    </div>
                    <div class="oneline" v-if="user_preferences.age_preference_max!=null">
                      <p class="font-weight-bold">do {{user_preferences.age_preference_max}}</p>
                    </div>
                  </li>

                  <li class="list-group-item">
                    Edukacja:
                    <div class="oneline">
                      <p class="font-weight-bold">{{user_preferences.education_preference}}</p>
                    </div>
                  </li>
                  <li class="list-group-item">
                    Waga:
                    <div class="oneline" v-if="user_preferences.weight_preference!=null">
                      <p class="font-weight-bold">do {{user_preferences.weight_preference}} kg</p>
                    </div>
                  </li>
                  <li class="list-group-item">
                    Sylwetka:
                    <div class="oneline">
                      <p class="font-weight-bold">{{user_preferences.body_type_preference}}</p>
                    </div>
                  </li>
                  <li class="list-group-item">
                    Włosy:
                    <div class="oneline">
                      <p class="font-weight-bold"></p>
                    </div>
                  </li>
                  <li class="list-group-item">
                    Kolor oczu:
                    <div class="oneline">
                      <p class="font-weight-bold">{{user_preferences.eye_color_preference}}</p>
                    </div>
                  </li>
                  <li class="list-group-item">
                    Znaki szczególne:
                    <div class="oneline" v-if="user_preferences.freckles_preference!=false">
                      <p class="font-weight-bold">piegi</p>
                    </div>
                    <div class="oneline" v-if="user_preferences.glasses_preference!=false">
                      <p>_</p>
                    </div>
                    <div class="oneline" v-if="user_preferences.glasses_preference!=false">
                      <p class="font-weight-bold">okulary</p>
                    </div>
                  </li>

                  <div v-if="user_preferences.is_smoking_preference==0">
                    <li class="list-group-item">
                      Papierosy:
                      <div class="oneline">
                        <p class="font-weight-bold">nie pali</p>
                      </div>
                    </li>
                  </div>

                  <div v-else-if="user_preferences.is_smoking_preference==1">
                    <li class="list-group-item">
                      Papierosy:
                      <div class="oneline">
                        <p class="font-weight-bold">okazjonalnie</p>
                      </div>
                    </li>
                  </div>
                  <div v-else-if="user_preferences.is_smoking_preference==2">
                    <li class="list-group-item">
                      Papierosy:
                      <div class="oneline">
                        <p class="font-weight-bold">często</p>
                      </div>
                    </li>
                  </div>
                  <div v-else-if="user_preferences.is_smoking_preference==3">
                    <li class="list-group-item">
                      Papierosy:
                      <div class="oneline">
                        <p class="font-weight-bold">codziennie</p>
                      </div>
                    </li>
                  </div>
                  <div v-else-if="user_preferences.is_smoking_preference==4">
                    <li class="list-group-item">
                      Papierosy:
                      <div class="oneline">
                        <p class="font-weight-bold">nałogowo</p>
                      </div>
                    </li>
                  </div>
                  <div v-else>
                    <li class="list-group-item">
                      Papierosy:
                      <div class="oneline">
                        <p class="font-weight-bold">obojętne</p>
                      </div>
                    </li>
                  </div>

                  <div v-if="user_preferences.is_drinking_alcohol_preference==0">
                    <li class="list-group-item">
                      Alkohol:
                      <div class="oneline">
                        <p class="font-weight-bold">nie pije</p>
                      </div>
                    </li>
                  </div>
                  <div v-else-if="user_preferences.is_drinking_alcohol_preference==1">
                    <li class="list-group-item">
                      Alkohol:
                      <div class="oneline">
                        <p class="font-weight-bold">okazjonalnie</p>
                      </div>
                    </li>
                  </div>
                  <div v-else-if="user_preferences.is_drinking_alcohol_preference==2">
                    <li class="list-group-item">
                      Alkohol:
                      <div class="oneline">
                        <p class="font-weight-bold">często</p>
                      </div>
                    </li>
                  </div>
                  <div v-else-if="user_preferences.is_drinking_alcohol_preference==3">
                    <li class="list-group-item">
                      Alkohol:
                      <div class="oneline">
                        <p class="font-weight-bold">codziennie</p>
                      </div>
                    </li>
                  </div>
                  <div v-else-if="user_preferences.is_drinking_alcohol_preference==4">
                    <li class="list-group-item">
                      Alkohol:
                      <div class="oneline">
                        <p class="font-weight-bold">nałogowo</p>
                      </div>
                    </li>
                  </div>
                  <div v-else>
                    <li class="list-group-item">Alkohol: {{user_data.is_drinking_alcohol}}</li>
                    <li class="list-group-item">
                      Alkohol:
                      <div class="oneline">
                        <p class="font-weight-bold">obojętnie</p>
                      </div>
                    </li>
                  </div>
                </ul>
              </div>
            </b-tab>
            <b-tab title="Cechy charakteru">
              <div class="card text-black bg-dark mb-3">
                <ul class="list-group list-group-flush">
                  <li class="list-group-item">
                    Pewność siebie:
                    <div class="oneline">
                      <p class="font-weight-bold">{{user_data.assertiveness}}</p>
                    </div>
                  </li>
                  <li class="list-group-item">
                    Szczerość:
                    <div class="oneline">
                      <p class="font-weight-bold">{{user_data.sincerity}}</p>
                    </div>
                  </li>
                  <li class="list-group-item">
                    Empatia:
                    <div class="oneline">
                      <p class="font-weight-bold">{{user_data.empathy}}</p>
                    </div>
                  </li>
                  <li class="list-group-item">
                    Komunikatywność:
                    <div class="oneline">
                      <p class="font-weight-bold">{{user_data.communication}}</p>
                    </div>
                  </li>
                  <li class="list-group-item">
                    Bezinteresowność:
                    <div class="oneline">
                      <p class="font-weight-bold">{{user_data.selflessness}}</p>
                    </div>
                  </li>
                  <li class="list-group-item">
                    Uczciwość:
                    <div class="oneline">
                      <p class="font-weight-bold">{{user_data.honesty}}</p>
                    </div>
                  </li>
                  <li class="list-group-item">
                    Sumienność:
                    <div class="oneline">
                      <p class="font-weight-bold">{{user_data.scrupulousness}}</p>
                    </div>
                  </li>
                  <li class="list-group-item">
                    Pracowitość:
                    <div class="oneline">
                      <p class="font-weight-bold">{{user_data.diligence}}</p>
                    </div>
                  </li>
                  <li class="list-group-item">
                    Życzliwość:
                    <div class="oneline">
                      <p class="font-weight-bold">{{user_data.kindness}}</p>
                    </div>
                  </li>
                  <li class="list-group-item">
                    Romantyczność:
                    <div class="oneline">
                      <p class="font-weight-bold">(?)</p>
                    </div>
                  </li>
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
  max-height: 400px;
  object-fit: cover;
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
.oneline {
  display: inline-block;
}
.h5 {
}
.h6 {
  align-content: left;
}
</style>