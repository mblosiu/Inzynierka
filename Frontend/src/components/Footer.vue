<template>
  <v-footer color="purple" padless>
    <v-row justify="center" no-gutters>
      <v-spacer></v-spacer>
      <v-btn
        color="yellow"
        text
        rounded
        class="my-2"
        href="https://docs.google.com/forms/d/e/1FAIpQLSdnh5tVIxGMyQSSCXP_nPGoVUZiZT-HDwFF3r_kCogy_vtK2A/viewform"
      >
        Feedback
      </v-btn>
      <v-spacer></v-spacer>
      <v-dialog v-model="dialog" width="600px">
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            color="white"
            text
            rounded
            class="my-2"
            v-bind="attrs"
            v-on="on"
          >
            <v-icon class="white"></v-icon>
            FAQ
          </v-btn>
        </template>
        <v-card>
          <v-card-title flex class="purple">
            <v-spacer></v-spacer>
            <span class="headline white--text"
              >Pytania i odpowiedzi dla nowych użytkowników</span
            >
            <v-spacer></v-spacer>
          </v-card-title>
          <br />
          <v-card-text class="text-left">
            <p class="font-weight-bold">1. Czy rejestracja/pełne użytkowanie serwisu jest darmowe?</p>
            <p>Tak. Serwis jest całkowicie darmowy, pozbawiony mikropłatności. Opcja premium jeśli planowana, zapewni niewielkie udogodnienia nie faworyzując przy tym posiadających ją użytkowników.</p>
            
            <p class="font-weight-bold">2. Czy weryfikacja konta jest niezbędna?</p>
            <p>Aby się zalogować i tym samym móc korzystać z serwisu, wymagana jest weryfikacja konta poprzez link aktywacyjny wysłany na podany przy rejestracji adres email. Ma to na celu ograniczenie nieuczciwych praktyk ze strony użytkowników. Niezweryfikowane konto nie jest również widoczne w serwisie dla innych użytkowników.</p>
            
            <p class="font-weight-bold">3. Zapomniałem hasła. Co mam robić?</p>
            <p>W takim przypadku należy skontaktować się z nami na jeden z adresów podanych w zakładce "kontakty" w stopce.</p>            
            <p class="font-weight-bold">4. Czy można usunąć konto z serwisu?</p>
            <p>Konto można usunąć będąc zalogowanym i przechodząc w panelu bocznym do zakładki ustawienia -> ustawienia prywatności. Wszystkie dane na temat konta zostają trwale usunięte i nie ma możliwości jego przywrócenia.</p>
            <p class="font-weight-bold">5. Czy moje konto jest anonimowe?</p>
            <p>Początkowo każde rejestrowane konto nie posiada w opisie kluczowych danych personalnych. To ile użytkownik o sobie ujawni zależy tylko i wyłącznie od niego.</p>
            <p class="font-weight-bold">6. Jak mogę zmienić swój profil?</p>
            <p>Należy będąc zalogowanym przejść do panelu bocznego i wybrać interesującą nas zakładkę w zależności od tego, co chcemy personalizować. W zakładce "galeria" można dodawać/usuwać zdjęcia, które będą widoczne dla podglądających nas użytkowników. Można tam również ustawiać zdjęcie profilowe. W zakładce "ustawienia" możemy uzupełniając odpowiednie pola dowolnie wzbogacić profil o dodatkowe informacje o naszej osobie.</p>
            <p class="font-weight-bold">7. Nie mogę wstawić zdjęcia, dlaczego?</p>
            <p>Jeśli nie możesz wstawić zdjęcia, najprawdopodobniej przyczyną problemu jest rozmiar lub typ dodawanego pliku. Preferujemy dodawanie mniejszych plików z racji problemów z obsługą większych zdjęć. Dodatkowo prosimy zwrócić uwagę na typ zdjęcia( preferowany JPG JPEG ) Jeśli jednak dalej nie udaje ci się wstawić zdjęcia, proszę skontaktuj się w tej sprawie pod adres w zakładce "kontakt".</p>
            <p class="font-weight-bold">8. Dlaczego nie mogę się zalogować?</p>
            <p>Sprawdź, czy nie masz włączonego klawisza CapsLock oraz czy podajesz poprawne hasło podane przy rejestracji. Upewnij się także, że masz włączoną obsługę ciasteczek w swojej przeglądarce oraz że posiadasz wszystkie aktualizacje do swojego oprogramowania. </p>
            <p class="font-weight-bold">9. Dlaczego nie otrzymałem linku aktywacyjnego?</p>
            <p>Sprawdź, czy mail z linkiem nie trafił do folderu ze spamem. Niektóre filtry anty-spamowe automatycznie uznają niektóre wiadomośći jako spam. Czasami też zdarza się, że link aktywacyjny nie dociera do adresata od razu, poczekaj 10-15 minut. Jeśli po tym czasie nadal nie otrzymasz linku aktywacyjnego, proszę skontaktuj się z nami.</p>
            <p class="font-weight-bold">10. Mogę zablokować innego użytkownika?</p>
            <p>Tak. Wystarczy wejść na profil danego użytkownika, następnie klikając w ikonę w lewym dolnym rogu zdjęcia wybrać opcję "zablokuj".</p>
            <p class="font-weight-bold">11. Jak odblokować użytkownika?</p>
            <p>Lista zablokowanych użytkowników dostpęna jest w zakładce "ustawienia" w prywatności. Klikając w guzik "czarna lista" można przeglądać zablokowanych użytkowików i ewentualnie takowego odblokować.</p>
            <p class="font-weight-bold">12. Jak dodać osoby do listy przyjaciół?</p>
            <p>Na profilu interesującego nas użytkownika, wystarczy kliknąć w ikonę znajdującą się obok jego nazwy i wybrać opcję "dodaj znajomego". W taki sam sposób można danego użytkownika usunąć. Panel z listą znajomych dostepny jest po wybraniu opcji "znajomi" z menu w górnym pasku.</p>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn color="purple darken-1" text @click="dialog = false">
              Zamknij
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
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

        <br />
        <v-card-text class="text-left">
          Serwis randkowy e-Love tworzony jest przez dwóch studentów informatyki
          uniwersytetu im. Adama Mickiewicza w Poznaniu, w ramach inżynierskiego
          projektu zespołowego.
          <br />
          <v-card-subtitle></v-card-subtitle>
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
          21.02.2021r.
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
            Aby założyć konto wymagane jest ukończenie 18 roku życia.
            <br />
            Bądźmy dla siebie mili i życzliwi. Serwis powstał aby szerzyć
            miłość, nie nienawiść.
          </p>
        </v-card-text>

        <v-divider></v-divider>
        <v-card-subtitle>
          Ostatnia aktualizacja:
          <p class="font-weight-bold"></p>
          21.02.2021r.
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
              <p class="font-italic">mblosiu@gmail.com</p>
              <v-divider></v-divider>
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
