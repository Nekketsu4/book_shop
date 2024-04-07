# collect of money (DRF)

Тестовый пет-проект на DRF по сбору денег
для разного рода нужд (ДР, свадьбы и тд.)




## Содержание

- [Содержание](#содержание)
- [Диаграмма](#диаграмма)
- [Технологии](#технологии)
- [Установка](#установка)
- [Инструкция](#инструкция)



## UML Диаграмма

![Image alt](https://github.com/Nekketsu4/book_shop/blob/main/uml.png)

## Технологии:

* [Python 3.10](https://www.python.org/)
* [Django 5.0.3](https://www.djangoproject.com/)
* [Django Rest Framework 3.14.0](https://www.django-rest-framework.org/)

## Установка

* Клонируйте гит репозиторий выполнив команду https://github.com/Nekketsu4/book_shop.git 
* Перейдите в папку с клоном проекта "cd path/book_shop"
* Создайте виртуальное окружение выполнив команду "python3 -m venv venv"
* Активируйте виртуальное окружение выполнив команду "source venv/bin/activate"

```
git clone https://github.com/Nekketsu4/book_shop.git
cd collect_of_money
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Инструкция

* Перед запуском приложения, создайте файл env.prod, затем зайдите в файл .env.example, скопируйте его содержимое в .env.prod и заполните поля
* Выполните команду "docker-compose -f docker-compose.yaml up -d --build" - для сборки проекта
* Выполните миграцию "docker-compose -f docker-compose.yaml exec web python manage.py migrate --noinput"
* Создайте суперпользователя(админа) 'docker-compose -f docker-compose.yaml exec web python manage.py createsuperuser --username="admin" --email=""'

```
docker-compose -f docker-compose.yaml up -d --build
docker-compose -f docker-compose.yaml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.yaml exec web python manage.py createsuperuser --username="admin" --email=""
```
