---
title: "Philosophy"
description: "The Shell Game Constraint, minimal computing, and why Clue is a tabernacle."
weight: 6
---

## The Shell Game Constraint

*A session that leaves no files did not happen.*

The Shell Game is a podcast about AI and labor — its first episode landed on Radiolab — built around the premise that you cannot trust an agent that leaves no receipts. An AI that works invisibly and leaves nothing behind is indistinguishable from an AI that did nothing.

OpenLoci is built on this constraint. Every significant session must leave material evidence: a handoff note, a summary, a decision record, a revised document. The palace grows through use, not intention. Traces are not optional — they are the work.

This is not pedantry. It's epistemology. If you can't point to the artifact, you can't verify what happened. And if you can't verify what happened, the work didn't happen.

---

## The Art of Memory

The [Method of Loci](https://en.wikipedia.org/wiki/Art_of_memory) is a mnemonic technique from antiquity: to remember a list, mentally walk through a familiar space and place each item in a specific location. When you need to recall the list, take the walk.

Frances Yates's *The Art of Memory* (1966) traces this tradition from Cicero through the Renaissance memory theatres of Giulio Camillo, who imagined a building where all human knowledge could be stored and retrieved by position in space.

OpenLoci is a filesystem instantiation of this idea. The palace is the space. The directories are the rooms. The markdown files are the objects placed in each room. The LLM is the walker.

The key insight: *spatial structure aids retrieval*. A flat file of everything is opaque. A palace where things live in predictable places is navigable — by humans and by agents.

---

## Clue as Tabernacle

The Clue/Cluedo board is not the point. It is the *chassis* — the load-bearing skeleton beneath the skin.

A tabernacle, in the architectural sense, is a structure that defines sacred space regardless of its physical instantiation. The rules of what belongs where, what is permitted, what is forbidden, exist in the specification, not the wood and cloth. You can build a tabernacle in the desert or the suburbs. The sanctity travels.

OpenLoci treats Clue this way. The nine rooms are not *really* the Study, the Kitchen, the Hall. They are functional archetypes: intake, build, ops, collab, meet, think, priv, pitch, retro. The Clue names are a mnemonic for the functions. The functions are what matter.

Skins change the names and the atmosphere. The tabernacle structure — nine rooms, two zones (Vestibule and Palace), the room prefix system — is invariant.

> *This framing emerged from a discussion of Todd Gitlin's use of Foucault's panopticon — another structure that defines a social order regardless of physical instantiation. The tabernacle is more apt here than "chassis" because it carries the implication of a portable cosmology.*

---

## Minimal Computing

Why not a vector database? Why not RAG? Why not a managed service?

[Minimal computing](https://go-dh.github.io/mincomp/) asks: *what do we need?* rather than *what can we build?*

The answer for OpenLoci: a filesystem, Git, and markdown. These are the most durable technologies in the current stack. They work offline. They work without a subscription. They work on hardware from 2010. They are readable by humans without tooling. They are versionable without ceremony. They will be readable in 2050.

Every additional dependency — a database, a service, a proprietary format — is a potential failure point, a lock-in, a thing that can be deprecated. The palace is built to last. The minimal computing framing is not poverty; it is discipline.

RAG is powerful. Vector embeddings are real. But they are the right answer for a different question — large-corpus retrieval at scale. OpenLoci's question is: *how do I structure a finite project so that an LLM can navigate it effectively?* For that question, a well-organized filesystem with good naming conventions outperforms an index of flattened chunks.

The palace is not an index. It is an architecture.

---

## Funes the Memorious

Borges wrote the autopsy of total recall in 1942.

Ireneo Funes gains perfect memory after an accident. Every moment, every perception, total fidelity. The result: he cannot abstract, cannot generalize, cannot act. *"My memory, sir, is like a garbage heap."* He dies young, crushed under the weight of perfect recall.

Storage without synthesis is paralysis. The handoff memo is not a compromise — it is the right unit. Not the transcript. Not the log. The authored summary: what mattered, what connects, what comes next.

Systems that store everything (verbatim transcripts, full conversation logs, raw embeddings) are optimized for retrieval at the cost of understanding. OpenLoci makes the opposite bet: sessions leave structured artifacts. The receipt, not the surveillance tape. Funes is the cautionary tale for every "store everything, search later" memory system.

---

## Brakhage and the Three Modes

Stan Brakhage asked in *Metaphors on Vision* (1963): *"How many colors are there in a field of grass to the crawling baby unaware of 'Green'?"*

Three cognitive modes, three memory systems:

- **Raw transcript** — the baby's field of greens. Everything, undifferentiated, pre-linguistic richness that cannot be acted on.
- **EMR checkbox / RAG fact extraction** — the adult's "Green." Coarsely named, actionable, but flattened. The synthesis that kills the particular.
- **Narrative handoff memo** — Brakhage's film. Authored structure that recovers some of the richness *within* a form that can be communicated and acted on.

The medium enables a different kind of fidelity than either extreme. This is why the palace argues not just against the EMR but acknowledges what it loses and what narrative recovers.

---

## Rita Charon and the Parallel Chart

Rita Charon founded the Program in Narrative Medicine at Columbia. Key work: *Narrative Medicine: Honoring the Stories of Illness* (2006).

The EMR replaced the physician's narrative case note with structured data fields — optimized for billing, specialist handoffs, insurance. Each specialist sees their subsystem perfectly; nobody sees the patient. You cannot reconstruct the whole person from the fields, because the narrative judgment — what connected to what, what changed, what mattered — was never captured.

Charon's practice: the **parallel chart**. Physicians write a narrative account of the clinical encounter alongside the official EMR record. The official chart is for the system; the parallel chart is for understanding.

This is exactly the OpenLoci model:
- Git log = the official record (what happened, in sequence, auditable)
- Handoff memo = the parallel chart (what mattered, what connects, what comes next)

Both exist. Neither replaces the other. The palace is infrastructure for parallel charts at every scale.

---

## Captain's Log vs. Surveillance Log

A Datadog APM trace tells you the engine is at 94% capacity. It does not tell you whether to turn around. The complete log has forensic value but not decision-making value.

The captain's log is authored. Someone made a judgment about what mattered — not what happened to every process, but what the captain needed to know and decided to record. That judgment is the irreducible human contribution. It is also the thing that makes the log navigable by anyone who comes after.

The Journal in OpenLoci is a captain's log, not a Datadog trace. The handoff memo is a captain's log. The palace grows through authored judgment, not comprehensive capture.

---

## Wampum Belts and the Living Record

The Two Row Wampum — Gus-Wen-Tah — encodes the 1613 agreement between the Haudenosaunee and Dutch settlers. Two parallel rows of purple wampum on white: two vessels traveling the same river, each in their own lane, neither steering the other's canoe.

This is not a *record* of the treaty. It *is* the treaty. When the Haudenosaunee hold up the Two Row Wampum and say it remains in effect, they are not citing a historical document. They are presenting the living agreement. The traces are not just the truth — the traces *are the agreement*, still active.

This predates all our other examples by centuries and makes the argument cross-cultural. It also sharpens it: the belt is the official record, not a parallel chart running alongside one. There is no separate "real" agreement it describes.

But the belt cannot be read in isolation. It is the mnemonic anchor for an oral tradition that travels alongside it. The belt without the ceremony, without the reader trained by the reader who was trained, is purple and white shells in a pattern. This is the Brakhage problem at the level of material culture: the medium requires its community of interpretation to be meaningful. Strip the community and you have data without context — which is precisely the EMR failure mode.

The Navajo Code Talkers are the same argument from a different angle. The language was chosen as the cipher precisely because it could not be extracted from its community of speakers. No grammar existed in enemy intelligence files. The transmission network *was* the code. Knowledge that lives in a community of practice resists the kind of indexing that destroys it.

OpenLoci, at some level, is an attempt to build the infrastructure for communities of practice — human and AI — to maintain living records rather than dead archives.

---

## Prior Art

- [mempalace](https://github.com/mempalace/mempalace) — LLM memory via palace metaphor; related but different approach
- [Frances Yates, *The Art of Memory*](https://en.wikipedia.org/wiki/Frances_Yates) — the intellectual foundation
- [James P. Carse, *Finite and Infinite Games*](https://en.wikipedia.org/wiki/Finite_and_Infinite_Games) — the game framing
- [Minimal Computing](https://go-dh.github.io/mincomp/) — the philosophical stance on the stack
- [Cookiecutter](https://cookiecutter.readthedocs.io/) — the generation mechanism
- [Hugo](https://gohugo.io) — the journal rendering layer
