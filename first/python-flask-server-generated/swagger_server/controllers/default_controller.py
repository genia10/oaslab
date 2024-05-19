import connexion
import six

from swagger_server.models.book import Book  # noqa: E501
from swagger_server import util

books = []


def books_book_id_delete(book_id):  # noqa: E501
    """Удалить книгу"""
    if not isinstance(book_id, int):
        return "Неверный ID", 400
    index = getIndexById(books, book_id)
    if index == -1:
        return "Книга не найдена", 404
    books.remove(books[index])
    return books


def books_book_id_get(book_id):  # noqa: E501
    """Получить информацию о книге"""
    if not isinstance(book_id, int):
        return "Неверный ID", 400
    index = getIndexById(books, book_id)
    if index == -1:
        return "Книга не найдена", 404
    return books[index]


def getIndexById(li, target):
    k = 0
    for x in li:
        if x.id == target:
            return k
        k = k + 1
    return -1


def getBooksByGenre(li, genre):
    res = []
    for x in li:
        if x.genre == genre:
            res.append(x)
    return res


def getBooksByAuthor(li, author):
    res = []
    for x in li:
        if x.author == author:
            res.append(x)
    return res


def getBooksByTitle(li, title):
    res = []
    for x in li:
        if x.title == title:
            res.append(x)
    return res


def books_book_id_put(body, book_id):  # noqa: E501
    """Обновить информацию о книге"""
    if not isinstance(book_id, int):
        return "Неверный ID", 400
    if connexion.request.is_json:
        body = Book.from_dict(connexion.request.get_json())  # noqa: E501
    index = getIndexById(books, book_id)
    if index == -1:
        return "Книга не найдена", 404
    books[index] = Book(body)
    return books[index]


def books_get():  # noqa: E501
    """Получить список книг"""
    if not books:
        return "Книг не найдено"
    return books


def books_post(body):  # noqa: E501
    """Добавить новую книгу"""
    book = Book
    if connexion.request.is_json:
        body = Book.from_dict(connexion.request.get_json())  # noqa: E501
        book = Book(body.id, body.title, body.author, body.genre)
        books.append(book)
    return book


def books_search_get(author=None, genre=None, title=None):  # noqa: E501
    """Поиск книг по различным критериям"""
    res = books.copy()
    if res and author is not None:
        res = getBooksByAuthor(res, author)
    if res and genre is not None:
        res = getBooksByGenre(res, genre)
    if res and title is not None:
        res = getBooksByTitle(res, title)
    return res