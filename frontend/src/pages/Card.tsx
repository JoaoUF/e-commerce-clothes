import { ThemeProvider } from "@emotion/react";
import {
  Button,
  Container,
  createTheme,
  CssBaseline,
  Typography,
} from "@mui/material";
import { useContext } from "react";
import { useNavigate } from "react-router-dom";
import AuthContext from "../contexts/AuthContext";

const defaultTheme = createTheme();

export default function Card() {
  let { user }: any = useContext(AuthContext);
  return (
    <ThemeProvider theme={defaultTheme}>
      <CssBaseline />
      <Container
        component="main"
        maxWidth="lg"
        sx={{
          minHeight: "70vh",
          display: "flex",
          flexDirection: "column",
        }}
      >
        {user ? <h1>hola2</h1> : <NotAuthorized />}
      </Container>
    </ThemeProvider>
  );
}

function NotAuthorized() {
  let navigate = useNavigate();
  return (
    <Container
      maxWidth="xs"
      sx={{
        height: "100%",
        flexGrow: 1,
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignContent: "center",
      }}
    >
      <Typography align="center" variant="h5" gutterBottom>
        SignIn for add product to your card
      </Typography>
      <Button onClick={() => navigate("/signin")} variant="contained">
        SignIn
      </Button>
    </Container>
  );
}

function ListItemDetail() {
  return (
    <>
      <h1>hola</h1>
    </>
  );
}
