<template>
  <div class>
    <h1>Profile</h1>
    {{user_data.username}}
    <br>
    {{user_data.sex}}
    <br>
    {{user_data.location}}
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
        .get("http://127.0.0.1:8000/api/account/properties", {
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
    getUserPreferences() {
      axios
        .get("http://127.0.0.1:8000/api/account/preferences", {
          params: {},
          headers: {
            Authorization: "Token " + localStorage.getItem("user-token")
          }
        })
        .then(response => {
          console.log(response), (this.user_preferences = response.data);
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