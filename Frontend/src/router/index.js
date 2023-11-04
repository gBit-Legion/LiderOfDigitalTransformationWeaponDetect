import { createRouter, createWebHashHistory } from "vue-router";
import VideoDet from "../components/VideoDet.vue";

const routes = [
  {
    path: "/",
    name: "home",

    component: () => import("../views/MainPage.vue"),
  },
  { path: '/videodet', component: VideoDet },
  
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
