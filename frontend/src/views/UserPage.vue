<template>
  <div id="userpage">
    <br />
    <b-container class="bv-example-row" fluid>
      <b-row>
        <b-col cols="2">
          <div>
            <b-nav-item>Szukaj osób</b-nav-item>
            <b-nav-item>Dopasuj</b-nav-item>
            <b-nav-item>Polubienia</b-nav-item>
            <b-nav-item>Wiadomości</b-nav-item>
            <b-nav-item>Kontakty</b-nav-item>
            <b-nav-item>Galeria</b-nav-item>
            <b-nav-item>Ustawienia profilu</b-nav-item>
            <b-nav-item disabled>Premium</b-nav-item>
          </div>
        </b-col>
        <b-col cols="7">
          <b-card
            img-src="https://www.manufacturingusa.com/sites/manufacturingusa.com/files/default.png"
            img-alt="Card image"
            img-left
            class="mb-3"
          >
            <b-card-text>Opis usera <br />
              Witam, jestem {{username}}

            </b-card-text>
          </b-card>
        </b-col>
        <b-col cols="3">
          <h1>O mnie:</h1>
          <p>Imię: {{username}}</p>
          <p>Wiek:</p>
          <p>Płeć:</p>
          <p>Mieszkam w:</p>
          <p>Urodziny:</p>
          <p>Wygląd:</p>
          <br />
          <h4>Cechy charakteru:</h4>
          <br /> 
          <h1>Zainteresowania: </h1>
          <p>Hobby:</p>
          <p>Muzyka:</p>

          <br />
          <h1>Szukam:</h1>
          <p>Płeć:</p>
          <p>Przedział wiekowy:</p>
          <p>Region:</p>
          <p></p>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>


<script>
export default {
  name: "UserPage",
  components: {},
  data() {
    return {
      token: localStorage.getItem("user-token") || null,
      username: localStorage.getItem("username") || null
    };
  },
  methods: {}
};
</script>


<style>
#userpage {
  height: 1200px;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: white;
  
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

.card-img-left {
  height: 300px;
  object-fit: scale-down;
}

.card-text{
  font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  text-align: left;
  font-size: 20px;
  color:midnightblue;

}

p{
  text-align: left;
}
</style>