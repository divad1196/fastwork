from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, Integer, String

engine = create_engine("sqlite:///test_migration.db")

SessionMaker = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


class Contact(Base):
    name = Column(String)
    # forname = Column(String)


Base.metadata.create_all(bind=engine)