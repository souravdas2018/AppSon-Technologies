// import { createRouter, createWebHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'

// const router = createRouter({
//   history: createWebHistory(import.meta.env.BASE_URL),
//   routes: [
//     {
//       path: '/',
//       name: 'home',
//       component: HomeView,
//     },
//     {
//       path: '/about',
//       name: 'about',
//       // route level code-splitting
//       // this generates a separate chunk (About.[hash].js) for this route
//       // which is lazy-loaded when the route is visited.
//       component: () => import('../views/AboutView.vue'),
//     },
//   ],
// })

// export default router


import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import CoursePage from '@/views/CoursePage.vue'
import ReportPage from '@/views/ReportPage.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/courses', name: 'Courses', component: CoursePage },
  { path: '/report', name: 'Report', component: ReportPage }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router


