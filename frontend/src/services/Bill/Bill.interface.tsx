import { UUID } from "crypto";

export interface Bill {
  id?: UUID;
  user: number;
  total: number;
  created: Date;
  modified: Date;
}
