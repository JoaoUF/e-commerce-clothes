import Button from "@mui/material/Button";
import Card from "@mui/material/Card";
import CardActions from "@mui/material/CardActions";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import Typography from "@mui/material/Typography";
import { ImageProductDetail } from "../services/Image/Image.interface";

interface ImgMediaCardProps {
  imageProductDetail: ImageProductDetail;
}

export default function ImgMediaCard({
  imageProductDetail,
}: ImgMediaCardProps) {
  return (
    <Card sx={{ maxWidth: 345 }}>
      <CardMedia
        component="img"
        alt={imageProductDetail.title}
        height="140"
        src={imageProductDetail.upload}
      />
      <CardContent>
        <Typography gutterBottom variant="h5" component="div">
          {imageProductDetail.product.title}
        </Typography>
        <Typography variant="body2" color="text.secondary">
          {imageProductDetail.product.description}
        </Typography>
      </CardContent>
      <CardActions>
        <Button size="small">Learn More</Button>
      </CardActions>
    </Card>
  );
}
