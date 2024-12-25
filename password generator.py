import random
import string

def generate_password(length, complexity):
    """Generates a random password based on the given length and complexity."""

    characters = ""

    if complexity == "weak":
        characters = string.ascii_lowercase
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "strong":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity level. Using default (medium).")
        characters = string.ascii_letters + string.digits

    password = "".join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    while True:
        try:
            length = int(input("Enter desired password length: "))
            complexity = input("Enter desired complexity (weak, medium, strong): ").lower()
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for length.")

    password = generate_password(length, complexity)
    print("Generated password:", password)
    