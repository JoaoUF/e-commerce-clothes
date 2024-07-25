import { Stack, Typography } from "@mui/material";

export default function Baner() {
  return (
    <Stack spacing={2} useFlexGap sx={{ width: { xs: "100%", sm: "70%" } }}>
      <Typography
        variant="h1"
        sx={{
          display: "flex",
          flexDirection: { xs: "column", md: "row" },
          alignSelf: "center",
          textAlign: "center",
          fontSize: "clamp(3.5rem, 10vw, 4rem)",
        }}
      >
        Our latest&nbsp;
        <Typography
          component="span"
          variant="h1"
          sx={{
            fontSize: "clamp(3rem, 10vw, 4rem)",
            color: "primary.main",
          }}
        >
          products
        </Typography>
      </Typography>
      <Typography
        textAlign="center"
        color="text.secondary"
        sx={{ alignSelf: "center", width: { sm: "100%", md: "80%" } }}
      >
        Explore our cutting-edge dashboard, delivering high-quality solutions
        tailored to your needs. Elevate your experience with top-tier features
        and services.
      </Typography>
    </Stack>
  );
}
