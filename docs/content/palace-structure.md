---
title: "Palace Structure"
description: "Rooms, prefixes, the Vestibule, and how everything fits together."
weight: 3
---

Every generated palace has two top-level directories:

```
my-palace/
├── The Vestibule/          ← global config — the threshold before the palace
│   ├── README.md           ← entry point; read this first
│   ├── Characters/         ← one file per character/agent
│   ├── Rooms/              ← room descriptions and atmosphere
│   ├── Principles/
│   │   └── master_prompt.md  ← DM instructions for LLM sessions
│   └── Journal/            ← Hugo site for rendering session notes
└── The Palace/             ← nine rooms, prefixed by function
    ├── intake_*/
    ├── build_*/
    ├── ops_*/
    ├── collab_*/
    ├── meet_*/
    ├── think_*/
    ├── priv_*/
    ├── pitch_*/
    └── retro_*/
```

---

## The Nine Rooms

Two parallel prefix systems make the palace self-documenting across any skin:

**Room prefixes** — functional labels that survive skin changes. The room does what its prefix says regardless of whether it's called "The Basement Office" or "The Garage."

| Prefix | Clue Room | Function |
|--------|-----------|----------|
| `intake_` | Hall | Inboxes, routing, triage |
| `build_` | Study | Active work, deep focus |
| `ops_` | Kitchen | Infrastructure, DevOps, builds |
| `collab_` | Conservatory | Pair work, implementation |
| `meet_` | Lounge | Decisions, charters, project management |
| `think_` | Library | Research, references, memory |
| `priv_` | Billiard Room | Private deliberation |
| `pitch_` | Ballroom | BizDev, external relations, presentations |
| `retro_` | Dining Room | Retrospectives, personal writing |

Each room has a `README.md` with YAML frontmatter describing its purpose and atmosphere within the current skin.

---

## Characters

Characters are named by the character — no role prefix. The character's file, personality card, and role description speak for themselves.

| Skin | Example character files |
|------|------------------------|
| clue | `miss_scarlett.md`, `col_mustard.md`, `dana_scully.md` |
| xfiles | `fox_mulder.md`, `dana_scully.md`, `cigarette_man.md` |
| muppets | `kermit.md`, `miss_piggy.md`, `fozzie.md` |

Each character file defines a role, personality, behavioral notes, and voice samples that an LLM can pick up and speak through. The role is described in the file — it doesn't need to be encoded in the filename.

---

## The Vestibule

The Vestibule is the threshold — the global configuration layer that sits outside the nine rooms and governs the palace as a whole.

**`Characters/`** — One markdown file per character the LLM can inhabit. Each file defines the character's role, personality, knowledge domain, and speaking style.

**`Rooms/`** — Atmospheric descriptions of each room. Consulted when an agent "enters" a room to set tone and scope.

**`Principles/master_prompt.md`** — The DM instructions. Loaded at the start of each session to orient the LLM to the palace, the active skin, the characters, and the session conventions.

**`Journal/`** — A Hugo site for rendering all palace session notes as a navigable, tagged web journal. Multi-taxonomy: rooms, characters, phases, session types. Runs locally with `hugo server`.

---

## YAML Frontmatter Protocol

Every significant file in a palace uses YAML frontmatter for metadata. The conventions are:

```yaml
---
title: "Session Title"
date: 2026-04-20
palace_room: build_study
character: moulder
phase: active
skin: xfiles
session_type: synthesis
tags: [openloci, docs, palace]
summary: "One-sentence summary of what happened."
---
```

The `session_type`, `phase`, and `skin` vocabularies are defined in `The Vestibule/Principles/taxonomy.yaml` within each palace instance.

---

## Intake Conventions

Each room's `intake_*/` directory follows a shared inbox convention:

```
intake_hall/
├── README.md
├── inbox_{character}/     ← per-character inboxes
│   └── handoff_{from}_{date}.md
└── routing/               ← triage and dispatch notes
```

Handoff files are the primary mechanism for passing context between sessions and between agents.
