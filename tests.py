import pytest

import data

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    # позитивный тест на добавление названий книг разрешенной длины ++
    @pytest.mark.parametrize('name', ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить'])
    def test_positive_add_new_book_number_of_symbols_true(self, collector, name):
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 1

    # негативные проверки на валидацию для метода add_new_book ++
    @pytest.mark.parametrize('negative_name', ['', 'Негативная проверка: название книги больше 40 символов'])
    def test_negative_add_new_book_number_of_symbols_true(self, collector, negative_name):
        collector.add_new_book(negative_name)
        assert collector.get_books_genre() == {}

    # негативная проверка для добавления существующих книг ++
    def test_negative_add_new_book_existing_books_true(self, collector):
        collector.books_genre = data.list_of_books
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert collector.get_books_genre() == data.list_of_books

    # проверка установки книге жанра ++
    @pytest.mark.parametrize('name', ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить'])
    def test_set_book_genre_true(self, collector, name):
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Ужасы')
        assert collector.get_books_genre() == {name: 'Ужасы'}

    # проверка списка genre, позитивный тест +++++
    @pytest.mark.parametrize('book_genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_positive_list_of_genre_true(self, collector, book_genre):
        assert book_genre in collector.genre

    # проверка списка genre, негативный тест +++++
    @pytest.mark.parametrize('no_book_genre', ['Жанр', 'Трагедия', '12345', 12345, ''])
    def test_negative_list_of_genre_true(self, collector, no_book_genre):
        assert no_book_genre not in collector.genre

    # проверка жанра книги по ее имени ++
    @pytest.mark.parametrize('name', ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить'])
    def test_get_book_genre_true(self, collector, name):
        collector.books_genre = data.list_of_books_with_genre
        assert collector.get_book_genre(name) == collector.books_genre.get(name)

    # проверка списка книг с определенным жанром ++
    @pytest.mark.parametrize('genre', ['Ужасы', 'Комедии'])
    def test_get_books_with_specific_genre_true(self, collector, genre):
        collector.books_genre = data.list_of_books_with_genre
        assert collector.get_books_with_specific_genre(genre) == data.list_of_genre_books.get(genre)


    # проверка отсутствия книг с возрастным жанром в списке книг для детей ++
    @pytest.mark.parametrize('book_age_genre', ['Ужасы', 'Детективы'])
    def test_negative_get_books_for_children_true(self, collector, book_age_genre):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', book_age_genre)
        assert collector.get_books_for_children() == []

    # проверка добавления книги в избранное, позитивный тест ++
    @pytest.mark.parametrize('name', ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить'])
    def test_positive_add_book_in_favorites_true(self, collector, name):
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.favorites

    # проверка добавления книги в Избранное, негативный тест, повторное добавление ++
    @pytest.mark.parametrize('repeat_name', ['Гордость и предубеждение и вампир', 'Что делать, если ваш капибара хочет вас убить'])
    def test_negative_add_book_in_favorites_true(self, collector, repeat_name):
        collector.favorites = data.list_of_favorites
        collector.add_new_book(repeat_name)
        collector.add_book_in_favorites(repeat_name)
        assert len(collector.get_list_of_favorites_books()) == 2

    # удаление книги из Избранного ++
    @pytest.mark.parametrize('name', ['Гордость и предубеждение и вампир', 'Что делать, если ваш капибара хочет вас убить'])
    def test_delete_book_from_favorites_true(self, collector, name):
        collector.favorites = data.list_of_favorites
        collector.delete_book_from_favorites(name)
        assert name not in collector.get_list_of_favorites_books()
