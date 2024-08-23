import pytest
from ..factories import SizeFactory


@pytest.fixture
def size_draft():
    return SizeFactory()


@pytest.mark.django_db
def test_name_model(size_draft):
    assert str(size_draft.id) + size_draft.name == size_draft.__str__()
