# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.book import Book  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_books_book_id_delete(self):
        """Test case for books_book_id_delete

        Удалить книгу
        """
        response = self.client.open(
            '/api/books/{bookId}'.format(book_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_books_book_id_get(self):
        """Test case for books_book_id_get

        Получить информацию о книге
        """
        response = self.client.open(
            '/api/books/{bookId}'.format(book_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_books_book_id_put(self):
        """Test case for books_book_id_put

        Обновить информацию о книге
        """
        body = Book()
        response = self.client.open(
            '/api/books/{bookId}'.format(book_id=789),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_books_get(self):
        """Test case for books_get

        Получить список книг
        """
        response = self.client.open(
            '/api/books',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_books_post(self):
        """Test case for books_post

        Добавить новую книгу
        """
        body = Book()
        response = self.client.open(
            '/api/books',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_books_search_get(self):
        """Test case for books_search_get

        Поиск книг по различным критериям
        """
        query_string = [('author', 'author_example'),
                        ('genre', 'genre_example'),
                        ('title', 'title_example')]
        response = self.client.open(
            '/api/books/search',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
