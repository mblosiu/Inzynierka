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


router.beforeEach((to, from, next) => {
  // LOGED OUT restrictions (not restricted: Home, Register, About)
  //to.name !== 'Home' && to.name !== 'Register' && to.name !== 'About'
  if (!['Home', 'Register', 'About'].includes(to.name) && !localStorage.getItem("user-token")) {
    next({ name: 'Home' })
  }
  // LOGED IN restrictions
  else if (['Register'].includes(to.name) && localStorage.getItem("user-token")) {
    next({ name: 'Home' })
  }
  else {
    next()
  }
})

export default router
