from fastapi import FastAPI
from schemas import Blog
from database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post('/blog')
def create(blog: Blog):
    return {'data': blog}