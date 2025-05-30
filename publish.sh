#!/bin/bash

# Simple publish script for Quartz digital garden
# This adds, commits, and pushes changes to trigger GitHub Actions deployment

echo "📝 Adding all changes..."
git add .

echo "💾 Committing changes..."
if [ -z "$1" ]; then
    git commit -m "Update garden content - $(date '+%Y-%m-%d %H:%M')"
else
    git commit -m "$1"
fi

echo "🚀 Pushing to GitHub (this will trigger deployment)..."
git push

echo "✅ Done! Check your GitHub Actions tab for deployment progress."
echo "🌐 Your site: https://paranjay.github.io/my-notes-public" 