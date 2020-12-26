<template>
 
    
    <v-footer
    color="purple"
    padless
    class="white--text"
  >
    
      <div class="container">
      
      <div class="row">
        <div class="col-sm">
          <a href="/about">O nas</a>
        </div>
        <div class="col-sm">
          <a href="/kontakt">Kontakt</a>
        </div>
        <div class="col-sm">
          <a href="/regulations">Regulamin</a>
        </div>
      </div>
      
      
    </div>

      <v-card-text class="py-2 white--text text-center">
        {{ new Date().getFullYear() }} — <strong>Vuetify</strong>
      </v-card-text>
    
  
  </v-footer>
  
</template>

<script>
export default {
  name: 'Footer',
  components: {},
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
