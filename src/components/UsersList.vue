<template>
  <div class>
    <div id="filters">
      <form id="filter-form" @submit.prevent="filterUsers">
        <div id="filter">
          <b-form-select v-model="location" :options="options" size="sm" class="mt-3"></b-form-select>
        </div>
        <div id="filter">
          <label for="birthday">birthday</label>
          <input class="ml-2" type="text" name="birthday" id="birthday" v-model="birthday" />
        </div>
        <p>
          <input type="submit" value="Submit" />
        </p>
      </form>
    </div>

    <h1>Lista potencjalnych partnerów</h1>
    <div id="users-list">
      <b-table striped hover :items="users" :fields="fields"></b-table>
    </div>

    <div class="card" style="width: 18rem;">
      <img class="card-img-top" src alt="Card image cap" />
      <div class="card-body">
        <h5 class="card-title">Imie nazwisko</h5>
        <ul class="list-group list-group-flush">
          <li class="list-group-item">Lokalizacja</li>
          <li class="list-group-item">Wiek</li>
          <li class="list-group-item">Płeć</li>
        </ul>
      </div>
      <p
        class="card-text"
      >Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin nibh augue, suscipit a, scelerisque sed, lacinia in, mi. Cras vel lorem. Etiam pellentesque aliquet tellus. Phasellus pharetra nulla ac diam. Quisque semper justo at risus.</p>

      <div class="card-body">
        <a href="#" class="card-link">Card link</a>
        <a href="#" class="card-link">Another link</a>
      </div>
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
      options: [
        { value: "Poznań", text: "Poznań" },
        { value: "Placeholder", text: "Placeholder" }
      ],
      fields: ["location", "sex", "birthday"]
    };
  },
  methods: {
    getUsers() {
      this.users = [];
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
#users-list {
  margin-left: 100px;
  margin-right: 100px;
}

#filter {
  width: 100px;
}
</style>