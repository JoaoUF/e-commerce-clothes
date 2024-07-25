import { AxiosResponse } from "axios";
import { UUID } from "crypto";
import AxiosConfig from "../AxiosConfig";
import { Image, ImageProductDetail } from "./Image.interface";

export class ImageService {
  list_images(): Promise<Image[]> {
    return AxiosConfig.get("image/").then(
      (response: AxiosResponse<Image[]>) => response.data
    );
  }

  list_product_image_detail(): Promise<ImageProductDetail[]> {
    return AxiosConfig.get("image-product-detail/").then(
      (response: AxiosResponse<ImageProductDetail[]>) => response.data
    );
  }

  retrieve_image(pk: UUID): Promise<Image> {
    return AxiosConfig.get(`image/${pk}/`).then(
      (response: AxiosResponse<Image>) => response.data
    );
  }

  create_image(data: Image): Promise<Image> {
    return AxiosConfig.post("image/", data).then(
      (response: AxiosResponse<Image>) => response.data
    );
  }

  update_image(data: Image): Promise<Image> {
    return AxiosConfig.put("image/", data).then(
      (response: AxiosResponse<Image>) => response.data
    );
  }

  delete_image(pk: UUID): Promise<Image> {
    return AxiosConfig.delete(`image/${pk}/`).then(
      (response: AxiosResponse<Image>) => response.data
    );
  }
}
