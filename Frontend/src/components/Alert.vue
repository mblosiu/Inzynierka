<template>
  <div>
    <div v-if="alertStatus==OK">
      <b-alert
        :show="dismissCountDown"
        dismissible
        variant="success"
        @dismissed="dismissCountDown=0"
        @dismiss-count-down="countDownChanged"
      >{{msg}}</b-alert>
    </div>
    <div v-else-if="alertStatus==WARN">
      <b-alert
        :show="dismissCountDown"
        dismissible
        variant="warning"
        @dismissed="dismissCountDown=0"
        @dismiss-count-down="countDownChanged"
      >{{msg}}</b-alert>
    </div>
    <div v-else>
      <b-alert
        :show="dismissCountDown"
        dismissible
        variant="danger"
        @dismissed="dismissCountDown=0"
        @dismiss-count-down="countDownChanged"
      >{{msg}}</b-alert>
    </div>
  </div>
</template>

<script>
export default {
  name: "Alert",
  components: {},
  data() {
    return {
      dismissSecs: 5,
      dismissCountDown: 0,
      props: [msg],
      props: [alertStatus]
    };
  },
  methods: {
    countDownChanged(dismissCountDown) {
      this.dismissCountDown = dismissCountDown;
    },
    showAlert() {
      this.dismissCountDown = this.dismissSecs;
    },
  },
};
</script>