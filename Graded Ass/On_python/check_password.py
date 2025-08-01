def check_password_strength(password):
    """
    Check if the given password meets the strength criteria:
    - At least 8 characters
    - At least one uppercase
    - At least one lowercase
    - At least one digit
    - At least one special character
    """
    
    """
    Checks the strength of a password and returns:
    - True + empty list if all criteria are met
    - False + list of feedback messages if criteria are violated
    """
    
    # Initialize feedback list
    # This list will collect feedback messages for each failed criterion
    # If the list is empty, the password is strong, empty list to collect feedback messages
    # This will be used to inform the user about any issues with their password
    feedback = []

    # Ensure the password meets the minimum length requirement (8 characters).
    # Short passwords are easier to guess or brute-force and are considered weak.
    # If this condition fails, add feedback to guide the user to choose a stronger password.
    if len(password) < 8:
        feedback.append(" Password must be at least 8 characters long.")

    # Check for at least one uppercase letter, one lowercase letter, one digit, and one special character
    if not any(map(lambda c: c.isupper(), password)):
        feedback.append(" Password must include at least one uppercase letter.")

    if not any(map(lambda c: c.islower(), password)):
        feedback.append(" Password must include at least one lowercase letter.")

    if not any(map(lambda c: c.isdigit(), password)):
        feedback.append(" Password must include at least one digit (0–9).")

    if not any(map(lambda c: c in "!@#$%^&*()-_=+[]{}|;:',.<>?/", password)):
        feedback.append(" Password must include at least one special character (!@#$, etc.).")

    is_strong = len(feedback) == 0
    return is_strong, feedback


def main():
    password = input("Enter your password: ")

    is_valid, issues = check_password_strength(password)

    if is_valid:
        print("\nStrong password!\nYou meet all security criteria.\n")
    else:
        print("\nWeak password! \n\nPlease fix the following issues:")

        for issue in issues:
            print("   " + issue)
        
# name guard to run the main function
if __name__ == "__main__":
    main()