from repositories.BaseRepository import BaseRepository
from models.user import User
from schemas.user import UserCreate, UserResponse
from models.user import User
from fastapi import HTTPException


class UserService:
    def __init__(self, user_repository: BaseRepository[User]):
        self.user_repository = user_repository
    
    def create_user(self, user_data: UserCreate) -> UserResponse:
        user = User(**user_data.model_dump()) 
        created_user = self.user_repository.create(user)
        return UserResponse.model_validate(created_user) 
    
    def get_user(self, user_id:int) -> UserResponse | None:
        user = self.user_repository.get_by_id(user_id)
        return UserResponse.model_validate(user) if user else None

    def delete_user(self, user_id:int) -> bool:
        if not self.user_repository.delete(user_id):
            raise HTTPException(status_code=404, detail="User not found")
        return True
