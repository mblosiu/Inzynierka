<template>
  <div class="page">
    <b-container class="bv-example-row" fluid>
      <b-row>
        <b-col cols="1"></b-col>
        <b-col cols="10">
          <nav class="navbar navbar-expand-lg">
            <div
              data-toggle="tooltip"
              data-placement="right"
              title="Wyszukaj użytkowników za pomocą nałożonych filtrów, bądź konkretnego z nich po nazwie"
            >
              <svg
                width="2em"
                height="2em"
                viewBox="0 0 16 16"
                class="bi bi-question-circle"
                fill="blue"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z" />
                <path
                  d="M5.255 5.786a.237.237 0 0 0 .241.247h.825c.138 0 .248-.113.266-.25.09-.656.54-1.134 1.342-1.134.686 0 1.314.343 1.314 1.168 0 .635-.374.927-.965 1.371-.673.489-1.206 1.06-1.168 1.987l.003.217a.25.25 0 0 0 .25.246h.811a.25.25 0 0 0 .25-.25v-.105c0-.718.273-.927 1.01-1.486.609-.463 1.244-.977 1.244-2.056 0-1.511-1.276-2.241-2.673-2.241-1.267 0-2.655.59-2.75 2.286zm1.557 5.763c0 .533.425.927 1.01.927.609 0 1.028-.394 1.028-.927 0-.552-.42-.94-1.029-.94-.584 0-1.009.388-1.009.94z"
                />
              </svg>
            </div>
            <form id="filters" @submit.prevent="getUsers">
              <table>
                <tr>
                  <th>
                    <div id="filter">
                      <b-form-select
                        :options="sex_options"
                        class="ml-2"
                        id="sex"
                        v-model="sex"
                        size="md"
                        value="sex"
                        placeholder="Płeć"
                      ></b-form-select>
                    </div>
                  </th>
                  <!--<th>
                    <div id="filter">
                      <b-form-select
                        :options="orientation_options"
                        class="ml-2"
                        id="orientation"
                        v-model="orientation"
                        size="md"
                        value="orientation"
                        placeholder="Orientacja"
                      ></b-form-select>
                    </div>
                  </th>
                  <th>
                    <div id="filter">
                      <b-form-select
                        :options="hair_color_options"
                        class="ml-2"
                        id="hair_color"
                        v-model="hair_color"
                        size="md"
                        value="hair_color"
                        placeholder="Kolor włosów"
                      ></b-form-select>
                    </div>
                  </th>
                  <th>
                    <div id="filter">
                      <b-form-select
                        :options="hair_length_options"
                        class="ml-2"
                        id="hair_length"
                        v-model="hair_length"
                        size="md"
                        value="hair_length"
                        placeholder="Długość włosów"
                      ></b-form-select>
                    </div>
                  </th>
                  <th>
                    <div id="filter">
                      <b-form-select
                        :options="eye_color_options"
                        class="ml-2"
                        id="eye_color"
                        v-model="eye_color"
                        size="md"
                        value="eye_color"
                        placeholder="Kolor oczu"
                      ></b-form-select>
                    </div>
                  </th>
                  <th>
                    <div id="filter">
                      <b-form-select
                        :options="body_type_options"
                        class="ml-2"
                        id="body_type"
                        v-model="body_type"
                        size="md"
                        value="body_type"
                        placeholder="Sylwetka"
                      ></b-form-select>
                    </div>
                  </th>-->
                  <th>
                    <div id="filter">
                      <b-form-select
                        :options="location_options"
                        class="ml-2"
                        id="location"
                        v-model="location"
                        size="md"
                        value="location"
                      ></b-form-select>
                    </div>
                  </th>
                  <th>
                    <b-row>
                      <b-col cols="2"></b-col>
                      <b-col cols="8">
                        <div class="p-1 text-white text-i">
                          <h6>Przedział wiekowy: {{ age_min }} - {{ age_max }}</h6>
                        </div>
                      </b-col>
                      <b-col cols="2"></b-col>
                    </b-row>
                    <b-row>
                      <b-col cols="1"></b-col>
                      <b-col cols="5">
                        <div>
                          <b-form-input id="age_min" v-model="age_min" type="range" min="18" max="99"></b-form-input>
                        </div>
                      </b-col>
                      <b-col cols="5">
                        <div>
                          <b-form-input
                            id="age_max"
                            v-model="age_max"
                            type="range"
                            :min="age_min"
                            max="100"
                          ></b-form-input>
                        </div>
                      </b-col>
                      <b-col cols="1"></b-col>
                    </b-row>
                  </th>
                  <!--<th>
                    <div id="filter">
                      <b-form-input
                        type="number"
                        id="agemin"
                        size="md"
                        placeholder="wiek min"
                        v-model="age_min"
                        class="form-control"
                      />
                    </div>
                  </th>
                  <th>
                    <div id="filter">
                      <input
                        type="number"
                        id="agemax"
                        size="md"
                        placeholder="wiek maks"
                        v-model="age_max"
                        class="form-control"
                      />
                    </div>
                  </th>-->
                  <!--<th>
                    <div id="filter">
                      <input
                        class="ml-2"
                        type="text"
                        name="birthday"
                        id="birthday"
                        v-model="birthday"
                        placeholder="birthday"
                      />
                    </div>
                  </th>-->
                  <th>
                    <b-nav-form>
                      <b-form-input
                        size="md"
                        class="mr-sm-2"
                        placeholder="Nazwa użytkownika"
                        v-model="searchText"
                      ></b-form-input>
                    </b-nav-form>
                  </th>
                  <th>
                    <div id="filter">
                      <button type="submit" class="btn btn-primary float-right">Filtruj</button>
                    </div>
                  </th>
                  <th>
                    <a
                      class="btn btn-primary ml-2 mr-2"
                      data-toggle="collapse"
                      href="#collapseExample"
                      role="button"
                      aria-expanded="false"
                      aria-controls="collapseExample"
                      >Więcej filtrów</a
                    >
                  </th>
                </tr>
                <tr>
                  <div class="collapse" id="collapseExample">
                    <div class="card card-body">
                      Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid.
                      Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident.
                    </div>
                  </div>
                </tr>
              </table>
            </form>

            <!--<input
              class="form-control mr-sm-2"
              type="search"
              placeholder="Nazwa użytkownika"
              aria-label="Search"
            />
            <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Filtruj</button>-->
          </nav>
        </b-col>
        <b-col cols="1"></b-col>
      </b-row>
      <b-row>
        <b-col cols="1"></b-col>
        <b-col cols="10">
          <div v-if="searchText">
            <div class="oneline">
              <h1 id="title">Wyniki wyszukiwania dla frazy</h1>
            </div>
            <div class="oneline">
              <h2>
                <p class="font-italic text-primary">{{ searchText }}</p>
              </h2>
            </div>
          </div>
          <div v-else>
            <h1 id="title">Wyniki wyszukiwania:</h1>
          </div>
        </b-col>
        <b-col cols="1"></b-col>
      </b-row>
      <b-row>
        <b-col cols="12" align-self="start" class="scroll">
          <b-row v-for="i in Math.ceil(users.length / 2)" v-bind:key="i">
            <b-col cols="6" v-for="user in users.slice((i - 1) * 2, i * 2)" v-bind:key="user.id" style="ml-5 mr-5">
              <router-link :to="{ name: 'userprofile', params: { pk: user.pk } }">
                <div cardbox>
                  <b-card :img-src="getUrl(user.profile_picture)" img-alt="Card image" img-left class="user-card">
                    <b-card-title>
                      <div class="oneline">
                        <h2>
                          <p class="font-weight-bold">{{ user.username }}</p>
                        </h2>
                      </div>
                      ({{ getAge(user.birthday) }})
                    </b-card-title>

                    <b-card-text>
                      <h4 v-if="user.description != null">
                        <p class="font-italic">{{ user.description }}</p>
                      </h4>
                      <h4 v-else>
                        <p class="font-italic">Brak opisu.</p>
                      </h4>
                    </b-card-text>
                  </b-card>
                </div>
              </router-link>
            </b-col>
          </b-row>
          <br />
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'UsersList',
  components: {},
  data() {
    return {
      searchText: null,
      birthday: null,
      sex: null,
      orientation: null,
      location: null,
      hair_color: null,
      hair_length: null,
      eye_color: null,
      body_type: null,
      users: [],
      profileImage: null,
      is_smoking: null,
      today: new Date(),
      birthDate: '',
      age: '',
      age_min: 18,
      age_max: 100,
      m: '',
      description: null,
      sex_options: [
        { value: null, text: 'płeć' },
        { value: 'Mężczyzna', text: 'mężczyzna' },
        { value: 'Kobieta', text: 'kobieta' },
        { value: 'Inna', text: 'inna' },
      ],
      orientation_options: [
        { value: null, text: 'orientacja' },
        { value: 'Hetero', text: 'heteroseksualna' },
        { value: 'Homo', text: 'homoseksualna' },
        { value: 'Bi', text: 'biseksualna' },
      ],
      location_options: [
        { value: null, text: 'lokalizacja' },
        { value: 'Poznań', text: 'Poznań' },
        { value: 'Warszawa', text: 'Warszawa' },
      ],
      body_type_options: [
        { value: null, text: 'Sylwetka' },
        { value: 'Normalna', text: 'normalna' },
        { value: 'Szczupła', text: 'szczupła' },
        { value: 'Wysportowana', text: 'wysportowana' },
        { value: 'Puszysta', text: 'puszysta' },
      ],
      eye_color_options: [
        { value: null, text: 'Kolor oczu' },
        { value: 'Szare', text: 'szare' },
        { value: 'Niebieskie', text: 'niebieskie' },
        { value: 'Brązowe', text: 'brązowe' },
        { value: 'Piwne', text: 'piwne' },
        { value: 'Szare', text: 'zieone' },
      ],
      hair_color_options: [
        { value: null, text: 'Kolor włosów' },
        { value: 'Blond', text: 'blond' },
        { value: 'Ciemny blond', text: 'ciemny blond' },
        { value: 'Jasny blond', text: 'jasny blond' },
        { value: 'Brązowe', text: 'brązowe' },
        { value: 'Ciemny brąz', text: 'ciemny brąz' },
        { value: 'Jasny brąz', text: 'jasny brąz' },
        { value: 'Czarne', text: 'czarne' },
        { value: 'Siwe', text: 'siwe' },
        { value: 'Inny', text: 'inny' },
      ],
      hair_length_options: [
        { value: null, text: 'Długość włosów' },
        { value: 'Bardzo krótkie', text: 'bardzo krótkie' },
        { value: 'Krótkie', text: 'krótkie' },
        { value: 'Średnie', text: 'średnie (do barków)' },
        { value: 'Dłuższe', text: 'dłuższe (do łopatek)' },
        { value: 'Długie', text: 'długie' },
        { value: 'Bardzo długie', text: 'bardzo długie (do pasa+)' },
        { value: 'Łysy', text: 'brak (łysy)' },
      ],
      smoking_options: [
        { value: null, text: '' },
        { value: '0', text: 'nie palę' },
        { value: '1', text: 'okazjonalnie' },
        { value: '2', text: 'często' },
        { value: '3', text: 'codziennie' },
        { value: '4', text: 'nałogowo' },
      ],
      fields: ['location', 'sex', 'birthday'],
    };
  },
  methods: {
    getUsers() {
      this.users = [];
      axios
        .get('http://127.0.0.1:8000/api/user/users', {
          params: {
            search: localStorage.getItem('search-text'),
            sex: this.sex,
            location: this.location,
            birthday: this.birthday,
            hair_length: this.hair_length,
            hair_color: this.hair_color,
            eye_color: this.eye_color,
            body_type: this.body_type,
            is_smoking: this.is_smoking,
            orientation: this.orientation,
          },
          headers: {
            Authorization: 'Token ' + localStorage.getItem('user-token'),
          },
        })
        .then((response) => {
          console.log(response), (this.users = response.data);
        })
        .catch((errors) => console.log(errors));
      this.searchText = localStorage.getItem('search-text');
      localStorage.removeItem('search-text');
    },
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
    getUrl(pic) {
      if (pic != null) return 'http://127.0.0.1:8000' + pic;
      else return 'https://www.manufacturingusa.com/sites/manufacturingusa.com/files/default.png';
    },
  },
  created() {
    this.getUsers();
  },
};
</script>

<style scoped>
.page {
  margin: auto;
  width: 100%;
}

#filters {
  margin: auto;
  width: 100%;
}
#filter {
  margin: auto;
  width: 100%;
  padding-left: 20px;
}
#title {
  padding: 1cm;
  color: white;
  color: #ad1717;
  text-shadow: 1px 1px #000000;
}
.card {
  margin-bottom: 15px;
  width: 100%;
  height: 300px;
  padding-block: 1px;
}
td {
  padding-left: 2.1cm;
  padding-right: 2.1cm;
  padding-bottom: 1cm;
}
.card-img-left {
  max-height: 300px;
  object-fit: cover;
  max-width: 300px;
}
.card-text {
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  text-align: left;
  font-size: 5px;
  color: white;
}
.user-card {
  background: #8d1515;
  color: white;
  border-style: solid;
  border-width: 2px;
  border-color: #aa1d37;
}
.user-card:hover {
  background: #aa1a1a;
}
.scroll {
  height: 100%;
  overflow-y: scroll;
  height: 100vh;
}
.navbar {
  border-radius: 17px;
  background-color: #db4460;
}
.oneline {
  display: inline-block;
}
.h1 {
  color: #ad1717;
  text-shadow: 1px 1px #ff0202;
}
.btn {
  border-radius: 12px;
}
.h6 {
  color: rgb(255, 255, 255);
}
</style>
