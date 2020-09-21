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
            <p>{{ user_data.username }} :</p>
            <p>{{ user.username }} :</p>
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
                <div class="oneline">
                  <h2>
                    <p class="font-weight-bold">{{ user.username }}</p>
                  </h2>
                </div>
                ({{ getAge(user.birthday) }})
              </b-card-title>
              <b-card-text>
                <div>
                  <h4 v-if="user.description != null">
                    <p class="font-italic">{{ user.description }}</p>
                  </h4>
                  <h4 v-else>
                    <p class="font-italic">Brak opisu.</p>
                  </h4>
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
                        color="lightblue"
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
                          color="lightblue"
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
                      title="Galeria użytkownika"
                      hide-footer
                    >
                      <div v-if="images != []">
                        <div>
                          <!--v-model="slide"-->
                          <b-carousel
                            id="carousel-1"
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
                    <div v-if="false==isUserLiked()">
                      <button
                        type="button"
                        v-on:click="likeUser"
                        class="btn btn-secondary"
                        data-toggle="tooltip"
                        data-placement="bottom"
                        title="Polub"
                      >
                        <svg
                          color="pink"
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
                    </div>
                    <div v-else>
                      <button
                        type="button"
                        v-on:click="dislikeUser"
                        class="btn btn-secondary"
                        data-toggle="tooltip"
                        data-placement="bottom"
                        title="Usuń polubienie"
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
                    </div>

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
                    <li class="list-group-item">
                      Imię i nazwisko:
                      <div class="oneline">
                        <p class="font-weight-bold">{{ user.name }} {{ user.surname }}</p>
                      </div>
                    </li>
                    <li class="list-group-item">
                      Płeć:
                      <div class="oneline">
                        <p class="font-weight-bold">{{ user.sex }}</p>
                      </div>
                    </li>
                    <li class="list-group-item">
                      Wiek:
                      <div class="oneline">
                        <p class="font-weight-bold">{{ getAge(user.birthday) }}</p>
                      </div>
                    </li>
                    <li class="list-group-item">
                      Mieszkam w:
                      <div class="oneline">
                        <p class="font-weight-bold">{{ user.location }}</p>
                      </div>
                    </li>
                    <li class="list-group-item">
                      Urodziny:
                      <div class="oneline">
                        <p class="font-weight-bold">{{ user.birthday }}</p>
                      </div>
                    </li>
                    <li class="list-group-item">
                      Status:
                      <div class="oneline">
                        <p class="font-weight-bold">{{ user.status }}</p>
                      </div>
                    </li>
                    <li class="list-group-item">
                      Wykształcenie:
                      <div class="oneline">
                        <p class="font-weight-bold">{{ user.education }}</p>
                      </div>
                    </li>

                    <div v-if="user.is_smoking == 0">
                      <li class="list-group-item">
                        Papierosy:
                        <div class="oneline">
                          <p class="font-weight-bold">nie palę</p>
                        </div>
                      </li>
                    </div>
                    <div v-else-if="user.is_smoking == 1">
                      <li class="list-group-item">
                        Papierosy:
                        <div class="oneline">
                          <p class="font-weight-bold">okazjonalnie</p>
                        </div>
                      </li>
                    </div>
                    <div v-else-if="user.is_smoking == 2">
                      <li class="list-group-item">
                        Papierosy:
                        <div class="oneline">
                          <p class="font-weight-bold">często</p>
                        </div>
                      </li>
                    </div>
                    <div v-else-if="user.is_smoking == 3">
                      <li class="list-group-item">
                        Papierosy:
                        <div class="oneline">
                          <p class="font-weight-bold">codziennie</p>
                        </div>
                      </li>
                    </div>
                    <div v-else-if="user.is_smoking == 4">
                      <li class="list-group-item">
                        Papierosy:
                        <div class="oneline">
                          <p class="font-weight-bold">nałogowo</p>
                        </div>
                      </li>
                    </div>
                    <div v-else>
                      <li class="list-group-item">
                        Papierosy:
                        <div class="oneline">
                          <p class="font-weight-bold">?</p>
                        </div>
                      </li>
                    </div>

                    <div v-if="user.is_drinking_alcohol == 0">
                      <li class="list-group-item">
                        Alkohol:
                        <div class="oneline">
                          <p class="font-weight-bold">nie piję</p>
                        </div>
                      </li>
                    </div>
                    <div v-else-if="user.is_drinking_alcohol == 1">
                      <li class="list-group-item">
                        Alkohol:
                        <div class="oneline">
                          <p class="font-weight-bold">okazjonalnie</p>
                        </div>
                      </li>
                    </div>
                    <div v-else-if="user.is_drinking_alcohol == 2">
                      <li class="list-group-item">
                        Alkohol:
                        <div class="oneline">
                          <p class="font-weight-bold">często</p>
                        </div>
                      </li>
                    </div>
                    <div v-else-if="user.is_drinking_alcohol == 3">
                      <li class="list-group-item">
                        Alkohol:
                        <div class="oneline">
                          <p class="font-weight-bold">codziennie</p>
                        </div>
                      </li>
                    </div>
                    <div v-else-if="user.is_drinking_alcohol == 4">
                      <li class="list-group-item">
                        Alkohol:
                        <div class="oneline">
                          <p class="font-weight-bold">nałogowo</p>
                        </div>
                      </li>
                    </div>
                    <div v-else>
                      <li class="list-group-item">
                        Alkohol:
                        <div class="oneline">
                          <p class="font-weight-bold">?</p>
                        </div>
                      </li>
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
                    <li class="list-group-item">
                      Wzrost:
                      <div class="oneline">
                        <p class="font-weight-bold">{{ user.growth }}</p>
                      </div>
                    </li>
                    <li class="list-group-item">
                      Waga:
                      <div class="oneline">
                        <p class="font-weight-bold">{{ user.weight }}</p>
                      </div>
                    </li>

                    <li class="list-group-item">
                      Włosy:
                      <div class="oneline">
                        <p class="font-weight-bold">{{ user.hair_length }} {{ user.hair_color }}</p>
                      </div>
                    </li>
                    <li class="list-group-item">
                      Kolor oczu:
                      <div class="oneline">
                        <p class="font-weight-bold">{{ user.eye_color }}</p>
                      </div>
                    </li>
                    <li class="list-group-item">
                      Sylwetka:
                      <div class="oneline">
                        <p class="font-weight-bold">{{ user.body_type }}</p>
                      </div>
                    </li>

                    <li class="list-group-item">
                      Znaki szczególne:
                      <div class="oneline" v-if="user.freckles != false">
                        <p class="font-weight-bold">mam piegi</p>
                      </div>
                      <div class="oneline" v-if="user.glasses != false">
                        <p class="font-weight-bold">noszę okulary</p>
                      </div>
                    </li>
                  </ul>
                </div>
              </b-tab>
              <b-tab title="Zainteresowania">
                <div class="card text-black bg-dark mb-3">
                  <div class="card-header">
                    <h3>Zainteresowania</h3>
                  </div>
                  <ul class="list-group list-group-flush">
                    <li class="list-group-item">
                      Rozrywka i hobby:
                      <div class="oneline">
                        <p class="font-weight-bold">{{ user.hobbies }}</p>
                      </div>
                    </li>
                    <li class="list-group-item">
                      Sport:
                      <div class="oneline">
                        <p class="font-weight-bold">{{ user.sport }}</p>
                      </div>
                    </li>
                    <li class="list-group-item">
                      Muzyka:
                      <div class="oneline">
                        <p class="font-weight-bold">{{ user.music }}</p>
                      </div>
                    </li>
                    <li class="list-group-item">
                      Kuchnia:
                      <div class="oneline">
                        <p class="font-weight-bold">{{ user.cooking }}</p>
                      </div>
                    </li>
                    <li class="list-group-item">
                      Ulubione miejsce:
                      <div class="oneline">
                        <p class="font-weight-bold">{{ user.favourite_place }}</p>
                      </div>
                    </li>
                    <li class="list-group-item">
                      Największa pasja:
                      <div class="oneline">
                        <p class="font-weight-bold">{{ user.passion }}</p>
                      </div>
                    </li>
                  </ul>
                </div>
              </b-tab>
              <b-tab title="Moje preferencje">
                <div class="card text-black bg-dark mb-3">
                  <div class="card-header">
                    <h3>Moje preferencje:</h3>
                  </div>
                  <ul class="list-group list-group-flush">
                    <li class="list-group-item">
                      Orientacja:
                      <div class="oneline">
                        <p class="font-weight-bold">{{ user.orientation }}</p>
                      </div>
                    </li>
                    <li class="list-group-item">
                      Przedział wiekowy:
                      <div class="oneline" v-if="user_preferences.age_preference_min != null">
                        <p class="font-weight-bold">od {{ user_preferences.age_preference_min }}</p>
                      </div>
                      <div class="oneline" v-if="user_preferences.age_preference_max != null">
                        <p class="font-weight-bold">do {{ user_preferences.age_preference_max }}</p>
                      </div>
                    </li>

                    <li class="list-group-item">
                      Edukacja:
                      <div class="oneline">
                        <p class="font-weight-bold">{{ user_preferences.education_preference }}</p>
                      </div>
                    </li>
                    <li class="list-group-item">
                      Waga:
                      <div class="oneline" v-if="user_preferences.weight_preference != null">
                        <p class="font-weight-bold">do {{ user_preferences.weight_preference }} kg</p>
                      </div>
                    </li>
                    <li class="list-group-item">
                      Sylwetka:
                      <div class="oneline">
                        <p class="font-weight-bold">{{ user_preferences.body_type_preference }}</p>
                      </div>
                    </li>
                    <li class="list-group-item">
                      Włosy:
                      <div class="oneline">
                        <p class="font-weight-bold"></p>
                      </div>
                    </li>
                    <li class="list-group-item">
                      Kolor oczu:
                      <div class="oneline">
                        <p class="font-weight-bold">{{ user_preferences.eye_color_preference }}</p>
                      </div>
                    </li>
                    <li class="list-group-item">
                      Znaki szczególne:
                      <div class="oneline" v-if="user_preferences.freckles_preference != false">
                        <p class="font-weight-bold">piegi</p>
                      </div>
                      <div class="oneline" v-if="user_preferences.glasses_preference != false">
                        <p>_</p>
                      </div>
                      <div class="oneline" v-if="user_preferences.glasses_preference != false">
                        <p class="font-weight-bold">okulary</p>
                      </div>
                    </li>

                    <div v-if="user_preferences.is_smoking_preference == 0">
                      <li class="list-group-item">
                        Papierosy:
                        <div class="oneline">
                          <p class="font-weight-bold">nie pali</p>
                        </div>
                      </li>
                    </div>

                    <div v-else-if="user_preferences.is_smoking_preference == 1">
                      <li class="list-group-item">
                        Papierosy:
                        <div class="oneline">
                          <p class="font-weight-bold">okazjonalnie</p>
                        </div>
                      </li>
                    </div>
                    <div v-else-if="user_preferences.is_smoking_preference == 2">
                      <li class="list-group-item">
                        Papierosy:
                        <div class="oneline">
                          <p class="font-weight-bold">często</p>
                        </div>
                      </li>
                    </div>
                    <div v-else-if="user_preferences.is_smoking_preference == 3">
                      <li class="list-group-item">
                        Papierosy:
                        <div class="oneline">
                          <p class="font-weight-bold">codziennie</p>
                        </div>
                      </li>
                    </div>
                    <div v-else-if="user_preferences.is_smoking_preference == 4">
                      <li class="list-group-item">
                        Papierosy:
                        <div class="oneline">
                          <p class="font-weight-bold">nałogowo</p>
                        </div>
                      </li>
                    </div>
                    <div v-else>
                      <li class="list-group-item">
                        Papierosy:
                        <div class="oneline">
                          <p class="font-weight-bold">obojętne</p>
                        </div>
                      </li>
                    </div>

                    <div v-if="user_preferences.is_drinking_alcohol_preference == 0">
                      <li class="list-group-item">
                        Alkohol:
                        <div class="oneline">
                          <p class="font-weight-bold">nie pije</p>
                        </div>
                      </li>
                    </div>
                    <div v-else-if="user_preferences.is_drinking_alcohol_preference == 1">
                      <li class="list-group-item">
                        Alkohol:
                        <div class="oneline">
                          <p class="font-weight-bold">okazjonalnie</p>
                        </div>
                      </li>
                    </div>
                    <div v-else-if="user_preferences.is_drinking_alcohol_preference == 2">
                      <li class="list-group-item">
                        Alkohol:
                        <div class="oneline">
                          <p class="font-weight-bold">często</p>
                        </div>
                      </li>
                    </div>
                    <div v-else-if="user_preferences.is_drinking_alcohol_preference == 3">
                      <li class="list-group-item">
                        Alkohol:
                        <div class="oneline">
                          <p class="font-weight-bold">codziennie</p>
                        </div>
                      </li>
                    </div>
                    <div v-else-if="user_preferences.is_drinking_alcohol_preference == 4">
                      <li class="list-group-item">
                        Alkohol:
                        <div class="oneline">
                          <p class="font-weight-bold">nałogowo</p>
                        </div>
                      </li>
                    </div>
                    <div v-else>
                      <li class="list-group-item">
                        Alkohol:
                        <div class="oneline">
                          <p class="font-weight-bold">obojętnie</p>
                        </div>
                      </li>
                    </div>
                  </ul>
                </div>
              </b-tab>
              <b-tab title="Cechy charakteru" disabled>
                <div class="card text-black bg-dark mb-3">
                  <div class="card-header">
                    <h3>Cechy charakteru:</h3>
                  </div>
                  <ul class="list-group list-group-flush">
                    <li class="list-group-item">
                      Pewność siebie:
                      <div class="oneline">
                        <p class="font-weight-bold">{{ user.assertiveness }}</p>
                      </div>
                    </li>
                    <li class="list-group-item">
                      Szczerość:
                      <div class="oneline">
                        <p class="font-weight-bold">{{ user.sincerity }}</p>
                      </div>
                    </li>
                    <li class="list-group-item">
                      Empatia:
                      <div class="oneline">
                        <p class="font-weight-bold">{{ user.empathy }}</p>
                      </div>
                    </li>
                    <li class="list-group-item">
                      Komunikatywność:
                      <div class="oneline">
                        <p class="font-weight-bold">{{ user.communication }}</p>
                      </div>
                    </li>
                    <li class="list-group-item">
                      Bezinteresowność:
                      <div class="oneline">
                        <p class="font-weight-bold">{{ user.selflessness }}</p>
                      </div>
                    </li>
                    <li class="list-group-item">
                      Uczciwość:
                      <div class="oneline">
                        <p class="font-weight-bold">{{ user.honesty }}</p>
                      </div>
                    </li>
                    <li class="list-group-item">
                      Sumienność:
                      <div class="oneline">
                        <p class="font-weight-bold">{{ user.scrupulousness }}</p>
                      </div>
                    </li>
                    <li class="list-group-item">
                      Pracowitość:
                      <div class="oneline">
                        <p class="font-weight-bold">{{ user.diligence }}</p>
                      </div>
                    </li>
                    <li class="list-group-item">
                      Życzliwość:
                      <div class="oneline">
                        <p class="font-weight-bold">{{ user.kindness }}</p>
                      </div>
                    </li>
                    <li class="list-group-item">
                      Romantyczność:
                      <div class="oneline">
                        <p class="font-weight-bold"></p>
                      </div>
                    </li>
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
      user_data: {},
      user: {},
      user_preferences: {},
      images: {},
      like: "like",
      //heartcolor: "grey",
      liked_user: {},
      user_likes: [],
      liked: false,
    };
  },
  methods: {
    likeUser() {
      //this.heartcolor = "red";
      //this.liked = true;
      const config = {
        headers: {
          Authorization: "Token " + localStorage.getItem("user-token"),
        },
      };

      axios
        .post(
          "http://127.0.0.1:8000/api/user/create-like",
          { value: "like", pk: this.$route.params.pk },
          config
        )
        .then((response) => {
          console.log(response);
        })
        .catch((errors) => console.log(errors));
      //this.$router.go();
    },
    dislikeUser() {
      //this.heartcolor = "pink";
      //like = false;
      const config = {
        headers: {
          Authorization: "Token " + localStorage.getItem("user-token"),
        },
      };

      axios
        .delete(
          "http://127.0.0.1:8000/api/user/delete-like",
          { pk: this.$route.params.pk },
          config
        )
        .then((response) => {
          console.log(response);
        })
        .catch((errors) => console.log(errors));
      this.$router.go();
    },
    getUserLikes() {
      //console.log(this.user_data['pk']); 
      axios
        .get(
          "http://127.0.0.1:8000/api/user/get-users-are-liked/" +
            this.$route.params.pk,
          {
            params: {},
            headers: {
              Authorization: "Token " + localStorage.getItem("user-token"),
            },
          }
        )
        .then((response) => {
          console.log(response),
            (this.user_likes = response.data),
            console.log(this.user_likes);
        })
        .catch((errors) => console.log(errors));
    },
    isUserLiked() {
      console.log(this.user_likes.length)
      //console.log("isuserliked 1");
      //console.log((this.user_likes).filter(pk => this.user_likes.pk === this.$route.params.pk))
      /*if(true==(user_likes.includes(user.pk))){
        liked = true;

      }else{
        liked = false;
      }*/
      for (var i = 0; i < this.user_likes.length; i++) {
        if (this.user_likes[i].pk == this.$route.params.pk) {
          console.log("polajkowany");
          return true;
          break;
        }
        console.log("nie polajkowany");
        return false;
        
      }
      //console.log(this.liked);
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
    this.getUserData();
    this.getUserLikes();
  },
  mounted() {
    //$(".carousel").carousel();
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
  background: #a01818;
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
  background: #ff9292d5;
  border-radius: 12px;
  border-style: solid;
  border-width: 2px;
  border-color: #aa1d37;
}
.card-header {
  background: #df4040;
}
.oneline {
  display: inline-block;
}
</style>
