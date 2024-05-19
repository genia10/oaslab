from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.host = 'http://localhost:8080/api/'
api_client = swagger_client.ApiClient(configuration=configuration)
api_instance = swagger_client.DefaultApi(api_client=api_client)
book_id = 789 # int | Идентификатор книги

try:
    # Удалить книгу
    api_instance.books_book_id_delete(book_id)
except ApiException as e:
    print("Exception when calling DefaultApi->books_book_id_delete: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
book_id = 789 # int | Идентификатор книги

try:
    # Получить информацию о книге
    api_response = api_instance.books_book_id_get(book_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->books_book_id_get: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.Book() # Book |
book_id = 789 # int | Идентификатор книги

try:
    # Обновить информацию о книге
    api_response = api_instance.books_book_id_put(body, book_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->books_book_id_put: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Получить список книг
    api_response = api_instance.books_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->books_get: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.Book() # Book |

try:
    # Добавить новую книгу
    api_response = api_instance.books_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->books_post: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
author = 'author_example' # str | Автор книги (optional)
genre = 'genre_example' # str | Жанр книги (optional)
title = 'title_example' # str | Название книги (optional)

try:
    # Поиск книг по различным критериям
    api_response = api_instance.books_search_get(author=author, genre=genre, title=title)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->books_search_get: %s\n" % e)