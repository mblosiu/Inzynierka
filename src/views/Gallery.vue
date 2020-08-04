<template>
  <div id="gallery">
    <br />
    <b-container class="bv-example-row" fluid>
      <b-row>
        <b-col cols="3">
          <div v-if="user_data.profile_picture!=null">
            <h5>Twoje aktualne zdjęcie profilowe.</h5>
            <div class="text-center">
              <img :src="user_data.profile_picture" class="rounded" />
              {{user_data.profile_picture}}
            </div>
            <br />
            <div class="card" style="width: 21rem;">
              <img class="card-img-top" src="../../public/img/add-image-icon2.png" alt="Card image cap" />
              <div class="card-body">
                <h5 class="card-title">Dodaj zdjęcie.</h5>
                <form @submit.prevent="editUserData" enctype="multipart/form-data">

                  <div class="field">
                    <label for="file" class="label"> Wybierz zdjęcie </label>
                    
                    <input
                      type="file"
                      ref="file"
                      @change="selectFile"
                      class="form-control"
                      />
                  </div>

                  <div class="field">
                    <button class="button is-info"> Wyślij </button>
                  </div>

                </form>
              </div>
            </div>
          </div>
          <div v-else>
            <h6>Brak zdjęcia profilowego. Wybierz ze swojej galerii lub prześlij nowe!</h6>
            <button @click="showPic"> showPic </button>
            <br />
            <div class="card" style="width: 21rem;">
              <img class="card-img-top" src="../../public/img/add-image-icon2.png" alt="Card image cap" />
              <div class="card-body">
                <h5 class="card-title">Dodaj nowe zdjęcie.</h5>
                <br/>
                <input type="file" accept="image/*" @change="onFileSelected">
                <button @click="onUpload"> Wyślij </button>
                <!--<form @submit.prevent="editUserData" enctype="multipart/form-data">

                  <div class="field">
                    <label for="profile_picture" class="label"> Wybierz zdjęcie </label>
                    <input
                      type="file"
                      ref="file"
                      @change="selectFile"
                      />
                  </div>

                  <div class="field">
                    <button class="button is-info"> Wyślij </button>
                  </div>

                </form>-->
              </div>
            </div>
          </div>
        </b-col>
        <b-col cols="9">
              <h1>Moje zdjęcia</h1>
          <br />
          <h4>Brak zdjęć.</h4>
          <!--<div v-if="user_data.user_galerry!=null">

          </div>
          <div v-else>

          </div>-->
        </b-col>
        <!--<b-col cols="1"></b-col>-->
      </b-row>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "Gallery",
  data() {
    return {
      user_data: {},
      selectedFile: null,
    };
  },
  methods: {
    /*selectFile() {
      this.file=this.$refs.file.files[0];
    },*/
    showPic(){
      console.log(this.user_data.profile_picture)
    },
    onFileSelected(event){
      this.selectedFile = event.target.files[0]
    },
    onUpload(){
      const fd = new FormData();
      fd.append('image', this.selectedFile, this.selectedFile.name)
      let config = {
        headers: {
          Authorization: "Token " + localStorage.getItem("user-token"),
        },
      };
      axios
        .patch(
          "http://127.0.0.1:8000/api/user/properties",
          {
            profile_picture: fd
          },
          config
        )
        .then((response) => {
          console.log(response);
          console.log(this.selectedFile)
        })
        .catch((errors) => console.log(errors));
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
  },
  created() {
    this.getUserData();
  },
};
</script>

<style>

.card-img-top{
  height: 300px;
  width: 100px;
}
</style>