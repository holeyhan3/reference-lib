# 1. Sync the Repository

After making changes:

git status

Review what changed.

git add .

Stage all changes.

git commit -m "Add dynamic category discovery"

Commit them.

git push

Push to GitHub.

That's all you need to keep the repository synchronized.

------------------------------------------------------------

# 2. Publish the Documentation

There are two common approaches.

Option A (Recommended): GitHub Pages + GitHub Actions

Whenever you push:

    Local repo
        │
        ▼
GitHub repository
        │
        ▼
GitHub Action
        │
        ▼
mkdocs build
        │
        ▼
GitHub Pages

Everything happens automatically.