ABoard

Очень простой учебный пример django-проекта. Содержит примитивную доску объявлений,
систему авторизации и регистрации пользователей, пример реализации API.

В проекте используется БД MySQL, redis для хранения сессий. На момент
коммита модуль для redis отключен, чтоб заработало достаточно снять комментарии.
При отключенном redis сессии хранятся в mysql.

Для поиска по объявлениям подключен Sphinx, в качестве очереди - Celery.

Т.к. проект учебный и его задача - быть простейшим примером (максимально упрощенным 
и легким для понимания), то реализация
функциональности минимальна - один тест, один API запрос, и т.п.

Создание проекта: /usr/local/bin/django-admin.py startproject aboard
Создание приложения: python3 manage.py startapp catalog

Запуск проекта: python3 manage.py runserver






