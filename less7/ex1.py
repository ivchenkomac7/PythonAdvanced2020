# 1) Написать контекстный менеджер для работы с SQLite DB.
# 2) Создать базу данных студентов. У студента есть факультет,
# группа, оценки, номер студенческого билета. Написать программу,
# с двумя ролями: Администратор, Пользователь. Администратор
# может добавлять, изменять существующих студентов.
# Пользователь может получать список отличников, список всех
# студентов, искать студентов по по номеру студенческого, получать
# полную информацию о конкретном студенте (включая оценки,
# факультет)

import sqlite3

students_input = [("Elon", "Mask"), ("Bill", "Gates"), ("Mark", "Zuckerberg")]

# conn = sqlite3.connect("students.db")
#
# cursor = conn.cursor()
#
# res = cursor.execute("INSERT INTO students ('name', 'surname') VALUES (?, ?)", students_input)
#
# conn.commit()
# conn.close()


def create_connection(db_name):
    connection = sqlite3.connect(db_name)
    return connection


def write_data_to_db(connection, query, data):
    try:
        with connection:
            connection.executemany(query, data)
    except sqlite3.IntegrityError as error:
        print(f"Error occurs: {error}")
        return False
    else:
        print("Запись данных прошла успешно")
        return True


def get_all_from_db(connection, query):
    result = [row for row in connection.execute(query)]
    return result


if __name__ == "__main__":
    conn = create_connection("students.db")
    query_insert = "INSERT INTO students ('name', 'surname') VALUES (?, ?)"
    query_get_all = "SELECT * FROM students"

    write_data_to_db(conn, query_insert, students_input)

    print(get_all_from_db(conn, query_get_all))

    conn.close()
