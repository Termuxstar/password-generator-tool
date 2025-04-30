import random
import string
import os
import time

# Function to generate password
def generate_password(length=12, use_special=False):
    chars = string.ascii_letters + string.digits
    if use_special:
        chars += string.punctuation

    # Generate password
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Function to print colourful text
def print_coloured(text, color_code):
    # ANSI escape codes for colour
    print(f"\033[{color_code}m{text}\033[0m")

# Function to create a colourful box
def print_boxed_text(text):
    # Create a box around the text
    border = "=" * (len(text) + 4)  # Border length depends on text length
    print_coloured(border, "34")  # Blue border
    print_coloured(f"  {text}  ", "35")  # Magenta text inside the box
    print_coloured(border, "34")  # Blue border

# Main function to interact with the user
def main():
    # Clear the screen before starting (for cleaner output)
    os.system('clear')

    # Print the box with "Created by Zabiullah Darkworld"
    print_boxed_text("Created by Zabiullah Darkworld")

    time.sleep(1)  # Pause for effect
    
    # Print the main title banner
    print_coloured("==================================================", "1")
    print_coloured("         Password Generator Tool", "1")
    print_coloured("==================================================", "1")
    time.sleep(1)  # Pause for effect

    while True:
        print_coloured("\nWelcome to the Password Generator Tool", "36")
        try:
            length = int(input("Enter password length (default 12): ") or 12)
        except ValueError:
            print_coloured("Invalid length, using default length of 12.", "31")
            length = 12

        use_special = input("Include special characters? (y/n): ").lower() == 'y'

        # Generate password
        password = generate_password(length, use_special)
        
        print_coloured(f"\nGenerated Password: {password}\n", "32")

        # Ask user whether to generate another password or exit
        choice = input("Do you want to generate another password? (y/n): ").lower()
        
        if choice != 'y':
            print_coloured("\nThank you for using the Password Generator Tool!", "33")
            break  # Exit the loop

if __name__ == "__main__":
    main()
