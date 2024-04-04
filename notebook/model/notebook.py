from datetime import datetime
from dataclasses import dataclass

@dataclass
class Note:
    HIGH: str = "HIGH"
    MEDIUM: str = "MEDIUM"
    LOW: str = "LOW"

    def __init__(self, code: int, title: str, text: str, importance: str):
        pass

    def add_tag(self, tag: str):
        pass

    def __str__(self) -> str:
        pass
    
class Notebook:
    def __init__(self):
        pass
    
    def add_note(self, title: str, text: str, importance: str):
        pass
    
    def importan_notes(self) -> list[Note]:
        pass
    
    def tag_notes_count(self) -> dict[str, int]:
        pass
    