from datetime import date
import faker
from random import randint, choice
import sqlite3
from faker.providers import DynamicProvider


NUMBER_STUDENTS = randint(30, 50)
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = randint(5, 8)
NUMBER_TEACHERS = randint(3, 5)
# NUMBER_ASSESSMENTS = randint(10, 20)


def generate_fake_data(
    number_students, number_subjects, number_teachers
) -> tuple():

    # встановлюємо локаль
    fake_data = faker.Faker("uk_UA")

    # список предметів для нового провайдера
    school_subject_provider = DynamicProvider(
        provider_name="school_subject",
        elements=[
            "хімія",
            "фізика",
            "алгебра",
            "анатомія",
            "історія",
            "астрономія",
            "географія",
            "інформатика",
            "культура",
            "література",
            "мова",
            "фізична культура",
        ],
    )

    # додаєм нового провайдера для навчальних предметів
    fake_data.add_provider(school_subject_provider)

    fake_students = []  # тут зберігатимемо студентів
    # fake_groups = []  # тут зберігатимемо групи
    fake_subjects = []  # тут зберігатимемо предмети
    fake_teachers = []  # тут зберігатимемо вчітелів

    # Згенеруємо набір студентів у кількості number_students
    for _ in range(number_students):
        fake_students.append(fake_data.unique.name())

    # Згенеруємо набір груп у кількості number_groups
    # for _ in range(number_groups):
    #     fake_groups.append(fake_data.building_number())

    # Згенеруємо набір предметів кількості number_subjects
    for _ in range(number_subjects):
        fake_subjects.append(fake_data.unique.school_subject())

    # Згенеруємо набір вчітелів у кількості number_teachers
    for _ in range(number_teachers):
        fake_teachers.append(fake_data.unique.name())

    # return fake_students, number_groups, number_subjects, number_teachers
    return fake_students, fake_subjects, fake_teachers


# def prepare_data(students, groups, subjects, teachers) -> tuple():
def prepare_data(students, subjects, teachers) -> tuple():
    for_students = []
    # готуємо список кортежів імен студентів
    for student in students:
        for_students.append((student,))

    for_groups = []  # для таблиці group
    for id_st in range(1, NUMBER_STUDENTS + 1):
        """
        Для записів у таблицю груп нам потрібно додати id всіх студентів.
        При створенні таблиці groups для поля id ми вказуем INTEGER AUTOINCREMENT - тому кожен запис
        отримуватиме послідовне число збільшене на 1, починаючи з 1. Рандомно розподіляємо студентів по групах.
        """
        for_groups.append((randint(1, NUMBER_GROUPS), id_st))

    # готуємо список кортежів імен вітелів
    for_teachers = []
    for teacher in teachers:
        for_teachers.append((teacher,))

    for_subjects = []
    for subject in subjects:
        """
        Для записів у таблицю всіх предметів нам потрібно додати випадково id вчітелів.
        """
        for_subjects.append((subject, randint(1, NUMBER_TEACHERS)))

    start_date = date(year=2023, month=9, day=1)
    for_assessments = []
    for id_st in range(1, NUMBER_STUDENTS + 1):
        for id_sb in range(1, NUMBER_SUBJECTS + 1):
            for _ in range(1, randint(10, 20)):
                for_assessments.append(
                    (
                        id_st,
                        id_sb,
                        randint(1, 12),
                        faker.Faker().date_between(start_date=start_date, end_date="today"),
                    )
                )

    # for month in range(1, 12 + 1):
    #     # Виконуємо цикл за місяцями'''
    #     payment_date = datetime(2021, month, randint(10, 20)).date()
    #     for emp in range(1, NUMBER_EMPLOYESS + 1):
    #         # Виконуємо цикл за кількістю співробітників
    #         for_payments.append((emp, payment_date, randint(1000, 10000)))

    return for_students, for_groups, for_subjects, for_teachers, for_assessments


def insert_data_to_db(students, groups, subjects, teachers, assessments) -> None:
    # Створимо з'єднання з нашою БД та отримаємо об'єкт курсору для маніпуляцій з даними

    with sqlite3.connect("learning.db") as con:

        cur = con.cursor()

        """Заповнюємо таблицю компаній. І створюємо скрипт для вставлення, де змінні, які вставлятимемо, відзначимо
        знаком заповнювача (?) """

        sql_to_students = """INSERT INTO students(name_st)
                               VALUES (?)"""

        """Для вставлення відразу всіх даних скористаємося методом executemany курсора. Першим параметром буде текст
        скрипта, а другим - дані (список кортежів)."""

        cur.executemany(sql_to_students, students)

        # Далі вставляємо дані про співробітників. Напишемо для нього скрипт і вкажемо змінні

        sql_to_groups = """INSERT INTO groups(number_gr, fr_st)
                               VALUES (?, ?)"""

        # Дані були підготовлені заздалегідь, тому просто передаємо їх у функцію

        cur.executemany(sql_to_groups, groups)

        sql_to_teachers = """INSERT INTO teachers(name_tc)
                               VALUES (?)"""
        cur.executemany(sql_to_teachers, teachers)

        sql_to_subjects = """INSERT INTO subjects(name_sb, fr_tc)
                               VALUES (?, ?)"""
        cur.executemany(sql_to_subjects, subjects)

        # Останньою заповнюємо таблицю із зарплатами

        sql_to_assessments = """INSERT INTO assessment_subj(fr_st, fr_sb, assessment, date_in)
                              VALUES (?, ?, ?, ?)"""

        # Вставляємо дані про зарплати

        cur.executemany(sql_to_assessments, assessments)

        # Фіксуємо наші зміни в БД

        con.commit()


if __name__ == "__main__":

    students, groups, subjects, teachers, assessments = prepare_data(
        *generate_fake_data(
            NUMBER_STUDENTS,
            NUMBER_SUBJECTS,
            NUMBER_TEACHERS,
        )
    )
    insert_data_to_db(students, groups, subjects, teachers, assessments)
