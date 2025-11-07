from sqlalchemy import create_engine, Column, Integer, Float, Boolean, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, Session
from datetime import datetime
from random import random

engine = create_engine('sqlite:///lab.db', echo=False)
Base = declarative_base()

# tabela łącząca Subject i Experiment (relacja wiele-do-wielu)
subject_experiment = Table(
    'subject_experiment',
    Base.metadata,
    Column('subject_id', Integer, ForeignKey('subjects.id')),
    Column('experiment_id', Integer, ForeignKey('experiments.id'))
)

class Experiment(Base):
    __tablename__ = 'experiments'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    type = Column(Integer)
    finished = Column(Boolean, default=False)
    subjects = relationship("Subject", secondary=subject_experiment, back_populates="experiments")
    data_points = relationship("DataPoint", back_populates="experiment")

class DataPoint(Base):
    __tablename__ = 'data_points'
    id = Column(Integer, primary_key=True)
    real_value = Column(Float)
    target_value = Column(Float)
    experiment_id = Column(Integer, ForeignKey("experiments.id"))
    experiment = relationship("Experiment", back_populates="data_points")

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    gdpr_accepted = Column(Boolean, default=False)
    experiments = relationship("Experiment", secondary=subject_experiment, back_populates="subjects")
