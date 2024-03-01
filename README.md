# test_project

Простой блог с использованием Django REST Framework и Docker для контейнеризации приложения. Позволяет пользователям создавать посты, добавлять комментарии к постам и ставить лайки.



## Установка 

1.Установить зависимости:

pip install -r requirements.txt

2.Применить миграции:

python manage.py migrate

3.Создать суперпользователя:

python manage.py createsuperuser

4.Запустить сервер разработки:

python manage.py runserver

5.Проверить тесты:

python manage.py test

### Также у меня подключен Docker для его запуска нужна команда:

docker-compose up --build

Запуск тестов:

docker-compose run web python manage.py test





