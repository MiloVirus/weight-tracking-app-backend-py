from typing import Dict
from userInterface import User  


class UserService(User):
    def __init__(self, name:str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password

    def create_user(self, name: str, email: str, password: str) -> Dict[str, str]:
        return {'name': name, 'email': email, 'password': password}
        
