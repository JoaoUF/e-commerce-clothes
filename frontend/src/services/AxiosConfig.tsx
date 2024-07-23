import axios from "axios";

const AxiosConfig = axios.create({
  baseURL: process.env.REACT_APP_API_PATH,
  timeout: 10000,
  withCredentials: true,
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
});

// interceptor
// get contex & cookie

export default AxiosConfig;
