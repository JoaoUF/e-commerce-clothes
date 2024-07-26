import { UUID } from "crypto";
import { Color } from "../Color/Color.interface";
import { Size } from "../Size/Size.interface";

export interface Price {
  id: UUID;
  color: UUID;
  size: UUID;
  product: UUID;
  originalPrice: number;
  discountPrice: number;
}

export interface PriceDetail {
  id: UUID;
  color: Color;
  size: Size;
  originalPrice: number;
  discountPrice: number;
}
