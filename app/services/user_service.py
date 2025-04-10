from venv import logger
from app.repositories.BaseRepository import BaseRepository
from app.database.models.user import User
from app.schemas.user import UserCreate, UserResponse
from exceptions import UserNotFoundException


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

    def delete_user(self, user_id:int) -> None:
        try:
            delete_user = self.user_repository.delete(user_id)
            return delete_user
        except UserNotFoundException:
            raise 
        except Exception as e:
            logger.error(f"Error deleting user {user_id}: {str(e)}")
            raise RuntimeError("Failed to delete user")
