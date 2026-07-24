# Reference Library

A structured, filesystem-driven knowledge management system built with Markdown and MkDocs.

The goal is to maintain a long-lived reference library where concepts, research notes, books, papers, and projects are organized into a navigable hierarchy.

Categories are discovered automatically from the `docs/` directory. Metadata is stored locally in `_category.yaml` files, and MkDocs navigation is generated automatically.

---

# Features

- Filesystem-based category organization
- Automatic category discovery
- Automatic generation of:
  - `index.md`
  - `_category.yaml`
- Dynamic MkDocs navigation generation
- Template-based note creation
- Interactive category selection
- Command-line category selection
- Numeric menu selection
- Metadata-driven ordering
- Type-safe Python utilities
- `uv` managed CLI commands

---

# Installation

Install dependencies:

```bash
uv sync

#Available commands:
uv run init-categories
uv run build-nav
uv run new-note
```
## Project Structure

```
reference-lib/

├── docs/
│   ├── foundations/
│   │   ├── mathematics/
│   │   │   ├── probability/
│   │   │   │   ├── index.md
│   │   │   │   ├── _category.yaml
│   │   │   │   └── monte-carlo-methods.md
│   │
│   └── assets/
│
├── scripts/
│   ├── __init__.py
│   ├── new_note.py
│   ├── build_nav.py
│   ├── init_categories.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── categories.py
│       ├── discovery.py
│       ├── metadata.py
│       ├── paths.py
│       └── types.py
│
├── config/
│   └── templates/
│
├── mkdocs.yml
├── pyproject.toml
├── uv.lock
└── README.md
```

# Workflow

## 1. Initialize Categories:

Create missing category metadata and overview pages:

```bash
uv run init-categories
```

This scans the `docs/` directory for folders and generates `_category.yaml` and `index.md` files for each category.

```
_category.yaml
index.md
```

Example:

```
docs/foundations/mathematics/probability/

├── _category.yaml
└── index.md
```
Generated metadata:

```yaml
title: Probability
description: Documentation about Probability.
```

## 2. Build Navigation

Generate MKDocs navigation from the category metadata:

```bash
uv run build-nav
```
The process:
1. Scans docs/
2. Ignores excluded directories
3. Loads _category.yaml
4. Builds the category tree
5. Generates the MkDocs nav configuration

Example:
Filesystem:
```
docs/
└── foundations/
    └── mathematics/
        └── probability/
            └── monte-carlo-methods.md
```
Generated navigation:
```yaml
nav:
  - Foundations:
      - Mathematics:
          - Probability:
              - Overview: foundations/mathematics/probability/index.md
              - Monte Carlo Methods: foundations/mathematics/probability/monte-carlo-methods.md
```
## 3. Create New Note

```bash
uv run new-note "Monte Carlo Methods"
```


## 3. Create a New Note

Create a note:

```bash
uv run new-note "Monte Carlo Methods"
```

The system will display an interactive category menu.

Example:

```text
Choose category

1. economics
2. finance
3. foundations
4. geopolitics

Choice:
```

---

## Direct Category Selection

Categories can also be supplied directly:

```bash
uv run new-note \
"Monte Carlo Methods" \
foundations mathematics probability
```

or using menu indexes:

```bash
uv run new-note \
"Monte Carlo Methods" \
3 4 2
```

---

# Category System

The filesystem is the source of truth.

Example:

```text
docs/

foundations/
└── mathematics/
    └── probability/
```

becomes:

```text
Foundations
└── Mathematics
    └── Probability
```

No separate category database is required.

---

# Category Metadata

Each category may contain:

```
_category.yaml
```

Example:

```yaml
title: Probability
description: Documentation about Probability.
order: 3
```

Fields:

| Field | Purpose |
|------|---------|
| title | Display name |
| description | Category description |
| order | Navigation priority |

---

# Category Index Pages

Each category contains:

```
index.md
```

Example:

```markdown
# Probability

Overview of Probability.
```

These pages become category overview pages in MkDocs.

---

# Note Types

Notes are created from templates.

Supported types:

| Type | Purpose |
|------|---------|
| concept | General concepts |
| book | Book notes |
| paper | Research papers |
| cheatsheet | Quick references |
| project | Project documentation |

Example:

```bash
uv run new-note \
"General Relativity" \
--type concept
```

---

# Architecture

```text
Filesystem
     │
     ▼
discovery.py
     │
     ▼
CategoryNode tree
     │
     ├──────────────┐
     ▼              ▼
new_note.py    build_nav.py
     │              │
     ▼              ▼
Markdown files  mkdocs.yml
```

---

# Core Components

## discovery.py

Responsible for:

- scanning directories
- reading `_category.yaml`
- building the category tree
- generating `CategoryNode` structures

Example:

```python
{
    "foundations": {
        "children": {
            "mathematics": {
                "children": {
                    "probability": {"path": "foundations/mathematics/probability"}
                }
            }
        }
    }
}
```

---

## metadata.py

Responsible for:

- loading `_category.yaml`
- validating metadata
- converting metadata into category nodes

---

## categories.py

Responsible for:

- interactive category menus
- category traversal
- resolving user input into filesystem paths

---

## build_nav.py

Responsible for:

- discovering categories
- converting category trees
- generating MkDocs navigation

---

## new_note.py

Responsible for:

- loading templates
- validating note types
- checking duplicate notes
- generating Markdown files

---

# Development Commands

Run tests:

```bash
uv run pytest
```

Type checking:

```bash
uv run mypy scripts
```

Linting:

```bash
uv run ruff check .
```

---

# Development Workflow

The project separates category initialization, navigation generation, note creation, and documentation serving into independent commands.

This keeps each command focused on a single responsibility and avoids unnecessary work.

| Command | Purpose | Typical Usage |
|---------|---------|---------------|
| `uv run init-categories` | Create missing `index.md` and `_category.yaml` files | When new folders are added |
| `uv run build-nav` | Rebuild the MkDocs navigation from the filesystem | After changing the category hierarchy |
| `uv run new-note` | Create a new note from a template | Daily note creation |
| `uv run serve-docs` | Launch the MkDocs development server | Daily development |

---

## Typical Workflow

### Initial project setup

When creating new documentation folders manually:

```bash
uv run init-categories
uv run build-nav
```

This will:

- create missing `index.md` files
- create missing `_category.yaml` files
- generate the MkDocs navigation

---

# Design Principles

## Filesystem as Source of Truth

The directory structure defines the knowledge hierarchy.

Categories are not maintained in a separate configuration file.

---

## Metadata Near Content

Metadata is stored next to documentation:

```text
category/

├── _category.yaml
├── index.md
└── notes/
```

This keeps the system portable and easy to maintain.

---

## Automation Over Manual Configuration

Common maintenance tasks are automated:

| Task | Command |
|------|---------|
| Initialize categories | `uv run init-categories` |
| Update navigation | `uv run build-nav` |
| Create notes | `uv run new-note` |

---

# Future Extensions

Potential additions:

- document validation
- orphan note detection
- backlink generation
- graph visualization
- automatic tagging
- citation management
- full-text search indexing
- knowledge graph extraction
- automated metadata enrichment