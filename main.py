from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

# CREATING A SCHEMA 
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "HI!! THIS IS MY FIRST API WITH FASTAPI"}

@app.get("/posts")
async def root():
    return {"post": "Congratulations on your first Post!!"}

@app.post("/posts")
def create_posts(post: Post):
    print(post.rating)
    return {"data": "New Post Created"}
# something else that is more new