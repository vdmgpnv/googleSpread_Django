# Тестовое задание для компании numbers

После клонирования репозитория необходимо установить все необходимые зависимости. Для этого в корневой папке откройте терминал и в командной строке выполните команду:

    pip install -r requirements.txt

После установки всех зависимостей для python перейти в папку /googlespread/script. В этой папке находится скрипт выполнения парсинга данных из таблицы и занесения этих данных в БД.

## Для запуска скрипта 

Чтобы запустить скрипт выполните команду:

    python work_with_data.py 

Это запустит скрипт, который будет проверят данные каждый час, если срок поставки, указанный в таблице истек, будет отправленно сообщение в час телеграмма с номером заказа. 

Ссылка на чат телеграмма:

> https://t.me/+H4u_qRPiupI2MjRi

## Для запуска сервера Django 

Чтобы запустить сервер Django либо откройте новый терминал(если не хотите останавливать выполнения скрипта P.S справедливо заметить, что на UNIX системах лучше использовать contrib), либо остановите скрипт и перейдите в папку /googlespread/ и выполните команду:

    python manage.py runserver

После запуска БЭК части проекста, откройте новый терминал и перейдите в папку /frontend и выполните команду для установки зависимостей:

    npm install

После того, как все зависимости были установлены, выполните команду 

    npm start 

У вас откроется приложение реакт, которое делает запрос к БЭК-части и выводит данные в виде таблицы, которые хранятся в БД.

ссылка на таблицу: https://docs.google.com/spreadsheets/d/1zRFmvrujT03J-pzbK77WF5HXXj-8-zS1lWjkNvf7yS0/edit#gid=0


# P.S. Инструкция предпологает, что на системе уже установлены Node.js и Python
