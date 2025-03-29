from types import new_class

from sqlalchemy import select

from db import engine, sessions, Base, Workload
from models import ResumesOrm, WorkersOrm


class SyncOrm:
    @staticmethod
    def create_table():
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    @staticmethod
    def insert_workers():
        with sessions() as session:
            session.add_all([WorkersOrm(username="Michael"),WorkersOrm(username="Jack"),])
            session.commit()


    @staticmethod
    def select_workers():
        with sessions() as session:
            worker_id = 1
            worker_jack = session.get(WorkersOrm, worker_id)
            result = session.execute(select(WorkersOrm))
            workers = result.scalars().all()
            print(f"{workers=}")

    @staticmethod
    def update_worker(worker_id: int = 2, new_username: str = "Misha"):
        with sessions() as session:
            worker = session.get(WorkersOrm, worker_id)
            worker.username = new_username
            session.commit()












    @staticmethod
    def insert_resumes():
        with sessions() as session:
            resume_jack_1 = ResumesOrm(
                title="Python Junior Developer", compensation=50000, workload=Workload.fulltime, workers=1)
            resume_jack_2 = ResumesOrm(
                title="Python Разработчик", compensation=150000, workload=Workload.fulltime, workers=1)
            resume_michael_1 = ResumesOrm(
                title="Python Data Engineer", compensation=250000, workload=Workload.parttime, workers=2)
            resume_michael_2 = ResumesOrm(
                title="Data Scientist", compensation=300000, workload=Workload.fulltime, workers=2)
            session.add_all([resume_jack_1, resume_jack_2,
                             resume_michael_1, resume_michael_2])
            session.commit()
