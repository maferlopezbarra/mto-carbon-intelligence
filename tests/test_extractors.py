from src.extractors import get_values
import pytest


def test_FileNotFound():
    with pytest.raises(FileNotFoundError):
        get_values("None")


def test_invalid_extension(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("text")
    with pytest.raises(ValueError):
        get_values(file)


def test_invalid_database(tmp_path):
    file = tmp_path / "invalid.db"
    file.write_text("not a sqlite database")
    with pytest.raises(ValueError):
        get_values(file)