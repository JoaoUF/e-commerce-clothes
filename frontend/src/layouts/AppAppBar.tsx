import MenuIcon from "@mui/icons-material/Menu";
import ShoppingCartIcon from "@mui/icons-material/ShoppingCart";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import Container from "@mui/material/Container";
import Divider from "@mui/material/Divider";
import Drawer from "@mui/material/Drawer";
import MenuItem from "@mui/material/MenuItem";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import * as React from "react";
import { useNavigate } from "react-router-dom";
import AuthContext from "../contexts/AuthContext";

function AppAppBar() {
  let { user, logoutUser }: any = React.useContext(AuthContext);
  const [open, setOpen] = React.useState(false);
  const navigate = useNavigate();

  const toggleDrawer = (newOpen: boolean) => () => {
    setOpen(newOpen);
  };

  return (
    <div>
      <AppBar
        position="fixed"
        sx={{
          boxShadow: 0,
          bgcolor: "transparent",
          backgroundImage: "none",
          mt: 2,
        }}
      >
        <Container maxWidth="lg">
          <Toolbar
            variant="regular"
            sx={{
              display: "flex",
              alignItems: "center",
              justifyContent: "space-between",
              flexShrink: 0,
              borderRadius: "999px",
              bgcolor: "rgba(255, 255, 255, 0.4)",
              backdropFilter: "blur(24px)",
              maxHeight: 40,
              border: "1px solid",
              borderColor: "divider",
              boxShadow: `0 0 1px rgba(85, 166, 246, 0.1), 1px 1.5px 2px -1px rgba(85, 166, 246, 0.15), 4px 4px 12px -2.5px rgba(85, 166, 246, 0.15)`,
            }}
          >
            <Box
              sx={{
                flexGrow: 1,
                display: "flex",
                alignItems: "center",
                ml: "-18px",
                px: 0,
              }}
            >
              <Box sx={{ display: { xs: "none", md: "flex" } }}>
                <MenuItem sx={{ py: "6px", px: "12px" }}>
                  <Typography variant="body2" color="text.primary">
                    Home
                  </Typography>
                </MenuItem>
              </Box>
            </Box>
            <Box
              sx={{
                display: { xs: "none", md: "flex" },
                gap: 0.5,
                alignItems: "center",
              }}
            >
              <Button
                color="primary"
                variant="contained"
                size="small"
                component="a"
                target="_blank"
                startIcon={<ShoppingCartIcon />}
                onClick={() => {
                  navigate("/card");
                }}
              >
                Card
              </Button>
              {user ? (
                <Button
                  color="primary"
                  variant="text"
                  size="small"
                  component="a"
                  target="_blank"
                  onClick={() => {
                    logoutUser();
                  }}
                >
                  Logout
                </Button>
              ) : (
                <>
                  <Button
                    color="primary"
                    variant="text"
                    size="small"
                    component="a"
                    target="_blank"
                    onClick={() => {
                      navigate("/signin");
                    }}
                  >
                    Sign in
                  </Button>
                  <Button
                    color="primary"
                    variant="contained"
                    size="small"
                    component="a"
                    target="_blank"
                    onClick={() => {
                      navigate("/signup");
                    }}
                  >
                    Sign up
                  </Button>
                </>
              )}
            </Box>
            <Box sx={{ display: { sm: "", md: "none" } }}>
              <Button
                variant="text"
                color="primary"
                aria-label="menu"
                onClick={toggleDrawer(true)}
                sx={{ minWidth: "30px", p: "4px" }}
              >
                <MenuIcon />
              </Button>
              <Drawer anchor="right" open={open} onClose={toggleDrawer(false)}>
                <Box
                  sx={{
                    minWidth: "60dvw",
                    p: 2,
                    backgroundColor: "background.paper",
                    flexGrow: 1,
                  }}
                >
                  <MenuItem>Home</MenuItem>
                  <Divider />
                  <MenuItem>
                    <Button
                      color="primary"
                      variant="outlined"
                      component="a"
                      target="_blank"
                      sx={{ width: "100%" }}
                      startIcon={<ShoppingCartIcon />}
                      onClick={() => {
                        navigate("/card");
                      }}
                    >
                      Card
                    </Button>
                  </MenuItem>
                  {user ? (
                    <MenuItem>
                      <Button
                        color="primary"
                        variant="outlined"
                        component="a"
                        target="_blank"
                        sx={{ width: "100%" }}
                        startIcon={<ShoppingCartIcon />}
                        onClick={() => {
                          logoutUser();
                        }}
                      >
                        Card
                      </Button>
                    </MenuItem>
                  ) : (
                    <>
                      <MenuItem>
                        <Button
                          color="primary"
                          variant="contained"
                          component="a"
                          target="_blank"
                          sx={{ width: "100%" }}
                          onClick={() => {
                            navigate("/signup");
                          }}
                        >
                          Sign up
                        </Button>
                      </MenuItem>
                      <MenuItem>
                        <Button
                          color="primary"
                          variant="outlined"
                          component="a"
                          target="_blank"
                          sx={{ width: "100%" }}
                          onClick={() => {
                            navigate("/signin");
                          }}
                        >
                          Sign in
                        </Button>
                      </MenuItem>
                    </>
                  )}
                </Box>
              </Drawer>
            </Box>
          </Toolbar>
        </Container>
      </AppBar>
    </div>
  );
}

export default AppAppBar;