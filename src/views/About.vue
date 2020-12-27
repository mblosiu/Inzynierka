<template>
  <v-container>
    <b-row></b-row>
    <b-row class="row justify-content-md-center">
      <br />
      <b-col cols="4"></b-col>
      <b-col cols="4" class="col align-self-center">
        <div class="card text-center">
          <div class="card-header">
            <h3>O twórcach</h3>
          </div>
          <div class="card-body">
            <br/>
            <h6
              class="card-title"
            >Serwis randkowy e-Love tworzony jest przez dwóch studentów informatyki uniwersytetu im. Adama Mickiewicza w Poznaniu, w ramach inżynierskiego projektu zespołowego.</h6>
            <br />
            <a
              href="https://github.com/mblosiu/Inzynierka"
              class="btn btn-dark"
            >Repozytorium</a>
            <br />
            <br />
            <br />
            <p class="card-text">~ Mateusz Błoszyk, Marcin Mirecki</p>
          </div>
          <div class="card-footer text-muted">
            Ostatnia aktualizacja:
            <p class="font-weight-bold"></p>22.09.2020r.
          </div>
        </div>
      </b-col>
      <b-col cols="4"></b-col>
    </b-row>
    <b-row></b-row>
    <v-row>
      <p></p>
    </v-row>
    <v-row>
      <p></p>
    </v-row>
    <v-row>
      <p></p>
    </v-row>
    <v-row>
      <p></p>
    </v-row>
    <v-row>
      <p></p>
    </v-row>
    <v-row>
      <p></p>
    </v-row>
    <v-row>
      <p></p>
    </v-row>
    <v-row>
      <p></p>
    </v-row>
  </v-container>
</template>

<script>
// @ is an alias to /src
export default {
  name: "About",
  components: {},
};
</script>

<style scoped>
.card-text {
  text-align: justify;
  font: Arial;
  font-size: 16px;
  float: right;
}
.card-header {
  background-color: rgba(248, 147, 197, 0.8);
  border: 1px solid;
  border-color: blueviolet;
}
.card-body {
  border: 1px solid;
  background-color: rgba(252, 198, 225, 0.8);
  border-color: blueviolet;
}
.card-footer {
  border: 1px solid;
  background-color: rgba(253, 191, 222, 0.8);
  border-color: blueviolet;
}
.card{
  border-radius: 2px;
}
.btn:hover{
  font-weight: 650;
}
</style>