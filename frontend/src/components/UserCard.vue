<template>
  <b-card
    v-if="profileImage==null"
    img-src="https://www.manufacturingusa.com/sites/manufacturingusa.com/files/default.png"
    img-alt="Card image"
    img-left
    class="mb-3"
  >
    <b-card-text>
      <h1>{{user_data.username}}</h1>
      <br />Description
    </b-card-text>
    
  </b-card>
</template>

<script>
//import Api from "../service/api";
//import { mapState } from "vuex";
import axios from 'axios';

export default {
  name: "UserCard",
  components: {},
  /*computed: {
    ...mapState(["currentUser"])
  },*/
  data() {
    return {
      user_data: {},
      profileImage: null

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
    }
  }
};

</script>
<style>
</style>