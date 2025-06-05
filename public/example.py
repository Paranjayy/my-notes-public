#!/usr/bin/env python3
"""
Example Python file for testing Quartz file support
"""

import json
import datetime
from typing import List, Dict, Any

class DigitalGarden:
    """A simple digital garden implementation"""
    
    def __init__(self, name: str):
        self.name = name
        self.notes: Dict[str, Dict[str, Any]] = {}
        self.created_at = datetime.datetime.now()
    
    def add_note(self, title: str, content: str, tags: List[str] = None) -> None:
        """Add a new note to the garden"""
        if tags is None:
            tags = []
            
        self.notes[title] = {
            "content": content,
            "tags": tags,
            "created": datetime.datetime.now().isoformat(),
            "modified": datetime.datetime.now().isoformat()
        }
        print(f"Added note: {title}")
    
    def search_notes(self, query: str) -> List[str]:
        """Search for notes containing the query"""
        results = []
        for title, note in self.notes.items():
            if (query.lower() in title.lower() or 
                query.lower() in note["content"].lower()):
                results.append(title)
        return results
    
    def export_to_json(self, filename: str) -> None:
        """Export garden to JSON file"""
        data = {
            "name": self.name,
            "created_at": self.created_at.isoformat(),
            "notes": self.notes
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Garden exported to {filename}")

if __name__ == "__main__":
    # Example usage
    garden = DigitalGarden("My Digital Garden")
    
    garden.add_note(
        "Getting Started", 
        "This is my first note in the digital garden!",
        ["meta", "getting-started"]
    )
    
    garden.add_note(
        "Python Tips",
        "Here are some useful Python patterns for note-taking apps.",
        ["programming", "python", "tips"]
    )
    
    # Search example
    results = garden.search_notes("python")
    print(f"Found {len(results)} notes about Python")
    
    # Export
    garden.export_to_json("garden_backup.json") 