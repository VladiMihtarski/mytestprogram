from project.library import Library
from project.user import User


class Registration:
    def add_user(self, user: User, library: Library):
        for existing_user in library.user_records:
            if existing_user.user_id == user.user_id:
                return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)
        return f"User {user.username} successfully registered."

    def remove_user(self, user: User, library: Library):
        if user in library.user_records:
            library.user_records.remove(user)
            return f"User {user.username} has been removed."
        else:
            return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        for user in library.user_records:
            if user.user_id == user_id:
                if user.username != new_username:
                    user.username = new_username
                    if user.username in library.rented_books:
                        library.rented_books[new_username] = library.rented_books.pop(user.username)
                        for books in library.rented_books[new_username]:
                            library.rented_books[new_username][books] = library.rented_books[new_username].pop(books)
                    return f"Username successfully changed to: {new_username} for user id: {user_id}"
                else:
                    return "Please check again the provided username - it should be different than the username used so far!"
        return f"There is no user with id = {user_id}!"