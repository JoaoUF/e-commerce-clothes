import pytest
from ..factories import PriceFactory


@pytest.fixture
def price_draft():
    return PriceFactory()


@pytest.mark.django_db
def test_name_model(price_draft):
    assert str(price_draft.id) == price_draft.__str__()
