from database import Base, engine
from fastapi import FastAPI
from routes import blog, user

app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)

Base.metadata.create_all(engine)