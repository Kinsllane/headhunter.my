from sqlalchemy import Integer, and_, func, text, insert, select, update
from db import engine
from models import metadata_obj, workers_table, Workload


class SyncCore:
    @staticmethod
    def create_tables():
        engine.echo = False
        metadata_obj.drop_all()
        metadata_obj.create_all(engine)
        engine.echo = True

    @staticmethod
    def insert_workers():
        with engine.connect() as con:
            stmt = insert(workers_table).values(
                [
                    {"username": "Jack"},
                    {"username": "Michael"},
                ]
            )
            con.execute(stmt)
            con.commit()

    @staticmethod
    def select_workers():
        with engine.connect() as con:
            engine.echo = False
            query = select(workers_table)
            result = con.execute(query)
            workers = result.scalars().all()
            print(f"{workers=}")

    @staticmethod
    def update_worker(worker_id: int=2, new_username: str='ГРЫША'):
        with engine.connect() as con:
            # stmt = text("UPDATE workers SET username=:username WHERE id=:id")  ---- 1 способ
            # stmt = stmt.bindparams(username=new_username, id=worker_id)
            # con.execute(stmt)
            # con.commit()
            stmt = (
                update(workers_table).values(username=new_username).filter_by(id=worker_id) # 2 способ
            )
            con.execute(stmt)
            con.commit()



