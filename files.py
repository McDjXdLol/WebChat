import os
import sys


class Files:
    def __init__(self):
        self.jokes = []

    @staticmethod
    def read_jokes() -> list[str]:
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(base_path, "data", "texts", "jokes.txt")

        with open(file_path, "r", encoding="utf-8") as f:
            jokes = f.readlines()
        return jokes

    @staticmethod
    def read_quotes() -> list[str]:
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(base_path, "data", "texts", "quotes.txt")

        with open(file_path, "r", encoding="utf-8") as f:
            quotes = f.readlines()
        return quotes
