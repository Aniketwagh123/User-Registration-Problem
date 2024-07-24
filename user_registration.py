import re


class User:
    def __init__(self, first_name: str, last_name: str, email: str):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email

    def __str__(self):
        return f"[First Name: {self.__first_name}, Last Name: {self.__last_name}, Email: {self.__email}]"


class UserValidator:
    @classmethod
    def validate_last_name(cls, last_name: str) -> bool:
        if len(last_name) >= 3 and last_name.istitle():
            return True
        return False

    @classmethod
    def validate_first_name(cls, first_name: str) -> bool:
        if len(first_name) >= 3 and first_name.istitle():
            return True
        return False

    @classmethod
    def validate_email(cls, email: str) -> bool:
        pattern = r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?$'
        return re.match(pattern, email) is not None


class InputReader:
    @classmethod
    def first_name_input(cls) -> str:
        while True:
            first_name = input("Enter your first name (e.g., Aniket): ")
            if UserValidator.validate_first_name(first_name):
                return first_name
            else:
                print(
                    "First name must be at least 3 characters long and the first character in caps. Please try again.")

    @classmethod
    def last_name_input(cls) -> str:
        while True:
            last_name = input("Enter your last name (e.g., Wagh): ")
            if UserValidator.validate_last_name(last_name):
                return last_name
            else:
                print(
                    "Last name must be at least 3 characters long and the first character in caps. Please try again.")

    @classmethod
    def email_input(cls) -> str:
        while True:
            email = input("Enter your email (e.g., abc.xyz@bl.co.in): ")
            if UserValidator.validate_email(email):
                return email
            else:
                print(
                    "Email must be in the format abc.xyz@bl.co.in with precise @ and . positions. Please try again.")


if __name__ == "__main__":
    first_name = InputReader.first_name_input()
    last_name = InputReader.last_name_input()
    email = InputReader.email_input()
    user = User(first_name=first_name, last_name=last_name, email=email)
    print(user)
