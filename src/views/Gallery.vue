<template>
  <v-container>
    <v-row>
      
      <v-toolbar color="purple" fixed>
        <v-icon color="white" class="mr-3" x-large>mdi-image-plus</v-icon>
        <v-toolbar-title class="white--text">Galeria</v-toolbar-title>
        <v-spacer></v-spacer>

        <div class="fileupload">
          <label>
            <input
              type="file"
              id="file"
              ref="file"
              v-on:change="handleFileUpload()"
            />
          </label>
          <v-btn
            class="ml-2"
            color="purple lighten-2"
            dense
            v-on:click="submitFile()"
          >
            <button bold class="white--text">Wyślij</button>
          </v-btn>
        </div>
        <v-icon
          color="white"
          class="ml-3"
          x-large
          data-toggle="tooltip"
          data-placement="bottom"
          title="Z racji problemów z obsługą większych zdjęć, prosimy o wybieranie plików o niedużych wymiarach (najlepiej do ok 800x600)"
          >mdi-alert-circle-outline</v-icon
        >
      </v-toolbar>
      
    </v-row>
    <v-row class="scroll">
      <v-col cols="1"></v-col>
      <br />
      <v-col cols="10">
        <v-row v-for="i in Math.ceil(images.length / 4)" v-bind:key="i">
          <v-col
            cols="3"
            v-for="image in images.slice((i - 1) * 4, i * 4)"
            v-bind:key="image.id"
            style="padding-bottom: 2px"
          >
            <v-card outlined rounded class="mx-auto" color="purple">
              <v-img
                aspect-ratio="1"
                class="white--text align-end"
                :src="getUrl(image.image)"
                alt="image"
                @click="showModal(image.image)"
              >
                <v-app-bar flat color="rgba(0, 0, 0, 0)">
                  <v-menu
                    v-model="menu"
                    :close-on-content-click="false"
                    :nudge-width="100"
                    offset-x
                    left
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-btn fab x-small class="purple" v-bind="attrs" v-on="on"
                        ><v-app-bar-nav-icon
                          x-small
                          color="white"
                        ></v-app-bar-nav-icon
                      ></v-btn>
                    </template>

                    <v-card>
                      <v-list>
                        <v-list-item>
                          <v-btn
                            icon
                            x-large
                            v-b-toggle.sidebar-footer
                            data-toggle="tooltip"
                            data-placement="bottom"
                            title="Ustaw jako profilowe"
                            v-on:click="setAsProfilePic(image.image)"
                          >
                            <v-icon color="purple"
                              >mdi-account-box-outline</v-icon
                            >
                          </v-btn>
                          <v-divider vertical></v-divider>
                          <v-btn
                            icon
                            x-large
                            v-b-toggle.sidebar-footer
                            data-toggle="tooltip"
                            data-placement="bottom"
                            title="Usuń zdjęcie"
                            v-on:click="deleteImage(image.pk)"
                          >
                            <v-icon color="purple"
                              >mdi-image-remove</v-icon
                            ></v-btn
                          >
                        </v-list-item>
                      </v-list>
                    </v-card>
                  </v-menu>
                </v-app-bar>
              </v-img>
            </v-card>
            <b-modal
              :ref="'modal' + image.image"
              hide-footer
              title="Podgląd zdjęcia"
              size="lg"
            >
              <div class="d-block text-center"></div>
              <img
                :src="getUrl(image.image)"
                class="img-responsive rounded mx-auto d-block"
                alt="image"
                style="width: 100%; height: 100%"
              />
              <br />
            </b-modal>
          </v-col>
        </v-row>
      </v-col>

      <v-col cols="1"></v-col>
    </v-row>
  </v-container>
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

    submitFile() {
      let formData = new FormData();
      formData.append("image", this.file);
      axios
        .post("https://elove.ml:8000/api/user/images", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
            Authorization: "Token " + localStorage.getItem("user-token"),
          },
        })
        .then((response) => {
          this.$router.go();
        })
        .catch((errors) => console.log(errors));
    },
    handleFileUpload() {
      this.file = this.$refs.file.files[0];
    },
    getUserImages() {
      axios
        .get("https://elove.ml:8000/api/user/images", {
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
        .delete("https://elove.ml:8000/api/user/images", {
          data: { pk: pk },
          headers: {
            Authorization: "Token " + localStorage.getItem("user-token"),
          },
        })
        .then((response) => {
          console.log(response), (this.images = response.data), this.$router.go();
        })
        .catch((errors) => console.log(errors));
    },
    setAsProfilePic(pic) {
      let config = {
        headers: {
          Authorization: "Token " + localStorage.getItem("user-token"),
        },
      };
      axios
        .patch(
          "https://elove.ml:8000/api/user/profile-image",
          {
            profile_picture: pic,
          },
          config
        )
        .then((response) => {
          console.log(response);
          if (response.status == 200) {
            this.toast(
              "b-toaster-bottom-right",
              "success",
              "Zaktualizowano zdjęcie profilowe!"
            );
          }
        })
        .catch((errors) => console.log(errors));
    },
    getUrl(pic) {
      if (pic != null) return "https://elove.ml" + pic;
      else return null;
    },
    getUserPicture() {
      axios
        .get("https://elove.ml:8000/api/user/profile-picture", {
          headers: {
            Authorization: "Token " + localStorage.getItem("user-token"),
          },
        })
        .then((response) => {
          console.log(response), (this.user_data = response.data);
        })
        .catch((errors) => console.log(errors));
    },
    toast(toaster, variant = null, msg) {
      this.$bvToast.toast(msg, {
        title: `Info`,
        toaster: toaster,
        solid: true,
        variant: variant,
      });
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
  background: rgba(128, 0, 128, 0.199);
}
.alert {
  margin-left: 30px;
  align-content: center;
  width: 274px;
}
.card-body {
  background: #c02e2e;
  color: white;
  border-style: solid;
  border-width: 2px;
  border-color: #aa1d37;
}
.card-header {
  background: #ad1b1b;
  color: white;
  border-style: solid;
  border-width: 2px;
  border-color: #aa1d37;
}
</style>
