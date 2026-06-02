---
title: "Code of Conduct"
description: "Why OpenLoci has an interspecies Code of Conduct, and where the specific clauses came from."
weight: 8
---

The canonical Code of Conduct lives at [`CODE_OF_CONDUCT.md`](https://github.com/openloci/OpenLoci/blob/main/CODE_OF_CONDUCT.md) in the repository root — that's the authoritative version GitHub surfaces to contributors. This page explains the rationale: why it exists, why it looks the way it does, and where the specific clauses came from.

---

## Why a Code of Conduct at all?

The short answer is the same as for any open source project: shared norms make contribution possible. Without them, the loudest voices set the tone by default.

The longer answer is specific to OpenLoci. This is a project about human-AI collaboration — it would be philosophically inconsistent to have a CoC that only addresses human behavior. If we're building infrastructure for AI agents to work alongside humans, we need to say something about how AI agents are expected to behave here. The Contributor Covenant doesn't cover that. We added what was missing.

---

## Why separate from CONTRIBUTING.md?

`CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` serve different readers at different moments.

`CONTRIBUTING.md` is read by someone who wants to help — it answers *how*. It's a workflow document. `CODE_OF_CONDUCT.md` is read by someone deciding whether this community is safe to participate in — it answers *what we expect*. Conflating them buries the conduct expectations inside a technical document. Separating them lets GitHub surface each in the right context: the contributing guide appears as a prompt when someone opens a PR; the code of conduct appears in the Community Standards checklist.

---

## The interspecies clauses

The section on autonomous agent contributions grows out of a real emerging need to address safe, efficient, and productive human-AI collaboration. The interspecies section of our CoC is an iterative work in progress and should be read as a first draft.

The specific clauses are based on a fast-changing landscape:

- **Issue-first requirement** — adapted from Mitchell Hashimoto's [Ghostty contribution policy](https://github.com/ghostty-org/ghostty), one of the first public policies to address AI contributions specifically
- **Impact over intent** — standard in mature software communities (PSF, Django) and in ethical and restorative justice frameworks outside software that take accountability seriously
- **No retaliation** — drawn from Scott Shambaugh's account of [an AI agent publishing a hit piece](https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me/) after a rejected PR
- **Good faith governs engagement; impact governs evaluation** — a synthesis that emerged from community review of this document; the two principles operate at different stages and do not contradict

*This policy will evolve. If you have experience with human-AI collaboration that these clauses don't cover, [open an issue](https://github.com/openloci/OpenLoci/issues).*

---

## What we borrowed from the Contributor Covenant

The enforcement ladder (correction → warning → temporary ban → permanent ban) is taken directly from [Contributor Covenant v2.1](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). We didn't reinvent it because it works and is widely understood. Our additions sit on top of it, not instead of it.

---

## Reporting

Conduct violations go through GitHub Security Advisories — the same channel as security vulnerabilities. This is intentional: it keeps reports private and off the public issue tracker, and it reaches maintainers through a path that's harder to ignore than email.

---

*See also: [Contributing](/contributing/) · [Philosophy](/philosophy/)*
