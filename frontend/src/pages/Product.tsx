import {
  Box,
  Button,
  Container,
  FormControl,
  ImageList,
  ImageListItem,
  InputLabel,
  MenuItem,
  Select,
  Stack,
  ToggleButton,
  ToggleButtonGroup,
  Typography,
} from "@mui/material";
import { useContext, useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import AuthContext from "../contexts/AuthContext";
import { Item } from "../services/Item/Item.interface";
import { ItemService } from "../services/Item/Item.service";
import { PriceDetail } from "../services/Price/Price.interface";
import { SingleProductDetail } from "../services/Product/Product.interface";
import { ProductService } from "../services/Product/Product.service";
import NotFound from "./NotFound";

export default function Product() {
  let { slug } = useParams();
  const [productDetail, setProductDetail] =
    useState<SingleProductDetail | null>(null);

  useEffect(() => {
    let fetchData = async () => {
      try {
        let productService = new ProductService();
        let productOutput = await productService.retrieve_single_product_detail(
          slug
        );
        setProductDetail(productOutput);
      } catch (error) {
        console.log(error);
      }
    };

    fetchData();
  }, []);

  return (
    <Container
      component="main"
      maxWidth="lg"
      sx={{
        minHeight: "70vh",
        display: "flex",
        flexDirection: "column",
      }}
    >
      {productDetail ? (
        <DisplayProduct productDetail={productDetail} />
      ) : (
        <NotFound />
      )}
    </Container>
  );
}

interface DisplayProductProps {
  productDetail: SingleProductDetail;
}

function DisplayProduct({ productDetail }: DisplayProductProps) {
  let { user, card }: any = useContext(AuthContext);
  let navigate = useNavigate();
  const [availableColors, setAvailableColors] = useState<string[]>(() => {
    let filterColors = new Set<string>();
    for (let color in productDetail.prices) {
      filterColors.add(productDetail.prices[color].color.name);
    }
    return Array.from(filterColors);
  });
  const [availableSizes, setAvailableSizes] = useState<string[]>(() => {
    let filterSizes = new Set<string>();
    for (let price in productDetail.prices) {
      filterSizes.add(productDetail.prices[price].size.name);
    }
    return Array.from(filterSizes);
  });
  const [colorSelected, setColorSelected] = useState<string>(
    availableColors[0]
  );
  const [sizeSelected, setSizeSelected] = useState<string>(availableSizes[0]);
  const [priceSelected, SetPriceSelected] = useState<PriceDetail | null>(null);
  const [quantity, setQuantity] = useState<number>(1);

  function filterPrice() {
    let data: PriceDetail = productDetail.prices?.filter(
      (price) =>
        price.color.name === colorSelected && price.size.name === sizeSelected
    )[0];
    SetPriceSelected(data);
  }

  async function onClickCard() {
    try {
      let itemService = new ItemService();
      let itemData: Item = {
        bill: card,
        price: priceSelected!.id,
        quantity: quantity,
      };
      await itemService.create_item(itemData);
      console.log("added to card");
    } catch (error) {
      console.log(error);
    }
  }

  useEffect(() => {
    filterPrice();
  }, [colorSelected, sizeSelected]);

  const changeColor = (
    event: React.MouseEvent<HTMLElement>,
    newAlignment: string
  ) => {
    setColorSelected(newAlignment);
  };
  const changeSize = (
    event: React.MouseEvent<HTMLElement>,
    newAlignment: string
  ) => {
    setSizeSelected(newAlignment);
  };

  return (
    <Container
      sx={{
        width: "100%",
        height: "100%",
        flexGrow: 1,
        display: "flex",
        flexDirection: "row",
        justifyContent: "start",
        alignContent: "center",
      }}
    >
      <Box
        my={3}
        mx={3}
        display="flex"
        flexDirection="column"
        sx={{
          flexGrow: 1,
          justifyContent: "center",
          alignContent: "center",
        }}
      >
        <ImageList variant="masonry" cols={3} gap={8}>
          {productDetail.images?.map((image) => (
            <ImageListItem key={image.upload}>
              <img
                srcSet={image.upload}
                src={`${image.upload}`}
                alt={image.title}
                loading="lazy"
              />
            </ImageListItem>
          ))}
        </ImageList>
      </Box>
      <Box
        my={3}
        mx={3}
        display="flex"
        flexDirection="column"
        sx={{
          justifyContent: "center",
          alignContent: "center",
        }}
      >
        <Stack
          direction="column"
          justifyContent="center"
          alignItems="center"
          spacing={2}
        >
          <Typography variant="h6" gutterBottom>
            {productDetail.product?.title}
          </Typography>
          <Typography variant="body1" gutterBottom>
            {productDetail.product?.description}
          </Typography>
          <Typography variant="h4" gutterBottom>
            {priceSelected?.discountPrice}
          </Typography>
          <Typography
            variant="h5"
            gutterBottom
            sx={{
              textDecorationLine: "line-through",
            }}
          >
            {priceSelected?.originalPrice}
          </Typography>
          <ToggleButtonGroup
            color="primary"
            value={colorSelected}
            exclusive
            onChange={changeColor}
            aria-label="Platform"
          >
            {availableColors.map((color, index) => (
              <ToggleButton key={index} value={color}>
                {color}
              </ToggleButton>
            ))}
          </ToggleButtonGroup>
          <ToggleButtonGroup
            color="primary"
            value={sizeSelected}
            exclusive
            onChange={changeSize}
            aria-label="Platform"
          >
            {availableSizes.map((size, index) => (
              <ToggleButton key={index} value={size}>
                {size}
              </ToggleButton>
            ))}
          </ToggleButtonGroup>
          <FormControl fullWidth>
            <InputLabel id="demo-simple-select-label">Age</InputLabel>
            <Select
              labelId="demo-simple-select-label"
              id="demo-simple-select"
              value={quantity}
              label="Age"
              onChange={(e) => {
                setQuantity(e.target.value as number);
              }}
            >
              <MenuItem value={1}>1</MenuItem>
              <MenuItem value={2}>2</MenuItem>
              <MenuItem value={3}>3</MenuItem>
              <MenuItem value={4}>4</MenuItem>
              <MenuItem value={5}>5</MenuItem>
              <MenuItem value={6}>6</MenuItem>
              <MenuItem value={7}>7</MenuItem>
              <MenuItem value={8}>8</MenuItem>
              <MenuItem value={9}>9</MenuItem>
              <MenuItem value={10}>10</MenuItem>
            </Select>
          </FormControl>
          {user ? (
            <Button
              onClick={() => {
                onClickCard();
              }}
              variant="contained"
              color="success"
            >
              Buy
            </Button>
          ) : (
            <Button
              onClick={() => {
                navigate("/signin");
              }}
              variant="contained"
              color="success"
            >
              SignIn
            </Button>
          )}
        </Stack>
      </Box>
    </Container>
  );
}
