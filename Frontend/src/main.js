import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import router from './router'
import BootstrapVue from 'bootstrap-vue'

Vue.config.productionTip = false
Vue.use(BootstrapVue)

import "bootstrap/dist/css/bootstrap.css"
import "bootstrap-vue/dist/bootstrap-vue.css"
import vuetify from './plugins/vuetify';

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')