from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import config

DATABASE_URL = \
    f"postgresql://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@{config.POSTGRES_HOST}:{config.POSTGRES_PORT}/{config.POSTGRES_DB}"

engine = create_engine(DATABASE_URL, echo = config.ECHO)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
