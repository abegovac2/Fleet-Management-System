from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String
import config

DATABASE_URL = \
    f"postgresql://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@{config.POSTGRES_HOST}:{config.POSTGRES_PORT}/{config.POSTGRES_DB}"

engine = create_engine(DATABASE_URL, echo = config.ECHO)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Driver(Base):
    __tablename__ = 'driver'
    id = Column(Integer, primary_key=True)
    full_name = Column(String(100))
    points = Column(Integer)

db = SessionLocal()

def update_driver_points(driver_id: int, points: int):
    driver = db.query(Driver).filter(Driver.id == driver_id).first()  
    driver.points += points
    db.commit()