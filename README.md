# Электронный дневник

Проект создан в учебный целях.

Скрипт содержит ряд функций для работы с базой данных электронного дневника.

## 1. Подключение
Файл `db_hack.py` должен быть размещен в том же месте что и файл `manage.py`.

## 2. Описание функций

`db_hack.get_schoolkid(schoolkid_name)` - В качестве аргумента принимает строку с фамилией и именем ученика (например: Петров Иван), возвращает объект с учетной записью ученика, если найдена одна запись. Если найдено больше, чем одна запись, необходимо в качестве аргумента передать строку с фамилией, именем и отчеством ученика (например: Петров Иван Иванович) 

`db_hack.fix_marks(schoolkid)` - В качестве аргумента принимает учетную запись ученика, находит все оценки 2 и 3 и исправляет на 5.

`db_hack.remove_chastisements(schoolkid)` - В качестве аргумента принимает учетную запись ученика, удаляет все замечания ученика.

`db_hack.create_commendation(schoolkid, subject_name)` - В качестве аргументов принимает учетную запись ученика и строку с наименованием предмета. Для указанного ученика создает похвалу.

## 3. Пример использования:
```python
$ python manage.py shell
>>> import db_hack
>>> schoolkid = db_hack.get_schoolkid('Петров Иван') 
>>> schoolkid.full_name
'Петров Иван Иванович'
>>> db_hack.fix_marks(schoolkid)
>>> db_hack.remove_chastisements(schoolkid) 
>>> db_hack.create_commendation(schoolkid, 'Музыка')
```
## Цели проекта:

Код написан в учебных целях. Это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
