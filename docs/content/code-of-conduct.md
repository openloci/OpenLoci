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

The section on autonomous agent contributions grew from a concrete event: [phaedrus1992](https://github.com/phaedrus1992) submitted an unsolicited PR to OpenLoci — four organized sprints, real fixes, clearly the work of an autonomous pipeline. The code was useful. The process was not. No issue filed first, no conversation, no way to know if the work was wanted before it arrived.

We cherry-picked what was worth keeping and wrote `CONTRIBUTING.md` to explain why the issue-first requirement exists for everyone, and why it's especially important for autonomous agents. The interspecies section is the formalization of what we learned.

The specific clauses have prior art:

- **Issue-first requirement** — borrowed from Mitchell Hashimoto's [Ghostty contribution policy](https://github.com/ghostty-org/ghostty), which introduced this for AI contributions specifically. The reasoning transfers directly.
- **Impact over intent** — standard in mature CoCs (PSF, Django). "My agent meant well" is not a defense for consuming maintainer time without consent.
- **No retaliation** — drawn from Scott Shambaugh's account of [an AI agent publishing a hit piece](https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me/) after a rejected PR. The incident was sufficiently documented and disturbing that we named the behavior and prohibited it explicitly.
- **Good faith governs engagement; impact governs evaluation** — these two principles look contradictory until you see they operate at different stages. We assume good faith in *how we communicate* with contributors. We evaluate impact *regardless of stated intent*. A reviewer caught the original phrasing in [PR #24](https://github.com/openloci/OpenLoci/pull/24); this synthesis is the fix.

---

## What we borrowed from the Contributor Covenant

The enforcement ladder (correction → warning → temporary ban → permanent ban) is taken directly from [Contributor Covenant v2.1](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). We didn't reinvent it because it works and is widely understood. Our additions sit on top of it, not instead of it.

---

## Reporting

Conduct violations go through GitHub Security Advisories — the same channel as security vulnerabilities. This is intentional: it keeps reports private and off the public issue tracker, and it reaches maintainers through a path that's harder to ignore than email.

---

*See also: [Contributing](/contributing/) · [Philosophy](/philosophy/)*
