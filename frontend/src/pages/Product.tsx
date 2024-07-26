import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

export default function Product() {
  let { slug } = useParams();
  const [validSlug, setValidSlug] = useState<boolean>(false);

  useEffect(() => {
    let fetchData = async () => {};
  }, []);
  return (
    <>
      <h1>hola</h1>
    </>
  );
}
