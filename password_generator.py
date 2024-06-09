import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        return "Error: No character types selected!"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


print("Password Generator")

try:
    length = int(input("Enter the desired length of the password: "))
    if length <= 0:
        print("Length must be a positive integer.")
        print(exit(0))
except ValueError:
    print("Invalid input! Please enter a numeric value.")
    print(exit(0))

use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_special = input("Include special characters? (y/n): ").lower() == 'y'

password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
print(f"Generated Password: {password}")

# OUTPUT
# Password Generator
# Enter the desired length of the password: 8
# Include uppercase letters? (y/n): y
# Include lowercase letters? (y/n): y
# Include digits? (y/n): y
# Include special characters? (y/n): y
# Generated Password: q)WMB*7H
