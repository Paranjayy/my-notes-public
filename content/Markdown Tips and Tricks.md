---
tags:
  - markdown
  - tutorial
  - formatting
---

# Markdown Tips and Tricks

This page covers advanced markdown techniques that work particularly well with Quartz. Master these to make your digital garden more engaging and functional!

## Basic Formatting

### Text Styling
- **Bold text** with `**bold**`
- *Italic text* with `*italic*`
- ***Bold and italic*** with `***bold and italic***`
- ~~Strikethrough~~ with `~~strikethrough~~`
- `Inline code` with backticks

### Lists and Checkboxes
- Bullet points with `-` or `*`
- Numbered lists with `1.`
- [ ] Unchecked checkbox
- [x] Checked checkbox

## Advanced Quartz Features

### Wiki Links
```markdown
[[Page Name]]                    # Basic link
[[Page Name|Custom Display]]     # Custom link text
[[folder/Page Name]]             # Link to subfolder
```

### Callouts and Admonitions
> [!info] Information
> This is an info callout that stands out

> [!warning] Warning
> Be careful with this approach

> [!tip] Pro Tip
> This will save you time!

### Code Blocks with Syntax Highlighting
```javascript
function buildGarden() {
  console.log("Growing your digital garden...");
  return "🌱";
}
```

```python
def digital_garden():
    return "Perfect for knowledge sharing!"
```

## Tables

| Feature | Supported | Notes |
|---------|-----------|-------|
| Wiki Links | ✅ | Full support |
| Backlinks | ✅ | Automatic |
| Graph View | ✅ | Visual connections |
| Search | ✅ | Full-text |
| Mobile | ✅ | Responsive design |

## Math Support

Inline math: $E = mc^2$

Block math:
$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$

## Images and Media

### Local Images
```markdown
![Alt text](./images/diagram.png)
```

### Web Images
```markdown
![Quartz Logo](https://quartz.jzhao.xyz/static/icon.png)
```

## Special Quartz Syntax

### Tags
Add tags to your frontmatter:
```yaml
---
tags:
  - productivity
  - note-taking
---
```

### Dates
```yaml
---
date: 2024-01-15
modified: 2024-01-20
---
```

## Organization Tips

### Folder Structure
```
content/
├── index.md              # Home page
├── daily/                # Daily notes
├── projects/             # Project notes
├── concepts/             # Core concepts
└── resources/            # References
```

### Linking Strategy
- Use descriptive link text
- Create hub pages for major topics
- Link frequently between related concepts
- Don't over-organize initially

## Useful Shortcuts

- `Cmd/Ctrl + K` - Quick link insertion (in Obsidian)
- `[[` + `Tab` - Link completion
- `#` - Tag suggestions

## Best Practices

1. **Start Writing**: Don't overthink the structure
2. **Link Liberally**: Create connections between ideas
3. **Use Descriptive Titles**: Make them searchable
4. **Regular Maintenance**: Update and expand notes
5. **Embrace Imperfection**: Gardens grow over time

## See Also

- [[Getting Started with Quartz]]
- [[Digital Gardening Philosophy]]
- [Markdown Guide](https://www.markdownguide.org/)

Happy writing! ✍️ 