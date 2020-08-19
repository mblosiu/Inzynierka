<template>
  <div class="page">
    <b-container class="bv-example-row" fluid>
      <b-row>
        <b-col cols="2">
          <div class="card text-white bg-secondary mb-5" style="width: 22rem; height: 20rem">
            <div class="card-body">
              <img
                class="card-img-top"
                src="../../public/img/add-image-icon.png"
                alt="Card image cap"
                style="width: 11rem; height: 11rem"
              />
              <h5 class="card-title">Dodaj nowe zdjęcie.</h5>
              <div class="large-12 medium-12 small-12 cell">
                <label>
                  <input type="file" id="file" ref="file" v-on:change="handleFileUpload()" />
                </label>
                <button type="button" class="btn btn-success" v-on:click="submitFile()">Wyślij</button>
              </div>
            </div>
          </div>
        </b-col>
        <b-col cols="1"></b-col>
        <b-col cols="9" align-self="start">
          <b-row v-for="i in Math.ceil(images.length / 2)" v-bind:key="i">
            <b-col cols="1"></b-col>
            <b-col
              cols="5"
              v-for="image in images.slice((i - 1) * 2, i * 2)"
              v-bind:key="image.id"
              style="padding-bottom:1cm;"
            >
              <img :src="getUrl(image.image)" class="img-responsive" alt="image" />
              <p>
                <button
                  type="button"
                  class="btn btn-primary"
                  v-on:click="setAsProfilePic(image.image)"
                >Ustaw jako profilowe</button>
                <button
                  type="button"
                  class="btn btn-danger"
                  v-on:click="deleteImage(image.pk)"
                >Usuń zdjęcie</button>
              </p>
            </b-col>
          </b-row>
        </b-col>
        <b-col cols="1"></b-col>
      </b-row>
<!--
      <b-row v-for="i in Math.ceil(images.length / 2)" v-bind:key="i">
        <b-col cols="1"></b-col>
        <b-col
          cols="5"
          v-for="image in images.slice((i - 1) * 2, i * 2)"
          v-bind:key="image.id"
          style="padding-bottom:1cm;"
        >
          <img :src="getUrl(image.image)" class="img-responsive" alt="image" />
          <p>
            <button
              type="button"
              class="btn btn-primary"
              v-on:click="setAsProfilePic(image.image)"
            >Ustaw jako profilowe</button>
            <button
              type="button"
              class="btn btn-danger"
              v-on:click="deleteImage(image.pk)"
            >Usuń zdjęcie</button>
          </p>
        </b-col>
        <b-col cols="1"></b-col>
      </b-row>
      -->
    </b-container>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      file: "",
      user_data: {},
      images: [],
    };
  },

  methods: {
    submitFile() {
      let formData = new FormData();
      formData.append("image", this.file);
      axios
        .put("http://127.0.0.1:8000/api/user/images", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
            Authorization: "Token " + localStorage.getItem("user-token"),
          },
        })
        .then(function () {
          console.log("SUCCESS!!");
        })
        .catch(function () {
          console.log("FAILURE!!");
        });
      this.$router.go();
    },
    handleFileUpload() {
      this.file = this.$refs.file.files[0];
    },
    getUserImages() {
      axios
        .get("http://127.0.0.1:8000/api/user/images", {
          headers: {
            Authorization: "Token " + localStorage.getItem("user-token"),
          },
        })
        .then((response) => {
          console.log(response), (this.images = response.data);
        })
        .catch((errors) => console.log(errors));
    },
    deleteImage(pk) {
      axios
        .delete("http://127.0.0.1:8000/api/user/images", {
          data: { pk: pk },
          headers: {
            Authorization: "Token " + localStorage.getItem("user-token"),
          },
        })
        .then((response) => {
          console.log(response), (this.images = response.data);
        })
        .catch((errors) => console.log(errors));
      this.$router.go();
    },
    setAsProfilePic(pic) {
      let config = {
        headers: {
          Authorization: "Token " + localStorage.getItem("user-token"),
        },
      };
      axios
        .patch(
          "http://127.0.0.1:8000/api/user/profile-image",
          {
            profile_picture: pic,
          },
          config
        )
        .then((response) => {
          console.log(response);
        })
        .catch((errors) => console.log(errors));
    },
    getUrl(pic) {
      if (pic != null) return "http://127.0.0.1:8000" + pic;
      else return null;
    },
    getUserPicture() {
      axios
        .get("http://127.0.0.1:8000/api/user/profile-picture", {
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
    this.getUserImages();
  },
};
</script>

<style scoped>
.img-responsive {
  width: 375px;
  height: 207px;
  object-fit: cover;
}
.card {
  /*width: 500px;
  height:276px;
  object-fit: cover;*/
}
</style>
