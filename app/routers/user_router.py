from fastapi import HTTPException, status, APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse
from app.database.database import get_db
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository  # Importa el repositorio

router = APIRouter()

def get_user_service(db: Session = Depends(get_db)) -> UserService:
    user_repository = UserRepository(db)  # Crea el repositorio
    return UserService(user_repository)  # Pasa el repositorio al servicio

@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"description": "Invalid input data"},
        500: {"description": "Internal server error"}
    }
)
def create_user_endpoint(user_data: UserCreate, user_service: UserService = Depends(get_user_service)):
    try:
        created_user = user_service.create_user(user_data)  # Crea el usuario
        return UserResponse.model_validate(created_user, from_attributes=True)
    except ValueError as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))