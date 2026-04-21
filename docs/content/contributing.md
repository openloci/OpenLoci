---
title: "Contributing"
description: "How to contribute to OpenLoci."
weight: 7
---

OpenLoci is GPL-3.0. The spec is open. Contributions are welcome.

## What We Need Most

**Skins** are the primary contribution surface. A skin is a directory in `templates/skins/` containing a room map, character files, and a master prompt. If you have a cultural frame you want to run a project through, build it and open a PR.

See the [Skin Authoring Guide](/skins/authoring/) for the full spec.

**Bug reports and feature requests** go in [GitHub Issues](https://github.com/mrenoch/OpenLoci/issues).

## Development

```bash
git clone https://github.com/mrenoch/OpenLoci
cd OpenLoci
uv venv && uv pip install -e ".[dev]"
pytest tests/ -v
```

Requires Python 3.10+. [uv](https://github.com/astral-sh/uv) recommended.

## Code of Conduct

Be excellent to each other. This is a free culture project. Fan fiction is welcome. The palace is being built.

---

*GPL-3.0 · [github.com/mrenoch/OpenLoci](https://github.com/mrenoch/OpenLoci) · ∃∞❤️*
