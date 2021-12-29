from database import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from hashing import Hash
from sqlalchemy.orm import Session
import models
import schemas
import tokens

router = APIRouter(
    tags = ['Auth']
)

@router.post('/login')
def login(request: schemas.Login, db: Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Credentials')

    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect Password')

    access_token = tokens.create_access_token({"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer"}