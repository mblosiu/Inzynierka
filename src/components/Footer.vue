<template>
  <v-footer color="purple" padless>
    <v-row justify="center" no-gutters>
      <v-spacer></v-spacer>
      <v-btn color="yellow" text rounded class="my-2" href="https://forms.gle/McQgxy2bTwmBjgXy9"> Feedback </v-btn>
      <v-spacer></v-spacer>
      <v-btn color="white" text rounded class="my-2" @click.stop="about = true">
        <v-icon class="white"></v-icon>
        O nas
      </v-btn>
      <v-spacer></v-spacer>
      <v-btn
        color="white"
        text
        rounded
        class="my-2"
        @click.stop="regulations = true"
      >
        Regulamin
      </v-btn>
      <v-spacer></v-spacer>
      <v-btn
        color="white"
        text
        rounded
        class="my-2"
        @click.stop="contact = true"
      >
        Kontakt
      </v-btn>

      <v-spacer></v-spacer>
      <v-col class="purple py-4 text-center white--text" cols="12">
        {{ new Date().getFullYear() }} — <strong>Vuetify</strong>
      </v-col>
    </v-row>

    <v-dialog v-model="about" max-width="700">
      <v-card class="purple lighten-5">
        <v-img
          class="white--text align-end"
          height="200px"
          src="https://www.otouczelnie.pl/assets/uploads/wydzial/834ff-wydzial-matematyki-uam.jpg"
        >
          <v-card-title><b>O twórcach</b></v-card-title>
        </v-img>

    
        <br/>
        <v-card-text class="text-left">
          Serwis randkowy e-Love tworzony jest przez dwóch studentów informatyki
          uniwersytetu im. Adama Mickiewicza w Poznaniu, w ramach inżynierskiego
          projektu zespołowego.
          <br />
          <v-card-subtitle>~ Mateusz Błoszyk, Marcin Mirecki </v-card-subtitle>
          <v-divider></v-divider>
          <v-row>
            <v-spacer></v-spacer>
            <v-btn
              color="purple darken-3"
              rounded
              elevation="10"
              href="https://github.com/mblosiu/Inzynierka"
              ><v-icon color="white" class="mr-2">mdi-github</v-icon
              ><button class="white--text">Repozytorium</button></v-btn
            >
            <v-spacer></v-spacer>
          </v-row>
          <v-divider></v-divider>
        </v-card-text>
        <v-card-subtitle>
          Ostatnia aktualizacja:
          <p class="font-weight-bold"></p>
          5.01.2021r.
        </v-card-subtitle>
      </v-card>
    </v-dialog>
    <v-dialog v-model="regulations" max-width="700">
      <v-card class="purple lighten-5">
        <v-card-title class="headline"> Regulamin </v-card-title>

        <v-divider></v-divider>
        <v-card-text>
          <h5 class="card-title">1. Postanowienia ogólne.</h5>

          <p class="font-italic">
            Bądźmy dla siebie mili i życzliwi. Serwis powstał aby szerzyć
            miłość, nie nienawiść.
          </p>
        </v-card-text>

        <v-divider></v-divider>
        <v-card-subtitle>
          Ostatnia aktualizacja:
          <p class="font-weight-bold"></p>
          5.01.2021r.
        </v-card-subtitle>
      </v-card>
    </v-dialog>
    <v-dialog v-model="contact" max-width="290">
      <v-card class="purple lighten-5">
        <v-card-title class="headline"> Kontakt </v-card-title>
        <v-divider></v-divider>
        <v-card-text>
          <div class="card-body">
            <div class="card-text">
              Mateusz Błoszyk:
              <p class="font-italic">mblosiu@gmail.com</p>
              Marcin Mirecki:
              <p class="font-italic">marmir@st.amu.edu.pl</p>
            </div>
          </div>
        </v-card-text>
      </v-card>
    </v-dialog>
  </v-footer>
</template>

<script>
export default {
  name: "Footer",
  components: {},
  data() {
    return {
      about: false,
      contact: false,
      regulations: false,
    };
  },
};
</script>
<style scoped>
a {
  color: white;
}

/* mouse over link */
a:hover {
  color: green;
  text-decoration: none;
}
.footer {
  background-color: #9a3f66;
}
</style>
