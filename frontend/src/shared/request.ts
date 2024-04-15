import axios, { type AxiosRequestConfig } from "axios";

axios.defaults.baseURL = "http://localhost:8000/";

export const request = async <T = any, D = any>({
    url = "/",
    method = "GET",
    data,
    ...config
}: AxiosRequestConfig<D>) => {
    return axios<T>({
        url,
        method,
        data,
        ...config,
        headers: {
            Authorization: `Bearer ${localStorage.getItem("access_token") ?? ""}`,
        },
    });
};
