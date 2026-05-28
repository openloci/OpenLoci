---
title: "Methodology & Best Practices"
description: "How to talk to your agent, reference files across palaces, and close a session so the next one doesn't start cold."
weight: 4
---

This page documents conventions that aren't enforced by the filesystem — they're practices that accumulate into a working system. A future agent reading this page should be able to orient itself to any palace without asking you to repeat context you've already paid to establish.

---

## The Core Problem

An LLM session can look productive and still leave nothing behind. The work happened in the transcript. The transcript expires. Tomorrow you're rebuilding context from memory.

OpenLoci's answer is the **Shell Game Constraint**:

> *A session that leaves no files did not happen.*

Every session should produce at minimum one artifact: a handoff note, an updated file, a journal entry, a decision record. The palace is the memory. The transcript is the working memory. Don't confuse them.

---

## Referencing Files Across Palaces

### The Problem

A single workspace may contain multiple palaces — a job hunt palace, a research palace, a personal palace — living as sibling directories. An agent navigating by filesystem path needs to know the absolute path to each. That's brittle and hard to type in conversation.

### The `@[Palace Name]` Notation

Borrow from Excel's cross-workbook reference convention (`=[Workbook]Sheet!Cell`) and use `@[Palace Name]` to specify a palace by its directory name, letting the agent resolve the full path from context.

```
@[Palace Name]/room_directory/subdirectory/filename.md
```

**Examples:**

```
@[Job Hunt]/The Palace/design_autopsy_bay/curriculum_research.md
@[Locus]/The Palace/think_library/mempalace/index.md
@[Investigation]/The Vestibule/Characters/mulder.md
```

**Rules:**

- `@[Palace Name]` refers to the top-level palace directory as it exists on disk (case-sensitive, spaces allowed).
- Everything after the closing bracket is a path relative to that palace's root.
- The agent should resolve `@[Name]` by scanning known workspace mounts for a directory matching `Name`.
- If the palace isn't mounted or the path doesn't exist, the agent should say so explicitly rather than guessing.

### Why Not Just Use Full Paths?

Full paths expose mount points, change when folders move, and are unreadable in conversation. The `@[Name]` notation is stable to renames of mount points and is intelligible to a human reading the transcript. It's also what you'd say out loud: *"look in the Job Hunt palace."*

### Documenting Your Palaces

Add a `palaces` map to your `CLAUDE.md` or `master_prompt.md` so any agent can resolve names to paths without asking:

```yaml
palaces:
  Locus: /Users/jonah/projects/DoveNest/Locus
  Job Hunt: /Users/jonah/projects/DoveNest/Job Hunt
  Investigation: /Users/jonah/projects/DoveNest/Investigation
```

---

## Session Start Ritual

A good session start is fast and non-redundant. The agent should be able to orient itself from files, not from the user re-explaining context.

**Recommended `CLAUDE.md` / `master_prompt.md` conventions:**

1. **Timestamp every response.** Run `TZ='America/New_York' date '+[%-m/%-d/%y %-I:%M%P]'` (or equivalent) at the start of every response and prefix with the result. Both parties share a timezone; no label needed.

2. **Read the terminal log in Observer Mode.** If a `diotima-terminal.log` (or equivalent activity log) exists, read the last 20 lines silently at session start. Incorporate what's there; don't narrate it unless it's relevant.

3. **Read the latest handoff note.** The intake room (`intake_*/`) is the inbox. Find the most recent handoff file and orient from it before responding to anything else.

4. **Declare the skin.** Note the active skin early so agent voice and room names are consistent throughout the session.

---

## Session Close Ritual

The session is not done when the last task is done. It's done when the next session has enough state to continue.

**Minimum closeout:**

- Write a handoff note to `intake_*/` with the naming convention `YYYY-MM-DD-handoff-{character}.md`
- Record: what was completed, what changed, what's pending, any open questions or warnings for the next session
- Update any relevant room files with decisions made during the session
- If a significant decision was reached, file a record in `retro_*/` or `meet_*/` as appropriate

**Handoff note template:**

```markdown
---
date: YYYY-MM-DD
from: {character}
to: {character}
session_type: handoff
tags: []
---

## Completed This Session
- ...

## Files Changed
- ...

## Pending / Next Actions
- ...

## Open Questions / Warnings
- ...
```

The handoff note is not a summary for you. It's a briefing for the agent starting cold tomorrow.

---

## The "Lying Session" Problem

As of mid-2026, AI tool vendors are beginning to document what OpenLoci practitioners already know: a session that looks productive can still leave the next session with nothing. The work gets trapped in the transcript. The agent starts fresh and asks questions you already answered.

The Shell Game Constraint and the handoff ritual exist to prevent this. The palace is not a record of what the agent said — it's a record of what actually changed. Those are different things, and conflating them is the source of the leak.

If you find yourself explaining context to an agent that you explained last session, the closeout ritual failed. File a handoff note. The next Gonzo will thank you.

---

## Cross-Palace Links in Frontmatter

When a file in one palace needs to reference a file in another, use the `@[Name]` notation in frontmatter:

```yaml
---
title: "Curriculum Research"
see_also:
  - "@[Locus]/The Palace/think_library/agentic_tools_landscape.md"
  - "@[Locus]/OpenLoci/docs/content/philosophy.md"
---
```

Agents should interpret these as resolvable references, not decorative metadata.

---

## Session Artifact Routing

Not all session output belongs in the same place. Three distinct destinations serve different purposes:

### Handoff notes → `The Palace/Hall/inbox_{character}/`

The Hall contains character inboxes (`inbox_gonzo`, `inbox_mulder`, `inbox_skinner`, etc.). Handoff notes go here. They are briefings for the *next agent*, not records for the archive. Name them `YYYY-MM-DD-handoff-{character}.md`. Write them as if the next agent just walked in cold — because it has.

### Narrative session summaries → `@[Palace]/The Vestibule/Journal/content/posts/`

The Journal is a Hugo site (`The Vestibule/Journal/`) with a Makefile. Narrative summaries of sessions — reflective prose accounts of what happened, what was decided, what threads are open — go here as `YYYY-MM-DD-slug.md`. Use the archetype frontmatter (title, date, draft, tags, characters, session_type, summary). These are internal records, not public posts, but they're meant to be readable and searchable over time.

To create a new post using the Makefile:
```bash
cd @[Palace]/The Vestibule/Journal
hugo new posts/YYYY-MM-DD-your-slug.md
```

### Raw / uncategorized conversations → `The Vestibule/Conversations/`

Session exports, full compressions, transcripts, and anything that hasn't yet found a home in a Palace room go in `The Vestibule/Conversations/`. This is the holding area, not the archive. Things that belong in a specific room should eventually be filed there; things that are purely ephemeral records can live here indefinitely.

**The distinction in practice:** A handoff note tells the next agent what to do. A journal post tells a future reader what happened. A conversation file preserves the raw material in case you need it. All three may exist for the same session; they serve different consumers.

---

## Summary: The Conventions at a Glance

| Convention | Format | Where |
|---|---|---|
| Palace reference | `@[Palace Name]/path/to/file.md` | Conversation, frontmatter |
| Palace map | `palaces:` YAML block | `CLAUDE.md` or `master_prompt.md` |
| Timestamp | `[M/D/YY H:MMam]` | Start of every agent response |
| Handoff note | `YYYY-MM-DD-handoff-{char}.md` | `@[Palace]/The Palace/Hall/inbox_{character}/` |
| Narrative summary | `YYYY-MM-DD-slug.md` | `@[Palace]/The Vestibule/Journal/content/posts/` |
| Raw conversation | Freeform markdown | `@[Palace]/The Vestibule/Conversations/` |
| Decision record | Freeform markdown | `retro_*/` or `meet_*/` |
| Terminal log | Last 20 lines, silent | Observer mode at session start |

---

*See also: [Palace Structure](/palace-structure/) · [Philosophy](/philosophy/) · [Quick Start](/quick-start/)*
