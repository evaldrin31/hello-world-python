import getpass

def login_system():
    # Predefined valid credentials
    stored_username = "admin"
    stored_password = "securePassword123"

    print("--- Welcome to the System ---")
    
    # Get user input (.strip() removes accidental leading/trailing spaces)
    username_input = input("Enter username: ").strip()
    
    # getpass hides the password typing in standard terminals for security
    password_input = getpass.getpass("Enter password: ")

    # Verify credentials
    if username_input == stored_username and password_input == stored_password:
        print("\n✅ Login successful! Welcome back.")
        return True
    else:
        print("\n❌ Invalid username or password. Access denied.")
        return False

# Run the program
if __name__ == "__main__":
    login_system()
