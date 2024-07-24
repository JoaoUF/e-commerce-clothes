import { useRoutes } from "react-router-dom";
import { AuthProvider } from "./contexts/AuthContext";
import LandingPage from "./pages/LandingPage";
import SignIn from "./pages/SignIn";
import SignUp from "./pages/SignUp";
import PrivateRoute from "./utils/PrivateRoute";

export default function App() {
  const routes = useRoutes([
    {
      path: "/",
      element: <AuthProvider />,
      children: [
        {
          path: "/",
          element: <LandingPage />,
        },
        {
          path: "/signin",
          element: <SignIn />,
        },
        {
          path: "/signup",
          element: <SignUp />,
        },
        {
          path: "/",
          element: <PrivateRoute />,
          children: [
            {
              path: "checkout",
              element: <></>,
            },
          ],
        },
      ],
    },
  ]);

  return routes;
}
