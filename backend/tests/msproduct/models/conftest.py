from pytest_factoryboy import register
from .factories import ColorFactory, SizeFactory, PriceFactory, ProductFactory

register(ColorFactory)
register(SizeFactory)
register(PriceFactory)
register(ProductFactory)