// Component.vue

export const getImage = (src: string) => {
  console.log(import.meta.env);

  return import.meta.env.VITE_API_PROXY_TARGET + "/api" + src;
};
