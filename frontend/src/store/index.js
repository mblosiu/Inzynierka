import Vue from "vue";
import Vuex from "vuex";
import Api from "../service/api";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    users: [],
    currentUser: { name: "storeTest" }

  },
  mutations: {
    SET_USERS(state, users) {
      state.users = users;
    },
    LOGOUT_USER(state) {
      state.currentUser = {}
      window.localStorage.currentUser = JSON.stringify({});
    },
    SET_CURRENT_USER(state, user) {
      state.currentUser = user;
      window.localStorage.currentUser = JSON.stringify(user);

    }
  },
  actions: {
    async loadUsers({ commit }) {
      let response = await Api().get('/account/users');
      let users = response.data.data;
      commit('SET_USERS', users.map(u => u.attributes));

      let user = JSON.parse(window.localStorage.currentUser);
      commit('SET_CURRENT_USER', user);
    },
    //async getUser({commit}){
    //  let response = await Api().post('account/users')
    //},
    logoutUser({ commit }) {
      commit('LOGOUT_USER')
    },
    async loginUser({ commit }, {username, password}) {
      console.log("kk");
      //try {
        let response = await Api().post('/account/login', {username, password});
        let token = response.data;
        let user = response//.data.attributes;
        //console.log(response)

        commit('SET_CURRENT_USER', token);
        return user;
      /*} catch {
        return {error: "Hasło bądź nazwa użytkownika zawiera błędy!"}
      }*/
    }
  },
  modules: {}
});
