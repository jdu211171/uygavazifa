import json
from typing import List, Optional
from typing import NamedTuple, Optional, List
from errors import UsernameAlreadyExistsError

class User(NamedTuple):
    id: int
    name: str
    surname: str
    username: str
    password: str


class Database:
    def selectAllUsers(self) -> List[User]:
        with open("./2024-08-28/database/users.json", "r", encoding="utf-8") as file:
            data = file.read()
            users = json.loads(data) or []
            return [User(**user) for user in users]

    def selectUser(self, username: str) -> Optional[User]:
        users = self.selectAllUsers()
        user = next((user for user in users if user.username == username), None)
        return user

    def login(self, username: str, password: str) -> Optional[dict]:
        users = self.selectAllUsers()
        user = next((user for user in users if user.username == username and user.password == password), None)
        return user._asdict() if user else None

    def register(self, name: str, surname: str, username: str, password: str) -> dict:
        foundUser = self.selectUser(username)

        if foundUser:
            raise UsernameAlreadyExistsError("Username band qilingan!")

        USERS = self.selectAllUsers()
        new_user = {
            "id": USERS[-1].id + 1 if USERS else 1,
            "name": name,
            "surname": surname,
            "username": username,
            "password": password,
        }
        USERS.append(User(**new_user))
        with open("./2024-08-28/database/users.json", "w") as file:
            file.write(json.dumps([user._asdict() for user in USERS], indent=4))

        return new_user

    def selectAllPosts(self) -> List[dict]:
        with open("./2024-08-28/database/posts.json", "r", encoding="utf-8") as file:
            data = file.read()
            posts = json.loads(data) or []
            return posts

    def selectUserPosts(self, user_id: int) -> List[dict]:
        with open("./2024-08-28/database/posts.json", "r", encoding="utf-8") as file:
            data = file.read()
            posts = json.loads(data) or []
            filteredPosts = list(filter(lambda p: p["user_id"] == user_id, posts))
            return filteredPosts

    def addPost(self, user_id: int, post_text: str) -> None:
        allPosts = self.selectAllPosts()
        ID = allPosts[-1]["id"] + 1 if allPosts else 1

        allPosts.append({
            "id": ID,
            "user_id": user_id,
            "text": post_text
        })

        with open("./2024-08-28/database/posts.json", "w") as file:
            data = json.dumps(allPosts, indent=4)
            file.write(data)


# database = Database()

# print(database.selectUserPosts(1))
