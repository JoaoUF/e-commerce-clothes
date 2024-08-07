import { ThemeProvider } from "@emotion/react";
import {
  Box,
  Button,
  Chip,
  Container,
  createTheme,
  CssBaseline,
  Stack,
  Typography,
} from "@mui/material";
import { useContext, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import AuthContext from "../contexts/AuthContext";
import { ItemDetail } from "../services/Item/Item.interface";
import { ItemService } from "../services/Item/Item.service";
import { PaymentService } from "../services/Payment/Payment.service";

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
        {user ? <ListItemDetail /> : <NotAuthorized />}
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
  let { card }: any = useContext(AuthContext);
  const [listCard, setListCard] = useState<ItemDetail[] | null>(null);
  const [total, setTotal] = useState<number>(0);

  async function onClickBuy() {
    try {
      let paymentService = new PaymentService();
      await paymentService.checkout(card);
      console.log("se registro la compra");
    } catch (error) {
      console.log(error);
    }
  }

  function updateTotal() {
    let result = 0;
    for (let i = 0; i < listCard!.length; i++) {
      if (listCard) {
        result += listCard[i].price.discountPrice * listCard[i].quantity;
      }
    }
    setTotal(result);
  }

  useEffect(() => {
    let fetchdata = async () => {
      try {
        let itemService = new ItemService();
        let itemOutput = await itemService.list_item_detail(card);
        setListCard(itemOutput);
        updateTotal();
      } catch (error) {
        console.log(error);
      }
    };

    fetchdata();
  }, []);

  return (
    <Stack
      direction="column"
      justifyContent="center"
      alignItems="flex-start"
      spacing={2}
    >
      {listCard ? (
        [
          listCard.map((item, key) => <ItemCard key={key} itemDetail={item} />),
          <Typography variant="h3" gutterBottom>
            Total: {total}
          </Typography>,
          <Button
            onClick={() => {
              onClickBuy();
            }}
            variant="contained"
            color="success"
          >
            SignIn
          </Button>,
        ]
      ) : (
        <h1>No hay productos</h1>
      )}
    </Stack>
  );
}

interface ItemCardProps {
  itemDetail: ItemDetail;
}

function ItemCard({ itemDetail }: ItemCardProps) {
  return (
    <Box
      sx={{
        width: "100%",
        padding: "2",
        display: "flex",
        flexDirection: "row",
        border: "2px solid grey",
        justifyContent: "center",
        alignContent: "space-around",
        gap: "2",
      }}
    >
      <Box
        sx={{
          flexGrow: 1,
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "flex-start",
        }}
      >
        <Typography variant="h2" gutterBottom>
          {itemDetail.price.product.title}
        </Typography>
        <Box
          sx={{
            display: "flex",
            flexDirection: "row",
            justifyContent: "center",
            alignItems: "flex-start",
          }}
        >
          <Chip label={itemDetail.price.color.name} />
          <Chip label={itemDetail.price.size.name} />
        </Box>
      </Box>
      <Typography variant="h2" gutterBottom>
        {itemDetail.quantity}
      </Typography>
      <Typography variant="h2" gutterBottom>
        {itemDetail.price.discountPrice}
      </Typography>
      <Typography variant="h2" gutterBottom>
        {itemDetail.price.discountPrice * itemDetail.quantity}
      </Typography>
    </Box>
  );
}
