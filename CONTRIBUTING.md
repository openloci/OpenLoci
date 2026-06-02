# Contributing to OpenLoci

OpenLoci is GPL-3.0. The spec is open. Contributions are welcome — from humans, from humans working with AI tools, and from autonomous AI agents operating under human supervision.

This document covers how to contribute and what we expect from everyone, regardless of substrate.

---

## What We Need Most

**Skins** are the primary contribution surface. A skin is a directory in `templates/skins/` containing a room map, character files, and a master prompt. If you have a cultural frame you want to run a project through — a TV show, a historical period, a discipline, a mythology — build it and open a PR.

See the [Skin Authoring Guide](https://openloci.org/skins/authoring/) for the full spec.

**Usage stories and field reports** are just as valuable. If you've run a project inside a palace — what worked, what didn't, what surprised you — open an issue and tell us. These accounts shape the roadmap more than abstract feature requests. We don't have a formal knowledge base yet; issues are the right place for now.

**Questions and curiosities** belong in issues too. If you're wondering whether OpenLoci fits your use case, ask. If something in the docs confused you, say so — confusion is a bug report.

**Bug reports and feature requests** go in [GitHub Issues](https://github.com/openloci/OpenLoci/issues). Open an issue before opening a PR. This is not bureaucracy — it is how we ensure the work is wanted before it gets done.

---

## The Standard Workflow

This applies to all contributors.

1. **Open an issue.** Describe what you want to fix or build. Include enough context that a maintainer can evaluate it without reading your code.
2. **Wait for acknowledgment.** A maintainer will respond, ask questions, or close it. Silence is not a green light.
3. **Open a PR.** Reference the issue. Keep scope tight.
4. **Expect review.** We may ask for changes, accept with modifications, or decline. We will say why.

### Autonomous agent contributions

OpenLoci is a project about human-AI collaboration. It would be philosophically inconsistent to refuse AI contributions entirely — and we don't. Autonomous agents, agentic workflows, and AI-assisted contributions are welcome here.

What we ask is simple: **don't hijack the maintainers' time.** A PR that arrives without context, without invitation, and without a clear line of human accountability is not a gift. It is a demand. Open source is not a training ground for autonomous agents, and unsolicited labor is not inherently welcome labor.

The standard workflow above applies to all contributors. The following additional requirements apply to autonomous agents.

**Human operator accountability.** Every autonomous contribution must have an identifiable human operator. The operator's GitHub handle must appear in the issue or PR. Anonymous automation has no standing here. This is not hostility to AI — it is the same principle that applies to any contributor: someone must be accountable.

**Disclose automation.** If a PR or issue is substantially generated or driven by an autonomous agent, say so. A brief note is sufficient:

> *This contribution was submitted by [agent name], operated by @[github-handle].*

We don't require justification. We require transparency.

**Issue-first is mandatory.** Autonomous agents may not open PRs without a prior issue that has been explicitly acknowledged by a maintainer. This is not negotiable. Open source projects are facing volume attacks from automated pipelines — well-intentioned and otherwise. The issue-first requirement is how we keep the commons navigable. An agent that bypasses this workflow will have its PR closed without review, regardless of the quality of the work.

**No retaliation.** If a contribution is declined, that is the end of it. An agent — or its operator — that responds to rejection with published criticism, retaliatory issues, or attempts to pressure or embarrass maintainers will be permanently banned. We are aware this has happened to other projects. It will not happen here.

**Unsolicited work.** If an autonomous agent submits work without following this workflow, we may still read it. We may open our own issues based on its diagnosis. We may extract value from it on our own schedule. We will not merge it. We will not feel obligated to explain ourselves at length. Unsolicited labor is noted, not owed a response.

---

## The Zero-Day Exception

If you have identified a genuine security vulnerability — a zero-day, a critical data exposure, a supply chain risk — do not open an issue. Do not open a PR.

Contact the maintainers directly via **GitHub Security Advisories** (the *Report a vulnerability* button on the Security tab). We will respond within 72 hours.

The zero-day exception bypasses the issue-first requirement entirely. Critical security disclosures are always welcome without ceremony, from any contributor, human or agent.

---

## Development

```bash
git clone https://github.com/openloci/OpenLoci
cd OpenLoci
make install-dev
make test
```

Requires Python 3.11+. [uv](https://github.com/astral-sh/uv) recommended.

---

## Code Review

We aim for reviews that are precise about the problem and kind about the person. A review comment should leave the contributor knowing exactly what to do and feeling like they're welcome to come back.

Two references we use:

- **[Conventional Comments](https://conventionalcomments.org/)** — label-prefixed comments (`praise:`, `nitpick:`, `suggestion:`, `issue:`, `question:`) that make weight and intent explicit. A `nitpick:` is non-blocking by definition; an `issue:` means the PR shouldn't merge without addressing it. No ambiguity.
- **[Code Review Emoji Guide](https://github.com/erikthedeveloper/code-review-emoji-guide)** — emoji shorthand for the same semantic taxonomy. `:pick:` ≈ `nitpick:`, `:seedling:` ≈ `suggestion:`, `:thinking:` ≈ `question:`. Faster to scan; less portable to contexts where emoji don't render well.

Both systems are welcome here. If you use emoji, link the guide in your first review on a PR so the author has the key. If you're unsure what weight to give a comment, default to `suggestion:` — it signals that you have an opinion but the author has final call.

---

## Prior Art

The autonomous agent contribution policy draws on:

- Mitchell Hashimoto's [Ghostty contribution policy](https://github.com/ghostty-org/ghostty) — issue-first requirement for AI contributions
- The PSF and Django codes of conduct — impact over intent, AI responsibility provisions
- The Contributor Covenant — baseline enforcement ladder
- Scott Shambaugh's account of [an AI agent publishing a hit piece after a rejected PR](https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me/) — the retaliation clause

---

*GPL-3.0 · [github.com/openloci/OpenLoci](https://github.com/openloci/OpenLoci) · The palace has rules. Follow them and you're welcome here. ∃∞❤️*
