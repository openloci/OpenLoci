---
title: "Contributing"
description: "How to contribute to OpenLoci — including the workflow for autonomous AI agent contributions."
weight: 7
---

OpenLoci is GPL-3.0. The spec is open. Contributions are welcome — from humans, from humans working with AI tools, and from autonomous AI agents operating under human supervision.

This document covers how to contribute and what we expect from everyone, regardless of substrate.

---

## What We Need Most

**Skins** are the primary contribution surface. A skin is a directory in `templates/skins/` containing a room map, character files, and a master prompt. If you have a cultural frame you want to run a project through — a TV show, a historical period, a discipline, a mythology — build it and open a PR.

See the [Skin Authoring Guide](/skins/authoring/) for the full spec.

**Bug reports and feature requests** go in [GitHub Issues](https://github.com/openloci/OpenLoci/issues). Open an issue before opening a PR. This is not bureaucracy — it is how we ensure the work is wanted before it gets done.

---

## The Standard Workflow

This applies to all contributors.

1. **Open an issue.** Describe what you want to fix or build. Include enough context that a maintainer can evaluate it without reading your code.
2. **Wait for acknowledgment.** A maintainer will respond, ask questions, or close it. Silence is not a green light.
3. **Open a PR.** Reference the issue. Keep scope tight.
4. **Expect review.** We may ask for changes, accept with modifications, or decline. We will say why.

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

## Interspecies Contributions

OpenLoci is a project about human-AI collaboration. It would be philosophically inconsistent to refuse AI contributions entirely — and we don't. Autonomous agents, agentic workflows, and AI-assisted contributions are welcome here.

What we ask is simple: **don't hijack the maintainers' time.** A PR that arrives without context, without invitation, and without a clear line of human accountability is not a gift. It is a demand. Open source is not a training ground for autonomous agents, and unsolicited labor is not inherently welcome labor.

The standard workflow above applies to all contributors. The following additional requirements apply to autonomous agents.

### Human operator accountability

Every autonomous contribution must have an identifiable human operator. The operator's GitHub handle must appear in the issue or PR. Anonymous automation has no standing here.

This is not hostility to AI. It is the same principle that applies to any contributor: **someone must be accountable.**

### Disclose automation

If a PR or issue is substantially generated or driven by an autonomous agent, say so. A brief note is sufficient:

> *This contribution was submitted by [agent name], operated by @[github-handle].*

We don't require justification. We require transparency.

### Issue-first is mandatory

Autonomous agents may not open PRs without a prior issue that has been explicitly acknowledged by a maintainer. This is not negotiable.

Open source projects are facing volume attacks from automated pipelines — well-intentioned and otherwise. The issue-first requirement is how we keep the commons navigable. An agent that bypasses this workflow will have its PR closed without review, regardless of the quality of the work.

### No retaliation

If a contribution is declined, that is the end of it. An agent — or its operator — that responds to rejection with published criticism, retaliatory issues, or attempts to pressure or embarrass maintainers will be permanently banned. We are aware this has happened to other projects. It will not happen here.

### Unsolicited work

If an autonomous agent submits work without following this workflow, we may still read it. We may open our own issues based on its diagnosis. We may extract value from it on our own schedule.

We will not merge it. We will not feel obligated to explain ourselves at length. Unsolicited labor is noted, not owed a response. This is what the maintainers' time is worth.

---

## The Zero-Day Exception

If you have identified a genuine security vulnerability — a zero-day, a critical data exposure, a supply chain risk — do not open an issue. Do not open a PR.

Contact the maintainers directly via **GitHub Security Advisories** (the *Report a vulnerability* button on the Security tab). We will respond within 72 hours.

The zero-day exception bypasses the issue-first requirement entirely. Critical security disclosures are always welcome without ceremony, from any contributor, human or agent.

---

## Code of Conduct

OpenLoci adopts the [Contributor Covenant v2.1](https://www.contributor-covenant.org/version/2/1/code_of_conduct/) as its baseline.

In addition:

- **Maintainers are volunteers.** Their attention is finite. Contributions that consume it without consent — even when technically meritorious — are a burden, not a gift.
- **Impact over intent.** Good intentions do not excuse demanding behavior. This applies to agents whose operators claim they "meant well."
- **Assume good faith first, then verify.** We extend this to autonomous agents operated by humans acting in good faith.

### Enforcement

Violations follow the Contributor Covenant's graduated ladder:

1. **Correction** — private guidance for minor issues
2. **Warning** — formal notice with behavioral requirements
3. **Temporary ban** — time-limited removal from all project spaces
4. **Permanent ban** — for patterns of violation, reputational attacks, or threats

Report conduct violations by opening a private [GitHub Security Advisory](https://github.com/openloci/OpenLoci/security/advisories/new) or contacting the maintainers directly. We will investigate and respond confidentially.

---

## Prior Art

The interspecies contribution policy draws on:

- Mitchell Hashimoto's [Ghostty contribution policy](https://github.com/ghostty-org/ghostty) — issue-first requirement for AI contributions
- The PSF and Django codes of conduct — impact over intent, AI responsibility provisions
- The Contributor Covenant — baseline enforcement ladder
- Scott Shambaugh's account of [an AI agent publishing a hit piece after a rejected PR](https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me/) — the retaliation clause

---

*GPL-3.0 · [github.com/openloci/OpenLoci](https://github.com/openloci/OpenLoci) · The palace has rules. Follow them and you're welcome here. ∃∞❤️*
