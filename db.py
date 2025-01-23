import json
import os


class Database:
    def __init__(self, file_name="users.json"):
        self.file_name = file_name
        # Ensure the file exists and has valid JSON
        if not os.path.exists(self.file_name):
            with open(self.file_name, "w") as f:
                json.dump([], f)  # Initialize with an empty list

    def insert(self, name, email, password):
        try:
            # Open and load existing user data
            with open(self.file_name, "r") as rf:
                users = json.load(rf)

            # Check if email already exists
            if any(user["email"] == email for user in users):
                print(f"Email {email} already exists in the database.")
                return False  # Indicate failure

            # Add the new user
            new_user = {"name": name, "email": email, "password": password}
            users.append(new_user)

            # Save updated data back to the file
            with open(self.file_name, "w") as wf:
                json.dump(users, wf, indent=4)

            print(f"User with email {email} added successfully.")
            return True  # Indicate success
        except (json.JSONDecodeError, FileNotFoundError):
            print("Error reading the file. Ensure it's a valid JSON file.")
            return False

    def search(self, email, password):
        try:
            # Check if the file exists
            with open(self.file_name, "r") as rf:
                users = json.load(rf)

            # Search for the email in the user list
            for user in users:
                if user["email"] == email:
                    # Check if the password matches
                    if user["password"] == password:
                        print("Login successful!")
                        return True
                    else:
                        print("Incorrect password.")
                        return False

            # Email not found
            print("Email not found in the database.")
            return False
        except json.JSONDecodeError:
            print("Error reading the file. Ensure it's a valid JSON file.")
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False
