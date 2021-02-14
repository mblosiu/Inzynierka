<template>
  <v-container background-image>
    <v-row no-gutters align="start">
      <v-col cols="4">
        <h1>Witamy w e-love</h1>
      </v-col>
      <v-col cols="7"></v-col>
    </v-row>
    <br />
    <v-row>
      <v-col class="leftside" lg="4" sm="7">
        <h4>Tu znajdziesz swoją drugą połówkę!</h4>
        <br />
        
        <div class="text">
          Jeśli szukasz miłości, życiowego partnera, lub po prostu osoby, z
          którą można porozmawiać na wspólne tematy to dobrze trafiłeś. Serwis
          e-Love skierowany jest do każdego użytkownika bez względu na wiek, czy
          rodzaj zawieranych relacji.
          <br />W dzisiejszych czasach samotność jest bardzo częstym problemem i
          dotyka ludzi z każdego przedziału wiekowego. Poza faktem iż samotność
          sama w sobie jest przykrym uczuciem, należy dodać, że jak donoszą
          najnowsze badania, długotrwałe jej doświadczanie bardzo niekorzystnie
          wpływa na nasze zdrowie. <br />
          Nasz portal jest stale rozwijany i powiększa się nie tylko o nowe
          funkcjonalności ale i nowych użytkowników. Zapraszamy do darmowej
          rejestracji!
          <br />
        </div>
        <br />

        <p></p>
        <blockquote class="blockquote text-right">
          <h6>
            "Każdy powinien mieć kogoś, z kim mógłby szczerze pomówić, bo choćby
            człowiek był nie wiadomo jak dzielny, czasami czuje się bardzo
            samotny."
          </h6>
          <footer class="blockquote-footer">
            Ernest Hemingway
            <cite title="Source Title">"Komu bije dzwon"</cite>
          </footer>
        </blockquote>
      </v-col>
      <br />
      <v-col lg="5" sm="1"></v-col>
      <v-col cols="3">
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

                  <v-form
                    @submit.prevent="createUser"
                    v-model="valid"
                    ref="form"
                  >
                    <!--<v-card-text>
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
                              :items="['Mężczyzna', 'Kobieta']"
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
                          </v-col>
                        </v-row>
                      </v-container>
                      <br />
                      <small>*Pola wymagane</small>
                    </v-card-text>-->
                    <v-card-text>
                      <v-container>
                        <v-row>
                          <v-col cols="12" sm="6">
                            <v-text-field
                              label="Nazwa użytkownika"
                              type="text"
                              name="username"
                              id="username"
                              v-model="username"
                              :rules="usernameRules"
                              :counter="20"
                              required
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" sm="6">
                            <v-text-field
                              label="Miejsce zamieszkania"
                              type="text"
                              name="Location"
                              id="Location"
                              v-model="location"
                              :rules="locationRules"
                              required
                            ></v-text-field>
                          </v-col>

                          <v-col cols="12" sm="6">
                            <v-text-field
                              label="Email"
                              type="email"
                              name="email"
                              id="email"
                              v-model="email"
                              :rules="emailRules"
                              required
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" sm="6">
                            <br />

                            Data urodzenia:
                            <input
                              type="date"
                              name="birthday"
                              id="birthday"
                              v-model="birthday"
                              :rules="ageRules"
                              required
                            />
                          </v-col>

                          <v-col cols="12">
                            <v-text-field
                              label="Hasło"
                              type="password"
                              name="password"
                              id="password"
                              v-model="password"
                              :rules="passwordRules"
                              required
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12">
                            <v-text-field
                              label="Powtórz hasło"
                              type="password"
                              name="password2"
                              id="password2"
                              v-model="password2"
                              :rules="
                                password2Rules.concat(passwordConfirmationRule)
                              "
                              required
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" sm="6">
                            <v-select
                              :items="['Mężczyzna', 'Kobieta']"
                              label="Płeć"
                              required
                              name="Sex"
                              id="Sex"
                              v-model="sex"
                              :rules="sexRules"
                            ></v-select>
                          </v-col>
                          <v-col cols="12" sm="6">
                            <!-- v-model="checked" -->
                            <v-checkbox
                              label="Akceptuję regulamin serwisu"
                              required
                              type="checkbox"
                              id="checkbox"
                              :rules="checkedRules"
                            ></v-checkbox>
                          </v-col>
                        </v-row>
                      </v-container>
                      <br />
                    </v-card-text>

                    <v-card-actions>
                      <v-btn
                        color="red darken-1"
                        text
                        outlined
                        @click="registerDialog = false"
                      >
                        Zamknij
                      </v-btn>
                      <!--<v-spacer></v-spacer>
                      <v-btn
                        color="green darken-1"
                        text
                        @click="validateUser()"
                        outlined
                      >
                        sprawdz
                      </v-btn>-->

                      <v-spacer></v-spacer>
                      <div v-if="valid == true">
                        <v-btn
                          color="green darken-1"
                          text
                          @click="createUser()"
                          outlined
                        >
                          Zarejestruj
                        </v-btn>
                      </div>
                      <div v-else>
                        <v-btn
                          color="grey darken-1"
                          text
                          @click="validate()"
                          outlined
                        >
                          Zarejestruj
                        </v-btn>
                      </div>
                    </v-card-actions>
                  </v-form>
                </v-card>
              </v-dialog>
            </v-row>
          </div>
          <br />
        </div>
      </v-col>
    </v-row>
    <v-row justify="center">
      <!--<v-btn color="primary" dark @click.stop="successDialog = true">
        Open Dialog
      </v-btn>-->

      <v-dialog v-model="ageDialog" max-width="300">
        <v-card>
          <v-card-title flex class="purple">
            <v-spacer></v-spacer>
            <span class="headline white--text">Ups</span>
            <v-spacer></v-spacer>
          </v-card-title>
          <br />
          <v-card-text>
            Aby założyć konto wymagane jest ukończenie 18 roku życia.
          </v-card-text>

          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn color="green lighten-1" text @click="ageDialog = false">
              <button>Zamknij</button>
            </v-btn>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <v-dialog v-model="successDialog" max-width="300">
        <v-card>
          <v-card-title flex class="purple">
            <v-spacer></v-spacer>
            <span class="headline white--text">Rejestracja udana!</span>
            <v-spacer></v-spacer>
          </v-card-title>
          <br />
          <v-card-text>
            Twoje konto zostało pomyślnie założone. Przejdź do strony głównej,
            aby się zalogować.
          </v-card-text>

          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn color="green lighten-1" text @click="successDialog = false">
              <button>Zamknij</button>
            </v-btn>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <v-dialog v-model="errorDialog" max-width="300">
        <v-card>
          <v-card-title flex class="purple">
            <v-spacer></v-spacer>
            <span class="headline white--text">Coś poszło nie tak.</span>
            <v-spacer></v-spacer>
          </v-card-title>
          <br />
          <v-card-text>
            <br />
            <div v-if="error != null">
              Użytkownik o podanej nazwie już istnieje!
            </div>
            <div v-if="error3 != null">Nie możesz zrobić więcej kont!</div>
            <br />
            <div v-if="error2 != null">Podany email jest już w użyciu!</div>
          </v-card-text>

          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn color="green lighten-1" text @click="errorDialog = false">
              <button>Zamknij</button>
            </v-btn>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
  </v-container>
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
      validationData: "",
      username: "",
      email: "",
      location: "",
      birthday: "",
      sex: "",
      password: "",
      password2: "",
      //checked: false,
      menu2: false,
      error_message: "",
      registerDialog: false,
      valid: false,
      successDialog: false,
      ageDialog: false,
      errorDialog: false,
      error: "",
      error2: "",
      error3: "",

      usernameRules: [
        (v) => !!v || "Nazwa użytkownika jest wymagana!",
        (v) => v.length <= 20 || "Maksymalna długość to 20 znaków!",
      ],

      emailRules: [
        (v) => !!v || "E-mail jest wymagany!",
        (v) => /.+@.+/.test(v) || "E-mail jest niepoprawny!",
      ],
      locationRules: [(v) => !!v || "Lokacja jest wymagana!"],
      ageRules: [
        (v) =>
          this.getAge(v) < 18 || "Aby założyć konto trzeba ukończyć 18 lat!",
      ],
      passwordRules: [
        (v) => !!v || "Hasło jest wymagane!",
        (v) => (v && v.length >= 8) || "Hasło musi zawierać minimum 8 znaków!",
      ],
      password2Rules: [(v) => !!v || "Hasło jest wymagane!"],
      sexRules: [(v) => !!v || "Wybierz swoją płeć!"],
      checkedRules: [(v) => !!v || "Akceptacja regulaminu jest wymagana!"],
    };
  },
  methods: {
    //http://46.101.213.106:8000/api/user/register
    getAge(dateString) {
      var today = new Date();
      var birthDate = new Date(dateString);
      var age = today.getFullYear() - birthDate.getFullYear();
      var m = today.getMonth() - birthDate.getMonth();
      if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
        age--;
      }
      return age;
    },
    validate() {
      this.$refs.form.validate();
    },
    validateUser() {
      axios
        .get("https://elove.ml:8000/api/user/registration-validation", {
          username: this.username,
          email: this.email,
        })
        .then((response) => {
          console.log(response), (this.validationData = response.data);
        })
        .catch((errors) => console.log(errors));
    },
    /*recaptcha() {
      this.$recaptcha('login').then((token) => {
        console.log(token) // Will print the token
      })
    },*/
    createUser() {
      if (this.birthday == "" || this.getAge(this.birthday) < 18) {
        this.registerDialog = false;
        this.ageDialog = true;
      } else {
        axios
          .post("https://elove.ml:8000/api/user/register", {
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
              //this.$router.go();
              this.registerDialog = false;
              this.successDialog = true;
            }
          })
          .catch((errors) => {
            console.log(errors.response);
            this.error = errors.response.data.username;
            this.error2 = errors.response.data.email;
            this.error3 = errors.response.data.detail;
            this.errorDialog = true;
          });
      }
    },

    toast(toaster, variant = null, msg) {
      this.$bvToast.toast(msg, {
        title: `Info`,
        toaster: toaster,
        solid: true,
        variant: variant,
      });
    },
  },
  computed: {
    passwordConfirmationRule() {
      return () =>
        this.password === this.password2 || "Hasła muszą być identyczne!";
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
  /*padding: 20px;*/
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
  /*padding: 20px;*/
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
.v-card__text,
.v-card__title {
  word-break: normal; /* maybe !important  */
}
</style>
