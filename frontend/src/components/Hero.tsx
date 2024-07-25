import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import { ReactNode } from "react";

interface HeroProps {
  component: ReactNode;
}

export default function Hero({ component }: HeroProps) {
  return (
    <Box
      id="hero"
      sx={{
        width: "100%",
        backgroundImage: "linear-gradient(180deg, #CEE5FD, #FFF)",
        backgroundSize: "100% 20%",
        backgroundRepeat: "no-repeat",
      }}
    >
      <Container
        sx={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          pt: { xs: 14, sm: 20 },
          pb: { xs: 8, sm: 12 },
        }}
      >
        {component}
      </Container>
    </Box>
  );
}
