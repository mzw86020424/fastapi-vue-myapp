from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import schemas
import models

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    
    return blogs

def create(blog: schemas.Blog, db: Session, current_user):
    user_ids = [d for d in current_user]
    user_id = user_ids[0].id
    new_blog = models.Blog(title=blog.title, body=blog.body, user_id=user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog

def delete(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not found')
    blog.delete(synchronize_session=False)
    db.commit()
    
    return 'Deletion completed'

def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not found')
    blog.update(request.dict())
    db.commit()
    
    return 'Update compelted'