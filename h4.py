import random

# Simulated User Database
users = {
    "user1": {
        "password": "password123",
        "fingerprint": "fingerprint_data"
    }
}

# Function to reduce OTP to a single digit
def reduce_to_single_digit(number):
    while number >= 10:
        number = sum(int(digit) for digit in str(number))
    return number

# Step 1: User Login
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username]["password"] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False

# Step 2: Generate and verify OTP
def verify_otp():
    otp = random.randint(1000, 9999)
    print(f"Your OTP is: {otp}")

    # Reduce OTP to a single digit
    reduced_otp = reduce_to_single_digit(otp)
    print(f"Reduced OTP to a single digit: {reduced_otp}")

    user_otp = int(input("Enter the single digit OTP: "))

    if user_otp == reduced_otp:
        print("OTP verification successful!")
        return True
    else:
        print("Invalid OTP.")
        return False

# Step 3: Fingerprint Verification
def verify_fingerprint(username):
    fingerprint_input = input("Place your finger on the scanner (input simulated fingerprint data): ")

    if fingerprint_input == users[username]["fingerprint"]:
        print("Fingerprint verified successfully!")
        return True
    else:
        print("Fingerprint verification failed.")
        return False

def main():
    if login():
        username = "user1"  # Simulating user1's login for simplicity
        if verify_otp():
            if verify_fingerprint(username):
                print("Access granted!")
            else:
                print("Access denied.")
        else:
            print("Access denied.")
    else:
        print("Access denied.")

if __name__ == "__main__":
    main()
