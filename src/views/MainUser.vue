<template>
  <div id="mainuser">
    <br />
    <b-container class="bv-example-row" fluid>
      <b-row>
        <!--<b-col cols="2">
        </b-col>
        <b-col cols="1"></b-col>-->
        <b-col cols="1"></b-col>
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
                  <div class="input-group input-group-lg" @submit.prevent="editUserData">
                    <textarea
                      class="form-control-lg"
                      placeholder="Aktualnie nie posiadasz opisu. Napisz coś o sobie!"
                      maxlength="500"
                      style="min-width: 100%"
                      rows="3"
                      aria-label="With textarea"
                    ></textarea>
                    <button type="submit" class="btn btn-secondary">Zapisz</button>
                  </div>
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
                  <div class="form-group" @submit.prevent="editUserData">
                    <label
                      for="exampleFormControlTextarea1"
                    >Aktualnie nie posiadasz opisu. Napisz coś o sobie.</label>
                    <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
                    <button type="submit" class="btn btn-secondary">Zapisz</button>
                  </div>
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

        <b-col cols="3">
          <div class="card text-white bg-secondary mb-3" style="width: 18rem;">
            <div class="card-header">
              <h3>O mnie:</h3>
            </div>
            <ul class="list-group list-group-flush">
              <li class="list-group-item">Imię i nazwisko: {{user_data.name}} {{user_data.surname}}</li>
              <li class="list-group-item">Płeć: {{user_data.sex}}</li>
              <li class="list-group-item">Wiek: {{getAge(user_data.birthday)}}</li>
              <li class="list-group-item">Mieszkam w: {{user_data.location}}</li>
              <li class="list-group-item">Urodziny: {{user_data.birthday}}</li>
              <li class="list-group-item">Status:</li>
              <li class="list-group-item">Papierosy:</li>
              <li class="list-group-item">Alkohol:</li>
            </ul>
          </div>

          <div class="card text-white bg-secondary mb-3" style="width: 18rem;">
            <div class="card-header">
              <h3>Wygląd:</h3>
            </div>
            <ul class="list-group list-group-flush">
              <li class="list-group-item">Wzrost: {{user_data.growth}}</li>
              <li class="list-group-item">Waga: {{user_data.weight}}</li>
              <li class="list-group-item">Włosy: {{user_data.hair_color}}</li>
              <li class="list-group-item">Sylwetka: {{user_data.body_type}}</li>
              <li class="list-group-item">Znaki szczególne:</li>
              <li class="list-group-item"></li>
            </ul>
          </div>

          <div class="card text-white bg-secondary mb-3" style="width: 18rem;">
            <div class="card-header">
              <h3>Cechy charakteru:</h3>
            </div>
            <ul class="list-group list-group-flush">
              <li class="list-group-item">Jakas cecha</li>
            </ul>
          </div>

          <div class="card text-white bg-secondary mb-3" style="width: 18rem;">
            <div class="card-header">
              <h3>Zainteresowania:</h3>
            </div>
            <ul class="list-group list-group-flush">
              <li class="list-group-item">Hobby:</li>
              <li class="list-group-item">Muzyka:</li>
            </ul>
          </div>

          <div class="card text-white bg-secondary mb-3" style="width: 18rem;">
            <div class="card-header">
              <h3>Poszukiwany ideał:</h3>
            </div>
            <ul class="list-group list-group-flush">
              <li class="list-group-item">Płeć: {{user_preferences.sex_preference}}</li>
              <li class="list-group-item">Przedział wiekowy:</li>
              <li class="list-group-item">ect</li>
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
#userpage {
  height: 1200px;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: white;
}
#nav {
  padding: 5px;
}
#nav a {
  font-weight: bold;
  color: #2c3e50;
}
#nav a.router-link-exact-active {
  color: #42b983;
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
textarea.form-control-lg {
  height: 100%;
}
</style>