from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.question import question_router
# import models
#
# from database import engine
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/hello")
# def hello():
#     return {"message": "World"}

app.include_router(question_router.router)