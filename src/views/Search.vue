<template>
  <div class="page">
    <form id="filters" @submit.prevent="filterUsers">
      <table>
        <tr>
          <th>
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
          </th>
          <th>
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
          </th>
          <th>
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
          </th>
          <th>
            <div id="filter">
              <input type="submit" value="Filtruj" />
            </div>
          </th>
        </tr>
      </table>
    </form>

    <h1 id="title">Wyniki wyszukiwania:</h1>
    <div class="users-list" v-for="user in users" v-bind:key="user.id">
      <router-link :to="{ name: 'userprofile', params: {username: user.username}}">
        <div id="photo">
          <b-card :img-src="getUrl(user.profile_picture)" img-alt="Card image" img-left class="user-card">
            <b-card-title>
              <h2>{{user.username}} ({{getAge(user.birthday)}})</h2>
            </b-card-title>
            <b-card-text>
              <br />
              <h3 v-if="user.description!=null">{{user.description}}</h3>
              <h3 v-else>Brak opisu.</h3>
            </b-card-text>
          </b-card>
        </div>
      </router-link>
      <br />
    </div>
    <!--
    <table id="users-list">
      <tr v-for="i in Math.ceil(users.length / 3)" v-bind:key="i">
        <td v-for="user in users.slice((i - 1) * 3, i * 3)" v-bind:key="user.id">
          <div class="card">
            <img
              class="card-img-top"
              src="https://image.shutterstock.com/image-vector/avatar-vector-male-profile-gray-260nw-538707355.jpg"
              alt="image alt"
            />
            <div class="card-body">
              <h5 class="card-title">{{user.name}} {{user.surname}}</h5>
              <ul class="list-group list-group-flush">
                <li class="list-group-item">Lokalizacja: {{user.location}}</li>
                <li class="list-group-item">Wiek: {{user.birthday}}</li>
                <li class="list-group-item">Płeć: {{user.sex}}</li>
              </ul>
            </div>
            <div class="card-text">{{user.description}}</div>
            <div class="card-body">
              <a href="#" class="card-link">Go to profile</a>
              <a href="#" class="card-link">Dodaj do ulubionych</a>
            </div>
          </div>
        </td>
      </tr>
    </table>
    -->
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
      description: null,
      sex_options: [
        { value: null, text: "Płeć" },
        { value: "Male", text: "Mężczyzna" },
        { value: "Female", text: "Kobieta" },
      ],
      location_options: [
        { value: null, text: "Lokalizacja" },
        { value: "Poznań", text: "Poznań" },
        { value: "Placeholder", text: "Placeholder" },
      ],
      fields: ["location", "sex", "birthday"],
    };
  },
  methods: {
    getUsers() {
      axios
        .get("http://127.0.0.1:8000/api/user/users", {
          params: {},
          headers: {
            Authorization: "Token " + localStorage.getItem("user-token"),
          },
        })
        .then((response) => {
          console.log(response), (this.users = response.data);
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
    filterUsers() {
      this.users = [];
      axios
        .get("http://127.0.0.1:8000/api/user/users", {
          data: {
            sex: this.sex,
            location: this.location,
            birthday: this.birthday,
          },
          headers: {
            Authorization: "Token " + localStorage.getItem("user-token"),
          },
        })
        .then((response) => {
          console.log(response), (this.users = response.data);
        })
        .catch((errors) => console.log(errors));
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
  width: 50%;
}
#filter {
  margin: auto;
  width: 100%;
  padding-left: 20px;
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
.card-img-left {
  height: 300px;
  object-fit: scale-down;
}
.card-text {
  font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;
  text-align: left;
  font-size: 20px;
  color: white;
}
.user-card {
  background: #343a40;
  color: white;
}
</style>