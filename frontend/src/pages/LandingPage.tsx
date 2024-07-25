import CssBaseline from "@mui/material/CssBaseline";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import Baner from "../components/Baner";
import getLPTheme from "../components/getLPTheme";
import Hero from "../components/Hero";
import AppAppBar from "../layouts/AppAppBar";

export default function LandingPage() {
  const LPtheme = createTheme(getLPTheme("light"));
  return (
    <ThemeProvider theme={LPtheme}>
      <CssBaseline />
      <AppAppBar />
      <Hero component={<Baner />} />
    </ThemeProvider>
  );
}
