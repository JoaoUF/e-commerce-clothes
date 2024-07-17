import { UUID } from "crypto";

export interface Image {
  id: UUID;
  title: string;
  description: string;
  slug: string;
  upload: string;
}
