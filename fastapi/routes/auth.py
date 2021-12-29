from database import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from hashing import Hash
from sqlalchemy.orm import Session
import models
import tokens

router = APIRouter(
    tags = ['Auth']
)

@router.post('/login')
# def login(request: schemas.Login, db: Session=Depends(get_db)):
def login(request: OAuth2PasswordRequestForm = Depends(),db: Session=Depends(get_db)):
    # OAuth2PasswordRequestFormはemail属性を持っていないため、usernameの中にemailを入れる
    user = db.query(models.User).filter(models.User.email == request.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Credentials')

    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect Password')

    access_token = tokens.create_access_token({"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer"}