import { UUID } from "crypto";
import { PriceDetailProduct } from "../Price/Price.interface";

export interface Item {
  id?: UUID;
  bill: UUID;
  price: UUID;
  quantity: number;
}

export interface ItemDetail {
  id: UUID;
  price: PriceDetailProduct;
  quantity: number;
}
