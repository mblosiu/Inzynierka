<template>
  <div id="search">
    <br />
    <div class="row" style="height: 200px">
      <div class="col-md-3 justify-content-center">
        <h1>Podaj kryteria i wyszukaj:</h1>
        <form id="filters" @submit.prevent="filterUsers">
          <div id="filter">
            <b-form-select
              :options="sex_options"
              class="ml-2"
              id="sex"
              v-model="sex"
              size="sm"
              value="sex"
            ></b-form-select>
          </div>
          <br />
          <div id="filter">
            <b-form-select
              :options="location_options"
              class="ml-2"
              id="location"
              v-model="location"
              size="sm"
              value="location"
            ></b-form-select>
          </div>
          <br />
          <div id="filter">
            <input
              class="ml-2"
              type="text"
              name="birthday"
              id="birthday"
              v-model="birthday"
              placeholder="birthday"
            />
          </div>
          <br />
          <div id="filter">
            <input type="submit" value="Filtruj" />
          </div>
        </form>
      </div>
      <div class="col-md-8 justify-content-center">
        <h1>tu karty userow</h1>
        <br />
        <div>
          <p v-bind:key="user.id" v-for="user in users">
            <b-card
              v-if="profileImage==null"
              img-src="https://www.manufacturingusa.com/sites/manufacturingusa.com/files/default.png"
              img-alt="Card image"
              img-left
              class="mb-3"
            >
              <b-card-text>
                <h1>{{user.username}} ({{getAge(user.birthday)}})</h1>
                <br />opis usera
              </b-card-text>
            </b-card>
          </p>
        </div>
      </div>
      <div class="col-md-1"></div>
    </div>
    <div class="row">
      <div class="col-md-3 justify-content-center"></div>

      <div class="col-md-8 d-flex justify-content-center"></div>
      <div class="col-md-1"></div>
    </div>
  </div>
</template>


<script>
import axios from "axios";
export default {
  name: "UsersList",
  components: {},
  data() {
    return {
      birthday: null,
      sex: null,
      location: null,
      users: [],
      profileImage: null,
      today: new Date(),
      birthDate: "",
      age: "",
      m: "",
      sex_options: [
        { value: null, text: "Płeć" },
        { value: "Male", text: "Mężczyzna" },
        { value: "Female", text: "Kobieta" }
      ],
      location_options: [
        { value: null, text: "Lokalizacja" },
        { value: "Poznań", text: "Poznań" },
        { value: "Placeholder", text: "Placeholder" }
      ],
      fields: ["location", "sex", "birthday"]
    };
  },
  methods: {
    getUsers() {
      axios
        .get("http://127.0.0.1:8000/api/user/users", {
          params: {},
          headers: {
            Authorization: "Token " + localStorage.getItem("user-token")
          }
        })
        .then(response => {
          console.log(response), (this.users = response.data);
        })
        .catch(errors => console.log(errors));
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
    filterUsers() {
      this.users = [];
      axios
        .get("http://127.0.0.1:8000/api/user/users", {
          data: {
            sex: this.sex,
            location: this.location,
            birthday: this.birthday
          },
          headers: {
            Authorization: "Token " + localStorage.getItem("user-token")
          }
        })
        .then(response => {
          console.log(response), (this.users = response.data);
        })
        .catch(errors => console.log(errors));
    }
  },
  created() {
    this.getUsers();
  }
};
</script>

<style scoped>
#filters {
  margin: auto;
  width: 50%;
}

#filter {
  margin: auto;
  width: 100%;
  padding-left: 10px;
  padding-right: 10px;
}

#title {
  padding: 1cm;
}

.card {
  margin: auto;
  width: 80%;
  height: 300px;
}

td {
  padding-left: 2.1cm;
  padding-right: 2.1cm;
  padding-bottom: 1cm;
}
#nav {
  padding: 30px;
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
  color: midnightblue;
}
</style>