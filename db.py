import enum
from enum import StrEnum

from sqlalchemy import create_engine, text, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from typing import Annotated
from config import settings

engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
)

sessions = sessionmaker(engine)

str_256 = Annotated[str, 256]
class Base(DeclarativeBase):
    type_annotated_map = {
        str_256: String(256)
    }


class Workload(enum.Enum):
    parttime = "parttime"
    fulltime = "fulltime"























# def init_db():
#     load_dotenv()
#     db_name = os.getenv('DB_NAME')
#     user = os.getenv('USER')
#     host = os.getenv('HOST')
#     password = os.getenv('PASSWORD')
#     port = os.getenv('PORT')
#
#     try:
#         connection = psycopg2.connect(
#             host = host,
#             user = user,
#             password = password,
#             database = db_name
#         )
#         return connection
#     except Exception as e:
#         print(f"Ошибка при подключении к базе данных: {e}")
#         return None
#
#
# def create_table():
#     connection = init_db()
#     if connection is None:
#         raise "Ошибка при подключении к базе данных"
#     with connection:
#         with connection.cursor() as cursor:
#             cursor.execute("""
#                 CREATE TABLE IF NOT EXISTS tasks(
#                 id SERIAL PRIMARY KEY,
#                 title VARCHAR(30),
#                 description TEXT,
#                 completed BOOLEAN NOT NULL DEFAULT FALSE
#                 )
#                 """)
#             connection.commit()
#
#
# def add_task(title: str, description: str):
#     connection = init_db()
#     if connection is None:
#         raise "Ошибка при подключении к базе данных"
#     with connection:
#         with connection.cursor() as cursor:
#             cursor.execute(f"""
#                 INSERT INTO tasks (title, description)
#                 VALUES(%s, %s)
#                 """, (title, description))
#             connection.commit()
#
#
# def get_task():
#     connection = init_db()
#     tasks = []
#     if connection is None:
#         raise "Ошибка при подключении к базе данных"
#     with connection:
#         with connection.cursor() as cursor:
#             cursor.execute("""SELECT * FROM tasks""")
#             tasks = cursor.fetchall()
#             return tasks
#
#
# def update_tasks(task_id, completed):
#     connection = init_db()
#     if connection is None:
#         raise "Ошибка при подключении к базе данных"
#     with connection:
#         with connection.cursor() as cursor:
#             cursor.execute(f"""
#                 UPDATE tasks SET completed = %s WHERE id = %s
#                 """, (completed, task_id))
#             connection.commit()
#
#
# def delete_tasks(task_id):
#     connection = init_db()
#     if connection is None:
#         raise "Ошибка при подключении к базе данных"
#     with connection:
#         with connection.cursor() as cursor:
#             cursor.execute(f"""
#                     DELETE FROM tasks WHERE id = %s
#                     """, (task_id,))
#             connection.commit()