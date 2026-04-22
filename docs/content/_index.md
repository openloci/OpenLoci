---
title: "OpenLoci"
description: "A filesystem-native collaborative Memory Palace for distributed cognition."
---

---

## ⚠ OpenLoci is early software under active development. <br> &nbsp;&nbsp;&nbsp; Feedback welcome → [GitHub Issues](https://github.com/openloci/OpenLoci/issues)

---

## What is OpenLoci?

OpenLoci is a filesystem-native memory palace generator. It creates structured project environments — *palaces* — from plain text and directory hierarchies, using the [Method of Loci](https://en.wikipedia.org/wiki/Art_of_memory) as both metaphor and architecture.

Every room is a directory. Every artifact is a markdown file. Every agent session leaves a trace. Your conversation with the agent is the walk thorugh space.

OpenLoci values [Minimal Computing](https://go-dh.github.io/mincomp/about/) and is built on top of simple and stable technologies, such as file system directories and plain text files.  This simplicity is also platform agnostic, and OpenLoci is compatible with any Large Language Model that can access your filesystem.

OpenLoci also ships with a Journal for regular blogging about your sessions, in short narrative form.   

**For finite games** — bounded projects with clear outputs: a blog migration, a job hunt, an investigation. You win when the work is done.

**For infinite games** — ongoing practices: research, writing, learning, building a company. The palace grows through use, not intention.

---

## The Tabernacle

The contemporary memory space utilized by OpenLoci is the Tudor Mansion from the board game [Clue](https://en.wikipedia.org/wiki/Cluedo). Nine rooms. Six suspects. A mystery that may or may not have a solution. OpenLoci treats Clue as a *tabernacle* — a cosmology that defines sacred space whether or not it's physically instantiated. Skins change the cultural frame. The structure stays.

```
my-palace/
├── Makefile            ← start here
├── The Vestibule/      
|   ├── Global config   ← Master prompts, 
|   ├── Characters      ← Agent profiles, prompts, personalities
|   ├── Principles      ← Guidelines, Schemas, Schemas and fixed vocabs
|   ├── Journal         ← Daily Journal/Blog which serves as narrative glue of the project 
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
| `clue` | The original Clue. Prof. Plum, Col. Mustard, Ms. Scarlet. |
| `xfiles` | X-Files over the Clue chassis. Mulder, Scully, Skinner, CSM. |
| `siliconvalley` | Silicon Valley. Pied Piper. Not a bug, a pivot. |
| `muppets` | The Muppets. Kermit, Piggy, Fozzie, Gonzo. It ain't easy being green. |
| `digitalcircus` | The Amazing Digital Circus. Pomni, Caine, Jax, Ragatha. You know none of this is real, right? |

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

*GPL-3.0 · [github.com/openloci/OpenLoci](https://github.com/openloci/OpenLoci) · The palace is being built. ∃∞❤️*
