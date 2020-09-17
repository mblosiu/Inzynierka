<template>
  <div id="userprofile">
    <br />
    <b-container class="bv-example-row" fluid>
      <b-row>
        <b-col cols="2">
          <b-sidebar id="sidebar-footer" aria-label="Okno chatu" no-header shadow>
            <template v-slot:footer="{ hide }">
              <div class="d-flex bg-dark text-light align-items-center px-3 py-2">
                <strong class="mr-auto"></strong>
                <b-button size="sm" @click="hide">Zamknij</b-button>
              </div>
            </template>
            <div class="px-3 py-2">
              <p>Okienko chatu</p>
            </div>
          </b-sidebar>
        </b-col>
        <b-col cols="4">
          <div>
            <b-card
              :img-src="getUrl(user.profile_picture)"
              img-alt="Card image"
              style="width: 27rem;"
              img-top
              class="user-card"
              alt="Card image cap"
            >
              <b-card-title>
                <h2>{{ user.username }} ({{ getAge(user.birthday) }})</h2>
              </b-card-title>
              <b-card-text>
                <div>
                  <div v-if="user.description != null">
                    <h3>{{ user.description }}</h3>
                  </div>
                  <div v-else>
                    <h3>Brak opisu.</h3>
                  </div>
                </div>
                <br />
                <div class="btn-toolbar" role="toolbar" aria-label="Toolbar with button groups">
                  <div class="btn-group mr-3 ml-3" role="group" aria-label="icons">
                    <button
                      v-b-toggle.sidebar-footer
                      type="button"
                      class="btn btn-secondary"
                      data-toggle="tooltip"
                      data-placement="bottom"
                      title="Wyślij wiadomość"
                    >
                      <svg
                        color="lightblue"
                        width="3em"
                        height="3em"
                        viewBox="0 0 16 16"
                        class="bi bi-chat-right-dots"
                        fill="currentColor"
                        xmlns="http://www.w3.org/2000/svg"
                      >
                        <path
                          fill-rule="evenodd"
                          d="M2 1h12a1 1 0 0 1 1 1v11.586l-2-2A2 2 0 0 0 11.586 11H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1zm12-1a2 2 0 0 1 2 2v12.793a.5.5 0 0 1-.854.353l-2.853-2.853a1 1 0 0 0-.707-.293H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h12z"
                        />
                        <path
                          d="M5 6a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm4 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm4 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0z"
                        />
                      </svg>
                    </button>
                    <button
                      type="button"
                      class="btn btn-secondary"
                      data-toggle="tooltip"
                      data-placement="bottom"
                      title="Zaproś do grona znajomych"
                    >
                      <svg
                        color="blue"
                        width="3em"
                        height="3em"
                        viewBox="0 0 16 16"
                        class="bi bi-person-plus-fill"
                        fill="currentColor"
                        xmlns="http://www.w3.org/2000/svg"
                      >
                        <path
                          fill-rule="evenodd"
                          d="M1 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H1zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm7.5-3a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1H13V5.5a.5.5 0 0 1 .5-.5z"
                        />
                        <path
                          fill-rule="evenodd"
                          d="M13 7.5a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 0 1H14v1.5a.5.5 0 0 1-1 0v-2z"
                        />
                      </svg>
                    </button>
                    <button
                      type="button"
                      class="btn btn-secondary"
                      data-toggle="tooltip"
                      data-placement="bottom"
                      title="Zobacz galerię"
                    >
                      <div id="show-btn" @click="$bvModal.show('bv-modal-example')">
                        <svg
                          color="lightgreen"
                          width="3em"
                          height="3em"
                          viewBox="0 0 16 16"
                          class="bi bi-images"
                          fill="currentColor"
                          xmlns="http://www.w3.org/2000/svg"
                        >
                          <path
                            fill-rule="evenodd"
                            d="M12.002 4h-10a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1zm-10-1a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V5a2 2 0 0 0-2-2h-10z"
                          />
                          <path
                            d="M10.648 8.646a.5.5 0 0 1 .577-.093l1.777 1.947V14h-12v-1l2.646-2.354a.5.5 0 0 1 .63-.062l2.66 1.773 3.71-3.71z"
                          />
                          <path
                            fill-rule="evenodd"
                            d="M4.502 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zM4 2h10a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1v1a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2h1a1 1 0 0 1 1-1z"
                          />
                        </svg>
                      </div>
                    </button>
                    <b-modal
                      id="bv-modal-example"
                      size="lg"
                      title="Galeria użytkownika" + {{user.username}}
                      hide-footer
                    >
                      <div v-if="images != []">
                        <div>
                          <b-carousel
                            id="carousel-1"
                            v-model="slide"
                            :interval="40000"
                            controls
                            indicators
                            background="#ababab"
                            img-width="100%"
                            img-height="100%"
                            style="text-shadow: 1px 1px 2px #333;"
                          >
                            <div
                              v-for="image in images"
                              v-bind:key="image.id"
                              style="padding-bottom:2px; img-height:50%;"
                            >
                              <b-carousel-slide :img-src="getUrl(image.image)"></b-carousel-slide>
                            </div>
                          </b-carousel>
                        </div>
                        <footer>
                          <b-row>
                            <b-col cols="10"></b-col>
                            <b-col cols="2">
                              <b-button
                                class="mt-3"
                                block
                                @click="$bvModal.hide('bv-modal-example')"
                              >Zamknij</b-button>
                            </b-col>
                          </b-row>
                          <b-row>
                            <b-col cols="1"></b-col>
                            <b-col cols="10"></b-col>
                            <div class="comments">
                              <h2>Komentarze:</h2>
                              <br />
                            </div>
                            <b-col cols="1"></b-col>
                          </b-row>
                        </footer>
                      </div>
                      <div v-else>
                        <footer>
                          <b-row>
                            <b-col cols="1"></b-col>
                            <b-col cols="10"></b-col>
                            <div class="comments">
                              <h2>Użytkownik nie posiada w swojej galerii żadnego zdjęcia :(</h2>
                              <br />
                            </div>
                            <b-col cols="1"></b-col>
                          </b-row>
                          <b-row>
                            <b-col cols="10"></b-col>
                            <b-col cols="2">
                              <b-button
                                class="mt-3"
                                block
                                @click="$bvModal.hide('bv-modal-example')"
                              >Zamknij</b-button>
                            </b-col>
                          </b-row>
                        </footer>
                      </div>
                    </b-modal>
                    <button
                      type="button"
                      class="btn btn-secondary"
                      data-toggle="tooltip"
                      data-placement="bottom"
                      title="Polub"
                    >
                      <svg
                        color="red"
                        width="3em"
                        height="3em"
                        viewBox="0 0 16 16"
                        class="bi bi-heart-fill"
                        fill="currentColor"
                        xmlns="http://www.w3.org/2000/svg"
                      >
                        <path
                          fill-rule="evenodd"
                          d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"
                        />
                      </svg>
                    </button>
                    <button
                      type="button"
                      class="btn btn-secondary"
                      data-toggle="tooltip"
                      data-placement="bottom"
                      title="Zablokuj użytkownika"
                    >
                      <svg
                        color="grey"
                        width="3em"
                        height="3em"
                        viewBox="0 0 16 16"
                        class="bi bi-lock-fill"
                        fill="currentColor"
                        xmlns="http://www.w3.org/2000/svg"
                      >
                        <path
                          d="M2.5 9a2 2 0 0 1 2-2h7a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-7a2 2 0 0 1-2-2V9z"
                        />
                        <path
                          fill-rule="evenodd"
                          d="M4.5 4a3.5 3.5 0 1 1 7 0v3h-1V4a2.5 2.5 0 0 0-5 0v3h-1V4z"
                        />
                      </svg>
                    </button>
                  </div>
                </div>
              </b-card-text>
            </b-card>
          </div>
        </b-col>
        <b-col cols="5">
          <div>
            <b-tabs pills card vertical>
              <b-tab title="O mnie" active>
                <div class="card text-black bg-dark mb-3">
                  <div class="card-header">
                    <h3>O mnie:</h3>
                  </div>
                  <ul class="list-group list-group-flush">
                    <li class="list-group-item">Imię i nazwisko: {{ user.name }} {{ user.surname }}</li>
                    <li class="list-group-item">Płeć: {{ user.sex }}</li>
                    <li class="list-group-item">Wiek: {{ getAge(user.birthday) }}</li>
                    <li class="list-group-item">Mieszkam w: {{ user.location }}</li>
                    <li class="list-group-item">Urodziny: {{ user.birthday }}</li>
                    <li class="list-group-item">Status/zajęcie: {{ user.status }}</li>
                    <li class="list-group-item">Edukacja: {{ user.education }}</li>
                    <div smoking>
                      <div v-if="user.is_smoking == 0">
                        <li class="list-group-item">Papierosy: nie palę</li>
                      </div>
                      <div v-else-if="user.is_smoking == 1">
                        <li class="list-group-item">Papierosy: okazjonalnie</li>
                      </div>
                      <div v-else-if="user.is_smoking == 2">
                        <li class="list-group-item">Papierosy: często</li>
                      </div>
                      <div v-else-if="user.is_smoking == 3">
                        <li class="list-group-item">Papierosy: codziennie</li>
                      </div>
                      <div v-else-if="user.is_smoking == 4">
                        <li class="list-group-item">Papierosy: nałogowo</li>
                      </div>
                      <div v-else>
                        <li class="list-group-item">Papierosy: {{ user.is_smoking }}</li>
                      </div>
                    </div>
                    <div v-if="user.is_drinking_alcohol == 0">
                      <li class="list-group-item">Alkohol: nie piję</li>
                    </div>
                    <div v-else-if="user.is_drinking_alcohol == 1">
                      <li class="list-group-item">Alkohol: okazjonalnie</li>
                    </div>
                    <div v-else-if="user.is_drinking_alcohol == 2">
                      <li class="list-group-item">Alkohol: często</li>
                    </div>
                    <div v-else-if="user.is_drinking_alcohol == 3">
                      <li class="list-group-item">Alkohol: codziennie</li>
                    </div>
                    <div v-else-if="user.is_drinking_alcohol == 4">
                      <li class="list-group-item">Alkohol: nałogowo</li>
                    </div>
                    <div v-else>
                      <li class="list-group-item">Alkohol: {{ user.is_drinking_alcohol }}</li>
                    </div>
                  </ul>
                </div>
              </b-tab>
              <b-tab title="Mój wygląd">
                <div class="card text-black bg-dark mb-3">
                  <div class="card-header">
                    <h3>Mój wygląd</h3>
                  </div>
                  <ul class="list-group list-group-flush">
                    <li class="list-group-item">Wzrost: {{ user.growth }}</li>
                    <li class="list-group-item">Waga: {{ user.weight }}</li>
                    <li class="list-group-item">Włosy: {{ user.hair_length }} {{ user.hair_color }}</li>
                    <li class="list-group-item">Kolor oczu: {{ user.eye_color }}</li>
                    <li class="list-group-item">Sylwetka: {{ user.body_type }}</li>
                    <li class="list-group-item">
                      Znaki szczególne
                      <p v-if="user.freckles != false">mam piegi</p>
                      <p v-if="user.glasses != false">noszę okulary</p>
                    </li>
                    <li class="list-group-item"></li>
                  </ul>
                </div>
              </b-tab>
              <b-tab title="Zainteresowania">
                <div class="card text-black bg-dark mb-3">
                  <div class="card-header">
                    <h3>Zainteresowania</h3>
                  </div>
                  <ul class="list-group list-group-flush">
                    <li class="list-group-item">Rozrywka i hobby:</li>
                    <li class="list-group-item">Sport:</li>
                    <li class="list-group-item">Muzyka:</li>
                    <li class="list-group-item">Kuchnia:</li>
                    <li class="list-group-item">Ulubione miejsce:</li>
                    <li class="list-group-item">Największa pasja:</li>
                  </ul>
                </div>
              </b-tab>
              <b-tab title="Moje preferencje">
                <div class="card text-black bg-dark mb-3">
                  <div class="card-header">
                    <h3>Moje preferencje:</h3>
                  </div>
                  <ul class="list-group list-group-flush">
                    <li class="list-group-item">Orientacja: {{ user_preferences.sex_preference }}</li>
                    <li
                      class="list-group-item"
                    >Przedział wiekowy: {{ user_preferences.age_preference }}</li>
                    <li class="list-group-item">Waga: {{ user_preferences.weight_preference }}</li>
                    <li
                      class="list-group-item"
                    >Sylwetka: {{ user_preferences.body_type_preference }}</li>
                    <li class="list-group-item">
                      Włosy: {{ user_preferences.hair_length_preference }}, blond: ({{
                      user_preferences.hair_color_blonde_preference
                      }}), brunatne: ({{ user_preferences.hair_color_brunette_preference }}), rude: ({{
                      user_preferences.hair_color_red_preference
                      }}), czarne: todo
                    </li>
                    <li class="list-group-item">Kolor oczu: todo</li>
                    <li class="list-group-item">
                      Znaki szczególne:
                      <p v-if="user_preferences.freckles_preference != false">piegi</p>
                      <p v-if="user_preferences.glasses_preference != false">okulary</p>+td tatuaże
                    </li>
                    <li
                      class="list-group-item"
                    >Edukacja: {{ user_preferences.education_preference }}</li>
                  </ul>
                </div>
              </b-tab>
              <b-tab title="Cechy charakteru">
                <div class="card text-black bg-dark mb-3">
                  <div class="card-header">
                    <h3>Cechy charakteru:</h3>
                  </div>
                  <ul class="list-group list-group-flush">
                    <li class="list-group-item">Pewność siebie: {{ user.assertiveness }}</li>
                    <li class="list-group-item">Szczerość: {{ user.sincerity }}</li>
                    <li class="list-group-item">Empatia: {{ user.empathy }}</li>
                    <li class="list-group-item">Komunikatywność: {{ user.communication }}</li>
                    <li class="list-group-item">Bezinteresowność: {{ user.selflessness }}</li>
                    <li class="list-group-item">Uczciwość: {{ user.honesty }}</li>
                    <li class="list-group-item">Sumienność: {{ user.scrupulousness }}</li>
                    <li class="list-group-item">Pracowitość: {{ user.diligence }}</li>
                    <li class="list-group-item">Życzliwość: {{ user.kindness }}</li>
                    <li class="list-group-item">+ romantyczność</li>
                  </ul>
                </div>
              </b-tab>
            </b-tabs>
          </div>
        </b-col>
        <b-col cols="1"></b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      user: {},
      user_preferences: {},
      images: {},
    };
  },
  methods: {
    getUsers() {
      axios
        .get("http://127.0.0.1:8000/api/user/users/" + this.$route.params.pk, {
          params: {},
          headers: {
            Authorization: "Token " + localStorage.getItem("user-token"),
          },
        })
        .then((response) => {
          console.log(response),
            (this.user = response.data),
            (this.user_preferences = this.user.preferences);
        })
        .catch((errors) => console.log(errors));
    },
    getUserImages() {
      axios
        .get(
          "http://127.0.0.1:8000/api/user/users/" +
            this.$route.params.pk +
            "/images",
          {
            headers: {
              Authorization: "Token " + localStorage.getItem("user-token"),
            },
          }
        )
        .then((response) => {
          this.images = response.data;
          console.log(this.images[0]);
        })
        .catch((errors) => console.log(errors));
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
      if (pic != null) return "http://127.0.0.1:8000" + pic;
      else
        return "https://www.manufacturingusa.com/sites/manufacturingusa.com/files/default.png";
    },
    //onSlideStart() {},
    //onSlideEnd() {},
    //slide() {},
  },
  created() {
    this.getUsers();
    this.getUserImages();
  },
  mounted() {
    $(".carousel").carousel();
  },
};
</script>

<style scoped>
.card-header {
  color: white;
}
.mainuser {
  margin: auto;
  width: 100%;
}
.card-img-top {
  /*height: 300px;*/
  object-fit: scale-down;
}
.card-text {
  font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;
  text-align: left;
  font-size: 20px;
}
.user-card {
  background: #8d1515;
  color: white;
}
.b-sidebar {
  width: 300px;
}
.svg {
  align-content: flex-start;
}
.list-group-item {
  background: #fadbdb;
}
.tabs {
  background: #eb6767;
  border-radius: 12px;
  border-style: solid;
  border-width: 2px;
  border-color: #aa1d37;
}
.card-header {
  background: #9e1d35;
}
.bv-modal-example {
  background: #eb6767;
}
</style>