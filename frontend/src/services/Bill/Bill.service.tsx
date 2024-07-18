import { AxiosResponse } from "axios";
import { UUID } from "crypto";
import AxiosConfig from "../AxiosConfig";
import { Bill } from "./Bill.interface";

export class BillService {
  list_bills(): Promise<Bill[]> {
    return AxiosConfig.get("bill/").then(
      (response: AxiosResponse<Bill[]>) => response.data
    );
  }

  retrieve_bill(pk: UUID): Promise<Bill> {
    return AxiosConfig.get(`bill/${pk}/`).then(
      (response: AxiosResponse<Bill>) => response.data
    );
  }

  retrieve_bill_zero(user: number): Promise<Bill> {
    return AxiosConfig.get(`bill/?user=${user}`).then(
      (response: AxiosResponse<Bill>) => response.data
    );
  }

  create_bill(data: Bill): Promise<Bill> {
    return AxiosConfig.post("bill/", data).then(
      (response: AxiosResponse<Bill>) => response.data
    );
  }

  update_bill(data: Bill): Promise<Bill> {
    return AxiosConfig.put("bill/", data).then(
      (response: AxiosResponse<Bill>) => response.data
    );
  }

  delete_bill(pk: UUID): Promise<Bill> {
    return AxiosConfig.delete(`bill/${pk}/`).then(
      (response: AxiosResponse<Bill>) => response.data
    );
  }
}
