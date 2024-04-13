<script setup lang="ts">
import tCard from "@/components/layouts/t-card";
import tButton from "@/components/atoms/t-button";
import tLogo from "@/components/icons/t-logo.vue";

import { getToken } from "@/api/auth";
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();

const isLoading = ref(false);
const login = ref("");
const password = ref("");

const onSubmit = async () => {
    isLoading.value = true;
    try {
        const { data } = await getToken({
            username: login.value,
            password: password.value,
        });

        localStorage.setItem("access_token", data.access);

        router.push({
            name: "home",
        });
    } catch {
    } finally {
        isLoading.value = false;
    }
};
</script>

<template>
    <main class="mt-16">
        <t-card>
            <t-logo class="logo mb-2" />

            <h1>Вход</h1>
            <p>Данные для доступа предоставляются администратором портала.</p>
            <form class="form" @submit.prevent="onSubmit">
                <input
                    v-model="login"
                    class="input"
                    :class="{ 'm-disabled': isLoading }"
                    placeholder="Введите логин"
                    :disabled="isLoading"
                    type="text"
                />

                <input
                    v-model="password"
                    class="input"
                    :class="{ 'm-disabled': isLoading }"
                    placeholder="Введите пароль"
                    :disabled="isLoading"
                    type="password"
                />

                <div class="mb-8">
                    <t-button :disabled="isLoading" block>Войти</t-button>
                </div>
            </form>
        </t-card>
    </main>
</template>

<style lang="scss" scoped>
.form {
    display: flex;
    flex-direction: column;
    gap: 16px;
}

.m-disabled {
    opacity: 0.5;
    pointer-events: none;
}

.input {
    all: unset;
    padding: 16px 16px;
    border-radius: 10px;
    background-color: var(--t-surface);
    border: 1px solid var(--t-primary);
    transition: all 0.2s ease;
    &:focus {
        -webkit-box-shadow: 0px 6px 19px -8px rgba(34, 60, 80, 0.2);
        -moz-box-shadow: 0px 6px 19px -8px rgba(34, 60, 80, 0.2);
        box-shadow: 0px 6px 19px -8px rgba(34, 60, 80, 0.2);
    }
}

.logo {
    color: var(--t-primary);
}
</style>
