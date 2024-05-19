# swagger_client.DefaultApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**books_book_id_delete**](DefaultApi.md#books_book_id_delete) | **DELETE** /books/{bookId} | Удалить книгу
[**books_book_id_get**](DefaultApi.md#books_book_id_get) | **GET** /books/{bookId} | Получить информацию о книге
[**books_book_id_put**](DefaultApi.md#books_book_id_put) | **PUT** /books/{bookId} | Обновить информацию о книге
[**books_get**](DefaultApi.md#books_get) | **GET** /books | Получить список книг
[**books_post**](DefaultApi.md#books_post) | **POST** /books | Добавить новую книгу
[**books_search_get**](DefaultApi.md#books_search_get) | **GET** /books/search | Поиск книг по различным критериям

# **books_book_id_delete**
> books_book_id_delete(book_id)

Удалить книгу

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
book_id = 789 # int | Идентификатор книги

try:
    # Удалить книгу
    api_instance.books_book_id_delete(book_id)
except ApiException as e:
    print("Exception when calling DefaultApi->books_book_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **int**| Идентификатор книги | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **books_book_id_get**
> Book books_book_id_get(book_id)

Получить информацию о книге

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
book_id = 789 # int | Идентификатор книги

try:
    # Получить информацию о книге
    api_response = api_instance.books_book_id_get(book_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->books_book_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **int**| Идентификатор книги | 

### Return type

[**Book**](Book.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **books_book_id_put**
> Book books_book_id_put(body, book_id)

Обновить информацию о книге

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.Book() # Book | 
book_id = 789 # int | Идентификатор книги

try:
    # Обновить информацию о книге
    api_response = api_instance.books_book_id_put(body, book_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->books_book_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Book**](Book.md)|  | 
 **book_id** | **int**| Идентификатор книги | 

### Return type

[**Book**](Book.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **books_get**
> list[Book] books_get()

Получить список книг

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Получить список книг
    api_response = api_instance.books_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->books_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Book]**](Book.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **books_post**
> Book books_post(body)

Добавить новую книгу

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.Book() # Book | 

try:
    # Добавить новую книгу
    api_response = api_instance.books_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->books_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Book**](Book.md)|  | 

### Return type

[**Book**](Book.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **books_search_get**
> list[Book] books_search_get(author=author, genre=genre, title=title)

Поиск книг по различным критериям

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
author = 'author_example' # str | Автор книги (optional)
genre = 'genre_example' # str | Жанр книги (optional)
title = 'title_example' # str | Название книги (optional)

try:
    # Поиск книг по различным критериям
    api_response = api_instance.books_search_get(author=author, genre=genre, title=title)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->books_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **author** | **str**| Автор книги | [optional] 
 **genre** | **str**| Жанр книги | [optional] 
 **title** | **str**| Название книги | [optional] 

### Return type

[**list[Book]**](Book.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

