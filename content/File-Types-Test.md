# File Types Test Page

This page tests how Quartz handles different file types beyond markdown.

## 📝 Text Files
Plain text files are copied as static assets:
- [View sample.txt](sample.txt) - Plain text file
- Direct link: `http://localhost:8080/sample.txt`

## 💻 Code Files  
Source code files are served as downloadable assets:
- [Download example.py](example.py) - Python source code
- [View raw Python](example.py) - Click to download

## 📊 Data Files
Structured data files:
- [View data.json](data.json) - JSON configuration data
- JSON files can be loaded by JavaScript on your pages

## 🎨 Code Syntax Highlighting (in Markdown)
Quartz has excellent syntax highlighting for code blocks:

### Python
```python
def process_notes(notes_dir):
    """Process all markdown notes in directory"""
    for file in os.listdir(notes_dir):
        if file.endswith('.md'):
            process_markdown_file(file)
```

### TypeScript
```typescript
interface Note {
  title: string;
  content: string;
  tags: string[];
  created: Date;
}

class DigitalGarden {
  private notes: Map<string, Note> = new Map();
  
  addNote(note: Note): void {
    this.notes.set(note.title, note);
  }
}
```

### JSON (Data)
```json
{
  "note": {
    "title": "Example Note",
    "tags": ["example", "test"],
    "content": "This is sample content"
  }
}
```

### Shell/Bash
```bash
#!/bin/bash
# Build and serve digital garden
echo "Building Quartz garden..."
npx quartz build --serve
echo "Visit: http://localhost:8080"
```

## 🔗 Embedding vs Linking

### Images (Auto-embedded)
![Sample Image](attachments/bd9cd777-a5c8-4e92-afa9-0af76f44e068.png)

### Text Files (Link only)
[Link to text file](sample.txt) - Opens in browser or downloads

### Code Files (Download)
[Download Python script](example.py) - Right-click to save

## ✅ Supported Features Summary

| File Type | Extension | Handling | Notes |
|-----------|-----------|----------|-------|
| **Markdown** | `.md` | Processed | Full Quartz features |
| **Images** | `.png`, `.jpg`, `.gif`, etc. | Auto-embed | In `<img>` tags |
| **Videos** | `.mp4`, `.webm`, `.mov` | Auto-embed | HTML5 `<video>` |
| **Audio** | `.mp3`, `.wav`, `.ogg` | Auto-embed | HTML5 `<audio>` |
| **PDFs** | `.pdf` | Auto-embed | In `<iframe>` |
| **Text** | `.txt`, `.log` | Static asset | Direct serving |
| **Code** | `.py`, `.js`, `.ts`, etc. | Static asset | Download/view |
| **Data** | `.json`, `.csv`, `.yaml` | Static asset | Can be loaded by JS |
| **Archives** | `.zip`, `.tar.gz` | Static asset | Download only |

## 🧪 Test Links

Try these links to test different file behaviors:
- **Text**: [sample.txt](sample.txt)
- **Code**: [example.py](example.py) 
- **Data**: [data.json](data.json)
- **Image**: [PNG file](attachments/bd9cd777-a5c8-4e92-afa9-0af76f44e068.png)

All non-markdown files are available at: `http://localhost:8080/filename.ext` 