import pytest
from app import Figure

def test_triangle_type():
    triangle = Figure("трикутник", 4)
    assert triangle.type == "трикутник"

def test_invalid_length():
    with pytest.raises(AssertionError):
        Figure("квадрат", 0)

@pytest.mark.parametrize("figure_type", Figure.FIGURES)
def test_allowed_figure(figure_type):
    assert Figure(figure_type, 1).type == figure_type

@pytest.fixture
def figure_length_10():
    return Figure("квадрат", 10)

def test_figure_length_10(figure_length_10):
    assert figure_length_10.get_figure_length == 10

def test_figure_type_length_10(figure_length_10):
    assert figure_length_10.type == "квадрат"

@pytest.mark.parametrize("invalid_type", ["коло", "ромб", "", "КВАДРАТ", 123])
def test_invalid_figure_type(invalid_type):
    with pytest.raises(AssertionError):
        Figure(invalid_type, 5)

@pytest.mark.parametrize("invalid_length", [0, -1, -100])
def test_invalid_figure_length(invalid_length):
    with pytest.raises(AssertionError):
        Figure("квадрат", invalid_length)

@pytest.mark.unit
def test_square_angles():
    assert Figure("квадрат", 5).get_angles() == 4

@pytest.mark.unit
def test_triangle_angles():
    assert Figure("трикутник", 5).get_angles() == 3

@pytest.fixture(scope="module")
def allowed_figures():
    return Figure.FIGURES

def test_figures_count(allowed_figures):
    assert len(allowed_figures) == 3

def test_figures_contains_square(allowed_figures):
    assert "квадрат" in allowed_figures