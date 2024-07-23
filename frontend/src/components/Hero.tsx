import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import Stack from "@mui/material/Stack";
import Typography from "@mui/material/Typography";

export default function Hero() {
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
            Explore our cutting-edge dashboard, delivering high-quality
            solutions tailored to your needs. Elevate your experience with
            top-tier features and services.
          </Typography>
        </Stack>
      </Container>
    </Box>
  );
}
