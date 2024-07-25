import { ReactNode } from "react";
import Hero from "../components/Hero";
import AppAppBar from "./AppAppBar";

interface AppContainerProps {
  component: ReactNode;
}

export default function AppContainer({ component }: AppContainerProps) {
  return (
    <>
      <AppAppBar />
      <Hero component={component} />
    </>
  );
}
