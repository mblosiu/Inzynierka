<template>
  <b-card
    v-if="profileImage==null"
    img-src="https://www.manufacturingusa.com/sites/manufacturingusa.com/files/default.png"
    img-alt="Card image"
    img-left
    class="mb-3"
  >
    <b-card-text>
      {{currentUser}}
      <br />Description
    </b-card-text>
    <button @click="getUser">getuser</button>
  </b-card>
</template>

<script>
import Api from "../service/api";
import { mapState } from "vuex";

export default {
  name: "UserCard",
  components: {},
  computed: {
    ...mapState(["currentUser"])
  },
  data() {
    return {
      profileImage: null

    };
  },
  methods: {
    getUser() {
      let currentUser = currentUser;
      Api().post("/account/users", {currentUser}), {
        headers: {
          'Authorization': currentUser
        }
      }
    }
  }
};

</script>
<style>
</style>