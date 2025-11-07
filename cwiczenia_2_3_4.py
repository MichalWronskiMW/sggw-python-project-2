from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Session
from datetime import datetime
from random import random
import os

engine = create_engine('sqlite:///lab.db', echo=False)
Base = declarative_base()

class Experiment(Base):
    __tablename__ = 'experiments'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    type = Column(Integer)
    finished = Column(Boolean, default=False)
    data_points = relationship("DataPoint", back_populates="experiment")

class DataPoint(Base):
    __tablename__ = 'data_points'
    id = Column(Integer, primary_key=True)
    real_value = Column(Float)
    target_value = Column(Float)
    experiment_id = Column(Integer, ForeignKey("experiments.id"))
    experiment = relationship("Experiment", back_populates="data_points")

Base.metadata.create_all(engine)

with Session(engine) as session:
    e1 = Experiment(title="Experiment A", type=1)
    e2 = Experiment(title="Experiment B", type=2)
    session.add_all([e1, e2])

    dpoints = [DataPoint(real_value=random()*100, target_value=random()*100) for _ in range(10)]
    session.add_all(dpoints)
    session.commit()

    exps = session.query(Experiment).all()
    dps = session.query(DataPoint).all()
    print("Experiments added:")
    for e in exps:
        print(e.id, e.title, e.type, e.created_at, e.finished)
    print("\nDataPoints added:")
    for d in dps:
        print(d.id, d.real_value, d.target_value)

    session.query(Experiment).update({Experiment.finished: True})
    session.commit()

    print("\nExperiments after update:")
    for e in session.query(Experiment).all():
        print(e.id, e.title, e.finished)

## Usunięcie wierszy z bazy
    # session.query(DataPoint).delete()
    # session.query(Experiment).delete()
    # session.commit()

    # print("\nCounts after delete:")
    # print("Experiments:", session.query(Experiment).count())
    # print("DataPoints:", session.query(DataPoint).count())

## Usunięcie bazy na potrzeby ćwiczenia IV
# if os.path.exists("lab.db"):
#     os.remove("lab.db")
