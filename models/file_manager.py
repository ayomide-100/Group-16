import os

class FileManager:
    """Manages file operations and storage initialization"""

    def __init__(self):
        self.DATA_DIR = "data"
        self.ACCOUNTS_FILE = os.path.join(self.DATA_DIR, "accounts.txt")

    def initialise_storage(self) -> None:
        """Creates directory and accounts file if they don't exist"""
        if not os.path.exists(self.DATA_DIR):
            os.makedirs(self.DATA_DIR)
        if not os.path.exists(self.ACCOUNTS_FILE):
            with open(self.ACCOUNTS_FILE, "w") as f:
                pass
