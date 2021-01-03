<template>
  <div class="home">
    <b-container class="bv-example-row" fluid>
      <b-row>
        <b-col cols="4">
          <h1>Witamy w e-love</h1>
        </b-col>
        <b-col cols="8"></b-col>
      </b-row>
      <br />
      <b-row>
        <b-col class="leftside" cols="4">
          <h4>Tu znajdziesz swoją drugą połówkę!</h4>
          <br />
          <div class="text">
            Jeśli szukasz miłości, życiowego partnera, lub po prostu osoby, z
            którą można porozmawiać na wspólne tematy to dobrze trafiłeś. Serwis
            e-Love skierowany jest do każdego użytkownika bez względu na wiek,
            czy rodzaj zawieranych relacji.
            <br />W dzisiejszych czasach samotność jest bardzo częstym problemem
            i dotyka ludzi z każdego przedziału wiekowego. Poza faktem iż
            samotność sama w sobie jest przykrym uczuciem, należy dodać, że jak
            donoszą najnowsze badania, długotrwałe jej doświadczanie bardzo
            niekorzystnie wpływa na nasze zdrowie. <br />
            Nasz portal jest stale rozwijany i powiększa się nie tylko o nowe
            funkcjonalności ale i nowych użytkowników. Zapraszamy do darmowej
            rejestracji!
            <br />
          </div>
          <br />

          <p></p>
          <blockquote class="blockquote text-right">
            <h6>
              "Każdy powinien mieć kogoś, z kim mógłby szczerze pomówić, bo
              choćby człowiek był nie wiadomo jak dzielny, czasami czuje się
              bardzo samotny."
            </h6>
            <footer class="blockquote-footer">
              Ernest Hemingway
              <cite title="Source Title">"Komu bije dzwon"</cite>
            </footer>
          </blockquote>
        </b-col>
        <br />
        <b-col cols="5"></b-col>
        <b-col cols="3">
          <br />

          <div class="card text-black mb-3 rightside" style="width: 19rem">
            <div class="card-body no-background">
              <br />
              <h3 class="card-title no-background">Nie masz konta?</h3>
              <br />
              <h6>
                <p class="card-text no-background">
                  Dołącz do społeczności e-love zakładając darmowe konto!
                </p>
              </h6>
              <br />
              <v-row justify="center">
                <v-dialog v-model="registerDialog" persistent max-width="600px">
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn
                      color="purple"
                      class="white--text"
                      x-large
                      dark
                      v-bind="attrs"
                      v-on="on"
                    >
                      <button class="font-weight-bold">Zarejestruj się</button>
                    </v-btn>
                  </template>
                  <v-card>
                    <v-card-title flex class="purple">
                      <br />
                      <v-spacer></v-spacer>
                      <span class="headline white--text">Rejestracja</span>
                      <v-spacer></v-spacer>
                    </v-card-title>
                    <v-form @submit.prevent="createUser">
                      <v-card-text class="purple lighten-5">
                        <v-container>
                          <v-row>
                            <v-col cols="12" sm="6">
                              <v-text-field
                                label="Nazwa użytkownika*"
                                required
                                type="text"
                                name="username2"
                                id="username2"
                                v-model="username"
                                pattern="[a-zA-Z0-9]{4,}"
                                hint="Nazwa może zawierać małe, duże litery i cyfry."
                              ></v-text-field>
                            </v-col>
                            <v-col cols="12" sm="6">
                              <v-text-field
                                label="Miejsce zamieszkania*"
                                name="Location"
                                id="Location"
                                v-model="location"
                                required
                              ></v-text-field>
                            </v-col>

                            <v-col cols="12" sm="6">
                              <v-text-field
                                label="Email*"
                                required
                                type="email"
                                name="email"
                                id="email"
                                v-model="email"
                              ></v-text-field>
                            </v-col>
                            <v-col cols="12" sm="6">
                              <br />
                              <button>
                                Data urodzenia:
                                <input
                                  type="date"
                                  name="birthday"
                                  id="birthday"
                                  v-model="birthday"
                                  required
                                />
                              </button>
                            </v-col>

                            <v-col cols="12">
                              <v-text-field
                                label="Hasło*"
                                type="password"
                                required
                                name="password"
                                id="password"
                                v-model="password"
                                hint="Bezpieczne hasło musi składać się z co najmniej 8 znaków!"
                                pattern=".{8,}"
                              ></v-text-field>
                            </v-col>
                            <v-col cols="12">
                              <v-text-field
                                label="Powtórz hasło*"
                                type="password"
                                required
                                name="password2"
                                id="password2"
                                v-model="password2"
                                oninput='password2.setCustomValidity(password.value != password2.value ? "Hasła się różnią" : "")'
                              ></v-text-field>
                            </v-col>
                            <v-col cols="12" sm="6">
                              <v-select
                                :items="['Mężczyzna', 'Kobieta', 'Inna']"
                                label="Płeć*"
                                required
                                name="Sex"
                                id="Sex"
                                v-model="sex"
                              ></v-select>
                            </v-col>
                            <v-col cols="12" sm="6">
                              <v-checkbox
                                label="Akceptuję regulamin serwisu"
                                required
                                type="checkbox"
                                id="checkbox"
                                v-model="checked"
                              ></v-checkbox>
                              <router-link to="/regulations"
                                >regulamin</router-link
                              >
                            </v-col>
                          </v-row>
                        </v-container>
                        <br />
                        <small>*Pola wymagane</small>
                      </v-card-text>
                      <v-card-actions class="purple lighten-5">
                        <v-btn
                          color="red darken-1"
                          text
                          outlined
                          @click="registerDialog = false"
                        >
                          Zamknij
                        </v-btn>
                        <v-spacer></v-spacer>
                        <v-btn
                          color="green darken-1"
                          text
                          @click="createUser()"
                          outlined
                        >
                          Zarejestruj
                        </v-btn>
                      </v-card-actions>
                    </v-form>
                  </v-card>
                </v-dialog>
              </v-row>
            </div>
            <br />
          </div>
        </b-col>
      </b-row>
    </b-container>
    <a href="/register" class="btn-lg">Zarejestruj się</a>
  </div>
</template>

<script>
// @ is an alias to /src
//import Register from "@/views/Register.vue";
import axios from "axios";

export default {
  name: "Home",
  components: {
    //Register,
  },
  data() {
    return {
      data: "",
      username: "",
      email: "",
      location: "",
      birthday: "",
      sex: "",
      password: "",
      password2: "",
      checked: false,
      error_message: "",
      registerDialog: false,
    };
  },
  methods: {
    countDownChanged(dismissCountDown) {
      this.dismissCountDown = dismissCountDown;
    },
    showMsg() {
      this.dismissCountDown = this.dismissSecs;
    },
    countDownChanged2(dismissCountDown) {
      this.dismissCountDown2 = dismissCountDown2;
    },
    showMsg2() {
      this.dismissCountDown2 = this.dismissSecs2;
    },
    createUser() {
      axios
        .post("http://127.0.0.1:8000/api/user/register", {
          username: this.username,
          password: this.password,
          password2: this.password2,
          email: this.email,
          birthday: this.birthday,
          location: this.location,
          sex: this.sex,
        })
        .then((response) => {
          console.log(response);
          if (response.status == 201) {
            this.$router.go();
          }
        })
        .catch((errors) => {
          console.log(errors.response);
        });
    },
    validate(inputID, inputID2) {
      axios
        .post("http://127.0.0.1:8000/api/user/validregister", {
          username: this.username,
          email: this.email,
        })
        .then((response) => {
          console.log(response), (this.data = response.data);
        })
        .catch((errors) => console.log(errors));

      var input = document.getElementById(inputID);
      var input2 = document.getElementById(inputID2);
      if (this.data["username"] != "valid") {
        input.setCustomValidity("Nazwa użytkownika zajęta");
        input.reportValidity();
      } else {
        input.setCustomValidity("");
        input.reportValidity();
      }
      if (this.data["email"] != "valid") {
        input2.setCustomValidity("Email jest już w użyciu");
        input2.reportValidity();
      } else {
        input2.setCustomValidity("");
        input2.reportValidity();
      }
    },
  },
};
</script>

<style scoped>
text {
  text-align: left;
}
.leftside {
  background-color: rgba(252, 198, 225, 0.8);
  padding: 20px;
  color: #812b3b;
  border-color: blueviolet;
  border-radius: 25px;
  border-style: solid;
  border-width: 1px;
  /*
  border-color: #a89172;
  background-color: #fdefddc0;
  box-shadow: 1px 1px #a89172;
  */
}
.rightside {
  background-color: rgba(252, 198, 225, 0.8);
  padding: 20px;
  color: #812b3b;
  border-color: blueviolet;
  border-radius: 25px;
  border-style: solid;
  border-width: 1px;
}
/*
.rightside:hover {
  background-color: rgba(255, 172, 213, 0.795);
  padding: 20px;
  color: #bd1131;
  border-color: rgb(243, 38, 38);
  border-radius: 25px;
  border-style: solid;
  border-width: 1px;
}
*/
.no-background {
  background-color: rgba(0, 0, 0, 0);
  border-style: none;
}
.text {
  text-align: justify;
  font: Arial;
  font-size: 16px;
}
h2 {
  font-size: 20px;
}
h1 {
  color: purple;
  text-shadow: 1px 1px #ac0101;
}
.card text-black bg-secondary mb-3 {
  background-color: rgba(255, 255, 255, 0.3);
  border-radius: 25px;
}
.btn-lg {
  background-color: #cdb7c0;
  color: #501c4c;
  font-weight: 600;
  border: grey 1px solid;
}
.btn-lg:hover {
  background-color: #0275d8;
  color: white;
  font-weight: 600;
}
</style>
