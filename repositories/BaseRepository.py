from abc import ABC, abstractmethod
from typing import List, Optional
from sqlmodel import SQLModel

class BaseRepository(ABC):
    @abstractmethod
    def create(self, obj_data: SQLModel) -> SQLModel:
        pass

    @abstractmethod
    def get_by_id(self, obj_id: int) -> Optional[SQLModel]:
        pass

    @abstractmethod
    def get_all(self) -> List[SQLModel]:
        pass

    @abstractmethod
    def update(self, obj_id:int, obj_data:dict) -> Optional[SQLModel]:
        pass

    @abstractmethod
    def delete(self, obj_id:int) -> bool:
        pass
