<template>
  <div class="page">
    <b-container class="bv-example-row" fluid>
      <b-row>
        <b-col cols="1"></b-col>
        <b-col cols="3">
          <form class="profile" @submit.prevent="editUserData">
            <p class="h4 text-center mb-4">Informacje o tobie</p>

            <label for="user_name" class="white-text">Imię</label>
            <input type="text" id="user_name" v-model="user_data.name" class="form-control" />

            <label for="user_surname" class="grey-text">Nazwisko</label>
            <input type="text" id="user_surname" v-model="user_data.surname" class="form-control" />

            <label for="user_location" class="grey-text">Adres</label>
            <input type="text" id="user_location" v-model="user_data.location" class="form-control" />

            <label for="user_sex" class="grey-text">Płeć</label>
            <b-form-select
              class="form-control"
              id="user_sex"
              v-model="user_data.sex"
              :options="sex_options"
            ></b-form-select>
            <br />

            <label for="is_smoking" class="grey-text">Papierosy</label>
            <b-form-select
              class="form-control"
              id="is_smoking"
              v-model="user_data.is_smoking"
              :options="smoking_options"
            ></b-form-select>

            <label for="is_drinking" class="grey-text">Alkohol</label>
            <b-form-select
              class="form-control"
              id="is_drinking_alcohol"
              v-model="user_data.is_drinking_alcohol"
              :options="alcohol_options"
            ></b-form-select>

            <div class="text-center mt-4">
              <button type="submit" class="btn btn-secondary">Zapisz</button>
            </div>
          </form>
        </b-col>
        <b-col cols="4">
          <form class="settings" @submit.prevent="editUserData">
            <p class="h4 text-center mb-4">Twój wygląd</p>

            <label for="user_name" class="white-text">Wzrost</label>
            <input type="text" id="user_name" v-model="user_data.growth" class="form-control" />

            <label for="user_weight" class="white-text">Waga</label>
            <input type="text" id="user_growth" v-model="user_data.weight" class="form-control" />

            <label for="hair_length" class="grey-text">Długość włosów</label>
            <b-form-select
              class="form-control"
              id="hair_length"
              v-model="user_data.hair_length"
              :options="hair_length_options"
            ></b-form-select>

            <label for="hair_color" class="grey-text">Kolor włosów</label>
            <b-form-select
              class="form-control"
              id="hair_color"
              v-model="user_data.hair_color"
              :options="hair_color_options"
            ></b-form-select>

            <label for="body_type" class="grey-text">Sylwetka</label>
            <b-form-select
              class="form-control"
              id="body_type"
              v-model="user_data.body_type"
              :options="body_type_options"
            ></b-form-select>

            <label for="eye_color" class="grey-text">Kolor oczu</label>
            <b-form-select
              class="form-control"
              id="eye_colour"
              v-model="user_data.eye_color"
              :options="eye_color_options"
            ></b-form-select>

            <div class="text-center mt-4">
              <button type="submit" class="btn btn-secondary">Zapisz</button>
            </div>
          </form>
        </b-col>
        <b-col cols="3">
          <form class="preferences" @submit.prevent="editUserPreferences">
            <p class="h4 text-center mb-4">Twoje preferencje</p>

            <label for="user_sex_preference" class="grey-text">Płeć</label>
            <b-form-select
              class="form-control"
              id="user_sex_preference"
              v-model="user_preferences.sex_preference"
              :options="sex_options"
            ></b-form-select>
            <br />
            <label for="user_name" class="white-text">Wzrost</label>
            <input
              type="text"
              id="user_name"
              v-model="user_preferences.growth_preference"
              class="form-control"
            />

            <label for="user_weight" class="white-text">Waga</label>
            <input
              type="text"
              id="user_growth"
              v-model="user_preferences.weight_preference"
              class="form-control"
            />

            <label for="body_type" class="grey-text">Sylwetka</label>
            <b-form-select
              class="form-control"
              id="body_type"
              v-model="user_preferences.body_type_preference"
              :options="body_type_options"
            ></b-form-select>

            <label for="eye_color" class="grey-text">Kolor oczu</label>
            <b-form-select
              class="form-control"
              id="eye_colour"
              v-model="user_data.eye_color"
              :options="eye_color_options"
            ></b-form-select>

            <label for="hair_length" class="grey-text">Długość włosów</label>
            <b-form-select
              class="form-control"
              id="hair_length"
              v-model="user_data.hair_length"
              :options="hair_length_options"
            ></b-form-select>

            <label for="hair_color" class="grey-text">Kolor włosów</label>
            <b-form-select
              class="form-control"
              id="hair_color"
              v-model="user_data.hair_color"
              :options="hair_color_options"
            ></b-form-select>

            <label for="is_smoking" class="grey-text">Papierosy</label>
            <b-form-select
              class="form-control"
              id="is_smoking"
              v-model="user_data.is_smoking_preference"
              :options="smoking_options"
            ></b-form-select>

            <label for="is_drinking" class="grey-text">Alkohol</label>
            <b-form-select
              class="form-control"
              id="is_drinking_alcohol"
              v-model="user_data.is_drinking_alcohol_preference"
              :options="alcohol_options"
            ></b-form-select>

            <div class="text-center mt-4">
              <button type="submit" class="btn btn-secondary">Zapisz</button>
            </div>
          </form>
        </b-col>
        <b-col cols="1"></b-col>
      </b-row>
    </b-container>
  </div>
</template>


<script>
import axios from "axios";
export default {
  name: "UsersProfile",
  components: {},
  data() {
    return {
      placeholder: null,
      active: "",
      user_data: {},
      user_preferences: {},
      sex_options: [
        { value: null, text: "" },
        { value: "mężczyzna", text: "mężczyzna" },
        { value: "kobieta", text: "kobieta" },
        { value: "inna", text: "inna" },
      ],
      body_type_options: [
        { value: null, text: "" },
        { value: "normalna", text: "normalna" },
        { value: "szczupła", text: "szczupła" },
        { value: "wysportowana", text: "wysportowana" },
        { value: "puszysta", text: "puszysta" },
      ],
      eye_color_options: [
        { value: null, text: "" },
        { value: "szare", text: "szare" },
        { value: "niebieskie", text: "niebieskie" },
        { value: "brązowe", text: "brązowe" },
        { value: "piwne", text: "piwne" },
        { value: "szare", text: "zieone" },
      ],
      hair_color_options: [
        { value: null, text: "" },
        { value: "blond", text: "blond" },
        { value: "ciemny blond", text: "ciemny blond" },
        { value: "jasny blond", text: "jasny blond" },
        { value: "brązowe", text: "brązowe" },
        { value: "ciemny brąz", text: "ciemny brąz" },
        { value: "jasny brąz", text: "jasny brąz" },
        { value: "czarne", text: "czarne" },
        { value: "siwe", text: "siwe" },
        { value: "inny", text: "inny" },
      ],
      hair_length_options: [
        { value: null, text: "" },
        { value: "bardzo krótkie", text: "bardzo krótkie" },
        { value: "krótkie", text: "krótkie" },
        { value: "średnie", text: "średnie (do barków)" },
        { value: "dłuższe", text: "dłuższe (do łopatek)" },
        { value: "długie", text: "długie" },
        { value: "bardzo długie", text: "bardzo długie (do pasa+)" },
        { value: "łysy", text: "brak (łysy)" },
      ],
      special_options: [
        { value: null, text: "" },
        { value: "piegi", text: "piegi" },
        { value: "okulary", text: "okulary" },
        { value: "blizny", text: "blizny" },
        { value: "tatuaże", text: "tatuaże" },
        { value: "body piercing", text: "body piercing" },
      ],
      status_options: [
        { value: null, text: "" },
        { value: "uczeń", text: "uczeń" },
        { value: "student", text: "student" },
        { value: "pracuję", text: "pracuję" },
        { value: "nie pracuję", text: "nie pracuję" },
        { value: "emeryt", text: "emeryt" },
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
          },
          config
        )
        .then((response) => {
          console.log(response);
        })
        .catch((errors) => console.log(errors));
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
            sex_preference: this.user_preferences.sex_preference,
            is_drinking_alcohol_preference: this.user_preferences
              .is_drinking_alcohol_preference,
            is_smoking_preference: this.user_preferences.is_smoking_preference,
          },
          config
        )
        .then((response) => {
          console.log(response);
        })
        .catch((errors) => console.log(errors));
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

