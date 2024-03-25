### Задания 1 и 2
Sql-команды для заданий 1 и 2 расположены в папке sql_task с названиями task_1.sql и task_2.sql соответственно

### Запуск автотестов
1. Склонировать репозиторий
2. В файле configuration.py поменять адрес сервера в константе BASE_URL, после генерации
3. Установить python 3, если не установлен
4. Выполнить команду `python -m venv venv`
5. Выполнить команду `venv\Scripts\activate.bat`
6. Установить локально пакет request командой `pip install requests`
7. Установить локально пакет pytest командой `pip install pytest`
8. Запустить файл order_test.py командой `pytest .\order_test.py`
9. Должен получиться результат как на скриншоте result.png