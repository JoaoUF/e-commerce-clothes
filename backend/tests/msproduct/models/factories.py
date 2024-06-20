import factory

class ColorFactory(factory.django.DjangoModelFactory):
    name = 'red'

    class Meta:
        model = 'msproduct.Color'