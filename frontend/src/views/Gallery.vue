<template>
  <div id="gallery">
    <br />
    <h1>Moje zdjęcia</h1>
    <br />
    <b-container class="bv-example-row" fluid>
      <b-row>
        <b-col cols="1"></b-col>
        <b-col cols="10">
          Dodaj zdjęcie: <input type="file" @change="selectFile"> <button @click="upload">Wrzuć</button>
          <br />
          {{image}}
        </b-col>
        <b-col cols="1"></b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>

//import axios from "axios";

export default {
  name: "Gallery",
  data() {
    return {
      image: null
    }
  },
  methods: {
      selectFile(event) {
          this.image = event.target.files[0]
      },
      uploadFile(){
          const fd = new FormData();
          fd.append('image', this.image, this.image.name)
          /*axios.post('http://127.0.0.1:8000/api/')*/
          
      }
     
  }
};
</script>

<style>
</style>