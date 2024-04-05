from sqlalchemy import Boolean, Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    question_str = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    upvotes_count = Column(Integer, default=0)
    down_votes_count = Column(Integer, default=0)

class Upvotes(Base):
    __tablename__ = "upvotes"
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer,  ForeignKey("questions.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

# class Comment(Base):
#     id = Column(Integer, primary_key=True, index=True)
#     question_str = Column(String)
#     upvotes_count = Column(Integer, default=0)
#     down_votes_count = Column(Integer, default=0)
#     user_id = Column(Integer, ForeignKey("users.id"))


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    is_active = Column(Boolean, default=True)
    items = relationship("Item", back_populates="owner")

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items")

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def getSession():
    return SessionLocal