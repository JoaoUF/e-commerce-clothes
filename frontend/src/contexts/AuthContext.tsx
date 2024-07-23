import { Context, createContext, useEffect, useState } from "react";
import { Outlet, useNavigate } from "react-router-dom";
import { useLocalStorage } from "../hooks/useLocalStorage";
import {
  SignIn,
  SignInOutput,
} from "../services/Authentication/Authentication.interface";
import { AuthenticationService } from "../services/Authentication/Authentication.service";
import { Bill } from "../services/Bill/Bill.interface";
import { BillService } from "../services/Bill/Bill.service";

interface ContextProps {
  user: number | null;
  loginUser: (data: SignIn) => Promise<void>;
  logoutUser: () => void;
}

const AuthContext = createContext<ContextProps | null>(
  null
) as Context<ContextProps>;

export default AuthContext;

export const AuthProvider = () => {
  let { card, updateCard, deleteCard } = useLocalStorage();
  let [user, setUser] = useState<number | null>(null);
  let [loading, setLoading] = useState<boolean>(false);
  const history = useNavigate();

  let loginUser = async (data: SignIn) => {
    try {
      let authenticationService = new AuthenticationService();
      let billService = new BillService();
      let serviceOutput: SignInOutput = await authenticationService.login(data);
      let billOutput: Bill = await billService.retrieve_bill_zero(
        serviceOutput.user.pk
      );
      setUser(serviceOutput.user.pk);
      updateCard(billOutput.id);
      history("/");
    } catch (error) {
      console.log(error);
    }
  };

  let logoutUser = async () => {
    deleteCard();
    setUser(null);
    history("/");
  };

  let updateToken = async () => {
    try {
      let authenticationService = new AuthenticationService();
      authenticationService.refresh_token();
    } catch (error) {
      console.log(error);
      logoutUser();
    }

    if (loading) {
      updateToken();
    }
  };

  useEffect(() => {
    console.log("RENICIANDO");

    if (loading) {
      updateToken();
    }

    let fiveMinutes = 1000 * 60 * 5;

    let interval = setInterval(() => {
      if (card) {
        updateToken();
      }
    }, fiveMinutes);

    return () => clearInterval(interval);
  }, [card, loading]);

  let contextProps: ContextProps = {
    user: user,
    loginUser: loginUser,
    logoutUser: logoutUser,
  };

  return (
    <AuthContext.Provider value={contextProps}>
      {loading ? null : <Outlet />}
    </AuthContext.Provider>
  );
};
