![Header](https://github.com/SultanovAsadbek/Hotel_website_in_django/blob/Example/assets/main.gif)


## Описание
В настоящее время, автоматизация процессов в гостиничном бизнесе является необходимостью. В связи с этим, создание веб-приложения, кото-рое позволяет производить регистрацию гостей, управлять бронировани-ем номеров, а также учетом занятых и свободных номеров, является акту-альной задачей.
Для автоматизации работы гос-отеля, можно использовать фрейм-ворк Django.       
Django — это высокоуровневый веб-фреймворк на языке Python, который позволяет быстро и удобно создавать веб-приложения. Данный фреймворк имеет встроенный ORM, а также вспомогательные библиотеки и инструменты для реализации различных функций.


Возможности ПО:
- Авторизация.
- Вход в в систему.
- Выход из системы.
- Отправка сообщений на почту администратора гостиницы. 
- Бронирование номеров в гостинице.
- Уведомить о бронирование номера, администратор гостиницы отправив 
  на почту сообщение.
- Уведомить о регистрации пользователя, администратор гостиницы отправив 
  на почту сообщение. 
- Возможность отредактировать услуги и изображение номеров. 


## Язык программирование
![Python](https://img.shields.io/badge/python-black?style=for-the-badge&logo=python&logoColor=yellow)


## Технологии
![Django](https://img.shields.io/badge/Django-black?style=for-the-badge&logo=django&logoColor=green)
![Sqlite](https://img.shields.io/badge/sqlite3-black?style=for-the-badge&logo=sqlite&logoColor=blue)
![HTML](https://img.shields.io/badge/HTML5-black?style=for-the-badge&logo=HTML5&logoColor=orange)
![CSS](https://img.shields.io/badge/CSS3-black?style=for-the-badge&logo=CSS3&logoColor=blue)

![.env](https://img.shields.io/badge/.env-black?style=for-the-badge&logo=.env&logoColor=green)
![Django](https://img.shields.io/badge/django_jet_reboot-black?style=for-the-badge&logo=Vectorworks&logoColor=red)


## Установка и запуск проекта
**Шаг 1 :**

![taks_list_admin_page](https://github.com/SultanovAsadbek/ToDoList-Django/blob/main/Project_assets/step-1_installing.png)
> Выбираем  **Download ZIP**, скачивается проект в архивированном виде.
---


**Шаг 2 :**

![taks_list_admin_page](https://github.com/SultanovAsadbek/ToDoList-Django/blob/main/Project_assets/step-2_installing.png)
> Извлечём скачанный файл.
---


**Шаг 3 :**

![taks_list_admin_page](https://github.com/SultanovAsadbek/ToDoList-Django/blob/main/Project_assets/step-3_installing.png)
> Открываем проект в удбном нам редакторе, в моём случай это **VS Code**.
---


**Шаг 4 :**
> Создаём [виртуальное окружение](https://pyneng.readthedocs.io/ru/latest/book/01_intro/virtualenv.html) для того чтобы:
+ изолировать проекты друг от друга 
+ не засорять систему 
+ установить файл зависимости локально 
+ выполнения программы внутри этого окружения 

```
python -m venv venv
```


**Шаг 5 :**
> Активируем виртуальное окружение

``` 
./venv/scripts/activate
```


**Шаг 6:**
> Переходим в директорию проекта

```
cd ToDoList-Django-main
```


**Шаг 7:**
> Установим все необходимые библиотеки из файла зависимости ```requirements.txt```

```
pip install -r requirements.txt
```


**Шаг 8 :**
> Создадим таблицы в базе данных, затем производим миграцию

```
python manage.py makemigrations
```

```
python manage.py migrate
```


**Шаг 9:**
> Запускаем локальный сервер:

```
python manage.py runserver
```
