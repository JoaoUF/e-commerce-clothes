import { AxiosResponse } from "axios";
import { UUID } from "crypto";
import AxiosConfig from "../AxiosConfig";
import { Color } from "./Color.interface";

export class ColorService {
  list_colors(): Promise<Color[]> {
    return AxiosConfig.get("color/").then(
      (response: AxiosResponse<Color[]>) => response.data
    );
  }

  retrieve_color(pk: UUID): Promise<Color> {
    return AxiosConfig.get(`color/${pk}/`).then(
      (response: AxiosResponse<Color>) => response.data
    );
  }

  create_color(data: Color): Promise<Color> {
    return AxiosConfig.post("color/", data).then(
      (response: AxiosResponse<Color>) => response.data
    );
  }

  update_color(data: Color): Promise<Color> {
    return AxiosConfig.put("color/", data).then(
      (response: AxiosResponse<Color>) => response.data
    );
  }

  delete_color(pk: UUID): Promise<Color> {
    return AxiosConfig.delete(`color/${pk}/`).then(
      (response: AxiosResponse<Color>) => response.data
    );
  }
}
