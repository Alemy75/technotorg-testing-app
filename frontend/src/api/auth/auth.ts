import { request } from "../request";

export const getToken = ({ username, password }: RequestOptions) =>
    request<Token>({
        url: `api/token/`,
        method: "POST",
        data: {
            username,
            password,
        },
    });

interface Token {
    refresh: string;
    access: string;
}

interface RequestOptions {
    username: string;
    password: string;
}
