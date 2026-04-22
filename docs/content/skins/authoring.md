---
title: "Skin Authoring Guide"
description: "How to build a custom skin for OpenLoci."
weight: 5
---

A skin is a directory in `templates/skins/` that provides a cultural frame for the Clue chassis. The nine rooms stay fixed; the skin supplies names, characters, atmosphere, and defaults.

---

## Directory Structure

```
templates/skins/
└── my-skin/
    ├── skin.json                          ← skin metadata and room map
    ├── cookiecutter.json                  ← template variables
    └── {{cookiecutter.palace_name}}/
        ├── The Vestibule/
        │   ├── README.md
        │   ├── Characters/
        │   │   ├── {character_name}.md
        │   │   ├── {character_name}.md
        │   │   └── ...
        │   └── Principles/
        │       └── master_prompt.md
        └── The Palace/
            ├── intake_{room-name}/
            │   └── README.md
            ├── build_{room-name}/
            │   └── README.md
            └── ... (all nine rooms)
```

---

## `skin.json`

Defines the skin's identity, room names, and character roster.

```json
{
  "skin_id": "my-skin",
  "display_name": "My Skin",
  "description": "Short description of the cultural frame.",
  "chassis": "clue",
  "rooms": {
    "intake":  "The Room Name (intake)",
    "build":   "The Room Name (build)",
    "ops":     "The Room Name (ops)",
    "collab":  "The Room Name (collab)",
    "meet":    "The Room Name (meet)",
    "think":   "The Room Name (think)",
    "priv":    "The Room Name (priv)",
    "pitch":   "The Room Name (pitch)",
    "retro":   "The Room Name (retro)"
  },
  "characters": [
    { "name": "character_slug", "display": "Character Name", "role": "Role description" },
    { "name": "character_slug", "display": "Character Name", "role": "Role description" },
    { "name": "character_slug", "display": "Character Name", "role": "Role description" }
  ]
}
```

All nine room keys are required. Characters are flexible — include as many as fit the skin's world.

---

## `cookiecutter.json`

Declares the template variables Cookiecutter will prompt for at generation time.

```json
{
  "palace_name": "my-palace",
  "author": "Your Name",
  "skin": "my-skin",
  "year": "2026"
}
```

`palace_name` is required — it's used as the root directory name. Other variables are available in templates via `{{ cookiecutter.variable_name }}`.

---

## Room READMEs

Each room's `README.md` sets the atmospheric context for that room within your skin. It will be read by both human collaborators and LLMs at the start of sessions.

```markdown
---
title: "The Room Name"
prefix: intake
skin: my-skin
---

# The Room Name

*One-sentence atmospheric framing.*

This room is for [functional description]. In the [skin world], it maps to [narrative location].

## What Belongs Here

- Incoming tasks, messages, requests
- Handoff notes from other sessions
- Routing decisions

## Atmosphere

[A paragraph of evocative description — the feel of the space, what it looks and sounds like in the skin's world.]
```

---

## Character Files

Each character file defines who the LLM is inhabiting when operating as that character.

```markdown
---
title: "Character Name"
role: "Chief Research Officer"
skin: my-skin
---

# Character Name

**Role:** Chief Research Officer

**Personality:** [Two or three sentences. Core traits, voice, worldview.]

**Domain:** [What this character knows and cares about.]

**Speaking style:** [How they communicate — terse? verbose? formal? wry?]

**In this palace:** [Their specific function and relationship to the work.]
```

---

## `master_prompt.md`

The `Principles/master_prompt.md` is loaded at the start of each session. It orients the LLM to:

- The palace structure and conventions
- The active skin and its cultural frame
- Which character is active
- The session type and expected outputs
- The Shell Game Constraint (receipts required)

See the `xfiles` skin's `master_prompt.md` for a reference implementation.

---

## Reference Implementation

The `xfiles` skin is the canonical reference. Study it before building your own:

```
templates/skins/xfiles/
├── skin.json
├── cookiecutter.json
└── {{cookiecutter.palace_name}}/
    └── The Vestibule/
        ├── Characters/
        │   ├── fox_mulder.md
        │   ├── dana_scully.md
        │   ├── walter_skinner.md
        │   └── ...
        └── Principles/
            └── master_prompt.md
```

---

## Submitting a Skin

Open a pull request to [github.com/mrenoch/OpenLoci](https://github.com/mrenoch/OpenLoci) with your skin directory under `templates/skins/`. Include a brief description in the PR body of the cultural frame and who it's for.

The spec is open. The palace is being built. ∃∞
