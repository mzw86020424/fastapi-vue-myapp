from database import get_db
from fastapi import APIRouter, Depends
from functions import user
from schemas import User, ShowUser
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/user',
    tags=['users']
)

@router.post('/')
def create_user(request: User, db: Session = Depends(get_db)):
    return user.create_user(request, db)

@router.get('/{id}', response_model=ShowUser)
def get_user(id: int, db: Session=Depends(get_db)):
    return user.get_user(id, db)