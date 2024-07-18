import { UUID } from "crypto";
import { Price } from "../Price/Price.interface";

export interface Item {
  id: UUID;
  bill: UUID;
  price: UUID;
  quantity: number;
}

export interface ItemDetail {
  id: UUID;
  bill: UUID;
  price: Price;
  quantity: number;
}
