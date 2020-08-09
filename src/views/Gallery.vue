<template>
  <div class="page">
    <b-container class="bv-example-row" fluid>
      <b-row>
        <b-col cols="1"></b-col>
        <b-col cols="10">
          <div>
            <img :src="getUrl(user_data.profile_picture)" />
          </div>
        </b-col>
        <b-col cols="1"></b-col>
      </b-row>
      <b-row>
        <b-col cols="1"></b-col>
        <b-col cols="10">
          <div class="large-12 medium-12 small-12 cell">
            <label>
              File
              <input type="file" id="file" ref="file" v-on:change="handleFileUpload()" />
            </label>
            <button v-on:click="submitFile()">Submit</button>
          </div>
        </b-col>
        <b-col cols="1"></b-col>
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
    };
  },

  methods: {
    submitFile() {
      let formData = new FormData();
      formData.append("profile_picture", this.file);
      axios
        .patch("http://127.0.0.1:8000/api/user/picture", formData, {
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
    },
    handleFileUpload() {
      this.file = this.$refs.file.files[0];
    },
    getUserPicture() {
      axios
        .get("http://127.0.0.1:8000/api/user/picture", {
          headers: {
            Authorization: "Token " + localStorage.getItem("user-token"),
          },
        })
        .then((response) => {
          console.log(response), (this.user_data = response.data);
        })
        .catch((errors) => console.log(errors));
    },
    getUrl(pic) {
      return "http://127.0.0.1:8000" + pic;
    },
  },
  created() {
    this.getUserPicture();
  },
};
</script>