import { AxiosResponse } from "axios";
import { UUID } from "crypto";
import AxiosConfig from "../AxiosConfig";
import { ProductImage } from "./ProductImage.interface";

export class ProductImageService {
  list_product_images(): Promise<ProductImage[]> {
    return AxiosConfig.get("product-image/").then(
      (response: AxiosResponse<ProductImage[]>) => response.data
    );
  }

  retrieve_product_image(pk: UUID): Promise<ProductImage> {
    return AxiosConfig.get(`product-image/${pk}/`).then(
      (response: AxiosResponse<ProductImage>) => response.data
    );
  }

  create_product_image(data: ProductImage): Promise<ProductImage> {
    return AxiosConfig.post("product-image/", data).then(
      (response: AxiosResponse<ProductImage>) => response.data
    );
  }

  update_product_image(data: ProductImage): Promise<ProductImage> {
    return AxiosConfig.put("product-image/", data).then(
      (response: AxiosResponse<ProductImage>) => response.data
    );
  }

  delete_product_image(pk: UUID): Promise<ProductImage> {
    return AxiosConfig.delete(`product-image/${pk}/`).then(
      (response: AxiosResponse<ProductImage>) => response.data
    );
  }
}
