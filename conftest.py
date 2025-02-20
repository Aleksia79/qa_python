import pytest

from main import BooksCollector

# фикстура для создания объекта класса BooksCollector
@pytest.fixture()
def collector():
    return BooksCollector()

