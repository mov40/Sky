from sqlalchemy import create_engine

# Подключение к базе данных

db = create_engine('postgresql://myuser:mypassword@localhost:5432/mydatabase')


# Тест №1: Проверка добавления студента
def test_create_student():
    connection = db.connect()

    # Получаем максимальный ID студентов
    max_id = connection.execute(
        "SELECT MAX(user_id) FROM student"
     ).etchone()[0]
    new_id = max_id + 1 if max_id else 1

    # Добавляем студента
    insert_sql = (
        f"INSERT INTO student "
        f"(user_id, level, education_form, subject_id) "
        f"VALUES ({new_id}, 'Beginner', 'personal', 1)"
    )
    connection.execute(insert_sql)

    # Проверяем добавление
    select_sql = (
        f"SELECT COUNT(*) FROM student "
        f"WHERE user_id={new_id}"
    )
    result = connection.execute(select_sql).fetchone()[0]
    assert result == 1

    # Удаляем студента после теста
    delete_sql = (
        f"DELETE FROM student "
        f"WHERE user_id={new_id}"
    )
    connection.execute(delete_sql)
    connection.close()


# Тест №2: Проверка обновления названия предмета
def test_update_subject():
    connection = db.connect()

    # Получаем максимальный ID предметов
    max_id = connection.execute(
        "SELECT MAX(subject_id) FROM subject"
    ).fetchone()[0]

    new_id = max_id + 1 if max_id else 1

    # Добавляем предмет
    insert_sql = (
        f"INSERT INTO subject "
        f"(subject_id, subject_title) VALUES ({new_id}, 'Экономика')"
    )
    connection.execute(insert_sql)

    # Обновляем название предмета
    update_sql = (
        f"UPDATE subject "
        f"SET subject_title='Волейбол' "
        f"WHERE subject_id={new_id}"
    )
    connection.execute(update_sql)

    # Проверяем обновление
    select_sql = (
        f"SELECT subject_title "
        f"FROM subject "
        f"WHERE subject_id={new_id}"
    )
    updated_subject = connection.execute(select_sql).fetchone()[0]
    assert updated_subject == 'Волейбол'

    # Удаляем предмет после теста
    delete_sql = (
        f"DELETE FROM subject "
        f"WHERE subject_id={new_id}"
    )
    connection.execute(delete_sql)
    connection.close()


# Тест №3: Проверка удаления предмета
def test_delete_subject():
    connection = db.connect()

    # Получаем максимальный ID предметов
    max_id = connection.execute(
        "SELECT MAX(subject_id) FROM subject"
    ).fetchone()[0]
    new_id = max_id + 1 if max_id else 1

    # Добавляем предмет
    insert_sql = (
        f"INSERT INTO subject "
        f"(subject_id, subject_title) VALUES ({new_id}, 'Правоведение')"
    )
    connection.execute(insert_sql)

    # Проверяем наличие предмета
    select_sql = (
        f"SELECT COUNT(*) "
        f"FROM subject "
        f"WHERE subject_id={new_id}"
    )
    result = connection.execute(select_sql).fetchone()[0]
    assert result == 1

    # Удаляем предмет
    delete_sql = (
        f"DELETE FROM subject "
        f"WHERE subject_id={new_id}"
    )
    connection.execute(delete_sql)

    # Проверяем удаление
    select_sql = (
        f"SELECT COUNT(*) "
        f"FROM subject "
        f"WHERE subject_id={new_id}"
    )
    result = connection.execute(select_sql).fetchone()[0]
    assert result == 0

    connection.close()
