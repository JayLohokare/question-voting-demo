from fastapi import FastAPI, HTTPException
from repo import get_user_repo, create_user_repo, create_question_repo, get_question_repo, get_all_question_repo, upvote_question_repo

app = FastAPI()


# Opt 1
# @app.post("/upvote/")
# Opt 2
# @app.post("/questions/{question_id}/upvote")


@app.post("/upvote/")
def upvote_question(question_id: int, user_id: int):
    # TODO Track User > question upvotes to dedup upvotes
    resp = upvote_question_repo(question_id, user_id)
    if resp is not None:
        raise resp
    return "Success"

@app.get("/questions/")
def get_all_question():
    questions = get_all_question_repo()
    if questions is None:
        raise HTTPException(status_code=404, detail="Questions not found")
    return questions

@app.get("/questions/{question_id}")
def get_question(question_id: int):
    question = get_question_repo(question_id)
    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return question

@app.post("/questions/")
def create_question(question_str: str, user_id: int):
    # basic data validation
    if question_str == "" or user_id == None:
        raise HTTPException(status_code=500, detail="User not found")
    question = create_question_repo(question_str, user_id)
    return question
# {
#     "down_votes_count": 0,
#     "id": 3,
#     "user_id": 1,
#     "upvotes_count": 0,
#     "question_str": "Amazing question 1"
# }

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = get_user_repo(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users/")
def create_user(name: str, email: str):
    user = create_user_repo(name, email)
    return user
   
# {
#     "name": "Jay",
#     "is_active": true,
#     "id": 1,
#     "email": "jay@test.com"
# }


@app.post("/esi/")
def evaluate_esi(oxygen_saturation: int, respiratory_rate: int, systolic_bp: int):
    if respiratory_rate >= 35 or oxygen_saturation < 88 or systolic_bp < 90:
        return 1
    elif respiratory_rate >= 30 or oxygen_saturation < 89 or systolic_bp < 100:
        return 2
    elif respiratory_rate >= 21 or oxygen_saturation < 91 or systolic_bp < 110:
        return 3
    else:
        return 4



if __name__ == '__main__':
    app.run(debug=True)



####
# Landing page -> Global Questions : Popular / Recent etc
# User page -> Questions by user ; Answers by the user 

# Decision for MVP :
# POST /question Create a new question, return question object 
# GET /question/id Return question object based on id

# GET /home_page returns all questions paginated based on some criteria (for now timestamp )

# GET user/id/questions/ returns all questions by user 
