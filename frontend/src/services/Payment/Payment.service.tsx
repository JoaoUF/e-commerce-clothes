import { UUID } from "crypto";
import AxiosConfig from "../AxiosConfig";

export class PaymentService {
  checkout(bill_uuid: UUID) {
    return AxiosConfig.post(`checkout-simple/${bill_uuid}/`);
  }
}
