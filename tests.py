import pytest
from roman import add

@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("I", "I", "II"),
        ("I", "II", "III"),
        ("II", "I", "III"),
    ]
)
def test1(a, b, expected):
    assert add(a, b) == expected

