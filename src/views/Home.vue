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
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. In et aliquet purus, ut facilisis ante. Phasellus
            eros sem, hendrerit vel lobortis at, luctus sed orci. Curabitur consequat, tellus vitae posuere tincidunt,
            nisi libero lacinia mauris, vehicula facilisis velit magna eget leo. Mauris vitae odio quis leo faucibus
            gravida. Proin suscipit, elit in egestas rhoncus, orci ligula egestas elit, eget dictum purus tortor posuere
            justo. Sed laoreet, nisi et accumsan vulputate, lectus risus fermentum arcu, eget tincidunt leo magna eu
            augue. Vivamus luctus ut augue eget feugiat. Nullam mollis sapien purus, vitae ornare metus malesuada quis.
            Mauris pretium purus velit, non commodo eros pulvinar eget. In eu ligula nisl. Pellentesque ultrices lorem
            in luctus vulputate. Ut vestibulum porttitor vehicula. Suspendisse at scelerisque turpis. Aliquam venenatis
            quam id dui tincidunt, et pulvinar nibh vestibulum. Curabitur et lobortis massa, et fermentum diam.
          </div>
        </b-col>
        <b-col cols="5"></b-col>
        <b-col cols="3">
          <br />

          <div class="card text-black mb-3 rightside" style="width: 19rem;">
            <div class="card-body no-background">
              <br />
              <h3 class="card-title no-background">Nie masz konta?</h3>
              <br />
              <p class="card-text no-background">Dołącz do społeczności e-love zakładając darmowe konto!</p>
              <br />
              <a href="/register" class="btn-lg btn-warning">Zarejestruj się</a>
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
  name: 'Home',
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
  background-color: rgba(255, 255, 255, 0.3);
  padding: 20px;
  color: #812b3b;
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
  background-color: rgba(255, 255, 255, 0.3);
  padding: 20px;
  color: #812b3b;
  border-radius: 25px;
  border-style: solid;
  border-width: 1px;
  /*
  border-color: #a89172;
  background-color: #fdefddc0;
  box-shadow: 1px 1px #a89172;
  */
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
  text-shadow: 1px 1px #ff0202;
}
.card text-black bg-secondary mb-3 {
  background-color: rgba(255, 255, 255, 0.3);
  border-radius: 25px;
}
</style>
