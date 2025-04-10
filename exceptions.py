
class UserNotFoundException(Exception):
    def __init__(self, user_id: str):
        super().__init(f"User {user_id} not found")

