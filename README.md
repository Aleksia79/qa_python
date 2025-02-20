# qa_python
- Тесты на проверку класса BooksCollector в приложении BooksCollector

## Требования
- Для запуска тестов должен быть установлен пакет pytest
- Запуск всех тестов выполянется командой pytest

## Список тестов

### test_positive_add_new_book_number_of_symbols_true
- позитивный тест на добавление названий книг разрешенной длины
- используется параметризация с двумя тестовыми данными 
- проверка метода add_new_book
- проверка метода get_books_genre

### test_negative_add_new_book_number_of_symbols_true
- используется параметризация с двумя тестовыми данными
- негативный тест на валидацию при добавлении книг
- проверка метода add_new_book
- проверка метода get_books_genre
- проверка метода __init__ (словарь books_genre)

### test_negative_add_new_book_existing_books_true
- негативная проверка на добавление существующих книг
- используется фикстура list_of_books
- проверка метода add_new_book
- проверка метода get_books_genre
- проверка метода __init__ (словарь books_genre)

### test_set_book_genre_true
- проверка установки книге жанра
- используется параметризация с двумя тестовыми данными
- проверка метода add_new_book
- проверка метода set_book_genre
- проверка метода get_books_genre
- проверка метода __init__ (словарь books_genre)

### test_positive_list_of_genre_true
- позитивная проверка списка genre
- используется параметризация с пятью тестовыми данными
- проверка метода __init__ (список genre)

### test_negative_list_of_genre_true
- негативная проверка списка genre
- используется параметризация с пятью тестовыми данными
- проверка метода __init__ (список genre)

### test_get_book_genre_true
- проверка жанра книги по ее имени
- используется фикстура list_of_books_with_genre
- используется параметризация с двумя тестовыми данными
- проверка метода get_book_genre
- проверка метода __init__ (словарь books_genre)

### test_get_books_with_specific_genre_true
- проверка получения списка книг с определенным жанром
- используются фикстуры list_of_genre_books и list_of_books_with_genre
- используется параметризация с двумя тестовыми данными
- проверка метода get_books_with_specific_genre

### test_negative_get_books_for_children_true
- негативная проверка отсутствия книг с возрастным жанром в списке книг для детей
- используется параметризация с двумя тестовыми данными
- проверка метода add_new_book
- проверка метода set_book_genre
- проверка метода __init__ (список genre_age_rating)
- проверка метода get_books_for_children

### test_positive_add_book_in_favorites_true
- позитивная проверка добавления книги в Избранное
- используется параметризация с двумя тестовыми данными
- проверка метода add_new_book
- проверка метода add_book_in_favorites
- проверка метода __init__ (список favorites)

### test_negative_add_book_in_favorites_true
- негативная проверка добавления книги в Избранное, если она там уже есть
- используется фикстура list_of_favorites
- используется параметризация с двумя тестовыми данными
- проверка метода add_new_book
- проверка метода add_book_in_favorites
- проверка метода get_list_of_favorites_books

### test_delete_book_from_favorites_true
- позитивная проверка удаления книги из Избранного
- используется фикстура list_of_favorites
- используется параметризация с двумя тестовыми данными
- проверка метода delete_book_from_favorites
- проверка метода get_list_of_favorites_books