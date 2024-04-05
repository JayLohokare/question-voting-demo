from models import getSession
from models import User, Question, Upvotes
from fastapi import HTTPException

def upvote_question_repo(question_id, user_id):
    db = getSession()()

    existing_upvote =  db.query(Upvotes).filter_by(user_id=user_id, question_id=question_id).first() 
    if existing_upvote is not None:
        return HTTPException(status_code=500, detail="Already upvotes")

    question = db.query(Question).filter_by(id=question_id).first() 
    question.upvotes_count = question.upvotes_count + 1

    new_upvote = Upvotes(user_id=user_id, question_id=question_id)
    upvote = db.add(new_upvote)
    
    db.commit()
    db.close()
    return



# @TODO add params for filtering Qs
def get_all_question_repo():
    db = getSession()()
    questions = db.query(Question).all()
    db.close()
    return questions


def get_question_repo(question_id):
    db = getSession()()
    user = db.query(Question).filter(Question.id == question_id).first()
    db.close()
    return user

def create_question_repo(question_str, user_id):
    db = getSession()()
    new_question = Question(question_str=question_str, user_id=user_id)
    question = db.add(new_question)
    db.commit()
    db.refresh(new_question)
    db.close()
    return new_question

def get_user_repo(user_id: int):
    db = getSession()()
    user = db.query(User).filter(User.id == user_id).first()
    db.close()
    return user

def create_user_repo(name, email):
    db = getSession()()
    new_user = User(name=name, email=email)
    user = db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()
    return new_user