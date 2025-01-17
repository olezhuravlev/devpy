# Домашнее задание к лекции 9.«Работа с библиотекой requests, http-запросы»

## Задача №1

Кто самый умный супергерой? Есть [API по информации о супергероях](https://superheroapi.com/?ref=apilist.fun#appearance)
. Нужно определить кто самый умный(intelligence) из трех супергероев- Hulk, Captain America, Thanos. Для определения id
нужно использовать метод _/search/name_

Токен, который нужно использовать для доступа к API: 2619421814940190.  
Таким образом, все адреса для доступа к API должны начинаться с https://superheroapi.com/api/2619421814940190/.

> :warning: Недавно сервис SuperHero API переехал на заблокированный Роскомнадзором IP-адрес, из-за чего некоторые интернет-провайдеры заблокировали к нему доступ, он может быть недоступен. В таком случае решайте это задание на [REPL.it](https://repl.it/) — оттуда всё должно быть доступно.

===

Решение:

API is permanently out of order.

---

## Задача №2

У Яндекс.Диска есть очень удобное и простое API. Для описания всех его методов
существует [Полигон](https://yandex.ru/dev/disk/poligon/). Нужно написать программу, которая принимает на вход путь до
файла на компьютере и сохраняет на Яндекс.Диск с таким же именем.

1. Все ответы приходят в формате json;
2. Загрузка файла по ссылке происходит с помощью метода put и передачи туда данных;
3. Токен можно получить кликнув на полигоне на кнопку "Получить OAuth-токен".

HOST: https://cloud-api.yandex.net:443

*Важно:* Токен публиковать в github не нужно, переменную для токена нужно оставить пустой!

Шаблон для программы

```python
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""
        # Тут ваша логика
        return 'Вернуть ответ об успешной загрузке'


if __name__ == '__main__':
    uploader = YaUploader('<Your Yandex Disk token>')
    result = uploader.upload('c:\my_folder\file.txt')
```

===

Решение:

https://github.com/olezhuravlev/devpy/blob/main/9.http.requests/excercise2.py

---

## Задача 3*

Самый важный сайт для программистов это [stackoverflow](https://stackoverflow.com/). И у него тоже
есть [API](https://api.stackexchange.com/docs)
Нужно написать программу, которая выводит все вопросы за последние два дня и содержит тэг 'Python'. Для этого задания
токен не требуется.

===

Решение:

https://github.com/olezhuravlev/devpy/blob/main/9.http.requests/excercise3.py

---
