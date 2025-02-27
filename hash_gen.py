import bcrypt

def generate_hash(password: str) -> str:
    # Convert the password to bytes
    password_bytes = password.encode('utf-8')
    
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt(rounds=14))
    
    return hashed_password.decode('utf-8')  # Convert to string for storage #

if __name__ == "__main__":
    user_password = input("Enter password to hash: ")
    hashed = generate_hash(user_password)
    print(f"Hashed Password: {hashed}")
