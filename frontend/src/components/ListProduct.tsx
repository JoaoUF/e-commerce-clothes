import { Container, Stack } from "@mui/material";
import { useEffect, useState } from "react";
import { ImageProductDetail } from "../services/Image/Image.interface";
import { ImageService } from "../services/Image/Image.service";
import ImgMediaCard from "./ImgMediaCard";

export default function ListProduct() {
  let [listProduct, setListProduct] = useState<ImageProductDetail[] | null>(
    null
  );

  useEffect(() => {
    let fetchData = async () => {
      try {
        let imageService = new ImageService();
        let imageOutput = await imageService.list_product_image_detail();
        setListProduct(imageOutput);
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
      <Stack
        useFlexGap
        spacing={{ xs: 2, sm: 2 }}
        direction="row"
        flexWrap="wrap"
        justifyContent={"space-around"}
        sx={{
          flexGrow: 1,
        }}
      >
        {listProduct &&
          listProduct?.map((item, index) => (
            <ImgMediaCard imageProductDetail={item} />
          ))}
      </Stack>
    </Container>
  );
}
