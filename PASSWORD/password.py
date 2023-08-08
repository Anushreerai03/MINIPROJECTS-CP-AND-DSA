import random
import string

def generate_password(length, num_lowercase, num_uppercase, num_special_chars):
    characters = ''
    
    characters += ''.join(random.choice(string.ascii_lowercase) for _ in range(num_lowercase))
    characters += ''.join(random.choice(string.ascii_uppercase) for _ in range(num_uppercase))
    characters += ''.join(random.choice(string.punctuation) for _ in range(num_special_chars))
    
    remaining_length = length - (num_lowercase + num_uppercase + num_special_chars)
    characters += ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(remaining_length))
    
    password_list = list(characters)
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    return password

def main():
    print("Welcome to Password Generator!")
    
    length = int(input("Enter the desired password length: "))
    num_lowercase = int(input("Enter the number of lowercase letters required: "))
    num_uppercase = int(input("Enter the number of uppercase letters required: "))
    num_special_chars = int(input("Enter the number of special characters required: "))
    
    password = generate_password(length, num_lowercase, num_uppercase, num_special_chars)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
