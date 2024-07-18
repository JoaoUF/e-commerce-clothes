import { AxiosResponse } from "axios";
import { UUID } from "crypto";
import AxiosConfig from "../AxiosConfig";
import { Price, PriceDetail } from "./Price.interface";

export class PriceService {
  list_prices(): Promise<Price[]> {
    return AxiosConfig.get("price/").then(
      (response: AxiosResponse<Price[]>) => response.data
    );
  }

  list_price_detail(pk: UUID): Promise<PriceDetail> {
    return AxiosConfig.get(`price/?product=${pk}`).then(
      (response: AxiosResponse<PriceDetail>) => response.data
    );
  }

  retrieve_price(pk: UUID): Promise<Price> {
    return AxiosConfig.get(`price/${pk}/`).then(
      (response: AxiosResponse<Price>) => response.data
    );
  }

  create_price(data: Price): Promise<Price> {
    return AxiosConfig.post("price/", data).then(
      (response: AxiosResponse<Price>) => response.data
    );
  }

  update_price(data: Price): Promise<Price> {
    return AxiosConfig.put("price/", data).then(
      (response: AxiosResponse<Price>) => response.data
    );
  }

  delete_product(pk: UUID): Promise<Price> {
    return AxiosConfig.delete(`price/${pk}/`).then(
      (response: AxiosResponse<Price>) => response.data
    );
  }
}
