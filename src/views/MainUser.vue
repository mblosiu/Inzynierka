<template>
  <div id="mainuser">
    <br />
    <b-container class="bv-example-row" fluid>
      <b-row>
        <b-col cols="2">
          <div>
            <router-link to="mainuser/search">Szukaj osób</router-link>
            <b-nav-item disabled>Dopasuj</b-nav-item>
            <b-nav-item disabled>Polubienia</b-nav-item>
            <b-nav-item disabled>Wiadomości</b-nav-item>
            <b-nav-item disabled>Kontakty</b-nav-item>
            <router-link to="mainuser/gallery">Galeria</router-link>
            <br />
            <router-link to="mainuser/settings">Ustawienia profilu</router-link>
            <b-nav-item disabled>Premium</b-nav-item>
          </div>
        </b-col>
        <b-col cols="7">
          <b-card
            v-if="profileImage==null"
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
              <div class="form-group" @submit.prevent="editUserData">
                <label for="exampleFormControlTextarea1">Aktualnie nie posiadasz opisu. Napisz coś o sobie.</label>
                <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
                <button type="submit" class="btn btn-secondary">Zapisz</button>
              </div>
              </div>
            </b-card-text>
          </b-card>
        </b-col>
        <b-col cols="3">
          <h1>O mnie:</h1>
          <p>Imię: {{user_data.username}}</p>
          <p>Wiek: {{getAge(user_data.birthday)}}</p>
          <p>Płeć: {{user_data.sex}}</p>
          <p>Mieszkam w: {{user_data.location}}</p>
          <p>Urodziny: {{user_data.birthday}}</p>
          <p>Wygląd:</p>
          <br />
          <h4>Cechy charakteru:</h4>
          <br />
          <h1>Zainteresowania:</h1>
          <p>Hobby:</p>
          <p>Muzyka:</p>

          <br />
          <h1>Szukam:</h1>
          <p>Płeć: {{user_preferences.sex_preference}}</p>
          <p>Przedział wiekowy:</p>
          <p>Region:</p>
          <p></p>
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
      profileImage: null,
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
</style>