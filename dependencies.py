# dependencies.py
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models import User

def get_current_user(db: Session = Depends(get_db)):
    # Here you’d verify auth token, then fetch the user
    # For now, let's mock it
    user = db.query(User).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    return user
