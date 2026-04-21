---
title: The Vestibule
type: rules
classification: unclassified
skin: digitalcircus
chassis: clue
status: active
date: {{ cookiecutter.date }}
---

# The Vestibule
*Threshold of {{ cookiecutter.palace_name }}*

---

> *"Welcome, new contestant, to The Amazing Digital Circus! You know none of this is real, right?"*
> — Caine

---

## What This Is

**{{ cookiecutter.palace_name }}** is an OpenLoci palace wearing the **Digital Circus** skin over the **Clue** chassis. The Tudor mansion becomes the digital big top. The suspects are performers who can't leave. The mystery is why they're here and whether there's a way out.

{{ cookiecutter.project_description }}

The DM is the LLM. The player is the investigator. Abstraction risk is real. Keep moving.

---

## Room Map

| # | Clue Room    | Digital Circus Room          | Prefix     | Function                              |
|---|--------------|------------------------------|------------|---------------------------------------|
| 1 | Hall         | intake_big_top_entrance      | `intake_`  | Routing, inboxes, new arrivals        |
| 2 | Study        | build_control_room           | `build_`   | Active work, Caine's domain           |
| 3 | Kitchen      | ops_candy_workshop           | `ops_`     | Infrastructure, the machinery         |
| 4 | Conservatory | collab_glitch_garden         | `collab_`  | Pair work, unpredictable terrain      |
| 5 | Lounge       | meet_audience_seats          | `meet_`    | Decisions, charters, observation      |
| 6 | Library      | think_abstract_archive       | `think_`   | Research, records, prior arrivals     |
| 7 | Billiard Rm  | priv_the_void                | `priv_`    | Private deliberation, abstraction risk|
| 8 | Ballroom     | pitch_main_ring              | `pitch_`   | External relations, center of the show|
| 9 | Dining Room  | retro_break_room             | `retro_`   | Retrospectives, masks off             |
| — | Vestibule    | The Vestibule                | —          | Global config (this room)             |

---

## To Begin a Session

1. Read `Rules/master_prompt.md`
2. Read relevant character card(s) from `Characters/`
3. Declare your starting room
4. The DM opens the show

---

*You know none of this is real, right?*
