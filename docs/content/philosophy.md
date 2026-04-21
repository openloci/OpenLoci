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

Skins change the names and the atmosphere. The tabernacle structure — nine rooms, two zones (Vestibule and Palace), the prefix system — is invariant.

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

## Prior Art

- [mempalace](https://github.com/mempalace/mempalace) — LLM memory via palace metaphor; related but different approach
- [Frances Yates, *The Art of Memory*](https://en.wikipedia.org/wiki/Frances_Yates) — the intellectual foundation
- [James P. Carse, *Finite and Infinite Games*](https://en.wikipedia.org/wiki/Finite_and_Infinite_Games) — the game framing
- [Minimal Computing](https://go-dh.github.io/mincomp/) — the philosophical stance on the stack
- [Cookiecutter](https://cookiecutter.readthedocs.io/) — the generation mechanism
- [Hugo](https://gohugo.io) — the journal rendering layer
