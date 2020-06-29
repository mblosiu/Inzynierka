<template>
  <b-card
    v-if="profileImage==null"
    img-src="https://www.manufacturingusa.com/sites/manufacturingusa.com/files/default.png"
    img-alt="Card image"
    img-left
    class="mb-3"
  >
    <b-card-text>
      {{currentUser.name}}
      <br />Description
    </b-card-text>
    <button @click="getUser">getuser</button>
  </b-card>
</template>

<script>
import Api from "../service/api";
import { mapState } from 'vuex';

export default {
  name: "UserCard",
  components: {},
  computed: {
    ...mapState(["currentUser"])
  },
  data() {
    return {
      username: localStorage.getItem("username") || null,
      profileImage: null
    };
  },
  methods: {
    getUser() {
      Api()
        .get("/account/users")
        .then(Response => {
          console.log(Response);
        })
        .catch(Error => {
          console.log(Error);
        });
    }
  }
};
</script>
<style>
</style>