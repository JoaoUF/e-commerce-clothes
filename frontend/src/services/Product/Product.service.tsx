import { AxiosResponse } from "axios";
import { UUID } from "crypto";
import AxiosConfig from "../AxiosConfig";
import { Product } from "./Product.interface";

export class ProductService {
  list_products(): Promise<Product[]> {
    return AxiosConfig.get("product/").then(
      (response: AxiosResponse<Product[]>) => response.data
    );
  }

  retrieve_product(pk: UUID): Promise<Product> {
    return AxiosConfig.get(`product/${pk}/`).then(
      (response: AxiosResponse<Product>) => response.data
    );
  }

  create_product(data: Product): Promise<Product> {
    return AxiosConfig.post("product/", data).then(
      (response: AxiosResponse<Product>) => response.data
    );
  }

  update_product(data: Product): Promise<Product> {
    return AxiosConfig.put("product/", data).then(
      (response: AxiosResponse<Product>) => response.data
    );
  }

  delete_product(pk: UUID): Promise<Product> {
    return AxiosConfig.delete(`product/${pk}/`).then(
      (response: AxiosResponse<Product>) => response.data
    );
  }
}
