import string
import random

def generate_password():
    print("=" * 30)
    print("   PASSWORD GENERATOR")
    print("=" * 30)
    
    try:
        length = int(input("Enter the desired length of the password: "))
        
        if length < 4:
            print("\nError: Password length should be at least 4 for better security.")
            print("-" * 30)
            return

        lower_letters = string.ascii_lowercase
        upper_letters = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation
        
        all_characters = lower_letters + upper_letters + digits + symbols
        
        password_list = random.choices(all_characters, k=length)
        password = "".join(password_list)
        
        print("\n" + "-" * 30)
        print(f"Generated Password: {password}")
        print("-" * 30)
        
    except ValueError:
        print("\nError: Invalid Input! Please enter a valid number for length.")
        print("-" * 30)

if __name__ == "__main__":
    generate_password()