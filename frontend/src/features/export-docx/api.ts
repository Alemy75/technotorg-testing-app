import { request } from "@/shared/request";

export const exportDocx = (tests: number[]) =>
  request({
    url: `api/tests/export/`,
    method: "post",
    responseType: "blob",
    data: {
      tests: tests
    }
  });
