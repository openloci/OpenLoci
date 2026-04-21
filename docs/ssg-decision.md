---
title: SSG Decision — Hugo for OpenLoci Journal
date: 2026-04-15
status: decided
deciders: [Tinkrwitch, Fox]
tags: [architecture, ssg, journal, hugo]
---

# SSG Decision: Hugo for the OpenLoci Journal

## Context

OpenLoci needs a static site generator (SSG) to render the palace journal — a lab notebook of dated session summaries, accessible to both human readers and LLMs. The filesystem is the primary LLM interface (agents read markdown directly); the SSG serves the human layer only.

The journal requires:
- Chronological, dated session entries
- A robust, multi-dimensional tagging and categorization schema (more axes than the 9 palace rooms alone)
- Fixed vocabularies defined in `The Vestibule/Rules/`
- Minimal installation friction for users who may lack root access or container expertise
- Performance that scales as session notes accumulate over time

## Alternatives Considered

### Quartz v4
- Purpose-built for networked markdown / digital gardens
- Good backlink and graph visualization
- **Rejected**: TypeScript/Node dependency chain (npm install hell). Flat tag taxonomy only — no multi-taxonomy support without custom TypeScript plugins. Not aligned with the palace's Python ecosystem.

### Pelican
- Python-native (Jinja2 templating); fits the OpenLoci stack language-wise
- Built-in tags and categories
- **Rejected**: Multi-taxonomy support is not first-class — requires thin, poorly-maintained plugins. Slower than Hugo. Smaller theme ecosystem. The "Python fits the stack" argument is weak: the SSG consumes palace output; it doesn't need to share a runtime with the generator.

### MkDocs + Material
- Python-native, excellent documentation rendering
- **Rejected**: Optimized for structured documentation, not chronological lab notebooks. Tag support is adequate but taxonomy system is limited.

## Decision: Hugo

Hugo is the SSG for OpenLoci journal rendering.

### Reasons

**1. Multi-taxonomy support — first-class**
Hugo's taxonomy system supports arbitrary named dimensions beyond tags and categories. OpenLoci needs at minimum:
```yaml
taxonomies:
  tag: tags
  palace_room: palace_rooms
  character: characters
  phase: phases
  skin: skins
  session_type: session_types
```
Each becomes a navigable index page. Fixed vocabularies live in `The Vestibule/Rules/taxonomy.yaml` and are consumed by `hugo.toml`. No plugins required.

**2. Single static binary — no dependencies**
Hugo ships as a single compiled Go binary with zero runtime dependencies. No Python environment, no npm, no pip, no containers. A user without root access can drop the binary in `~/.local/bin` or even inside the palace directory itself and run it immediately. This is non-trivial for OpenLoci's target audience, which includes people who are not comfortable with global installs or system administration.

**3. Speed at scale**
Hugo builds thousands of pages in milliseconds. Session notes accumulate. Disk is cheap; time is not. A palace in active use for a year could have hundreds of entries — Hugo handles this without perceptible delay. Pelican and MkDocs slow meaningfully at this scale.

**4. Theme ecosystem**
Hugo has the largest SSG theme ecosystem. OpenLoci skins can map to Hugo themes — or ship a custom minimal theme tuned for palace aesthetics.

**5. Git-native workflow**
Hugo's content model (markdown files + frontmatter) is identical to the palace's filesystem structure. No import/export step. `hugo server --watch` works naturally with any file-writing agent.

## Proposed Taxonomy Schema

```yaml
# hugo.toml taxonomies block
[taxonomies]
  tag = "tags"
  palace_room = "palace_rooms"
  character = "characters"
  phase = "phases"
  skin = "skins"
  session_type = "session_types"
```

Fixed vocabulary definitions live in `The Vestibule/Rules/taxonomy.yaml` within each palace instance. The `openloci new` command should scaffold this file from the skin template.

Example session note frontmatter:
```yaml
---
title: "Tax Day — Extensions Filed"
date: 2026-04-15
palace_room: retro
character: fox
phase: debrief
skin: xfiles
session_type: synthesis
tags: [taxes, ibm, openloci, jobs]
summary: "Filed federal and CT extensions. IBM stock basis calculated. OpenLoci SSG decision reached."
---
```

## Installation Design (Open Questions)

The Hugo binary needs to be present for journal rendering. Options:

**A. Download at `openloci new` time**
The install script detects OS/arch, downloads the appropriate Hugo binary from GitHub releases, and places it at a conventional path (`{palace}/.bin/hugo` or `~/.local/bin/hugo`). Version is pinned in `The Vestibule/Rules/hugo_version.txt`.

**B. Vendor the binary into the palace template**
Ship a platform-specific Hugo binary inside the generated palace. Eliminates network dependency at runtime, but increases template size and complicates cross-platform distribution. Probably too heavy.

**C. Document-only (user installs Hugo)**
Provide install instructions in `The Vestibule/README.md`. Simplest for maintainers, most friction for users.

**Recommendation (tentative):** Option A, with Option C as fallback. The install script should check for an existing Hugo binary (in PATH or `.bin/`) before downloading. Update responsibility stays with the user — OpenLoci pins a minimum version, not an exact one. We are not in the business of being a Hugo update delivery mechanism.

## Status

Decided. Implementation pending:
- [ ] Fix render issue in Job Hunt Journal (likely missing theme or baseURL mismatch)
- [ ] Define taxonomy schema in Vestibule/Rules template
- [ ] Add `openloci journal` CLI subcommand
- [ ] Write Hugo install detection logic in `openloci new`
- [ ] Design minimal Hugo theme for palace journal rendering
