import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Example: Generate a random password of length 12
password = generate_password(9)
print("Random Password:", password)