import re


class User:
    def __init__(self, first_name: str, last_name: str, email: str, mobile_number: str, password: str):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__mobile_number = mobile_number
        self.__password = password

    def __str__(self):
        return f"[First Name: {self.__first_name}, Last Name: {self.__last_name}, Email: {self.__email}, Mobile Number: {self.__mobile_number}]"


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
        email_regex = r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2})?$'
        if re.match(email_regex, email):
            return True
        return False

    @classmethod
    def validate_mobile_number(cls, mobile_number: str) -> bool:
        mobile_regex = r'^\d{2} \d{10}$'
        if re.match(mobile_regex, mobile_number):
            return True
        return False

    @classmethod
    def validate_password(cls, password: str) -> bool:
        # Rule1: Minimum 8 characters
        # Rule2: At least 1 uppercase letter
        # Rule3: At least 1 numeric digit
        # Rule4: Exactly 1 special character

        if len(password) < 8:
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"[0-9]", password):
            return False

        special_characters = re.findall(r"[!@#$%^&*(),.?\":{}|<>]", password)
        if len(special_characters) != 1:
            return False

        return True


class InputReader:
    @classmethod
    def first_name_input(cls) -> str:
        while True:
            first_name = input("Enter your first name (e.g. Aniket): ")
            if UserValidator.validate_first_name(first_name):
                return first_name
            else:
                print(
                    "First name must be at least 3 characters long and the first character in caps. Please try again.")

    @classmethod
    def last_name_input(cls) -> str:
        while True:
            last_name = input("Enter your last name (e.g. Wagh): ")
            if UserValidator.validate_last_name(last_name):
                return last_name
            else:
                print(
                    "Last name must be at least 3 characters long and the first character in caps. Please try again.")

    @classmethod
    def email_input(cls) -> str:
        while True:
            email = input("Enter your email (e.g. abc.xyz@bl.co.in): ")
            if UserValidator.validate_email(email):
                return email
            else:
                print("Invalid email format. Please try again.")

    @classmethod
    def mobile_number_input(cls) -> str:
        while True:
            mobile_number = input(
                "Enter your mobile number (e.g. 91 9919819801): ")
            if UserValidator.validate_mobile_number(mobile_number):
                return mobile_number
            else:
                print(
                    "Mobile number must be in the format '91 9919819801'. Please try again.")

    @classmethod
    def password_input(cls) -> str:
        while True:
            password = input(
                "Enter your password (minimum 8 characters, including at least 1 uppercase letter, 1 digit, and exactly 1 special character): ")
            if UserValidator.validate_password(password):
                return password
            else:
                print("Password must be at least 8 characters long and include at least one uppercase letter, one numeric digit, and exactly one special character. Please try again.")


if __name__ == "__main__":
    first_name = InputReader.first_name_input()
    last_name = InputReader.last_name_input()
    email = InputReader.email_input()
    mobile_number = InputReader.mobile_number_input()
    password = InputReader.password_input()
    user = User(first_name=first_name, last_name=last_name,
                email=email, mobile_number=mobile_number, password=password)
    print(user)
