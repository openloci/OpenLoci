---
title: "Palace Structure"
description: "Rooms, prefixes, the Vestibule, and how everything fits together."
weight: 3
---

Every generated palace has two top-level directories:

```
my-palace/
├── the-vestibule/          ← global config — the threshold before the palace
│   ├── README.md           ← entry point; read this first
│   ├── Characters/         ← one file per character/agent
│   ├── Rooms/              ← room descriptions and atmosphere
│   ├── Principles/
│   │   └── master_prompt.md  ← DM instructions for LLM sessions
│   └── Journal/            ← Hugo site for rendering session notes
└── the-mansion/            ← nine rooms, prefixed by function
    ├── communicating_*/
    ├── synthesizing_*/
    ├── iterating_*/
    ├── releasing_*/
    ├── deliberating_*/
    ├── researching_*/
    ├── brainstorming_*/
    ├── pitching_*/
    └── planning_*/
```

---

## The Nine Rooms

Two parallel prefix systems make the palace self-documenting across any skin:

**Room prefixes** — gerund labels that name the *activity*, not the place. The room does what its prefix says regardless of whether it's called "The Basement Office" or "The Garage." Prefixes are derived from the Kabbalistic Tree of Life: each room corresponds to one of the nine lower Sefirot, with the estate itself as Malkuth.

| Prefix | Clue Room | Sefirah | Function |
|--------|-----------|---------|----------|
| `communicating_` | Hall | Tiferet | Inboxes, routing, the hub where all paths meet |
| `synthesizing_` | Study | Binah | Original writing, theory, deep focus work |
| `iterating_` | Kitchen | Hod | Infrastructure, DevOps, builds — where things get cooked |
| `releasing_` | Conservatory | Yesod | Airlock — release notes, changelogs, almost-prod docs |
| `deliberating_` | Lounge | Gevurah | Retros, grooming, blameless retrospection |
| `researching_` | Library | Chokhmah | External sources, references, links, the flash of outside insight |
| `brainstorming_` | Billiard Room | Keter | Private ideation, unformed will, not ready to surface |
| `pitching_` | Ballroom | Netzach | BizDev, investor decks, external relations — the grandest room |
| `planning_` | Dining Room | Chesed | Specs, PRDs, sprint charters — expanding the plan before Gevurah cuts |

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

## the-vestibule

the-vestibule is the threshold — the global configuration layer that sits outside the nine rooms and governs the palace as a whole.

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
palace_room: synthesizing_study
character: moulder
phase: active
skin: xfiles
session_type: synthesis
tags: [openloci, docs, palace]
summary: "One-sentence summary of what happened."
---
```

The `session_type`, `phase`, and `skin` vocabularies are defined in `the-vestibule/Principles/taxonomy.yaml` within each palace instance.

---

## Communicating Room Conventions

The `communicating_*/` room (Hall) follows a shared inbox convention:

```
communicating_hall/
├── README.md
├── inbox_{character}/     ← per-character inboxes
│   └── handoff_{from}_{date}.md
└── routing/               ← triage and dispatch notes
```

Handoff files are the primary mechanism for passing context between sessions and between agents.
