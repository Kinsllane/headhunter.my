import datetime

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, func, text
from sqlalchemy.orm import Mapped, mapped_column
from db import Base, Workload, str_256
from typing import Annotated

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(default=func.now())]
updated_at = Annotated[datetime.datetime, mapped_column(
    default=func.now(),
    onupdate=func.now
)]

class WorkersOrm(Base):
    __tablename__ = 'workers'

    id: Mapped[intpk]
    username: Mapped[str] = mapped_column()


class ResumesOrm(Base):
    __tablename__ = 'resumes'

    id: Mapped[intpk]
    title: Mapped[str_256]
    compensation: Mapped[int] = mapped_column(nullable=True)
    workload: Mapped[Workload]
    workers: Mapped[int] = mapped_column(ForeignKey('workers.id', ondelete="CASCADE"))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]






metadata_obj = MetaData()

workers_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String),
)


