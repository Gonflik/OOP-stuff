
import pytest
from app import Figure


# @pytest.mark.parametrize("figure_type, length, expected_angles", [
#     ("квадрат", 5, 4),
#     ("прямокутник", 10, 4),
#     ("трикутник", 3, 3),
# ])
# def test_get_angles(figure_type, length, expected_angles):
#     figure = Figure(figure_type, length)

#     assert figure.get_angles() == expected_angles


# def test_get_figure_type():
#     figure = Figure("квадрат", 5)

#     assert figure.get_figure_type == "квадрат"


def test_get_figure_length():
    figure = Figure("прямокутник", 10)

    assert figure.get_figure_length == 10


def test_invalid_figure_type():
    with pytest.raises(AssertionError, match="Невідомий тип фігури"):
        Figure("коло", 5)


# def test_invalid_length():
#     with pytest.raises(AssertionError, match="Довжина має бути більшою за 0!"):
#         Figure("квадрат", 0)

