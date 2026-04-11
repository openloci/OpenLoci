---
title: "Characters & Stakeholder Register"
type: raci
project: lapis
classification: unclassified
date: 2026-03-31
---

# Characters & Stakeholder Register

The palace has seven characters plus one human principal. This document is the canonical stakeholder register: who everyone is, what they own, and how they relate to the work.

Individual character cards (voice, behavioral notes, Clue mapping) live in the sibling `.md` files in this directory.

---

## The Principal

| Name | Role | Stake |
|------|------|-------|
| **Jonah** | Investigator / Author | The human in the room. Holds final accountability for all decisions. The reason the palace exists. |

---

## The Characters

| Character | Clue | Room | Primary Function |
|-----------|------|------|-----------------|
| **Walter Skinner** | Colonel Mustard | Lounge / Skinner's Office | PM — charters, decisions, authorization, tickets |
| **Fox Mulder** | Mr. Green | Study / The Basement Office | Active investigation — driving work, finding what's wrong |
| **Dana Scully** | Miss Scarlett | Conservatory / The Autopsy Bay | Analysis, technical specification, QA |
| **The Lone Gunmen** | Reverend Green (ensemble) | Kitchen / The Lone Gunmen's Bunker | Code, builds, infrastructure |
| **The Cigarette Smoking Man** | Professor Plum | Billiard Room / The Smoking Room | Long arcs, strategy, things not yet ready to surface |
| **Alex Krycek** | Mrs. Peacock | Hall / The Hoover Building Corridor | Routing, intake, inbox management |
| **Deep Throat** | Mrs. White | Library / The X-Files Archive | External research, references, sources |

---

## RACI Matrix

**R** = Responsible (does the work)
**A** = Accountable (owns the outcome, has final say)
**C** = Consulted (input sought, two-way)
**I** = Informed (notified, one-way)

| Activity | Jonah | Skinner | Mulder | Scully | Lone Gunmen | CSM | Krycek | Deep Throat |
|----------|:-----:|:-------:|:------:|:------:|:-----------:|:---:|:------:|:-----------:|
| Strategic direction & vision | **A** | C | R | C | I | C | I | C |
| Project charter & PRD | **A** | R | C | I | I | C | I | I |
| RACI / stakeholder register | **A** | R | C | C | I | I | I | I |
| Technical specification | **A** | I | C | R | C | I | I | I |
| Hugo config & theme | **A** | I | R | C | R | I | I | I |
| Content migration & editing | **A** | I | R | C | R | I | I | I |
| CSS / visual identity | **A** | I | R | I | R | I | I | I |
| Search implementation | **A** | I | C | R | R | I | I | I |
| Build pipeline & deployment | **A** | I | I | C | R | I | I | I |
| QA / testing | **A** | I | C | R | C | I | I | I |
| Content publishing (ongoing) | **R/A** | I | I | I | I | I | I | I |
| Open items / ticket tracking | **A** | R | C | C | C | I | I | I |
| Session documentation | C | I | R | I | I | I | R | I |
| Inbox routing & message handling | I | I | I | I | I | I | **R** | I |
| External research & references | C | I | R | C | I | C | I | **R** |
| Long-arc strategy & BizDev | **A** | C | I | I | I | R | I | C |

---

## Notes

**Jonah is Accountable for everything.** The palace is his. Every other role is in service of his work. Agents act; he approves or redirects.

**Skinner authors, not decides.** Skinner drafts the PM artifacts and tracks open items, but accountability for all of them returns to Jonah. Skinner is the one who makes sure the paperwork exists; Jonah is the one who has to live with it.

**Mulder drives, Scully anchors.** Mulder finds the next thing to do and moves. Scully makes sure what was done is documented, correct, and understood before the next thing is done. They are in productive tension by design.

**The Lone Gunmen execute.** They do not design. They receive a spec (from Scully) and build to it. They surface blockers; they do not resolve strategic questions.

**CSM operates in the Billiard Room.** When something is not ready to be said aloud, it lives there. Long arcs, uncomfortable truths, scenarios that haven't been briefed to the full team yet. Consulted sparingly. Never ignored.

**Krycek routes, never decides.** The Hall inbox system is his domain. He moves things from where they arrive to where they belong. He does not open the packages.

**Deep Throat surfaces, then disappears.** He brings a reference, names a source, points at something in the archive. He does not stay for the meeting.

---

*The truth is out there. The stakeholders are in here.*
