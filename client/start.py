from __future__ import print_function

import logging
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

#logging.basicConfig(filename='E:/PyProects/oaslab/var/log/1.log', level=logging.INFO)

trace.set_tracer_provider(TracerProvider())
otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)
tracer = trace.get_tracer(__name__)

configuration = swagger_client.Configuration()
configuration.host = 'http://localhost:8080/'
api_client = swagger_client.ApiClient(configuration=configuration)
api_instance = swagger_client.DefaultApi(api_client=api_client)


body = swagger_client.Book(789, "poem", "Pushkin", "example")

'''body = {
  "author": "Pushkin",
  "genre": "poem",
  "id": 789,
  "title": "example"
} # Book'''

with tracer.start_as_current_span("API BOOKS_LIST"):
  # Добавить новую книгу
  api_response = api_instance.books_post(body)
  pprint(api_response)


# create an instance of the API class
book_id = 789
# int | Идентификатор книги

with tracer.start_as_current_span("API GET_BOOK"):
  # Получить информацию о книге
  api_response = api_instance.books_get()
  pprint(api_response)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.Book(789, "fantastika", "Pushkin", "example")
'''body = {
  "author": "Pushkin",
  "genre": "fantastika",
  "id": 789,
  "title": "example"
} # Book
body = swagger_client.Book(body)'''
book_id = 789 # int | Идентификатор книги

with tracer.start_as_current_span("API UPDATE_BOOK"):
  # Обновить информацию о книге
  api_response = api_instance.books_book_id_put(body, book_id)
  pprint(api_response)

with tracer.start_as_current_span("API BOOKS_LIST"):
  # Получить список книг
  api_response = api_instance.books_get()
  pprint(api_response)

# create an instance of the API class
author = 'Pushkin' # str | Автор книги (optional)
genre = 'fantastika' # str | Жанр книги (optional)
title = 'example' # str | Название книги (optional)

with tracer.start_as_current_span("API SEARCH"):
  # Поиск книг по различным критериям
  api_response = api_instance.books_search_get(author=author, genre=genre, title=title)
  pprint(api_response)


# create an instance of the API class


body = {
  "author": "Pushkin",
  "genre": "fantastika",
  "id": 777,
  "title": "example1"
} # Book
api_response = api_instance.books_post(body)

# Удалить книгу
with tracer.start_as_current_span("API DELETE_BOOK"):
  api_instance.books_book_id_delete(777)
with tracer.start_as_current_span("API DELETE_BOOK"):
  api_instance.books_book_id_delete(789)
