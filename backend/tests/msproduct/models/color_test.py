import pytest
from ..factories import ColorFactory


@pytest.fixture
def color_draft():
    return ColorFactory()


@pytest.fixture
def color_published():
    return ColorFactory(id="f019c17f-6d37-4489-908a-d5b2f17632c4", name="yellow")


@pytest.mark.django_db
def test_color_id(color_draft, color_published):
    assert color_draft.id != color_published.id


@pytest.mark.django_db
def test_color_self_name(color_draft):
    assert color_draft.__str__() == color_draft.name


@pytest.mark.django_db
def test_color_name(color_draft, color_published):
    assert color_draft.name != color_published.name
