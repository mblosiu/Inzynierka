<template>
  <div class="page">
    <b-container class="bv-example-row" fluid>
      <b-row flex>
        <b-col cols="2">
          <b-row>
            <b-col cols="5"></b-col>
            <b-col cols="4">
              <h1 class="display-4">Galeria</h1>
            </b-col>
            <b-col cols="3"></b-col>
            <br />
          </b-row>
          <b-row>
            <b-col cols="12">
              <br />
            </b-col>
          </b-row>
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

          <b-alert
            :show="dismissCountDown"
            fade
            variant="success"
            @dismissed="dismissCountDown=0"
            @dismiss-count-down="countDownChanged"
          >{{msg}}</b-alert>
        </b-col>
        <b-col cols="1"></b-col>
        <b-col cols="9" align-self="start" class="scroll">
          <b-row v-for="i in Math.ceil(images.length / 2)" v-bind:key="i">
            <b-col cols="1"></b-col>
            <b-col
              cols="5"
              v-for="image in images.slice((i - 1) * 2, i * 2)"
              v-bind:key="image.id"
              style="padding-bottom:2px;"
            >
              <div class="card bg-secondary mb-3" style="width: 377px; height: 285px">
                <img
                  :src="getUrl(image.image)"
                  class="img-responsive rounded mx-auto d-block"
                  alt="image"
                  @click="showModal(i)"
                />

                <b-modal :ref="'modal' + i" hide-footer title="Podgląd zdjęcia" size="lg">
                  <div class="d-block text-center">
                  </div>
                  <img
                    :src="getUrl(image.image)"
                    class="img-responsive rounded mx-auto d-block"
                    alt="image"
                    style="width:100%; height:100%"
                  />
                  <br/>
                </b-modal>
                <div class="card-body">
                  <p>
                    <button
                      type="button"
                      class="btn btn-primary"
                      v-on:click="setAsProfilePic(image.image)"
                    >Ustaw jako profilowe</button>

                    <button
                      type="button"
                      class="btn btn-danger ml-2"
                      v-on:click="deleteImage(image.pk)"
                    >Usuń zdjęcie</button>
                  </p>
                </div>
              </div>
            </b-col>
          </b-row>
        </b-col>

        <b-col cols="1"></b-col>
      </b-row>
      <b-row>
        <b-col cols="12">
          <p></p>
        </b-col>
      </b-row>
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
      msg: "",
      dismissSecs: 5,
      dismissCountDown: 0,
      //id: "",
    };
  },

  methods: {
    modalId(i) {
      return "modal" + i;
    },
    showModal(i) {
      console.log(this.$refs["modal" + i][0]);
      this.$refs["modal" + i][0].show();
    },
    hideModal(i) {
      this.$refs["modal" + i][0].hide();
    },
    countDownChanged(dismissCountDown) {
      this.dismissCountDown = dismissCountDown;
    },
    showMsg() {
      this.dismissCountDown = this.dismissSecs;
    },
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
          console.log(response.data);
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
          if (response.status == 200) {
            this.showMsg(), (this.msg = "Zmieniono zdjęcie profilowe.");
          }
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
.scroll {
  height: 100%;
  overflow-y: scroll;
  height: 100vh;
}
.alert {
  margin-left: 40px;
  align-content: center;
  width: 274px;
}
</style>
