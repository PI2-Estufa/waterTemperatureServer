import datetime 
import os
from sqlalchemy import create_engine, Column, Integer, Float, Unicode, Sequence, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine(os.environ.get("POSTGRES_URL"), echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class WaterTemperature(Base):

    __tablename__ = 'waterTemperature'

    id = Column(Integer, 
            Sequence('waterTemperature_id_seq'), primary_key=True)
    value = Column(Float)
    created_date = Column(DateTime, default=datetime.datetime.utcnow) 
    unit = Column(Unicode(2), nullable=False)

Base.metadata.create_all(engine)