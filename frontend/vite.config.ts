import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import path from "path";

export const API_PROXY_TARGET = "http://127.0.0.1:8000";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],

  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src")
    }
  }
});
