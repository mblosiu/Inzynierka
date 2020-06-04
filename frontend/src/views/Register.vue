<template>
  <div class="register-form">
    <form @submit.prevent="registerUser">
      <label for="Name">Name</label> <br />
      <input type="text" name="Name" id="Name" v-model="name"> <br />
      <label for="el">Email</label> <br />
      <input type="email" name="el" id="el" v-model="email"> <br />
      <label for="ur">Username</label> <br />
      <input type="text" name="ur" id="ur" v-model="username"> <br />
      <label for="pwr">Password</label> <br />
      <input type="password" name="pwr" id="pwr" v-model="password"> <br />
      <label for="pass">Password Confirmation</label> <br />
      <input type="password" name="pass" id="pass" v-model="confirm"> <br />
      <button type="submit">Register</button> <br />
    </form>
  </div>
</template>

<script>
export default {};
</script>

<style>
</style>