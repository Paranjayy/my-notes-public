# My Digital Garden 🌱

A beautiful digital garden built with [Quartz v4](https://quartz.jzhao.xyz/) - a free, open-source alternative to Obsidian Publish.

## 🚀 Quick Start

1. **Prerequisites**
   - Node.js (v18 or later)
   - Git

2. **Installation**
   ```bash
   git clone <your-repo-url>
   cd Quartz-Obsi
   npm install
   ```

3. **Development**
   ```bash
   npx quartz build --serve
   ```
   
   Visit `http://localhost:8080` to see your garden!

## 📁 Project Structure

```
Quartz-Obsi/
├── content/                 # Your markdown content
│   ├── index.md            # Home page
│   ├── Getting Started with Quartz.md
│   ├── Digital Gardening Philosophy.md
│   ├── Markdown Tips and Tricks.md
│   └── Publishing Your Garden.md
├── quartz/                 # Quartz engine (don't modify)
├── quartz.config.ts        # Site configuration
├── quartz.layout.ts        # Layout configuration
└── package.json           # Dependencies
```

## ✨ Features

- **🔗 Bidirectional Links**: Connect ideas with `[[wiki-links]]`
- **🔍 Full-text Search**: Find content across your garden
- **📱 Mobile Responsive**: Looks great on all devices
- **⚡ Fast Loading**: Static site generation
- **🎨 Customizable**: Themes and layouts
- **📊 Graph View**: Visualize connections
- **🏷️ Tags**: Organize and categorize content

## 🖋️ Writing Content

### Basic Markdown
All standard markdown syntax is supported, plus:

- Wiki-style links: `[[Page Name]]`
- Tags in frontmatter: `tags: [tag1, tag2]`
- Callouts: `> [!info] This is important`
- Math equations: `$E = mc^2$`

### Example Note

```markdown
---
tags:
  - example
  - tutorial
date: 2024-01-15
---

# My Example Note

This is a note that links to [[Another Note]].

> [!tip] Pro Tip
> Use wiki links to connect your ideas!
```

## 🔧 Customization

### Site Configuration
Edit `quartz.config.ts` to customize:
- Site title and description
- Base URL
- Theme colors
- Analytics
- Plugins

### Styling
Create custom CSS in `quartz/styles/custom.scss`

## 🌐 Publishing

### GitHub Pages (Free)
1. Push to GitHub
2. Enable GitHub Pages
3. Set up deployment workflow

### Other Options
- Netlify
- Vercel  
- Custom hosting

See [[Publishing Your Garden]] for detailed instructions.

## 📚 Learning Resources

- [Quartz Documentation](https://quartz.jzhao.xyz/)
- [Obsidian Help](https://help.obsidian.md/)
- [Markdown Guide](https://www.markdownguide.org/)

## 🤝 Contributing

Feel free to suggest improvements or report issues!

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

Happy gardening! 🌿✨
