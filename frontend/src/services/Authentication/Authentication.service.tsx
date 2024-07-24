import { AxiosResponse } from "axios";
import AxiosConfig from "../AxiosConfig";
import {
  RefreshToken,
  SignIn,
  SignInOutput,
  SignUp,
  VerifyEmail,
} from "./Authentication.interface";

export class AuthenticationService {
  register(data: SignUp) {
    return AxiosConfig.post("register/", data).catch((error) => error.data);
  }

  verify_email(data: VerifyEmail) {
    return AxiosConfig.post("verify-email/", data).catch((error) => error.data);
  }

  refresh_token(): Promise<RefreshToken | void> {
    return AxiosConfig.post("token/refresh/")
      .then((response: AxiosResponse<RefreshToken>) => response.data)
      .catch((error) => {
        console.log("ERROR REFRESH");
        console.log(error.message);
      });
  }

  login(data: SignIn): Promise<SignInOutput> {
    return AxiosConfig.post("login/", data).then(
      (response: AxiosResponse<SignInOutput>) => response.data
    );
  }

  logout() {
    return AxiosConfig.post("logout/");
  }
}
