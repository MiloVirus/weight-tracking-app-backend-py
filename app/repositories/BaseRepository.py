from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)

class BaseRepository(ABC, Generic[T]):
    @abstractmethod
    def create(self, obj_data: T) -> T:
        pass

    @abstractmethod
    def get_by_id(self, obj_id: int) -> Optional[T]:
        pass

    @abstractmethod
    def get_all(self) -> List[T]:
        pass

    @abstractmethod
    def update(self, obj_id: int, obj_data: dict) -> Optional[T]:
        pass

    @abstractmethod
    def delete(self, obj_id: int) -> bool:
        pass
