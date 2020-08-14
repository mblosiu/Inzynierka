<template>
  <div class="home">
    <b-container class="bv-example-row" fluid>
      <b-row>
        <b-col cols="3"></b-col>
        <b-col cols="5">
          <h1>Witamy w e-love!</h1>
        </b-col>
        <b-col cols="4"></b-col>
      </b-row>
      <br />
      <b-row>
        <b-col cols="3">
          <h5>Tu znajdziesz swoją drugą połówkę.</h5>
          <br/>
          <div class="row justify-content-start">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. In et aliquet purus, ut facilisis ante. Phasellus eros sem, hendrerit vel lobortis at, luctus sed orci. Curabitur consequat, tellus vitae posuere tincidunt, nisi libero lacinia mauris, vehicula facilisis velit magna eget leo. Mauris vitae odio quis leo faucibus gravida. Proin suscipit, elit in egestas rhoncus, orci ligula egestas elit, eget dictum purus tortor posuere justo. Sed laoreet, nisi et accumsan vulputate, lectus risus fermentum arcu, eget tincidunt leo magna eu augue. Vivamus luctus ut augue eget feugiat. Nullam mollis sapien purus, vitae ornare metus malesuada quis. Mauris pretium purus velit, non commodo eros pulvinar eget. In eu ligula nisl. Pellentesque ultrices lorem in luctus vulputate. Ut vestibulum porttitor vehicula. Suspendisse at scelerisque turpis. Aliquam venenatis quam id dui tincidunt, et pulvinar nibh vestibulum. Curabitur et lobortis massa, et fermentum diam. 
          </div>
        </b-col>
        <b-col cols="6"></b-col>
        <b-col cols="3">
          <br/>
          <br/>
          <div class="card text-black bg-secondary mb-3" style="width: 19rem;">
            <div class="card-body">
              <br/>
              <h3 class="card-title">Nie masz konta?</h3>
              <br/>
              <p
                class="card-text"
              >Dołącz do społeczności e-love zakładając darmowe konto!</p>
              <br/>
              <a href="/register" class="btn btn-outline-warning">Zarejestruj się</a>
              <br/>
            </div>
            <br/>
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
text{
  text-align: left;
}
</style>