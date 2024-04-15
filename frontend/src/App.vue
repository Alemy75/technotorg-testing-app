<script setup lang="ts">
import tContainer from "./components/layouts/t-container";
import { useRouter } from "vue-router";
import tLogout from "./components/icons/t-logout.vue";
import tDoc from "./components/icons/t-doc.vue";
import { themes, themeNames } from "./themes";
import { onMounted, ref, watch } from "vue";

const router = useRouter();
const theme = ref(themeNames.DARK);

const onSignOut = () => {
    localStorage.removeItem("access_token");

    router.push({
        name: "login",
    });
};

const toggleTheme = () => {
    if (theme.value == themeNames.LIGHT) {
        theme.value = themeNames.DARK;
    } else {
        theme.value = themeNames.LIGHT;
    }
};

const setTheme = (value: string) => {
    Object.entries(themes[value]).forEach(([key, value]) => {
        document.body.style.setProperty(key, value);
    });
};

watch(theme, (value) => setTheme(value));

onMounted(() => {
    setTheme(theme.value);
});
</script>

<template>
    <div class="nav">
        <t-container class="nav-container">
            <div>
                <button @click="onSignOut">
                    <t-logout />
                </button>
                <button class="ml-2" @click="onSignOut">
                    <t-doc />
                </button>
            </div>
            <button @click="toggleTheme">Сменить тему</button>
        </t-container>
    </div>

    <t-container>
        <router-view></router-view>
    </t-container>
</template>

<style lang="scss" scoped>
.logo {
    color: var(--t-primary);
}

.nav {
    padding: 1rem 0;
    background-color: var(--t-surface);
    box-shadow: 0px 6px 33px -3px rgba(75, 75, 75, 0.096);
    .nav-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
}
</style>
