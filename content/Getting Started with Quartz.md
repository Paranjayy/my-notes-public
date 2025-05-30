# Getting Started with Quartz

Quartz is a powerful static site generator designed specifically for creating digital gardens from your markdown notes. Here's everything you need to know to get started!

## What is Quartz?

Quartz v4 is a set of tools that helps you publish your digital garden and notes as a website. For those coming from Obsidian, it's like a free, open-source alternative to Obsidian Publish.

## Key Features

- **🔗 Bidirectional Links**: Create connections between your notes with `[[wiki-links]]`
- **🔍 Full-text Search**: Find content across your entire garden
- **📱 Mobile Responsive**: Looks great on all devices  
- **⚡ Fast Loading**: Static site generation for optimal performance
- **🎨 Customizable**: Themes, layouts, and components you can modify
- **📊 Graph View**: Visualize connections between your notes

## Installation

1. **Prerequisites**: Node.js (v18+) and Git
2. **Clone**: `git clone https://github.com/jackyzha0/quartz.git`
3. **Install**: `npm install`
4. **Create**: `npx quartz create`
5. **Build & Serve**: `npx quartz build --serve`

## Writing Content

### Basic Markdown
All standard markdown syntax works:
- Headers with `#`
- **Bold** and *italic* text
- Lists and checkboxes
- Code blocks and inline `code`

### Wiki Links
Link to other pages using double brackets:
- `[[Page Name]]` - links to "Page Name.md"
- `[[Page Name|Custom Text]]` - custom link text
- `[[folder/Page Name]]` - link to pages in subfolders

### Tags
Use tags to categorize your content:
```yaml
---
tags:
  - productivity
  - note-taking
  - digital-garden
---
```

## Next Steps

- Explore [[Digital Gardening Philosophy]]
- Learn [[Markdown Tips and Tricks]]
- Check out the [official documentation](https://quartz.jzhao.xyz/)

## Useful Commands

- `npx quartz build` - Build your site
- `npx quartz build --serve` - Build and serve locally
- `npx quartz sync` - Sync content changes
- `npx quartz update` - Update Quartz to latest version

Happy gardening! 🌱 