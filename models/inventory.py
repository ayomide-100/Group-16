import os
import re
from typing import Dict, List
from models.file_manager import FileManager

class Inventory:
    """Manages inventory operations and item searching"""

    def __init__(self):
        self.file_manager = FileManager()

    def load_inventory(self) -> Dict:
        """Loads inventory from warehouse files"""
        inventory = {}

        # Create sample inventory if no warehouse files exist
        if not any(f.startswith("warehouse") and f.endswith(".txt") for f in os.listdir(self.file_manager.DATA_DIR)):
            self.create_sample_inventory()

        for file in os.listdir(self.file_manager.DATA_DIR):
            if file.startswith("warehouse") and file.endswith(".txt"):
                path = os.path.join(self.file_manager.DATA_DIR, file)
                with open(path, 'r') as f:
                    content = f.read()
                    items = content.strip().split(";")
                    for item in items:
                        if item.strip():
                            try:
                                name, price = item.split(":")
                                inventory[name.strip()] = int(price.strip())
                            except ValueError:
                                continue
        return inventory

    def create_sample_inventory(self) -> None:
        """Creates sample inventory files"""
        sample_items = [
            "iPhone 13 Pro:450000",
            "Samsung Galaxy S21:320000",
            "MacBook Pro M1:850000",
            "Dell XPS 13:520000",
            "Apple Watch Series 7:180000",
            "AirPods Pro:95000",
            "Sony WH-1000XM4:125000",
            "iPad Air:280000",
            "Nintendo Switch:150000",
            "PlayStation 5:285000"
        ]
        warehouse_file = os.path.join(self.file_manager.DATA_DIR, "warehouse1.txt")
        with open(warehouse_file, 'w') as f:
            f.write(";".join(sample_items))

    def search_inventory(self, query: str, inventory: Dict) -> List[str]:
        """Searches for items matching the query"""
        if not query:
            return list(inventory.keys())

        search_terms = query.strip().split()
        regex_patterns = [re.compile(re.escape(term), re.IGNORECASE) for term in search_terms]

        matched = []
        for item_name in inventory:
            if all(pattern.search(item_name) for pattern in regex_patterns):
                matched.append(item_name)

        return matched
