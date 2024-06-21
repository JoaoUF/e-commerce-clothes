import factory

class ColorFactory(factory.django.DjangoModelFactory):
    name = 'red'

    class Meta:
        model = 'msproduct.Color'

class SizeFactory(factory.django.DjangoModelFactory):
    name = 'small'

    class Meta:
        model = 'msproduct.Size'

class PriceFactory(factory.django.DjangoModelFactory):
    color = factory.SubFactory(ColorFactory)
    size = factory.SubFactory(SizeFactory)
    originalPrice = 20.50
    discountPrice = 17.99

    class Meta:
        model = 'msproduct.Price'

class ProductFactory(factory.django.DjangoModelFactory):
    price = factory.SubFactory(PriceFactory)
    title = 'tshirt'
    description = 'this is a description'

    class Meta:
        model = 'msproduct.Product'