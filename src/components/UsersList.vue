<template>
  <div class>
    <div v-if="token != null">{{$router.push('/')}}</div>
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

    <h1 id="title">Lista potencjalnych partnerów</h1>

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
        .catch(errors => {
          if (errors.response.status == 401) {
            this.$router.push("/");
          }
          console.log(errors.status);
        });
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
  min-width: 100%;
  height: 700px;
}

td {
  padding-left: 2.1cm;
  padding-right: 2.1cm;
  padding-bottom: 1cm;
}
</style>