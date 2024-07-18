import { AxiosResponse } from "axios";
import { UUID } from "crypto";
import AxiosConfig from "../AxiosConfig";
import { Item, ItemDetail } from "./Item.interface";

export class ItemService {
  list_items(): Promise<Item[]> {
    return AxiosConfig.get("item/").then(
      (response: AxiosResponse<Item[]>) => response.data
    );
  }

  list_item_detail(pk: UUID): Promise<ItemDetail> {
    return AxiosConfig.get(`item/?bill=${pk}`).then(
      (response: AxiosResponse<ItemDetail>) => response.data
    );
  }

  retrieve_item(pk: UUID): Promise<Item> {
    return AxiosConfig.get(`item/${pk}/`).then(
      (response: AxiosResponse<Item>) => response.data
    );
  }

  create_item(data: Item): Promise<Item> {
    return AxiosConfig.post("item/", data).then(
      (response: AxiosResponse<Item>) => response.data
    );
  }

  update_item(data: Item): Promise<Item> {
    return AxiosConfig.put("item/", data).then(
      (response: AxiosResponse<Item>) => response.data
    );
  }

  delete_product(pk: UUID): Promise<Item> {
    return AxiosConfig.delete(`item/${pk}/`).then(
      (response: AxiosResponse<Item>) => response.data
    );
  }
}
