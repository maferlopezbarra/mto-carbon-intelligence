from src.extractors import get_values
import pytest


def test_file():
    with pytest.raises(FileNotFoundError):
        get_values("None")
    with pytest.raises(ValueError):
        get_values("src/main.py")