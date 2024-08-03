from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [
    {"title": "title post 1", "content": "content post 1", "id": 1},
    {"title": "favorite food", "content": "I like pizza", "id": 2}
]

@app.get("/")
def root():
    return {"message": "Hello World!"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts")
def create_posts(post: Post):
    print(post.rating)
    print(post.model_dump())
    return {"data": post}
# title str, content str