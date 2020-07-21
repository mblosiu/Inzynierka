import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import MainUser from "../views/MainUser.vue"
import Gallery from "../views/Gallery.vue"
import Search from "../views/Search.vue"
import Settings from "../views/Settings.vue"

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home/*,
    beforeEnter( to, from, next){
      let currentUser = JSON.parse(window.localStorage.currentUser);
      if(currentUser!={}){
        console.log("zalogowany")
        next('/mainuser'); 
      } else {
        console.log("brakusera")
        next('/');
      }
    }*/
  },
  {
    path: "/login",
    name: "login",
    component: Login
  },
  {
    path: "/register",
    name: "register",
    component: Register
  },
  {
    path: "/mainuser",
    name: "mainuser",
    component: MainUser
  },
  {
    path: "/mainuser/search",
    name: "search",
    component: Search
  },
  {
    path: "/mainuser/gallery",
    name: "gallery",
    component: Gallery
    /*beforeEnter( to, from, next){
      let currentUser = JSON.parse(window.localStorage.currentUser);
      if(currentUser!={}){
        console.log("zalogowany")
        next(); 
      } else {
        console.log("brakusera")
        next('/');
      }*/
    
  },
  {
    path: "/mainuser/settings",
    name: "Settings",
    component: Settings
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
