import os

def say_hello(name: str, age: int, address: str):
    """
    This function prints out the user's data.

    Parameters:
        name (str): This is the username.
        age (int): User's age
        address (str): User's address
    """

    print(f"Hello {name}.")
    print(f"You live in {address}")
    print(f"You are {age} years old")