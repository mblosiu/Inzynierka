<template>
  <div class="footer">
    <div class="container">
      <br />
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
      <br />
      <div class="row">
        <div class="col-sm"></div>
        <div class="col-sm">
          <center>©{{ new Date().getFullYear() }}</center>
        </div>
        <div class="col-sm"></div>
      </div>
      <br />
    </div>
  </div>
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
