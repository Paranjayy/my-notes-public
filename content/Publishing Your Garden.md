---
tags:
  - hosting
  - deployment
  - publishing
date: 2024-01-15
---

# Publishing Your Garden 🌐

Once you've created your digital garden with Quartz, you'll want to share it with the world! Here are the best ways to publish your garden online.

## Free Hosting Options

### GitHub Pages (Recommended)
**Pros**: Free, reliable, good performance
**Cost**: Free
**Setup**: 
1. Push your Quartz project to GitHub
2. Enable GitHub Pages in repository settings
3. Set up GitHub Actions for automatic deployment

```yaml
# .github/workflows/deploy.yml
name: Deploy Quartz site to GitHub Pages
 
on:
  push:
    branches:
      - main
```

### Netlify
**Pros**: Easy deployment, great performance, custom domains
**Cost**: Free tier available
**Setup**: Connect your GitHub repo to Netlify

### Vercel
**Pros**: Excellent performance, easy setup
**Cost**: Free tier available  
**Setup**: Import project from GitHub

## Custom Domain Setup

1. **Purchase a domain** (Namecheap, Google Domains, etc.)
2. **Configure DNS** to point to your hosting provider
3. **Update baseUrl** in `quartz.config.ts`:
   ```typescript
   baseUrl: "yourdomain.com"
   ```

## Automation Workflows

### Obsidian → GitHub → Auto-publish
1. Store your Obsidian vault in Git
2. Use Obsidian Git plugin for automatic syncing
3. GitHub Actions deploys changes automatically

### Local → Git → Deploy
```bash
# Daily workflow
npx quartz sync    # Sync content changes
git add .
git commit -m "Update garden"
git push           # Triggers auto-deployment
```

## Performance Tips

- **Optimize images**: Compress before adding to your garden
- **Use CDN**: For better global performance
- **Enable caching**: Most hosts do this automatically
- **Monitor size**: Keep individual pages reasonable

## SEO Considerations

### Essential Meta Tags
```yaml
---
title: Your Page Title
description: A brief description of the page content
tags: [relevant, keywords]
---
```

### Site Configuration
Update `quartz.config.ts`:
```typescript
analytics: {
  provider: "google", // or "plausible"
  tagId: "G-XXXXXXXXXX"
}
```

## Backup Strategies

1. **Git repositories**: Primary backup
2. **Export options**: Regular markdown exports
3. **Multiple platforms**: Consider mirroring to multiple hosts

## Legal Considerations

- **License**: Add a license for your content
- **Privacy**: Include privacy policy if using analytics
- **Attribution**: Credit sources and inspirations

## Maintenance

### Regular Tasks
- Update Quartz: `npx quartz update`
- Review broken links
- Update outdated content
- Monitor analytics and performance

### Content Strategy
- Write consistently, even if briefly
- Link new content to existing notes
- Review and update popular pages
- Gather feedback from readers

## Advanced Features

### Custom CSS
Create `quartz/styles/custom.scss` for personalization:
```scss
// Custom garden styling
.page-title {
  color: #2d5016;
}
```

### Plugins
Explore community plugins for additional functionality

## Troubleshooting

Common issues and solutions:
- **Build failures**: Check Node.js version compatibility
- **Broken links**: Use consistent file naming
- **Slow builds**: Optimize image sizes, reduce plugin usage
- **Missing pages**: Verify file extensions and frontmatter

## See Also

- [[Getting Started with Quartz]]
- [[Digital Gardening Philosophy]]
- [Hosting Documentation](https://quartz.jzhao.xyz/hosting)

Ready to share your garden with the world? Start with GitHub Pages and expand from there! 🚀 