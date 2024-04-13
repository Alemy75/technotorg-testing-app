import { createWebHistory, createRouter } from "vue-router";

const routes = [
    {
        path: "/login",
        name: "login",
        component: () => import(/* webpackChunkName: "login" */ "./login"),
    },
    {
        path: "/",
        name: "home",
        component: () => import(/* webpackChunkName: "home" */ "./home"),
        meta: {
            auth: true,
        },
    },
    {
        path: "/test/:testId",
        name: "test",
        component: () => import(/* webpackChunkName: "home" */ "./test"),
        meta: {
            auth: true,
        },
    },
];

export const router = createRouter({
    history: createWebHistory(),
    routes,
});

router.beforeEach((to, _, next) => {
    if (to.meta.auth && !localStorage.getItem("access_token")) {
        next({
            path: "/login",
            query: { redirect: to.fullPath },
        });
    } else {
        next();
    }
});
