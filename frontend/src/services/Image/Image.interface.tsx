import { UUID } from "crypto";
import { Product } from "../Product/Product.interface";

export interface Image {
  id?: UUID;
  title: string;
  description: string;
  slug: string;
  upload: string;
  product: UUID;
}

export interface ImageProductDetail {
  id: UUID;
  title: string;
  description: string;
  slug: string;
  upload: string;
  product: Product;
}
