<script setup lang="ts">
import { getTests } from "@/api/tests";
import { onMounted, ref } from "vue";
import tCard from "@/components/layouts/t-card";
import tGrid from "@/components/layouts/t-grid/t-grid.vue";
import tTest from "@/components/icons/t-test.vue";
import { router } from "..";

const isLoading = ref(false);
const tests = ref<Test[]>([]);

const uploadTests = async () => {
    isLoading.value = true;

    try {
        const { data } = await getTests();

        tests.value = data;
    } catch {
    } finally {
        isLoading.value = false;
    }
};

const onTest = (id: number) => {
    router.push({
        name: "test",
        params: {
            testId: id,
        },
    });
};

onMounted(async () => {
    uploadTests();
});

interface Test {
    id: number;
    name: string;
}
</script>

<template>
    <main class="mt-16">
        <div>
            <h1>Тесты</h1>
        </div>
        <p>Список достуных тестов</p>
        <t-grid class="list">
            <t-card
                v-for="test in tests"
                :key="test.id"
                class="test"
                :class="{ completed: test.id === 24 }"
                @click="onTest(test.id)"
            >
                <div class="title">
                    <t-test />
                    <h3>{{ test.name }}</h3>
                </div>
                <div class="status mt-2">
                    Статус: {{ test.id === 24 ? "Пройден" : "Не пройден" }}
                </div>
            </t-card>
        </t-grid>
    </main>
</template>

<style lang="scss" scoped>
.test {
    padding: 20px;
    outline: 1px solid #ffffff00;
    cursor: pointer;
    user-select: none;
    &:hover {
        outline: 1px solid var(--t-primary);
    }

    .title {
        color: var(--t-tertiary);
        display: flex;
        align-items: center;
        gap: 4px;

        svg {
            min-width: 24px;
            color: var(--t-primary);
        }

        h3 {
            padding-bottom: 0;
        }
    }

    .status {
        color: var(--t-secondary);
    }
}

.completed {
    outline: 1px solid var(--t-success);
    svg {
        color: var(--t-success) !important;
    }
}
</style>
