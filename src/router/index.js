import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import Register from '../components/Register.vue'
import Profile from '../components/Profile.vue'
import Settings from '../components/Settings.vue'
import UsersList from '../components/UsersList.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/home',
    redirect: '/'
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
  },
  {
    path: '/settings',
    name: 'Settings',
    component: Settings
  },
  {
    path: '/users',
    name: 'Users',
    component: UsersList
  },
]

const router = new VueRouter({
  routes,
  mode: 'history'
})

export default router
