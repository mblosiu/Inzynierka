<template>
  <div class="page">
    <b-container class="bv-example-row" fluid>
      <b-row>
        <b-col cols="1"></b-col>
        <b-col cols="10">
          <b-alert
            :show="dismissCountDown"
            dismissible
            fade
            variant="success"
            @dismissed="dismissCountDown=0"
            @dismiss-count-down="countDownChanged"
          >{{msg}}</b-alert>
          <b-alert
            :show="dismissCountDown2"
            dismissible
            fade
            variant="danger"
            @dismissed="dismissCountDown2=0"
            @dismiss-count-down="countDownChanged2"
          >{{msg2}}</b-alert>
          <div class="card text-black bg-white mb-3">
            <b-tabs pills card horizontal>
              <form class="card" @submit.prevent="editUserData">
                <b-tab title="Podstawowe informacje" active>
                  <ul class="list-group list-group-flush">
                    <li class="list-group-item">
                      <b-row>
                        <b-col cols="6">
                          <label for="name" class="white-text">Imię</label>
                          <input
                            type="text"
                            id="name"
                            v-model="user_data.name"
                            class="form-control"
                          />
                        </b-col>
                        <b-col cols="6">
                          <label for="surname" class="grey-text">Nazwisko</label>
                          <input
                            type="text"
                            id="surname"
                            v-model="user_data.surname"
                            class="form-control"
                          />
                        </b-col>
                      </b-row>
                    </li>
                    <ul class="list-group-item">
                      <b-row>
                        <b-col cols="6">
                          <label for="location" class="grey-text">Miejsce zamieszkania</label>
                          <input
                            type="text"
                            id="location"
                            v-model="user_data.location"
                            class="form-control"
                          />
                        </b-col>
                        <b-col cols="6">
                          <label for="sex" class="grey-text">Płeć</label>
                          <b-form-select
                            class="form-control"
                            id="sex"
                            v-model="user_data.sex"
                            :options="sex_options"
                          ></b-form-select>
                        </b-col>
                      </b-row>
                    </ul>

                    <ul class="list-group-item">
                      <b-row>
                        <b-col cols="6">
                          <label for="is_smoking" class="grey-text">Papierosy</label>
                          <b-form-select
                            class="form-control"
                            id="is_smoking"
                            v-model="user_data.is_smoking"
                            :options="smoking_options"
                          ></b-form-select>
                        </b-col>
                        <b-col cols="6">
                          <label for="is_drinking" class="grey-text">Alkohol</label>
                          <b-form-select
                            class="form-control"
                            id="is_drinking"
                            v-model="user_data.is_drinking_alcohol"
                            :options="alcohol_options"
                          ></b-form-select>
                        </b-col>
                      </b-row>
                    </ul>

                    <ul class="list-group-item">
                      <b-row>
                        <b-col cols="6">
                          <label for="status" class="grey-text">Status</label>
                          <b-form-select
                            class="form-control"
                            id="status"
                            v-model="user_data.status"
                            :options="status_options"
                          ></b-form-select>
                        </b-col>
                        <b-col cols="6">
                          <label for="education" class="grey-text">Edukacja</label>
                          <b-form-select
                            class="form-control"
                            id="education"
                            v-model="user_data.education"
                            :options="education_options"
                          ></b-form-select>
                        </b-col>
                      </b-row>
                    </ul>
                  </ul>

                  <div class="text-center mt-4">
                    <button type="submit" class="btn btn-success">Zapisz</button>
                  </div>
                  <p></p>
                </b-tab>
              </form>
              <form class="card" @submit.prevent="editUserData">
                <b-tab title="Wygląd">
                  <ul class="list-group list-group-flush">
                    <ul class="list-group-item">
                      <b-row>
                        <b-col cols="6">
                          <label for="growth" class="white-text">Wzrost</label>
                          <input
                            type="number"
                            id="growth"
                            v-model="user_data.growth"
                            class="form-control"
                            placeholder="Wzrost w cm"
                          />
                        </b-col>
                        <b-col cols="6">
                          <label for="weight" class="white-text">Waga</label>
                          <input
                            type="text"
                            id="weight"
                            v-model="user_data.weight"
                            class="form-control"
                            placeholder="Waga w kg"
                          />
                        </b-col>
                      </b-row>
                    </ul>
                    <ul class="list-group-item">
                      <b-row>
                        <b-col cols="6">
                          <label for="hair_length" class="grey-text">Długość włosów</label>
                          <b-form-select
                            class="form-control"
                            id="hair_length"
                            v-model="user_data.hair_length"
                            :options="hair_length_options"
                          ></b-form-select>
                        </b-col>
                        <b-col cols="6">
                          <label for="hair_color" class="grey-text">Kolor włosów</label>
                          <b-form-select
                            class="form-control"
                            id="hair_color"
                            v-model="user_data.hair_color"
                            :options="hair_color_options"
                          ></b-form-select>
                        </b-col>
                      </b-row>
                    </ul>
                    <ul class="list-group-item">
                      <b-row>
                        <b-col cols="6">
                          <label for="body_type" class="grey-text">Sylwetka</label>
                          <b-form-select
                            class="form-control"
                            id="body_type"
                            v-model="user_data.body_type"
                            :options="body_type_options"
                          ></b-form-select>
                        </b-col>
                        <b-col cols="6">
                          <label for="eye_color" class="grey-text">Kolor oczu</label>
                          <b-form-select
                            class="form-control"
                            id="eye_color"
                            v-model="user_data.eye_color"
                            :options="eye_color_options"
                          ></b-form-select>
                        </b-col>
                      </b-row>
                      <br />
                      <b-row>
                        <br />
                        <b-col cols="12">
                          <!--<label for="special_options" class="grey-text">Znaki szczególne</label>
                          <br />
                          <input
                            type="checkbox"
                            id="glasses"
                            value="okulary"
                            v-model="special_options"
                          />
                          <label for="glasses">Okulary</label>
                          <input
                            type="checkbox"
                            id="freckles"
                            value="piegi"
                            v-model="special_options"
                          />
                          <label for="freckles">Piegi</label>
                          <input
                            type="checkbox"
                            id="scars"
                            value="blizny"
                            v-model="special_options"
                          />
                          <label for="scars">Blizny</label>
                          <input
                            type="checkbox"
                            id="body_piercing"
                            value="body piercing"
                            v-model="special_options"
                          />
                          <label for="body_piercing">Body piercing</label>
                          <input
                            type="checkbox"
                            id="tattoos"
                            value="tatuaże"
                            v-model="special_options"
                          />
                          <label for="tattoos">Tatuaże</label>
                          <br />
                          <span>Zaznaczono: {{ special_options }}</span>-->
                        </b-col>
                      </b-row>
                    </ul>
                  </ul>

                  <div class="text-center mt-4">
                    <button type="submit" class="btn btn-success">Zapisz</button>
                  </div>
                  <p></p>
                </b-tab>
              </form>
              <form class="card" @submit.prevent="editUserData">
                <b-tab title="Zainteresowania">
                  <ul class="list-group list-group-flush">
                    <ul class="list-group-item">
                      <b-row>
                        <!--<b-col cols="6">
                          <label for="entertainment" class="grey-text">Rozrywka i hobby:</label>
                          <br />
                          <input type="checkbox" id="jack" value="Shopping" v-model="checkedNames" />
                          <label for="jack">Shopping</label>
                          <input type="checkbox" id="john" value="Netflix" v-model="checkedNames" />
                          <label for="john">Netflix</label>
                          <input type="checkbox" id="mike" value="Książki" v-model="checkedNames" />
                          <label for="mike">Książki</label>
                        </b-col>
                        <b-col cols="6">
                          <label for="sport" class="grey-text">Sport:</label>
                          <br />
                          <input
                            type="checkbox"
                            id="jack"
                            value="Piłka nożna"
                            v-model="checkedNames"
                          />
                          <label for="jack">Piłka nożna</label>
                          <input
                            type="checkbox"
                            id="john"
                            value="Koszykówka"
                            v-model="checkedNames"
                          />
                          <label for="john">Koszykówka</label>
                          <input type="checkbox" id="mike" value="Pływactwo" v-model="checkedNames" />
                          <label for="mike">Pływactwo</label>
                        </b-col>-->
                      </b-row>
                    </ul>
                    <ul class="list-group-item">
                      <b-row>
                        <b-col cols="6">
                          <!--<label for="music" class="grey-text">Muzyka:</label>
                          <br />
                          <input type="checkbox" id="jack" value="Rock" v-model="checkedNames" />
                          <label for="jack">Rock</label>
                          <input type="checkbox" id="john" value="Jazz" v-model="checkedNames" />
                          <label for="john">Jazz</label>
                          <input type="checkbox" id="mike" value="Pop" v-model="checkedNames" />
                          <label for="mike">Pop</label>-->
                        </b-col>
                        <b-col cols="6">
                          <!--<label for="cooking" class="grey-text">Kuchnia:</label>
                          <br />
                          <input type="checkbox" id="jack" value="Polska" v-model="checkedNames" />
                          <label for="jack">Polska</label>
                          <input
                            type="checkbox"
                            id="john"
                            value="Orientalna"
                            v-model="checkedNames"
                          />
                          <label for="john">Orientalna</label>
                          <input type="checkbox" id="mike" value="Studencka" v-model="checkedNames" />
                          <label for="mike">Studencka</label>-->
                        </b-col>
                      </b-row>
                    </ul>
                    <ul class="list-group-item">
                      <b-row>
                        <b-col cols="6">
                          <label for="favourite_place" class="white-text">Ulubione miejsce:</label>
                          <input
                            type="text"
                            id="favourite_place"
                            v-model="user_data.favourite_place"
                            class="form-control"
                          />
                        </b-col>
                        <b-col cols="6">
                          <label for="passion" class="white-text">Największa pasja:</label>
                          <input
                            type="text"
                            id="passion"
                            v-model="user_data.passion"
                            class="form-control"
                          />
                        </b-col>
                      </b-row>
                    </ul>
                  </ul>

                  <div class="text-center mt-4">
                    <button type="submit" class="btn btn-success">Zapisz</button>
                  </div>
                  <p></p>
                </b-tab>
              </form>
              <form class="card" @submit.prevent="editUserPreferences">
                <b-tab title="Twoje preferencje">
                  <div class="card text-black bg-dark mb-3">
                    <ul class="list-group list-group-flush">
                      <ul class="list-group-item">
                        <b-row>
                          <b-col cols="6">
                            <label for="orientation" class="grey-text">Orientacja</label>
                            <b-form-select
                              class="form-control"
                              id="orientation"
                              v-model="user_preferences.orientation"
                              :options="orientation_options"
                            ></b-form-select>
                          </b-col>
                          <b-col cols="6">
                            <label for="age_preference_min" class="white-text">Przedział wiekowy</label>
                            <b-row>
                              <b-col cols="6">
                                <input
                                  type="number"
                                  id="age_preference_min"
                                  placeholder="wiek minimalny"
                                  v-model="user_preferences.age_preference_min"
                                  class="form-control"
                                />
                              </b-col>
                              <b-col cols="6">
                                <input
                                  type="number"
                                  id="age_preference_max"
                                  placeholder="wiek maksymalny"
                                  v-model="user_preferences.age_preference_max"
                                  class="form-control"
                                />
                              </b-col>
                            </b-row>
                          </b-col>
                        </b-row>
                      </ul>
                      <ul class="list-group-item">
                        <b-row>
                          <b-col cols="6">
                            <label for="body_type_preference" class="grey-text">Sylwetka</label>
                            <b-form-select
                              class="form-control"
                              id="body_type_preference"
                              v-model="user_preferences.body_type_preference"
                              :options="body_type_options"
                            ></b-form-select>
                          </b-col>
                          <b-col cols="6">
                            <label for="weight_preference" class="white-text">Waga maks</label>
                            <input
                              type="number"
                              id="weight_preference"
                              placeholder="maksymalna waga"
                              v-model="user_preferences.weight_preference"
                              class="form-control"
                            />
                          </b-col>
                        </b-row>
                      </ul>
                      <ul class="list-group-item">
                        <b-row>
                          <b-col cols="6">
                            <label for="education_preference" class="white-text">Edukacja</label>
                            <b-form-select
                              class="form-control"
                              id="education_preference"
                              v-model="user_preferences.education_preference"
                              :options="education_options"
                            ></b-form-select>
                          </b-col>
                          <b-col cols="6">
                            <label for="eye_color_preference" class="grey-text">Kolor oczu</label>
                            <b-form-select
                              class="form-control"
                              id="eye_color_preference"
                              v-model="user_preferences.eye_color_preference"
                              :options="eye_color_options"
                            ></b-form-select>
                          </b-col>
                        </b-row>
                      </ul>
                      <ul class="list-group-item">
                        <b-row>
                          <b-col cols="6">
                            <label for="hair_length_preference" class="grey-text">Długość włosów</label>
                            <b-form-select
                              class="form-control"
                              id="hair_length_preference"
                              v-model="user_preferences.hair_length_preference"
                              :options="hair_length_options"
                            ></b-form-select>
                          </b-col>
                          <b-col cols="6">
                            <label for="hair_color_preference" class="grey-text">Kolor włosów</label>
                            <b-form-select
                              class="form-control"
                              id="hair_color_preference"
                              v-model="user_preferences.hair_color_preference"
                              :options="hair_color_options"
                            ></b-form-select>
                          </b-col>
                        </b-row>
                      </ul>
                      <ul class="list-group-item">
                        <b-row>
                          <b-col cols="6">
                            <label for="is_smoking_preference" class="grey-text">Papierosy</label>
                            <b-form-select
                              class="form-control"
                              id="is_smoking_preference"
                              v-model="user_preferences.is_smoking_preference"
                              :options="smoking_options"
                            ></b-form-select>
                          </b-col>
                          <b-col cols="6">
                            <label for="is_drinking_preference" class="grey-text">Alkohol</label>
                            <b-form-select
                              class="form-control"
                              id="is_drinking_preference"
                              v-model="user_preferences.is_drinking_alcohol_preference"
                              :options="alcohol_options"
                            ></b-form-select>
                          </b-col>
                        </b-row>
                      </ul>
                      <ul class="list-group-item">
                        <b-row>
                          <b-col cols="6"></b-col>
                          <b-col cols="6"></b-col>
                        </b-row>
                      </ul>
                    </ul>

                    <div class="text-center mt-4">
                      <button type="submit" class="btn btn-success">Zapisz</button>
                    </div>
                    <p></p>
                  </div>
                </b-tab>
              </form>
              <b-tab title="Opis profilu">
                <div class="card text-black bg-dark mb-3">
                  <br/>
                  <p>
                    <br/>
                    {{user_data.description}}
                  </p>
                </div>
              </b-tab>
              <b-tab title="Ustawienia prywatności">
                <div
                  class="card text-black bg-dark mb-3"
                >funkcjonalności dot. funkcjonowania konta aż po jego usuwanie</div>
              </b-tab>
            </b-tabs>
            <p></p>
          </div>
        </b-col>
        <b-col cols="1"></b-col>
      </b-row>
    </b-container>
  </div>
</template>


<script>
import axios from "axios";
//import Alert from "@/components/Alert.vue";
export default {
  name: "UsersProfile",
  components: {},
  data() {
    return {
      placeholder: null,
      active: "",
      checkedNames: [],
      special_options: [],
      user_data: {},
      user_preferences: {},
      msg: "",
      dismissSecs: 5,
      dismissCountDown: 0,
      dismissSecs2: 5,
      dismissCountDown2: 0,
      msg2: "",
      sex_options: [
        { value: null, text: "" },
        { value: "Mężczyzna", text: "mężczyzna" },
        { value: "Kobieta", text: "kobieta" },
        { value: "Inna", text: "inna" },
      ],
      orientation_options: [
        { value: null, text: "" },
        { value: "Hetero", text: "heteroseksualna" },
        { value: "Homo", text: "homoseksualna" },
        { value: "Bi", text: "biseksualna" },
      ],
      body_type_options: [
        { value: null, text: "" },
        { value: "Normalna", text: "normalna" },
        { value: "Szczupła", text: "szczupła" },
        { value: "Wysportowana", text: "wysportowana" },
        { value: "Puszysta", text: "puszysta" },
      ],
      eye_color_options: [
        { value: null, text: "" },
        { value: "Szare", text: "szare" },
        { value: "Niebieskie", text: "niebieskie" },
        { value: "Brązowe", text: "brązowe" },
        { value: "Piwne", text: "piwne" },
        { value: "Szare", text: "zieone" },
      ],
      hair_color_options: [
        { value: null, text: "" },
        { value: "Blond", text: "blond" },
        { value: "Ciemny blond", text: "ciemny blond" },
        { value: "Jasny blond", text: "jasny blond" },
        { value: "Brązowe", text: "brązowe" },
        { value: "Ciemny brąz", text: "ciemny brąz" },
        { value: "Jasny brąz", text: "jasny brąz" },
        { value: "Czarne", text: "czarne" },
        { value: "Siwe", text: "siwe" },
        { value: "Inny", text: "inny" },
      ],
      hair_length_options: [
        { value: null, text: "" },
        { value: "Bardzo krótkie", text: "bardzo krótkie" },
        { value: "Krótkie", text: "krótkie" },
        { value: "Średnie", text: "średnie (do barków)" },
        { value: "Dłuższe", text: "dłuższe (do łopatek)" },
        { value: "Długie", text: "długie" },
        { value: "Bardzo długie", text: "bardzo długie (do pasa+)" },
        { value: "Łysy", text: "brak (łysy)" },
      ],
      status_options: [
        { value: null, text: "" },
        { value: "Uczeń", text: "uczeń" },
        { value: "Student", text: "student" },
        { value: "Pracuję", text: "pracuję" },
        { value: "Nie pracuję", text: "nie pracuję" },
        { value: "Emeryt", text: "emeryt" },
      ],
      education_options: [
        { value: null, text: "brak" },
        { value: "Podstawowe", text: "podstawowe" },
        { value: "Gimnazjalne", text: "gimnazjalne" },
        { value: "Zawodowe", text: "zawodowe" },
        { value: "Średnie", text: "średnie" },
        { value: "Wyższe", text: "wyższe" },
      ],
      smoking_options: [
        { value: null, text: "" },
        { value: "0", text: "nie palę" },
        { value: "1", text: "okazjonalnie" },
        { value: "2", text: "często" },
        { value: "3", text: "codziennie" },
        { value: "4", text: "nałogowo" },
      ],
      alcohol_options: [
        { value: null, text: "" },
        { value: "0", text: "nie piję" },
        { value: "1", text: "okazjonalnie" },
        { value: "2", text: "często" },
        { value: "3", text: "codziennie" },
        { value: "4", text: "nałogowo" },
      ],
    };
  },
  methods: {
    countDownChanged(dismissCountDown) {
      this.dismissCountDown = dismissCountDown;
    },
    showMsg() {
      this.dismissCountDown = this.dismissSecs;
    },
    countDownChanged2(dismissCountDown2) {
      this.dismissCountDown2 = dismissCountDown2;
    },
    showMsg2() {
      this.dismissCountDown2 = this.dismissSecs2;
    },
    getUserData() {
      axios
        .get("http://127.0.0.1:8000/api/user/properties", {
          params: {},
          headers: {
            Authorization: "Token " + localStorage.getItem("user-token"),
          },
        })
        .then((response) => {
          console.log(response), (this.user_data = response.data);
        })
        .catch((errors) => console.log(errors));
    },
    editUserData() {
      let config = {
        headers: {
          Authorization: "Token " + localStorage.getItem("user-token"),
        },
      };
      axios
        .patch(
          "http://127.0.0.1:8000/api/user/properties",
          {
            surname: this.user_data.surname,
            name: this.user_data.name,
            location: this.user_data.location,
            sex: this.user_data.sex,
            is_smoking: this.user_data.is_smoking,
            is_drinking_alcohol: this.user_data.is_drinking_alcohol,
            status: this.user_data.status,
            education: this.user_data.education,
            growth: this.user_data.growth,
            weight: this.user_data.weight,
            hair_length: this.user_data.hair_length,
            hair_color: this.user_data.hair_color,
            eye_color: this.user_data.eye_color,
            body_type: this.user_data.body_type,
            favourite_place: this.user_data.favourite_place,
            passion: this.user_data.passion,
          },
          config
        )
        .then((response) => {
          if (response.status == 200) {
            this.showMsg(), (this.msg = "Zapisano zmiany");
          }
          console.log(response);
        })
        .catch((errors) => {
          if (errors.response.status != 200) {
            this.showMsg2(), (this.msg2 = "Formularz zawiera błędy");
          }
          console.log(errors);
        });
    },
    getUserPreferences() {
      axios
        .get("http://127.0.0.1:8000/api/user/preferences", {
          params: {},
          headers: {
            Authorization: "Token " + localStorage.getItem("user-token"),
          },
        })
        .then((response) => {
          console.log(response), (this.user_preferences = response.data);
        })
        .catch((errors) => console.log(errors));
    },
    editUserPreferences() {
      let config = {
        headers: {
          Authorization: "Token " + localStorage.getItem("user-token"),
        },
      };
      axios
        .patch(
          "http://127.0.0.1:8000/api/user/preferences",
          {
            orientation: this.user_preferences.orientation,
            is_drinking_alcohol_preference: this.user_preferences
              .is_drinking_alcohol_preference,
            is_smoking_preference: this.user_preferences.is_smoking_preference,
            age_preference_min: this.user_preferences.age_preference_min,
            age_preference_max: this.user_preferences.age_preference_max,
            body_type_preference: this.user_preferences.body_type_preference,
            weight_preference: this.user_preferences.weight_preference,
            education_preference: this.user_preferences.education_preference,
            eye_color_preference: this.user_preferences.eye_color_preference,
            hair_length_preference: this.user_preferences
              .hair_length_preference,
            hair_color_preference: this.user_preferences.hair_color_preference,
          },
          config
        )
        .then((response) => {
          if (response.status == 200) {
            this.showMsg(), (this.msg = "Zapisano zmiany");
          }
          console.log(response);
        })
        .catch((errors) => {
        
          if (errors.response.status != 200) {
            this.showMsg2(), (this.msg2 = "Formularz zawiera błędy");
          }
          console.log(errors);
        })
    },
    getUserSettings() {},
    editUserSetting() {},
  },
  created() {
    this.getUserData();
    this.getUserPreferences();
    this.getUserSettings();
  },
};
</script>

<style scoped>
.profile {
  width: 300px;
  min-height: 500px;
  margin-left: auto;
  margin-right: auto;
  border-radius: 25px;
  padding: 0.5cm;
  background: #343a40;
  color: white;
}
.preferences {
  width: 300px;
  min-height: 500px;
  margin-left: auto;
  margin-right: auto;

  border-radius: 25px;
  padding: 0.5cm;
  background: #343a40;
  color: white;
}
.settings {
  width: 300px;
  min-height: 500px;
  margin-left: auto;
  margin-right: auto;
  border-radius: 25px;
  padding: 0.5cm;
  background: #343a40;
  color: white;
}
table {
  margin-left: auto;
  margin-right: auto;
  width: 80%;
  position: relative;
}
</style>

