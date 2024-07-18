import { UUID } from "crypto";

export interface ProductImage {
  id: UUID;
  product: UUID;
  image: UUID;
}
