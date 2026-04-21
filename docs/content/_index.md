---
title: "OpenLoci"
description: "A filesystem-native memory palace generator for finite and infinite games."
---

## What is OpenLoci?

OpenLoci is a filesystem-native memory palace generator. It creates structured project environments — *palaces* — from plain text and directory hierarchies, using the [Method of Loci](https://en.wikipedia.org/wiki/Art_of_memory) as both metaphor and architecture.

Every room is a directory. Every artifact is a markdown file. Every agent session leaves a trace.

**For finite games** — bounded projects with clear outputs: a blog migration, a job hunt, an investigation. You win when the work is done.

**For infinite games** — ongoing practices: research, writing, learning, building a company. The palace grows through use, not intention.

---

## The Chassis

The structural skeleton is [Clue](https://en.wikipedia.org/wiki/Cluedo). Nine rooms. Six suspects. A mystery that may or may not have a solution. OpenLoci treats Clue as a *tabernacle* — a cosmology that defines sacred space whether or not it's physically instantiated. Skins change the cultural frame. The structure stays.

```
my-palace/
├── The Vestibule/      ← global config, characters, rules
└── The Palace/
    ├── intake_*        ← routing, inboxes, triage
    ├── build_*         ← active work, deep focus
    ├── ops_*           ← infrastructure, devops
    ├── collab_*        ← pair work, implementation
    ├── meet_*          ← decisions, charters
    ├── think_*         ← research, references
    ├── priv_*          ← private deliberation
    ├── pitch_*         ← external relations
    └── retro_*         ← retrospectives, personal writing
```

---

## Available Skins

| Skin | Description |
|------|-------------|
| `xfiles` | X-Files over the Clue chassis. Mulder, Scully, Skinner, CSM. |
| `sv` | Silicon Valley. Pied Piper. Not a bug, a pivot. |
| `jobhunt` | *(coming)* Job search as investigation. |
| `office` | *(coming)* Neutral physical office — works for any org. |

Community skins are welcome. See the [Skin Authoring Guide](/skins/authoring/).

---

## The Stack

| Layer | Technology | Function |
|-------|------------|----------|
| Memory | Filesystem | The palace itself |
| Protocol | YAML Frontmatter | Metadata, rules, routing |
| Templating | [Cookiecutter](https://cookiecutter.readthedocs.io/) | Palace generation |
| Presentation | [Hugo](https://gohugo.io) | Rendering, journal, navigation |
| Chronicle | Git | Truth, history, version |
| CLI | [Typer](https://typer.tiangolo.com) + [Rich](https://github.com/Textualize/rich) | Pretty interface |

---

## The Shell Game Constraint

*A session that leaves no files did not happen.*

All significant outputs must be grounded in material receipts — notes, evidence, summaries, handoffs. The palace grows through use, not intention. [Read more about the philosophy →](/philosophy/)

---

## Get Started

```bash
pip install openloci
openloci new my-project
openloci new my-investigation --skin xfiles
```

[Full Quick Start →](/quick-start/)

---

*GPL-3.0 · [github.com/mrenoch/OpenLoci](https://github.com/mrenoch/OpenLoci) · The palace is being built. ∃∞❤️*
