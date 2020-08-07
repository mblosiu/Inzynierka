<template>
  <div class="container">
    <div class="large-12 medium-12 small-12 cell">
      <label>
        File
        <input type="file" id="file" ref="file" v-on:change="handleFileUpload()" />
      </label>
      <button v-on:click="submitFile()">Submit</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      file: "",
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
  },
};
</script>