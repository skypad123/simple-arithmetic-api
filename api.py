from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from arithmetic import MathWorksheetGenerator,QuestionInfo

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_item(mathType: str = "+", maxNum: int = 999 , questionCount: int = 10) -> QuestionInfo :
    questionGen = MathWorksheetGenerator(mathType, maxNum)
    questionList = questionGen.get_list_of_questions(questionCount)

    return {
        "questions": [ [" ".join([ str(inner) for inner in item[:3] ]),item[3]] for item in questionList]
    }