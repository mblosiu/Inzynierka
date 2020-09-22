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
            Jeśli szukasz miłości, życiowego partnera, lub po prostu osoby, z którą można porozmawiać na wspólne tematy to dobrze trafiłeś. Serwis e-Love skierowany jest do każdego użytkownika bez względu na wiek, czy rodzaj zawieranych relacji.
            <br />W dzisiejszych czasach samotność jest bardzo częstym problemem i dotyka ludzi z każdego przedziału wiekowego. Poza faktem iż samotność sama w sobie jest przykrym uczuciem, należy dodać, że jak donoszą najnowsze badania, długotrwałe jej doświadczanie bardzo niekorzystnie wpływa na nasze zdrowie. <br/>
            Nasz portal jest stale rozwijany i powiększa się nie tylko o nowe funkcjonalności ale i nowych użytkowników. Zapraszamy do darmowej rejestracji!
            <br />
          </div>
          <br />

          <p></p>
          <blockquote class="blockquote text-right">
            <h6>"Każdy powinien mieć kogoś, z kim mógłby szczerze pomówić, bo choćby człowiek był nie wiadomo jak dzielny, czasami czuje się bardzo samotny."</h6>
            <footer class="blockquote-footer">
              Ernest Hemingway
              <cite title="Source Title">"Komu bije dzwon"</cite>
            </footer>
          </blockquote>
        </b-col>
        <b-col cols="5"></b-col>
        <b-col cols="3">
          <br />

          <div class="card text-black mb-3 rightside" style="width: 19rem;">
            <div class="card-body no-background">
              <br />
              <h3 class="card-title no-background">Nie masz konta?</h3>
              <br />
              <h6>
                <p
                  class="card-text no-background"
                >Dołącz do społeczności e-love zakładając darmowe konto!</p>
              </h6>
              <br />
              <b-button variant="warning" size="lg" href="/register">Zarejestruj się</b-button>
              <!--<a href="/register" class="btn-lg">Zarejestruj się</a>-->
              <br />
            </div>
            <br />
          </div>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
// @ is an alias to /src
//import Register from "@/views/Register.vue";

export default {
  name: "Home",
  components: {
    //Register,
  },
};
</script>

<style scoped>
text {
  text-align: left;
}
.leftside {
  background-color: rgba(252, 198, 225, 0.795);
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
  background-color: rgba(255, 172, 213, 0.795);
  padding: 20px;
  color: #812b3b;
  border-color: blueviolet;
  border-radius: 25px;
  border-style: solid;
  border-width: 1px;
}
.rightside:hover {
  background-color: rgba(255, 172, 213, 0.795);
  padding: 20px;
  color: #bd1131;
  border-color: rgb(243, 38, 38);
  border-radius: 25px;
  border-style: solid;
  border-width: 1px;
}
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
  color: #ad1717;
  text-shadow: 1px 1px #ac0101;
}
.card text-black bg-secondary mb-3 {
  background-color: rgba(255, 255, 255, 0.3);
  border-radius: 25px;
}

.btn-lg:hover {
  background-color: #ffd000;
  color: rgb(204, 0, 0);
  font-weight: 600;
  border-style: solid;
  border-width: 1px;
}
</style>
