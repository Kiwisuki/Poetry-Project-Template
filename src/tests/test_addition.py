import pytest

from template_app.addition import add


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (1, 2, 3),
        (0, 0, 0),
        (-1, -1, -2),
        (1, -1, 0),
    ],
)
def test_add(a: float, b: float, expected: float) -> None:
    """Test the add function."""
    assert add(a, b) == expected
