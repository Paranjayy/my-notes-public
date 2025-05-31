# Code Examples Test

## Python Example
```python
def hello_world():
    print('Hello from Quartz!')
    return 42

# This is a comment
class DigitalGarden:
    def __init__(self):
        self.notes = []
    
    def add_note(self, content):
        self.notes.append(content)
```

## JavaScript Example
```javascript
// Modern JavaScript with syntax highlighting
const garden = {
    notes: new Map(),
    
    addNote(title, content) {
        this.notes.set(title, {
            content,
            created: new Date(),
            tags: []
        });
    },
    
    // Arrow function with destructuring
    searchNotes: (query) => {
        return [...garden.notes.entries()]
            .filter(([title, note]) => 
                title.includes(query) || 
                note.content.includes(query)
            );
    }
};
```

## Other Languages

### Rust
```rust
// Rust code with highlighting
fn main() {
    let message = "Hello, Quartz!";
    println!("{}", message);
}
```

### Go
```go
// Go code
package main
import "fmt"
func main() {
    fmt.Println("Digital Garden in Go!")
}
```

### SQL
```sql
SELECT title, content, created_at 
FROM notes 
WHERE tags LIKE '%digital-garden%'
ORDER BY created_at DESC;
```

### Bash/Shell
```bash
#!/bin/bash
echo "Building digital garden..."
npx quartz build --serve
echo "Garden is ready! 🌱"
``` 