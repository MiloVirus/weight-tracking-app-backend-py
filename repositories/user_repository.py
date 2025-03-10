from sqlalchemy.orm import Session
from typing import List, Optional
from sqlmodel import SQLModel
from models.user import User
from repositories.BaseRepository import BaseRepository
from schemas.user import UserCreate, UserResponse

class UserRepository(BaseRepository):
    def __init__(self, db:Session):
        self.db = db

    
    def create(self, obj_data: UserCreate) -> UserResponse:
        user = User(**obj_data.model_dump())
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return UserResponse.model_validate(user)
    
    def get_by_id(self, obj_id: int) -> Optional[UserResponse]:
        return self.db.query(User).filter(User.id == obj_id).first()
    

    def get_all(self) -> List[UserResponse]:
        users = self.db.query(User.id, User.name, User.email).all()  
        return [UserResponse(id=u.id, name=u.name, email=u.email) for u in users]
    
    def update(self, obj_id: int, obj_data: dict) -> Optional[User]:
        user = self.get_by_id(obj_id)
        if user:
            for key, value in obj_data.items():
                setattr(user,key,value)
            self.db.commit()
            self.db.refresh(user)
        return user
    
    def delete(self, obj_id: int) -> bool:
        user = self.get_by_id(obj_id)
        if user:
            self.db.delete(user)
            self.db.commit()
            return True
        return False