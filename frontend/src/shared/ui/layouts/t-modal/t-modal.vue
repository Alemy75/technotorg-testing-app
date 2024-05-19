<template>
  <div v-if="isVisible" class="t-modal" :class="{ 'm-show': show }">
    <div class="content">
      <h3 class="mb-2">По каким тестам необходимо сформировать отчёт?</h3>

      <div v-if="tests.length" class="b-tests mb-4">
        <div v-for="test in tests" class="e-test">
          <input
            class="custom-checkbox"
            :id="test.id.toString()"
            type="checkbox"
            :value="test.id"
            @change="onCheck"
          />

          <label :for="test.id.toString()">{{ test.name }}</label>
        </div>
      </div>

      <div class="actions">
        <t-button @click="close">Закрыть</t-button>

        <t-button @click="onExportDocx" :disabled="!checkedTests.length"
          >Выгрузить отчет</t-button
        >
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { getTests } from "@/entities/tests";
import {
  ref,
  onMounted,
  defineProps,
  defineEmits,
  toRefs,
  watch,
  toRaw
} from "vue";
import { useSnackbar } from "@/shared/snackbar";
import { exportDocx } from "@/features/export-docx";

import tButton from "@/shared/ui/atoms/t-button/t-button.vue";

const tests = ref<Test[]>([]);
const snackbar = useSnackbar();
const isLoading = ref(false);
const props = defineProps<{
  isVisible: boolean;
}>();
const emit = defineEmits<{
  (event: "close"): void;
}>();

const { isVisible } = toRefs(props);
const show = ref(false);
const checkedTests = ref<number[]>([]);

const onExportDocx = async () => {
  try {
    const { data } = await exportDocx(checkedTests.value);

    const url = window.URL.createObjectURL(new Blob([data]));
    const link = document.createElement("a");
    link.href = url;
    link.setAttribute(
      "download",
      `Отчет_за_${new Date().toLocaleDateString()}.docx`
    ); // указываем имя файла для скачивания
    document.body.appendChild(link);
    link.click();
    link.parentNode?.removeChild(link);

    snackbar.show({
      type: "success",
      message: "Отчет сформирован успешно!",
      timeout: 2000
    });
  } catch {
    snackbar.show({
      type: "danger",
      message: "Ошибка формирования отчета! Повторите попытку позже.",
      timeout: 2000
    });
  }
};

const onCheck = (event: Event) => {
  const checkbox = event.target as HTMLInputElement;
  if (checkbox.checked) {
    checkedTests.value.push(+checkbox.id);
  } else {
    checkedTests.value = checkedTests.value.filter(el => el !== +checkbox.id);
  }

  console.log(toRaw(checkedTests.value));
};

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

const close = () => {
  show.value = false;

  setTimeout(() => {
    emit("close");
  }, 300);
};

onMounted(() => {
  uploadTests();
});

watch(isVisible, value => {
  setTimeout(() => {
    show.value = value;
  }, 1);
});

interface Test {
  id: number;
  name: string;
  completed: boolean;
}
</script>

<style lang="scss" scoped>
.t-modal {
  position: fixed;
  top: 50%;
  left: 50%;
  padding: 2rem;
  border-radius: 1rem;
  background-color: var(--t-surface);
  box-shadow: 4px 4px 0px 9999px #00000000;
  transition: all 0.3s ease;
  opacity: 0;
  transform: translateY(100px) translate(-50%, -50%);
}

.content {
  .b-tests {
    max-height: 50vh;
    overflow-y: scroll;
    &::-webkit-scrollbar {
      width: 5px;
    }

    &::-webkit-scrollbar-track {
      background-color: none;
    }

    &::-webkit-scrollbar-thumb {
      background-color: var(--t-primary);
    }
    .e-test {
      display: flex;
      align-items: flex-start;
      gap: 1rem;
      padding: 0.5rem 0;
      cursor: pointer;
      border-top: 1px solid
        color-mix(in srgb, var(--t-secondary) 5%, transparent);
      label {
        cursor: pointer;
        max-width: 300px;
      }
    }
  }
  .actions {
    display: flex;
    gap: 0.5rem;
  }
}

.m-show {
  box-shadow: 4px 4px 0px 9999px #00000050;
  opacity: 1;
  transform: translateY(0) translate(-50%, -50%);
}

.custom-checkbox {
  position: absolute;
  z-index: -1;
  opacity: 0;
}

/* для элемента label, связанного с .custom-checkbox */
.custom-checkbox + label {
  display: inline-flex;
  align-items: center;
  user-select: none;
}

/* создание в label псевдоэлемента before со следующими стилями */
.custom-checkbox + label::before {
  content: "";
  display: inline-block;
  width: 1em;
  height: 1em;
  flex-shrink: 0;
  flex-grow: 0;
  border: 1px solid color-mix(in srgb, var(--t-secondary) 30%, transparent);
  border-radius: 0.25em;
  margin-right: 0.5em;
  background-repeat: no-repeat;
  background-position: center center;
  background-size: 50% 50%;
}

/* стили при наведении курсора на checkbox */
.custom-checkbox:not(:disabled):not(:checked) + label:hover::before {
  border-color: var(--t-primary);
}

/* стили для активного чекбокса (при нажатии на него) */
.custom-checkbox:not(:disabled):active + label::before {
  background-color: var(--t-background);
  border-color: var(--t-background);
}

/* стили для чекбокса, находящегося в фокусе */
.custom-checkbox:focus + label::before {
  box-shadow: 0 0 0 0.2rem var(--t-background);
}

/* стили для чекбокса, находящегося в фокусе и не находящегося в состоянии checked */
.custom-checkbox:focus:not(:checked) + label::before {
  border-color: var(--t-background);
}

/* стили для чекбокса, находящегося в состоянии checked */
.custom-checkbox:checked + label::before {
  border-color: var(--t-primary);
  background-color: var(--t-primary);
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3e%3cpath fill='%23fff' d='M6.564.75l-3.59 3.612-1.538-1.55L0 4.26 2.974 7.25 8 2.193z'/%3e%3c/svg%3e");
}

/* стили для чекбокса, находящегося в состоянии disabled */
.custom-checkbox:disabled + label::before {
  background-color: var(--t-background);
}
</style>
