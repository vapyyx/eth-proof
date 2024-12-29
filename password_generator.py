import random
import string

def generate_password(length=12):
    if length < 6:
        return "Password length must be at least 6 characters."
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired password length (min 6): "))
        print(f"Generated password: {generate_password(length)}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
