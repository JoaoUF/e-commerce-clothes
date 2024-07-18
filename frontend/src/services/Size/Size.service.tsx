import { AxiosResponse } from "axios";
import { UUID } from "crypto";
import AxiosConfig from "../AxiosConfig";
import { Size } from "./Size.interface";

export class SizeService {
  list_sizes(): Promise<Size[]> {
    return AxiosConfig.get("size/").then(
      (response: AxiosResponse<Size[]>) => response.data
    );
  }

  retrieve_size(pk: UUID): Promise<Size> {
    return AxiosConfig.get(`size/${pk}/`).then(
      (response: AxiosResponse<Size>) => response.data
    );
  }

  create_size(data: Size): Promise<Size> {
    return AxiosConfig.post("size/", data).then(
      (response: AxiosResponse<Size>) => response.data
    );
  }

  update_size(data: Size): Promise<Size> {
    return AxiosConfig.put("size/", data).then(
      (response: AxiosResponse<Size>) => response.data
    );
  }

  delete_size(pk: UUID): Promise<Size> {
    return AxiosConfig.delete(`size/${pk}/`).then(
      (response: AxiosResponse<Size>) => response.data
    );
  }
}
