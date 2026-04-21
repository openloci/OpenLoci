---
title: "Quick Start"
description: "Install OpenLoci and generate your first palace in under five minutes."
weight: 2
---

## Installation

Requires Python 3.10+. [uv](https://github.com/astral-sh/uv) recommended.

```bash
pip install openloci
```

Or with uv:

```bash
uv add openloci
```

---

## Generate a Palace

```bash
# Base template — no skin
openloci new my-project

# With a skin
openloci new my-investigation --skin xfiles
openloci new my-startup --skin sv
```

This creates a directory at `my-project/` containing `The Vestibule/` and `The Palace/` with all nine rooms.

---

## Explore Your Palace

```bash
# List available skins
openloci skins

# Show room map for a skin
openloci rooms xfiles

# Inspect an existing palace
openloci info ./my-investigation
```

---

## Development Install

```bash
git clone https://github.com/mrenoch/OpenLoci
cd OpenLoci
uv venv && uv pip install -e ".[dev]"

# Run tests
pytest tests/ -v

# CLI
openloci --help
```

---

## Render the Journal

Each palace includes a Hugo journal for rendering session notes as a browsable site. To run it locally:

```bash
# From inside your palace's Vestibule/Journal directory
hugo server --watch
# → http://localhost:1313
```

You'll need [Hugo](https://gohugo.io/installation/) installed. Hugo ships as a single static binary — no Node, no Python, no dependencies.

---

## Next Steps

- [Palace Structure](/palace-structure/) — understand rooms, prefixes, and the Vestibule
- [Available Skins](/skins/) — pick a cultural frame for your palace
- [Skin Authoring Guide](/skins/authoring/) — build your own skin
