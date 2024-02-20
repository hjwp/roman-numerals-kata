import pytest
from roman import add

@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("I", "I", "II"),
        ("I", "II", "III"),
        ("II", "I", "III"),
        ("I", "III", "IIII"),
        ("III", "I", "IIII"),
        ("II", "II", "IIII"),
        ("I", "IIII", "V"),
        ("V", "I", "VI"),
        ("III", "III", "VI"),
        ("I", "V", "VI"),
        ("V", "V", "X"),
        ("V", "VI", "XI"),
        ("VI", "VI", "XII"),
    ]
)
def test1(a, b, expected):
    assert add(a, b) == expected

