<template>
  <div class>
    <h1>Users list</h1>
    <div>
      <p v-bind:key="user.id" v-for="user in users">
        {{user.username}}
        <br />
        {{user.sex}}
        <br />
        {{user.location}}
        <br />
        <br />
      </p>
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
      users: []
    };
  },
  methods: {
    getUsers() {
      axios
        .get("http://127.0.0.1:8000/api/account/users", {
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
  },
  created() {
    this.getUsers();
  }
};
</script>