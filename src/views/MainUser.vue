<template>
  <div class="mainuser">
    <br />
    <b-container class="bv-example-row" fluid>
      <b-row>
        <b-col cols="8">
          <div v-if="user_data.profilePicture==null">
            <b-card
              img-src="https://www.manufacturingusa.com/sites/manufacturingusa.com/files/default.png"
              img-alt="Card image"
              img-left
              class="user-card"
            >
              <b-card-title>
                <h2>{{user_data.username}} ({{getAge(user_data.birthday)}})</h2>
              </b-card-title>
              <b-card-text>
                <div v-if="user_data.description!=null">
                  <h3>{{user_data.description}}</h3>
                </div>
                <div v-else>
                  <br />
                  <form class="description" @submit.prevent="editUserData">
                    <!--<input type="text" id="user_name" v-model="user_data.name" class="form-control" />-->
                    <textarea
                      v-model="user_data.description"
                      placeholder="Aktualnie nie posiadasz opisu. Napisz coś o sobie."
                      class="form-control"
                    ></textarea>
                    <button type="submit" class="btn btn-secondary">Zapisz</button>
                  </form>
                </div>
              </b-card-text>
            </b-card>
          </div>
          <div v-else>
            <b-card
              img-src="user_data.profilePicture"
              img-alt="Card image"
              img-left
              class="user-card"
            >
              <b-card-title>
                <h2>{{user_data.username}} ({{getAge(user_data.birthday)}})</h2>
              </b-card-title>
              <b-card-text>
                <div v-if="user_data.description!=null">
                  <h3>{{user_data.description}}</h3>
                </div>
                <div v-else>
                  <form class="description" @submit.prevent="editUserData">
                    <!--<input type="text" id="user_name" v-model="user_data.name" class="form-control" />-->
                    <textarea
                      v-model="user_data.description"
                      placeholder="Aktualnie nie posiadasz opisu. Napisz coś o sobie."
                    ></textarea>
                    <button type="submit" class="btn btn-secondary">Zapisz</button>
                  </form>
                </div>
              </b-card-text>
            </b-card>
          </div>
          <br />

          <b-col cols="4">
            <div
              class="nav flex-column nav-pills"
              id="v-pills-tab"
              role="tablist"
              aria-orientation="vertical"
            >
              <a
                class="nav-link active"
                id="v-pills-home-tab"
                data-toggle="pill"
                href="#v-pills-home"
                role="tab"
                aria-controls="v-pills-home"
                aria-selected="true"
              >O mnie</a>
              <a
                class="nav-link"
                id="v-pills-profile-tab"
                data-toggle="pill"
                href="#v-pills-profile"
                role="tab"
                aria-controls="v-pills-profile"
                aria-selected="false"
              >Mój wygląd</a>
              <a
                class="nav-link"
                id="v-pills-messages-tab"
                data-toggle="pill"
                href="#v-pills-messages"
                role="tab"
                aria-controls="v-pills-messages"
                aria-selected="false"
              >Cechy charakteru</a>
              <a
                class="nav-link"
                id="v-pills-settings-tab"
                data-toggle="pill"
                href="#v-pills-settings"
                role="tab"
                aria-controls="v-pills-settings"
                aria-selected="false"
              >Zainteresowania</a>
            </div>
          </b-col>

          <b-col cols="4">
            <div class="tab-content" id="v-pills-tabContent">
              <div
                class="tab-pane fade show active"
                id="v-pills-home"
                role="tabpanel"
                aria-labelledby="v-pills-home-tab"
              >1</div>
              <div
                class="tab-pane fade"
                id="v-pills-profile"
                role="tabpanel"
                aria-labelledby="v-pills-profile-tab"
              >22</div>
              <div
                class="tab-pane fade"
                id="v-pills-messages"
                role="tabpanel"
                aria-labelledby="v-pills-messages-tab"
              >3333</div>
              <div
                class="tab-pane fade"
                id="v-pills-settings"
                role="tabpanel"
                aria-labelledby="v-pills-settings-tab"
              >4</div>
            </div>
          </b-col>
        </b-col>

        <b-col cols="4">
          <div class="card text-white bg-secondary mb-3">
            <div class="card-header">
              <h3>O mnie:</h3>
            </div>
            <ul class="list-group list-group-flush">
              <li class="list-group-item">Imię i nazwisko: {{user_data.name}} {{user_data.surname}}</li>
              <li class="list-group-item">Płeć: {{user_data.sex}}</li>
              <li class="list-group-item">Wiek: {{getAge(user_data.birthday)}}</li>
              <li class="list-group-item">Mieszkam w: {{user_data.location}}</li>
              <li class="list-group-item">Urodziny: {{user_data.birthday}}</li>
              <li
                class="list-group-item"
              >Status/zajęcie: dodać np ->uczeń/student/pracuję/emerytura/dumna madka</li>
              <div smoking>
              <div v-if="user_data.is_smoking===false">
                <li class="list-group-item">Papierosy: nie palę</li>
              </div>
              <div v-else-if="user_data.is_smoking===sometimes">
                <li class="list-group-item">Papierosy: okazyjnie</li>
              </div>
              <div v-else-if="user_data.is_smoking===true">
                <li class="list-group-item">Papierosy: palę</li>
              </div>
              <div v-else>
                <li class="list-group-item">Papierosy: {{user_data.is_smoking}} </li>
              </div>
              </div>
              <div v-if="user_data.is_drinking_alcohol===false">
                <li class="list-group-item">Alkohol: nie piję</li>
              </div>
              <div v-else-if="user_data.is_drinking_alcohol===sometimes">
                <li class="list-group-item">Alkohol: okazyjnie</li>
              </div>
              <div v-else-if="user_data.is_drinking_alcohol===true">
                <li class="list-group-item">Alkohol: piję</li>
              </div>
              <div v-else>
                <li class="list-group-item">Alkohol: {{user_data.is_drinking_alcohol}} </li>
              </div>
            </ul>
          </div>

          <div class="card text-white bg-secondary mb-3">
            <div class="card-header">
              <h3>Wygląd:</h3>
            </div>
            <ul class="list-group list-group-flush">
              <li class="list-group-item">Wzrost: {{user_data.growth}}</li>
              <li class="list-group-item">Waga: {{user_data.weight}}</li>
              <li
                class="list-group-item"
              >Włosy: {{user_data.hair_length}} {{user_data.hair_color}} +dziś farbują włosy więc można dodać kolor farbowany/nietypowy + brak koloru czarnego</li>
              <li class="list-group-item">Kolor oczu: dodać</li>
              <li
                class="list-group-item"
              >Sylwetka: szczupła/gruba/wysportowana etc {{user_data.body_type}}</li>
              <li class="list-group-item">
                Znaki szczególne:
                <p v-if="user_data.freckles!=false">mam piegi</p>
                <p v-if="user_data.glasses!=false">noszę okulary</p>+można dodać tatuaże/kolczyki
              </li>
              <li class="list-group-item"></li>
            </ul>
          </div>

          <div class="card text-white bg-secondary mb-3">
            <div class="card-header">
              <h3>Cechy charakteru:</h3>
            </div>
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
              <li class="list-group-item">+ romantyczność można dodać na razie</li>
            </ul>
          </div>

          <div class="card text-white bg-secondary mb-3">
            <div class="card-header">
              <h3>Zainteresowania: dodać (raczej pola tekstowe)</h3>
            </div>
            <ul class="list-group list-group-flush">
              <li class="list-group-item">Hobby:</li>
              <li class="list-group-item">Muzyka:</li>
              <li class="list-group-item">Kuchnia:</li>
              <li class="list-group-item">Ulubione miejsca:</li>
            </ul>
          </div>

          <div class="card text-white bg-secondary mb-3">
            <div class="card-header">
              <h3>Moje preferencje:</h3>
            </div>
            <ul class="list-group list-group-flush">
              <li class="list-group-item">Płeć: {{user_preferences.sex_preference}}</li>
              <li class="list-group-item">Przedział wiekowy: todo</li>
              <li class="list-group-item">Wzrost: {{user_preferences.growth_preference}}</li>
              <li class="list-group-item">Sylwetka: {{user_preferences.body_type_preference}}</li>
              <li
                class="list-group-item"
              >Włosy: {{user_preferences.hair_length_preference}}, blond: ({{user_preferences.hair_color_blonde_preference}}), brunatne: ({{user_preferences.hair_color_brunette_preference}}), rude: ({{user_preferences.hair_color_red_preference}}), czarne: todo</li>
              <li class="list-group-item">Kolor oczu: todo</li>
              <li class="list-group-item">
                Znaki szczególne:
                <p v-if="user_preferences.freckles_preference!=false">piegi</p>
                <p v-if="user_preferences.glasses_preference!=false">okulary</p>+td tatuaże
              </li>
              <li class="list-group-item">Idealne miejsce na randkę: ewentualnie można dodać</li>
            </ul>
          </div>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>



<script>
//import { mapState } from 'vuex';
//import UserCard from '../components/UserCard.vue'
import axios from "axios";
export default {
  name: "MainUser",
  components: {
    //UserCard
  },
  data() {
    return {
      user_data: {},
      user_preferences: {},
      today: new Date(),
      birthDate: "",
      age: "",
      m: "",
    };
  },
  methods: {
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
  },
  created() {
    this.getUserData();
    this.getUserPreferences();
  },
};
</script>


<style scoped>
.mainuser {
  margin: auto;
  width: 100%;
}
.card-img-left {
  height: 300px;
  object-fit: scale-down;
}
.card-text {
  font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;
  text-align: left;
  font-size: 20px;
}
.user-card {
  background: #343a40;
  color: white;
}
textarea {
  height: 100%;
  width: 100%;
}
</style>