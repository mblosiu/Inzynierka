<template>
  <div class>
    <h1>Informations about you</h1>
    <form id="editUser" @submit.prevent="editUserData">
      <p>
        <label for="user_data.location">Location</label>
        <input
          class="ml-2"
          type="text"
          name="user_data.location"
          id="user_data.location"
          v-model="user_data.location"
          value="user_data.location"
        />
      </p>
      <p>
        <label for="user_data.sex">Sex</label>
        <input
          class="ml-2"
          type="text"
          name="user_data.sex"
          id="user_data.sex"
          v-model="user_data.sex"
          value="user_data.sex"
        />
      </p>
      <p>
        <input type="submit" value="Save" />
      </p>
    </form>

    <h1>Your preferences</h1>

    <form id="editUserPreferences" @submit.prevent="editUserPreferences">
      <p>
        <label for="user_preferences.sex_preference">Sex preference</label>
        <input
          class="ml-2"
          type="text"
          name="user_preferences.sex_preference"
          id="user_preferences.sex_preference"
          v-model="user_preferences.sex_preference"
          value="user_preferences.sex_preference"
        />
      </p>
      <p>
        <input type="submit" value="Save" />
      </p>
    </form>
  </div>
</template>


<script>
import axios from "axios";
export default {
  name: "UsersProfile",
  components: {},
  data() {
    return {
      user_data: {},
      user_preferences: {}
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
          { location: this.user_data.location, sex: this.user_data.sex },
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
    }
  },
  created() {
    this.getUserData();
    this.getUserPreferences();
  }
};
</script>