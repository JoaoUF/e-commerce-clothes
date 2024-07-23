import CssBaseline from "@mui/material/CssBaseline";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import AppAppBar from "../components/AppAppBar";
import getLPTheme from "../components/getLPTheme";
import Hero from "../components/Hero";

export default function LandingPage() {
  const LPtheme = createTheme(getLPTheme("light"));
  return (
    <ThemeProvider theme={LPtheme}>
      <CssBaseline />
      <AppAppBar />
      <Hero />
    </ThemeProvider>
  );
}
