import { Button } from "@mui/material";
import { useGoogleLogin } from "@react-oauth/google";
import { AuthenticationService } from "../services/Authentication/Authentication.service";

export default function GoogleButton() {
  const googleResponse = async (response: any) => {
    console.log("this is the response", response);
    try {
      let authenticationService = new AuthenticationService();
      let authenticationOutput =
        await authenticationService.register_google_code(response.code);
      console.log("google output", authenticationOutput);
      console.log("token", response.code);
    } catch (error) {
      console.log(error);
    }
  };

  const loginGoogle = useGoogleLogin({
    onSuccess: (tokenResponse) => googleResponse(tokenResponse),
  });

  return (
    <Button
      fullWidth
      onClick={() => loginGoogle()}
      variant="contained"
      sx={{ mt: 3, mb: 2 }}
    >
      Sign in with Google
    </Button>
  );
}
