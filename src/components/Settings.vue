<template>
  <div class>
    <table>
      <tr>
        <td>
          <form class="profile" @submit.prevent="editUserData">
            <p class="h4 text-center mb-4">Informacje o tobie</p>

            <label for="user_name" class="grey-text">Imie</label>
            <input type="text" id="user_name" v-model="user_data.name" class="form-control" />

            <label for="user_surname" class="grey-text">Nazwisko</label>
            <input type="text" id="user_surname" v-model="user_data.surname" class="form-control" />

            <label for="user_location" class="grey-text">Adres</label>
            <input type="text" id="user_location" v-model="user_data.location" class="form-control" />

            <label for="user_sex" class="grey-text">Płeć</label>
            <b-form-select
              class="form-control"
              id="user_sex"
              v-model="user_data.sex"
              :options="sex_options"
            ></b-form-select>
            <div class="text-center mt-4">
              <button type="submit" class="btn btn-secondary">Zapisz</button>
            </div>
          </form>
        </td>
        <td>
          <form class="preferences" @submit.prevent="editUserPreferences">
            <p class="h4 text-center mb-4">Twoje preferencje</p>

            <label for="user_sex_preference" class="grey-text">Preferencje seksualne</label>
            <b-form-select
              class="form-control"
              id="user_sex_preference"
              v-model="user_preferences.sex_preference"
              :options="sex_options"
            ></b-form-select>
            <div class="text-center mt-4">
              <button type="submit" class="btn btn-secondary">Zapisz</button>
            </div>
          </form>
        </td>
        <td>
          <form class="settings" @submit.prevent="editUserSettings">
            <p class="h4 text-center mb-4">Twoje ustawienia</p>

            <label for="user_sex_preference" class="grey-text">Placeholder</label>
            <b-form-select
              class="form-control"
              id="placeholder"
              v-model="placeholder"
              :options="sex_options"
            ></b-form-select>

            <label for="placeholder" class="grey-text">Placeholder</label>
            <input type="text" id="placeholder" v-model="placeholder" class="form-control" />

            <div class="text-center mt-4">
              <button type="submit" class="btn btn-secondary">Zapisz</button>
            </div>
          </form>
        </td>
      </tr>
    </table>
  </div>
</template>


<script>
import axios from "axios";
export default {
  name: "UsersProfile",
  components: {},
  data() {
    return {
      placeholder: null,
      active: "",
      user_data: {},
      user_preferences: {},
      sex_options: [
        { value: null, text: "Wybierz płeć" },
        { value: "Male", text: "Mężczyzna" },
        { value: "Female", text: "Kobieta" }
      ]
    };
  },
  methods: {
    getUserData() {
      axios
        .get("http://127.0.0.1:8000/api/user/properties", {
          params: {},
          headers: {
            Authorization: "Token " + localStorage.getItem("user-token")
          }
        })
        .then(response => {
          console.log(response), (this.user_data = response.data);
        })
        .catch(errors => console.log(errors));
    },
    editUserData() {
      let config = {
        headers: {
          Authorization: "Token " + localStorage.getItem("user-token")
        }
      };
      axios
        .patch(
          "http://127.0.0.1:8000/api/user/properties",
          {
            surname: this.user_data.surname,
            name: this.user_data.name,
            location: this.user_data.location,
            sex: this.user_data.sex
          },
          config
        )
        .then(response => {
          console.log(response);
        })
        .catch(errors => console.log(errors));
    },
    getUserPreferences() {
      axios
        .get("http://127.0.0.1:8000/api/user/preferences", {
          params: {},
          headers: {
            Authorization: "Token " + localStorage.getItem("user-token")
          }
        })
        .then(response => {
          console.log(response), (this.user_preferences = response.data);
        })
        .catch(errors => console.log(errors));
    },
    editUserPreferences() {
      let config = {
        headers: {
          Authorization: "Token " + localStorage.getItem("user-token")
        }
      };
      axios
        .patch(
          "http://127.0.0.1:8000/api/user/preferences",
          { sex_preference: this.user_preferences.sex_preference },
          config
        )
        .then(response => {
          console.log(response);
        })
        .catch(errors => console.log(errors));
    },
    getUserSettings() {},
    editUserSetting() {}
  },
  created() {
    this.getUserData();
    this.getUserPreferences();
    this.getUserSettings();
  }
};
</script>

<style scoped>
.profile {
  width: 300px;
  margin-left: auto;
  margin-right: auto;
  border: 2px groove #343a40;
  border-radius: 25px;
  padding: 0.5cm;
}
.preferences {
  width: 300px;
  margin-left: auto;
  margin-right: auto;
  border: 2px groove #343a40;
  border-radius: 25px;
  padding: 0.5cm;
}
.settings {
  width: 300px;
  margin-left: auto;
  margin-right: auto;
  border: 2px groove #343a40;
  border-radius: 25px;
  padding: 0.5cm;
}
table {
  margin-left: auto;
  margin-right: auto;
  width: 80%;
}
</style>

