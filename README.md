# OpenLoci

> *"A finite game is played for the purpose of winning. An infinite game is played for the purpose of continuing the play."*
> — James P. Carse, *Finite and Infinite Games* (1986)

**OpenLoci** is a filesystem-native memory palace generator for finite and infinite games.

It generates structured project environments — *palaces* — from plain text and directory hierarchies, using the Method of Loci as both metaphor and architecture. Every room is a directory. Every artifact is a markdown file. Every character is a card an agent can pick up and speak through.

---

## What It Is

OpenLoci is two things:

**A finite game engine** — for bounded projects with clear outputs. A blog migration. A job hunt. An investigation. You win when the work is done.

**A scaffold for infinite games** — via [OpenMuse](https://github.com/nullspaceink/openmuse) (coming), a spec for describing entire RPG worlds. Mount the world on a filesystem, point an LLM at it, and the game begins.

The chassis is [Clue](https://en.wikipedia.org/wiki/Cluedo). Nine rooms. Six suspects. A mystery that may or may not have a solution. Skins change the cultural frame. The structure stays.

---

## Quick Start

```bash
# Install (PyPI release coming — use dev install for now, see Development below)
pip install openloci

# Generate a new palace (base template)
openloci new my-project

# Generate with a skin
openloci new my-investigation --skin xfiles
openloci new my-startup --skin siliconvalley

# List available skins
openloci skins

# Show room map for a skin
openloci rooms xfiles

# Inspect an existing palace
openloci info ./my-investigation
```

---

## The Palace Structure

Every generated palace has two top-level directories:

```
my-palace/
├── The Vestibule/          # Global config — the threshold before the palace
│   ├── README.md           # Entry point. Read this first.
│   ├── Characters/         # One file per character/agent (prefixed: cro_, cto_, ...)
│   ├── Rooms/              # Room descriptions and atmosphere
│   └── Rules/
│       └── master_prompt.md  # DM instructions for LLM play
└── The Palace/             # Nine rooms, prefixed by function
    ├── intake_*/           # Routing, inboxes, intake
    ├── build_*/            # Active work, deep focus
    ├── ops_*/              # Infrastructure, DevOps
    ├── collab_*/           # Pair work, implementation
    ├── meet_*/             # Decisions, charters
    ├── think_*/            # Research, memory palace
    ├── priv_*/             # Private deliberation
    ├── pitch_*/            # BizDev, external relations
    └── retro_*/            # Retrospectives, personal writing
```

### Prefix Conventions

Two parallel prefix systems make the palace self-documenting across any skin:

**Room prefixes** (`intake_`, `build_`, `ops_`, ...) — functional labels that survive skin changes. The room does what its prefix says regardless of whether it's called "The Basement Office" or "The Garage."

**Character prefixes** (`ceo_`, `cro_`, `cto_`, ...) — C-suite role labels. `cro_fox_mulder.md` and `cro_erlich_bachman.md` are both Chief Research Officers wearing different skins.

---

## Available Skins

| Skin | Description |
| --- | --- |
| `xfiles` | X-Files over the Clue chassis. Mulder, Scully, Skinner, CSM. |
| `sv` | Silicon Valley. Pied Piper. Not a bug, a pivot. |
| `jobhunt` | *(coming)* Job search as investigation. |
| `office` | *(coming)* Neutral physical office — works for any org. |

Community skins welcome. See [CONTRIBUTING](#contributing).

---

## The Stack

| Layer | Technology | Function |
| --- | --- | --- |
| Memory | Filesystem | The palace itself |
| Protocol | YAML Frontmatter | Metadata, rules, routing |
| Templating | [Cookiecutter](https://github.com/cookiecutter/cookiecutter) | Palace generation |
| Presentation | [Hugo](https://gohugo.io) | Rendering, journal, navigation |
| Chronicle | Git | Truth, history, version |
| CLI | [Typer](https://typer.tiangolo.com) + [Rich](https://github.com/Textualize/rich) | Pretty interface |

---

## The Shell Game Constraint

*Yetzirah (Formation / Narrative) without Assiyah (Action / Artifacts) is fantasy.*

A session that leaves no files did not happen. All significant outputs must be grounded in material receipts — notes, evidence, summaries, handoffs. The palace grows through use, not intention.

---

## Development

All dev commands run from the **repo root** (`OpenLoci/`). Requires [uv](https://docs.astral.sh/uv/getting-started/installation/).

```bash
# 0. Install uv (once, system-wide — not per project)
#    Mac/Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh
#    Windows:
winget install --id=astral-sh.uv

# 1. Clone
git clone https://github.com/openloci/OpenLoci
cd OpenLoci

# 2. Install the openloci CLI globally (run once after cloning)
make install
#    After this, 'openloci' is available in any terminal, no activation needed.

# 3. Use it
openloci --help
openloci skins
openloci new my-investigation --skin xfiles

# 4. Install dev dependencies (for running tests and linting)
make install-dev

# 5. Run tests
make test

# 6. See all available make targets
make
```

`uv tool install --editable .` (what `make install` runs) installs the CLI into uv's managed tool store and wires it into your PATH — works on Mac, Linux, and Windows. The `--editable` flag means code changes are reflected immediately without reinstalling.

Requires Python 3.10+.

---

## Contributing

Skins are the primary contribution surface. A skin is a directory in `templates/skins/` containing:

- `skin.json` — room map, character list, metadata
- `cookiecutter.json` — template variables
- `{{cookiecutter.palace_name}}/` — the generated palace template

See `templates/skins/xfiles/` for a reference implementation.

Fan fiction is welcome. The spec is open. The palace is being built.

---

## Related Projects

- [OpenMuse](https://github.com/nullspaceink/openmuse) *(coming)* — infinite game engine, RPG world spec
- [mempalace](https://github.com/mempalace/mempalace) — related project, LLM memory via palace metaphor
- [The Art of Memory](https://en.wikipedia.org/wiki/Art_of_memory) — Frances Yates, 1966

---

## License

GPL-3.0. See [LICENSE](LICENSE).

---

*The palace is being built. ∃∞❤️*
