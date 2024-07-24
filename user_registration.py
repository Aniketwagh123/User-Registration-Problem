class User:
    def __init__(self, name):
        self.__first_name = name

    def __str__(self):
        return self.__first_name


class UserValidator:

    @classmethod
    def validate_first_name(cls, first_name: str) -> bool:
        if len(first_name) >= 3 and first_name.istitle():
            return True
        return False


class InputReader:
    @classmethod
    def name_input(cls) -> str:
        while True:
            first_name = input("Enter your first name: ")
            if UserValidator.validate_first_name(first_name):
                return first_name
            else:
                print("First name must be at least 3 characters long. Please try again.")


if __name__ == "__main__":
    first_name = InputReader.name_input()
    user = User(first_name)
    print(user)
