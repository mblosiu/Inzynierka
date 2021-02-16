<template>
  <v-container fluid>
    <div v-for="i in 12"><br /></div>

    <v-dialog v-model="verificationDialog" persistent max-width="400">
      <v-container>
        <v-card color="purple lighten-5">
          <v-card-title flex class="purple">
            <v-spacer></v-spacer>
            <div v-if="verificationStatus == true">
              <span class="headline white--text">Udało się!</span>
            </div>
            <div v-else>
              <span class="headline white--text">Coś poszło nie tak.</span>
            </div>
            <v-spacer></v-spacer>
          </v-card-title>
          <br />

          <v-row>
            <v-spacer></v-spacer>
            <div v-if="verificationStatus == true">
              <v-card-text class="text--primary">
                Twoje konto zostało pomyślnie zweryfikowane.
                <br />
              </v-card-text>
            </div>
            <div v-else>
              <v-card-text class="text--primary">
                Wystąpił błąd podczas weryfikacji konta.
              </v-card-text>
            </div>
            <v-spacer></v-spacer>
          </v-row>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="purple" text outlined @click="$router.push('/home')">
              Powrót na stronę główną
            </v-btn>
            <v-spacer></v-spacer>
          </v-card-actions>
          <br />
        </v-card>
      </v-container>
    </v-dialog>

    <v-row> </v-row>
    <v-row> </v-row>
    <div v-for="i in 12"><br /></div>
  </v-container>
</template>

<script>
// @ is an alias to /src
//import Register from "@/views/Register.vue";
import axios from "axios";

export default {
  name: "Verification",
  components: {
    //Register,
  },
  data() {
    return {
      code: "",
      verificationDialog: false,
      verificationStatus: "",
    };
  },
  methods: {
    //http://46.101.213.106:8000/api/user/register
    getVerificationCode() {
      this.code = this.$route.fullPath.slice(13);
      //console.log(this.$route.fullPath);
      //console.log("code");
      console.log(this.code);
      //this.verificationDialog = true;
    },
    verifyAccount() {
      this.getVerificationCode();
      axios
        .patch("https://elove.ml:8000/api/user/account-verify", {
          verify_code: this.code,
        })
        .then((response) => {
          console.log(response);
          this.verificationStatus = true;
          this.verificationDialog = true;
        })
        .catch((errors) => {
          console.log(errors);
          this.verificationStatus = false;
          this.verificationDialog = true;
        });
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
  mounted() {
    //this.getVerificationCode();
    this.verifyAccount();
  },
};
</script>

<style>
.v-card__text,
.v-card__title {
  word-break: normal; /* maybe !important  */
}
</style>