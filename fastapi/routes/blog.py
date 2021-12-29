from database import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from functions import blog
from schemas import Blog, ShowBlog, User
from sqlalchemy.orm import Session
from typing import List
import models, oauth2

router = APIRouter(
    prefix='/blog',
    tags=['blogs'],
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: Blog, db: Session = Depends(get_db)):
    return blog.create(request, db)

@router.get('/', response_model=List[ShowBlog])
def all_fetch(db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowBlog)
def show(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not available')
    return blog

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: Blog, db: Session = Depends(get_db)):
    return blog.update(id, request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session=Depends(get_db)):
    return blog.delete(id, db)