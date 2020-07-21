<template>
  <div id="search">
    <br />
    <div class="row" style="height: 200px">
      <div class="col-md-3 justify-content-center">
        <h1>Podaj kryteria i wyszukaj:</h1>
        <br />searchForm
        <br />
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
                <h1>{{user.username}}</h1>
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
//import UserCard from '../components/UserCard';
//import Api from '../service/api';
import axios from "axios";

export default {
  name: "Search",
  components: {
    //UserCard
  },
  data() {
    return {
      users: [],
      profileImage: null
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
    }
  },
  created() {
    this.getUsers();
  }
};
</script>

<style>
</style>