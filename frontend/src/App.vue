<script setup lang="ts">
import tContainer from "./shared/ui/layouts/t-container";
import tLogout from "./shared/ui/icons/t-logout.vue";
import tDoc from "./shared/ui/icons/t-doc.vue";
import tColor from "./shared/ui/icons/t-color.vue";

import { useRouter } from "vue-router";
import { themes, themeNames } from "./themes";
import { onMounted, ref, watch } from "vue";

const router = useRouter();
const theme = ref(themeNames.DARK);

const onSignOut = () => {
  localStorage.removeItem("access_token");
  localStorage.removeItem("refresh_token");

  router.push({
    name: "login"
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

watch(theme, value => setTheme(value));

onMounted(() => {
  setTheme(theme.value);
});
</script>

<template>
  <div class="nav">
    <t-container class="nav-container">
      <div class="wrap">
        <button class="btn" @click="onSignOut">
          <t-logout />
        </button>
        <button class="btn" @click="onSignOut">
          <t-doc />
        </button>
        <button class="btn" @click="toggleTheme">
          <t-color />
        </button>
      </div>
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

  .wrap {
    display: flex;
    gap: 0 0.5rem;
    .btn {
      border-radius: 8px;
      width: 30px;
      height: 30px;
      display: flex;
      align-items: center;
      justify-content: center;
      background-color: #00000000;
      transition: all 0.3s ease;
      outline: 1px solid color-mix(in srgb, var(--t-secondary) 10%, transparent);
      &:hover {
        background-color: color-mix(
          in srgb,
          var(--t-secondary) 10%,
          transparent
        );
      }
    }
  }
}
</style>
