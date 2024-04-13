import { request } from "../request";

export const getTests = () =>
    request<TestDto[]>({
        url: `api/tests/`,
        method: "get",
    });

interface TestDto {
    id: number;
    name: string;
}

export const getTest = (testId: number) =>
    request<FullTestDto>({
        url: `api/tests/${testId}`,
        method: "get",
    });

export interface FullTestDto extends TestDto {
    questions: Question[];
}

export interface Question {
    id: number;
    text: string;
    answers: Answers[];
}

export interface Answers {
    id: number;
    text: string;
    is_correct: boolean;
}
