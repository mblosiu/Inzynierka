<template>
  <div class>
    <h1>User Registration</h1>

    <form id="formvideo" @submit.prevent="CreateUser">
      <p>
        <label for="username">Username</label>
        <input class="ml-2" type="text" name="username" id="username1" v-model="username" />
      </p>
      <p>
        <label for="password">Password</label>
        <input class="ml-2" type="text" name="password" id="password1" v-model="password" />
      </p>
      <p>
        <label for="password2">password2</label>
        <input class="ml-2" type="text" name="password2" id="password2" v-model="password2" />
      </p>
      <p>
        <label for="email">email</label>
        <input class="ml-2" type="text" name="email" id="email" v-model="email" />
      </p>
      <p>
        <label for="birthday">birthday</label>
        <input class="ml-2" type="text" name="birthday" id="birthday" v-model="birthday" />
      </p>
      <p>
        <label for="location">location</label>
        <input class="ml-2" type="text" name="location" id="location" v-model="location" />
      </p>
      <p>
        <label for="sex">sex</label>
        <input class="ml-2" type="text" name="sex" id="sex" v-model="sex" />
      </p>
      <p>
        <input type="submit" value="Submit" />
      </p>
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "register",
  components: {},
  data() {
    return {
      username: null,
      password: null,
      password2: null,
      email: null,
      birthday: null,
      location: null,
      sex: null
    };
  },
  methods: {
    CreateUser() {
      console.log(this.username);
      axios
        .post("http://127.0.0.1:8000/api/user/register", {
          username: this.username,
          password: this.password,
          password2: this.password2,
          email: this.email,
          birthday: this.birthday,
          location: this.location,
          sex: this.sex
        })
        .then(response => console.log(response))
        .catch(errors => console.log(errors));
      this.$router.push("/");
    }
  }
};
</script>