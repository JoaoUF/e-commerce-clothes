import { UUID } from "crypto";
import { Image } from "../Image/Image.interface";
import { PriceDetail } from "../Price/Price.interface";

export interface Product {
  id?: UUID;
  title: string;
  description: string;
  slug: string;
}

export interface SingleProductDetail {
  prices: PriceDetail[];
  images: Image[];
  product: Product;
}
