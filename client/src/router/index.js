import { createRouter, /*createWebHistory,*/ createWebHashHistory } from 'vue-router'
import IRTableView from '../views/IRTableView.vue'

const router = createRouter({
  // history: createWebHistory(import.meta.env.BASE_URL),
  history: createWebHashHistory(),
  routes: [
    {
      path: '/irtable',
      name: 'irtable',
      component: IRTableView
    }
  ]
})

export default router
