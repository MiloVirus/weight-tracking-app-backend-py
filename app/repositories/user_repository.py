from sqlalchemy.orm import Session
from typing import List, Optional
from app.database.models.user import User
from app.repositories.BaseRepository import BaseRepository
from exceptions import UserNotFoundException
from sqlalchemy.exc import SQLAlchemyError

class UserRepository(BaseRepository[User]):
    def __init__(self, db: Session):
        self.db = db

    def create(self, obj_data: User) -> User:
        self.db.add(obj_data)
        self.db.commit()
        self.db.refresh(obj_data)
        return obj_data

    def get_by_id(self, obj_id: int) -> Optional[User]:
        return self.db.query(User).filter(User.id == obj_id).first()

    def get_all(self) -> List[User]:
        return self.db.query(User).all()

    def update(self, obj_id: int, obj_data: dict) -> Optional[User]:
        user = self.get_by_id(obj_id)
        if user:
            for key, value in obj_data.items():
                setattr(user, key, value)
            self.db.commit()
            self.db.refresh(user)
        return user

    def delete(self, obj_id: int) -> None:
        try:
            user = self.get_by_id(obj_id)
            if not user:
                raise UserNotFoundException(obj_id)

            self.db.delete(user)  # Corrige el uso de delete
            self.db.commit()
        except SQLAlchemyError as e:
            self.db.rollback()
            logger.error(f"DB error while deleting user {obj_id}: {str(e)}")
            raise


