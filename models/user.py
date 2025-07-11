import os
import re
from typing import Dict, Optional
from models.file_manager import FileManager

class User:
    """Represents a user with authentication and account management"""

    def __init__(self):
        self.file_manager = FileManager()

    def is_existing_user(self, username: str, email: str) -> bool:
        if not os.path.exists(self.file_manager.ACCOUNTS_FILE):
            return False

        with open(self.file_manager.ACCOUNTS_FILE, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 2:
                    if username == parts[0] or email == parts[1]:
                        return True
        return False

    def is_valid_password(self, password: str) -> bool:
        if len(password) < 16:
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"\d", password):
            return False
        if not re.search(r"[\W_]", password):
            return False
        return True

    def create_account(self, username: str, email: str, password: str) -> bool:
        if self.is_existing_user(username, email):
            return False

        with open(self.file_manager.ACCOUNTS_FILE, 'a') as f:
            f.write(f"{username},{email},{password},0.00\n")
        return True

    def authenticate(self, username_or_email: str, password: str) -> Optional[Dict]:
        if not os.path.exists(self.file_manager.ACCOUNTS_FILE):
            return None

        with open(self.file_manager.ACCOUNTS_FILE, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 4:
                    username, email, stored_password, balance = parts
                    if (username_or_email == username or username_or_email == email) and password == stored_password:
                        return {
                            "username": username,
                            "email": email,
                            "password": stored_password,
                            "balance": float(balance)
                        }
        return None

    def update_user_balance(self, user: Dict) -> None:
        updated_lines = []
        with open(self.file_manager.ACCOUNTS_FILE, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 4:
                    username, email, password, _ = parts
                    if username == user['username']:
                        new_line = f"{username},{email},{password},{user['balance']:.2f}\n"
                        updated_lines.append(new_line)
                    else:
                        updated_lines.append(line)
        with open(self.file_manager.ACCOUNTS_FILE, 'w') as f:
            f.writelines(updated_lines)

    def update_user_info(self, old_username: str, new_username: str = None, new_email: str = None, new_password: str = None) -> None:
        updated_lines = []
        with open(self.file_manager.ACCOUNTS_FILE, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 4:
                    username, email, password, balance = parts
                    if username == old_username:
                        username = new_username if new_username else username
                        email = new_email if new_email else email
                        password = new_password if new_password else password
                        updated_lines.append(f"{username},{email},{password},{balance}\n")
                    else:
                        updated_lines.append(line)
        with open(self.file_manager.ACCOUNTS_FILE, 'w') as f:
            f.writelines(updated_lines)
