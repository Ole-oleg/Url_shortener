# URL shortener for avito

Простой аналог bitly на django. Посмотреть на его работу можно [тут.](http://18.223.136.2/) Сайт загружен на AWS по адрусу http://18.223.136.2/

# Возможности
Есть простой UI с двумя плями: url и slug. Первое — собственно url, который Вы хотите сткратить, второе — человекочитаемая форма (необязательный параметр). Например 
  - URL: https://www.avito.ru/moskva/doma_dachi_kottedzhi 
  - SLUG: avito_dachi 
  - Результат: http://18.223.136.2/avito_dachi

JSON API сайта находится тут: http://18.223.136.2/api/ . Он принимает HTTP GET запросы с двумя параметрами url (обязательный) и slug (опциональный). Например:
```sh
http://18.223.136.2/api/?url=google.com&slug=search
```
Ответ:
```sh
{"status": "ok", "urll": "google.com", "short_url": "http://18.223.136.2/search"}
```
Если url не существует:
```sh
{"status": "fail", "comment": "url validation fail", "url": "gooom"}
```
Если slug уже занят:
```sh
{"status": "fail", "comment": "slug in database", "slug": "search"}
```
# Инструкция по установке
В файле requirements.txt перечислены все необходимые python пакеты. Их необходимо установить. Кроме того, вам потребуется Redis сервер, чтобы установить его в Linux введите команду:
```sh
$ sudo apt install redis-server
```
Запустите Redis:
```sh
$ redis-server
```
Затем в директории проекта запустите django сервер:
```sh
$ python3 manage.py runserver
```
Сайт должен стать доступен по адресу http://127.0.0.1:8000

# Нагрузочное тестрирование
В директории есть файл locustfile.py. В нем - код простенького нагрузочного теста api и домашней страницы. Чтобы запустить его, нужно ввести:
```sh
$ locust
```
далее, в браузере набираем localhost:8089, настраиваем параметры и тестируем.
