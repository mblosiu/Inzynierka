<template>
  <div class="register-form">
    <form @submit.prevent="registerUser">
      <p>
      <label for="el"><h5>Email</h5></label> <br />
      <input type="email" name="el" id="el" v-model="email"> <br /> <br />
      </p>
      <p>
      <label for="Name"><h5>Nazwa konta</h5></label> <br />
      <input type="text" name="Name" id="Name" v-model="name"> <br /> <br />
      </p>
      <p>
      <label for="Sex"><h5>Płeć</h5></label> <br />
      <select class="ml-2" name="Sex" id="Sex" v-model="sex"> <br />
        <option>mężczyzna</option>
        <option>kobieta</option>
        <option>inna</option>
      </select>
      </p>
      <p>
      <label for="date"><h5>Data urodzenia</h5></label> <br />
      <input type="date" name="Date" id="Locatiom" v-model="date"> <br /> <br />
      </p>
      <p>
      <label for="Location"><h5>Lokacja</h5></label> <br />
      <input type="text" name="Location" id="Locatiom" v-model="location"> <br /> <br />
      </p>
      <p>
      <label for="pwr"><h5>Hasło</h5></label> <br />
      <input type="password" name="pwr" id="pwr" v-model="password"> <br /> <br />
      </p>
      <p>
      <label for="pass"><h5>Powtórz hasło</h5></label> <br />
      <input type="password" name="pass" id="pass" v-model="confirm"> <br /> <br /> <br />
      </p>
      <p>
      <!--<button type="submit">Zarejestruj</button> <br />-->
      <input class="btn btn-outline-success" type="submit" value="Zarejestruj">
      </p>
    </form>
  </div>
</template>

<script>

//import axios from 'axios'

export default {};
</script>

<style>

h5{
  color: gold;
}

box{
  background-color: lightgrey;
  width: 300px;
  border: 15px solid green;
  padding: 50px;
  margin: 20px;
}
</style>