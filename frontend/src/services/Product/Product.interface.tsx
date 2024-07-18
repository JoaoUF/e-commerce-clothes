import { UUID } from "crypto";

export interface Product {
  id: UUID;
  title: string;
  description: string;
  slug: string;
}
