import { useRoutes } from "react-router-dom";
import { AuthProvider } from "./contexts/AuthContext";
import LandingPage from "./pages/LandingPage";

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
      ],
    },
  ]);

  return routes;
}
