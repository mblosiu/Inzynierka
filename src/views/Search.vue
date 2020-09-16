<template>
  <div class="page">
    <b-container class="bv-example-row" fluid>
      <b-row>
        <b-col cols="1"></b-col>
        <b-col cols="10">
          <nav class="navbar navbar-expand-lg">
            <div
              data-toggle="tooltip"
              data-placement="right"
              title="Wyszukaj użytkowników za pomocą nałożonych filtrów, bądź konkretnego z nich po jego nazwie"
            >
              <svg
                width="2em"
                height="2em"
                viewBox="0 0 16 16"
                class="bi bi-question-circle"
                fill="currentColor"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  fill-rule="evenodd"
                  d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"
                />
                <path
                  d="M5.255 5.786a.237.237 0 0 0 .241.247h.825c.138 0 .248-.113.266-.25.09-.656.54-1.134 1.342-1.134.686 0 1.314.343 1.314 1.168 0 .635-.374.927-.965 1.371-.673.489-1.206 1.06-1.168 1.987l.003.217a.25.25 0 0 0 .25.246h.811a.25.25 0 0 0 .25-.25v-.105c0-.718.273-.927 1.01-1.486.609-.463 1.244-.977 1.244-2.056 0-1.511-1.276-2.241-2.673-2.241-1.267 0-2.655.59-2.75 2.286zm1.557 5.763c0 .533.425.927 1.01.927.609 0 1.028-.394 1.028-.927 0-.552-.42-.94-1.029-.94-.584 0-1.009.388-1.009.94z"
                />
              </svg>
            </div>
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
                      <b-form-select
                        :options="location_options"
                        class="ml-2"
                        id="location"
                        v-model="location"
                        size="md"
                        value="location"
                      ></b-form-select>
                    </div>
                  </th>
                  <th>
                    <div id="filter">
                      <b-form-input
                        type="number"
                        id="agemin"
                        size="md"
                        placeholder="wiek min"
                        v-model="age_min"
                        class="form-control"
                      />
                    </div>
                  </th>
                  <th>
                    <div id="filter">
                      <input
                        type="number"
                        id="agemax"
                        size="md"
                        placeholder="wiek maks"
                        v-model="age_max"
                        class="form-control"
                      />
                    </div>
                  </th>
                  <!--<th>
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
                  </th>-->
                  <th>
                    <b-nav-form>
                      <b-form-input
                        size="md"
                        class="mr-sm-2"
                        placeholder="Nazwa użytkownika"
                        v-model="searchText"
                      ></b-form-input>
                    </b-nav-form>
                  </th>
                  <th>
                    <div id="filter">
                      <button type="submit" class="btn btn-primary float-right">Filtruj</button>
                    </div>
                  </th>
                </tr>
              </table>
            </form>

            <!--<input
              class="form-control mr-sm-2"
              type="search"
              placeholder="Nazwa użytkownika"
              aria-label="Search"
            />
            <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Filtruj</button>-->
          </nav>
        </b-col>
        <b-col cols="1"></b-col>
      </b-row>
      <b-row>
        <b-col cols="1"></b-col>
        <b-col cols="10">
          <h1 id="title" v-if="searchText">Wyniki wyszukiwania dla frazy {{ searchText }}:</h1>
          <h1 id="title" v-else>Wyniki wyszukiwania:</h1>
        </b-col>
        <b-col cols="1"></b-col>
      </b-row>
      <b-row>
        <b-col cols="12" align-self="start" class="scroll">
          <b-row v-for="i in Math.ceil(users.length / 2)" v-bind:key="i">
            <b-col
              cols="6"
              v-for="user in users.slice((i - 1) * 2, i * 2)"
              v-bind:key="user.id"
              style="ml-5 mr-5"
            >
              <router-link :to="{ name: 'userprofile', params: { pk: user.pk } }">
                <div cardbox>
                  <b-card
                    :img-src="getUrl(user.profile_picture)"
                    img-alt="Card image"
                    img-left
                    class="user-card"
                  >
                    <b-card-title>
                      <h2>{{ user.username }} ({{ getAge(user.birthday) }})</h2>
                    </b-card-title>

                    <b-card-text>
                      <br />
                      <h3 v-if="user.description != null">{{ user.description }}</h3>
                      <h3 v-else>Brak opisu.</h3>
                    </b-card-text>
                  </b-card>
                </div>
              </router-link>
            </b-col>
          </b-row>
          <br />
          <!--<div class="users-list" v-for="user in users" v-bind:key="user.id">
            <router-link :to="{ name: 'userprofile', params: { pk: user.pk } }">
              <div id="photo">
                <b-card :img-src="getUrl(user.profile_picture)" img-alt="Card image" img-left class="user-card">
                  <b-card-title>
                    <h2>{{ user.username }} ({{ getAge(user.birthday) }})</h2>
                  </b-card-title>
                  <b-card-text>
                    <br />
                    <h3 v-if="user.description != null">{{ user.description }}</h3>
                    <h3 v-else>Brak opisu.</h3>
                  </b-card-text>
                </b-card>
              </div>
            </router-link>
            <br />
          </div>-->
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "UsersList",
  components: {},
  data() {
    return {
      searchText: null,
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
        { value: null, text: "płeć" },
        { value: "Male", text: "mężczyzna" },
        { value: "Female", text: "kobieta" },
        { value: "Other", text: "inna" },
      ],
      location_options: [
        { value: null, text: "lokalizacja" },
        { value: "Poznań", text: "Poznań" },
        { value: "Warszawa", text: "Warszawa" },
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
}
.navbar {
  border-radius: 17px;
  background-color: #db4460;
}
.title{

}
</style>
