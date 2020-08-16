import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import Register from '../views/Register.vue'
import MainUser from '../views/MainUser.vue'
import Settings from '../views/Settings.vue'
import Search from '../views/Search.vue'
import Gallery from '../views/Gallery.vue'
import UserProfile from '../views/UserProfile.vue'
import Regulations from '../views/Regulations.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: {
      title: 'Home'
    }
  },
  {
    path: '/home',
    redirect: '/'
  },
  {
    path: '/about',
    name: 'About',
    component: About,
    meta: {
      title: 'O nas'
    }
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
    meta: {
      title: 'Rejestracja'
    }
  },
  {
    path: '/mainuser',
    name: 'MainUser',
    component: MainUser,
    meta: {
      title: 'Mój profil'
    }
  },
  {
    path: "/mainuser/settings",
    name: "Settings",
    component: Settings,
    meta: {
      title: 'Ustawienia'
    }
  },
  {
    path: "/mainuser/search",
    name: "search",
    component: Search,
    meta: {
      title: 'Wyszukiwanie'
    }
  }, 
  {
    path: '/mainuser/search/:username',
    name: 'userprofile',
    component: UserProfile,
    params: true
  }, 
  {
    path: '/mainuser/gallery',
    name: 'Gallery',
    component: Gallery,
    meta: {
      title: 'Galeria'
    }
  },
  {
    path: '/regulations',
    name: 'Regulations',
    component: Regulations,
    meta: {
      title: 'Regulamin'
    }
  },
]

const router = new VueRouter({
  routes,
  mode: 'history'
})


router.beforeEach((to, from, next) => {
  // LOGED OUT restrictions (not restricted: Home, Register, About)
  //to.name !== 'Home' && to.name !== 'Register' && to.name !== 'About'
  if (!['Home', 'Register', 'About', 'Regulations'].includes(to.name) && !localStorage.getItem("user-token")) {
    next({ name: 'Home' })
  }
  // LOGED IN restrictions
  else if (['Register'].includes(to.name) && localStorage.getItem("user-token")) {
    next({ name: 'mainuser' })
  }
  else {
    next()
  }
  // This goes through the matched routes from last to first, finding the closest route with a title.
  // eg. if we have /some/deep/nested/route and /some, /deep, and /nested have titles, nested's will be chosen.
  const nearestWithTitle = to.matched.slice().reverse().find(r => r.meta && r.meta.title);

  // Find the nearest route element with meta tags.
  const nearestWithMeta = to.matched.slice().reverse().find(r => r.meta && r.meta.metaTags);
  const previousNearestWithMeta = from.matched.slice().reverse().find(r => r.meta && r.meta.metaTags);

  // If a route with a title was found, set the document (page) title to that value.
  if (nearestWithTitle) document.title = nearestWithTitle.meta.title;

  // Remove any stale meta tags from the document using the key attribute we set below.
  Array.from(document.querySelectorAll('[data-vue-router-controlled]')).map(el => el.parentNode.removeChild(el));

  // Skip rendering meta tags if there are none.
  if (!nearestWithMeta) return next();

  // Turn the meta tag definitions into actual elements in the head.
  nearestWithMeta.meta.metaTags.map(tagDef => {
    const tag = document.createElement('meta');

    Object.keys(tagDef).forEach(key => {
      tag.setAttribute(key, tagDef[key]);
    });

    // We use this to track which meta tags we create, so we don't interfere with other ones.
    tag.setAttribute('data-vue-router-controlled', '');

    return tag;
  })
    // Add the meta tags to the document head.
    .forEach(tag => document.head.appendChild(tag));
})

export default router
