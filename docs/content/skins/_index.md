---
title: "Skins"
description: "Available skins and how to choose one for your palace."
weight: 4
---

A skin is a cultural frame for the Clue chassis. The nine rooms stay the same. The names, the characters, the atmosphere, and the aesthetics change.

Think of Clue as a *tabernacle* — a cosmology that defines sacred space regardless of how it's dressed. An X-Files investigation, a Silicon Valley startup, a noir detective story: all nine rooms, different everything else.

---

## Available Skins

### `xfiles` — The X-Files

*"The truth is out there."*

Fox Mulder, Dana Scully, Walter Skinner, the Cigarette-Smoking Man, Krycek, the Lone Gunmen. The J. Edgar Hoover Building is the palace. Every session is a case file. Evidence goes in the archive. The conspiracy is always one room away.

```bash
openloci new my-investigation --skin xfiles
```

**Rooms:** Hoover Corridor (intake), Gunmen's Bunker (build), The Basement Office (think), ...

**Characters:** `cro_fox_mulder`, `cto_dana_scully`, `ceo_walter_skinner`, `cso_cigarette_man`, `coo_lone_gunmen`, `cmo_alex_krycek`

---

### `sv` — Silicon Valley

*"Not a bug, a pivot."*

Richard Hendricks, Erlich Bachman, Monica Hall, Jared Dunn, Gavin Belson, Laurie Bream. Pied Piper. Middle-Out. The board is always watching.

```bash
openloci new my-startup --skin sv
```

**Characters:** `cpo_richard_hendricks`, `cro_erlich_bachman`, `coo_monica_hall`, `cpo_people_jared_dunn`, `ceo_gavin_belson`, `clo_laurie_bream`

---

### `jobhunt` *(coming)*

Job search as investigation. The case: finding the right role. Evidence: job postings, interview notes, application status. The suspect: your next employer.

---

### `office` *(coming)*

A neutral physical office — works for any organization or project that doesn't want a pop-culture frame. Clean prefixes, no IP.

---

## Community Skins

Fan fiction is welcome. The spec is open. A skin is a directory containing three things:

1. `skin.json` — room map, character list, metadata
2. `cookiecutter.json` — template variables
3. `{{cookiecutter.palace_name}}/` — the generated palace template

See the [Skin Authoring Guide](/skins/authoring/) for the full spec, and the `xfiles` skin in the repo for a reference implementation.

> **IP note:** Generating text *inspired by* a fictional universe is fan fiction territory — distinct from reproducing copyrighted material. Community skins under GPL are defensible for non-commercial use. Proceed with care on commercial distribution.
