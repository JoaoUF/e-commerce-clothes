import factory


class ColorFactory(factory.django.DjangoModelFactory):
    name = "red"

    class Meta:
        model = "msproduct.Color"


class SizeFactory(factory.django.DjangoModelFactory):
    name = "small"

    class Meta:
        model = "msproduct.Size"


class ProductFactory(factory.django.DjangoModelFactory):
    title = "tshirt"
    description = "this is a description"

    class Meta:
        model = "msproduct.Product"


class PriceFactory(factory.django.DjangoModelFactory):
    color = factory.SubFactory(ColorFactory)
    size = factory.SubFactory(SizeFactory)
    product = factory.SubFactory(ProductFactory)
    originalPrice = 20.50
    discountPrice = 17.99

    class Meta:
        model = "msproduct.Price"
