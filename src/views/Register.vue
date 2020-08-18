<template>
  <div>
    <b-row>
      <b-col cols="1"></b-col>
      <b-col cols="10">
        <b-alert
          :show="dismissCountDown"
          dismissible
          fade
          variant="danger"
          @dismissed="dismissCountDown=0"
          @dismiss-count-down="countDownChanged"
        >{{msg}}</b-alert>
      </b-col>
      <b-col cols="1"></b-col>
    </b-row>
    <div class="register-form d-flex justify-content-center">
      <b-row class="row justify-content-md-center">
        <b-alert v-model="showDismissibleAlert" variant="success" dismissible>{{ error_message }}</b-alert>
        <b-col cols="12" class="col align-self-center">
          <div class="card text-black bg-secondary mb-3" style="width: 30rem;" fluid>
            <form class="card" @submit.prevent="CreateUser">
              <div class="card-header">
                <h5>Rejestracja</h5>
              </div>
              <ul class="list-group list-group-flush">
                <li class="list-group-item">
                  <b-row>
                    <b-col cols="6">
                      <label for="username">Nazwa konta</label>
                      <input type="text" name="username" id="username" v-model="username" />
                    </b-col>
                    <b-col cols="6">
                      <label for="email">Email</label>
                      <input type="email" name="email" id="email" v-model="email" />
                    </b-col>
                  </b-row>
                </li>

                <li class="list-group-item">
                  <b-row>
                    <b-col cols="6">
                      <label for="Location">Lokacja</label>
                      <input type="text" name="Location" id="Locatiom" v-model="location" />
                    </b-col>
                    <b-col cols="6">
                      <label for="birthday">Data urodzenia</label>
                      <input type="date" name="birthday" id="birthday" v-model="birthday" />
                    </b-col>
                  </b-row>
                </li>

                <li class="list-group-item">
                  <b-row>
                    <b-col cols="6">
                      <label for="password">Hasło</label>
                      <input type="password" name="password" id="password" v-model="password" />
                    </b-col>
                    <b-col cols="6">
                      <label for="password2">Powtórz hasło</label>
                      <input type="password" name="password2" id="password2" v-model="password2" />
                    </b-col>
                  </b-row>
                </li>

                <li class="list-group-item">
                  <b-row>
                    <b-col cols="12">
                      <label for="sex">Płeć</label>
                      <br />
                      <select class="ml-2" name="Sex" id="Sex" v-model="sex">
                        <br />
                        <option>mężczyzna</option>
                        <option>kobieta</option>
                        <option>inna</option>
                      </select>
                    </b-col>
                  </b-row>
                </li>
                <li class="list-group-item">
                  <b-row>
                    <b-col cols="12">
                      <br />
                      <label for="checkbox">
                        Akceptuję
                        <router-link to="/regulations">regulamin</router-link>
                      </label>
                      <input type="checkbox" id="checkbox" v-model="checked" />
                    </b-col>
                  </b-row>
                </li>
                <li class="list-group-item">
                  <b-row>
                    <b-col cols="12">
                      <input
                        v-on:click="CreateUser"
                        class="btn btn-outline-success"
                        type="submit"
                        value="Zarejestruj"
                      />
                    </b-col>
                  </b-row>
                </li>
              </ul>
            </form>
          </div>
        </b-col>
        <!--<b-col cols="1"></b-col>-->
      </b-row>
    </div>
    <b-row>
      <b-col cols="1"></b-col>
      <b-col cols="10">
        <b-alert
          :show="dismissCountDown2"
          dismissible
          fade
          variant="danger"
          @dismissed="dismissCountDown2=0"
          @dismiss-count-down="countDownChanged2"
        >{{msg2}}</b-alert>
      </b-col>
      <b-col cols="1"></b-col>
    </b-row>
  </div>
</template>

<script>
import axios from "axios";
//import Api from "../service/api";

export default {
  name: "Register",
  components: {},
  data() {
    return {
      username: "",
      email: "",
      location: "",
      birthday: "",
      sex: "",
      password: "",
      password2: "",
      msg: "",
      msg2: "",
      dismissSecs: 5,
      dismissCountDown: 0,
      dismissSecs2: 5,
      dismissCountDown2: 0,
      checked: false,
      showDismissibleAlert: false,
      error_message: "",
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
    CreateUser() {
      //console.log(this.username);
      if (this.checked == false) {
        this.showMsg2(), (this.msg2 = "Musisz zaakceptować regulamin");
      } else {
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
              this.error_message = "Udało się!";
              this.showDismissibleAlert = true;
            }
          })
          .catch(
            (errors) => {
              if (errors.response.status != 200) {
                this.showMsg(), (this.msg = "Formularz zawiera błędy");
              }
              console.log(errors);
              //if (errors.response.status != 201) {
              //this.error_message = 'Formularz zawiera błędy!';
              //this.showDismissibleAlert = true;
            }
            /*}*/
          );
        //this.$router.push('/');
      }
    },
  },
};
</script>

<style scoped>
h5 {
  color: whitesmoke;
}
.card-header {
  background-color: #343a40;
}
</style>
