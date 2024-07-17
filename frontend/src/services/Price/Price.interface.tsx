import { UUID } from "crypto";

export interface Price {
  id: UUID;
  color: UUID;
  size: UUID;
  originalPrice: number;
  discountPrice: number;
}
