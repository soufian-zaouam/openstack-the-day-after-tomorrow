*Part V — Evolving Without Losing Control*

# Chapter 18 — Evolving a Mission-Critical Platform

Evolution is necessary, and it is one of the moments when control is most easily lost. A platform that never changes becomes difficult to support, secure and evolve; a platform that changes too aggressively destabilizes production and overwhelms the organization. Evolution therefore starts from the current operating state rather than from the target architecture. The organization needs to understand how workloads, dependencies, recovery and ownership will move from where they are to where they should be, and direction matters as much as destination: which risks need to decrease, which capabilities need to improve, which dependencies should disappear, how close the platform should remain to upstream.

## Evolution is a sequence of operating states

A transformation roadmap should not be a list of technical projects. An upgrade, a network redesign, a deployment-tool change, a storage migration or a team reorganization matters because it moves the platform from one operating state to another, and for each transition the organization should define what changes, what remains protected, what new capability is created, what risk is introduced and how it will know the transition is complete. That makes the roadmap operational rather than architectural, and it exposes the difference between technical sequencing and control sequencing. An upgrade may be technically possible while its recovery procedure is untested; the missing dependency is organizational control, not software. The best sequence is the one that leaves the organization more able to perform the *next* transition.

Do not transform everything at once because it is technically possible; Chapter 9’s rule against stacking uncertainty applies to roadmaps as much as to changes. The existing service must be protected during transformation; control-plane and data-plane changes may need different sequencing; some workloads require live migration while others tolerate a restart. The appropriate scope of any step depends on the control the organization actually has. A transformation that consumes more control than the organization possesses is not controlled.

## Guardrails before scoring

Some conditions should be treated as gates rather than as weighted dimensions. An option should normally be rejected if it violates a mandatory security or regulatory requirement, has no credible recovery strategy for its consequence, exceeds an explicitly unacceptable business impact, depends on expertise the organization cannot provide or obtain, or introduces an unbounded blast radius. Scoring applies only to options that have passed these gates.

## A weighted decision model, applied to a realistic situation

When several evolution paths remain viable after the gates, a weighted scoring model makes the trade-offs explicit. This is the model I use; its weights are illustrative and should change with context. To show what it does and does not decide, consider a platform in the following state, which is not unusual.

The platform runs a series that has left maintenance and is two SLURP releases behind the current one. It carries about a dozen locally applied patches, three of which touch Nova scheduling and were written by an engineer who has since left. Control-plane recovery has been demonstrated once, two years ago, by that same engineer. The team has shrunk from six to four in the past year. A security advisory affects the running series, the upstream fix exists only for maintained series, and a backport is possible but untested. Three options survive the gates: an *immediate* campaign that performs both SLURP hops in one maintenance programme over a quarter; a *progressive* path that performs the first hop, stabilizes and rebuilds recovery capability, and performs the second hop six months later; and a *postponement* that spends the next two quarters removing the local patches and rebuilding recovery before any upgrade, carrying the security backport meanwhile. The postponement passes the security gate only because a tested backport is credible; without it, the option would be rejected before scoring.

| Dimension (weight) | Immediate: both hops in one quarter | Progressive: one hop, stabilize, second hop | Postpone: reduce debt first, upgrade later |
| --- | :---: | :---: | :---: |
| Business value or risk reduction (25 %) | 5 | 4 | 2 |
| Control improvement (25 %) | 4 | 4 | 3 |
| Transition risk (20 %) | 1 | 3 | 4 |
| Operational complexity (10 %) | 3 | 3 | 4 |
| Lifecycle and upstream alignment (10 %) | 5 | 4 | 1 |
| Organizational readiness (10 %) | 2 | 3 | 4 |
| **Weighted score** | **3.45** | **3.60** | **2.95** |

Each option is scored from 1 to 5 on every dimension, with 5 always the preferable end of the scale: for transition risk and operational complexity, 5 means the *lowest* risk or complexity. The option score is the sum of each dimension score multiplied by its weight.

The numbers are illustrative, and the table is more useful for what it shows than for the winner it names. The gap between the immediate and the progressive path is small enough to be inside the uncertainty of the scores; what separates them is the transition-risk line, and that score of 1 rests on a specific fact, that recovery has not been demonstrated by anyone still on the team. If a recovery exercise were run successfully next month, the immediate option’s transition risk would move to 2 or 3 and the ranking would flip. The model has therefore told the organization what to do first, and it is not an upgrade: it is a recovery exercise. The postponement scores lowest because the platform stays unmaintained for two more quarters, but it scores highest on readiness, which is the honest signal that the team is the constraint. Those are the conversations the model exists to force: why is the transition risk a 1 rather than a 3, what evidence supports the readiness score, which assumption is most uncertain, what event would change the ranking. A security-driven situation may give more weight to risk reduction; a platform already suffering from instability may weight transition risk and control improvement more heavily; a team undergoing major change may need to raise the weight of readiness. The model is a decision-support mechanism and a conversation tool, not a risk calculator, and it never overrides a gate. Appendix A gives the full framework.

## The roadmap and its decision points

A practical roadmap can be expressed in four horizons. The **current state** establishes facts, critical risks and constraints. The **control horizon** closes the gaps that would make the next transition unsafe. The **lifecycle horizon** performs upgrades, removes local divergence and uses major lifecycle events to simplify. The **future horizon** evolves the architecture and the operating capabilities once the organization can sustain them. The horizons are dependencies between capabilities rather than dates, and the roadmap becomes *Assess* → *Prepare* → *Reassess* → *Change* → *Verify* → *Learn* → *Prepare the next transition*. A multi-year roadmap cannot predict every technical detail, but it can define when the organization will reassess: after recovery validation, after capacity expansion, after a major release, after removing a key customization, after training the operating team. If a planned upgrade has to move because recovery is not ready, that is evidence that the plan has become more accurate rather than a planning failure.

## A target state is an operating state

A target architecture is incomplete without a target operating state. The organization should be able to describe how the new platform will be monitored, supported, recovered, upgraded and owned, and who will do each of those things: who owns Nova, Neutron, Cinder and their dependencies, who can recover them, how much expertise is concentrated in individuals. A new platform may require different skills, different operating hours, different support arrangements and different ownership, and if those changes are not funded and organized, the technical transformation is incomplete. A target that is technically elegant but operated by a team that does not understand it is not a successful target.

Every evolution is also the starting point for the next one. A good transformation leaves fewer unexplained customizations, better recovery, stronger documentation and a team that understands the result, so that the next upgrade is easier because of this one. Before declaring an evolution successful, ask whether the resulting platform is more understandable, recoverable and operable than the previous one: can more than one person operate it, can the organization explain its dependencies, can it recover critical capabilities, can it follow the next release without unexplained divergence, can it change without exhausting capacity, can the team challenge the architecture.

The final test is the one Chapter 1 applied to deployment: could the organization operate the resulting platform without the people who transformed it?

> **Principle.** A successful OpenStack evolution is a platform whose future can still be operated deliberately, not merely a newer one.

The two chapters that follow are not recipes. They work through situations in which technical evidence, business impact and operational constraints collided, and they show how the framework behaves when the answer is not obvious. Each is told through the same grid:

**Context** → **Signal** → **Uncertainty** → **Business risk** → **Options** → **Decision** → **Trade-off** → **Outcome** → **Lesson**

Both situations are abstracted from real operations. Details that would identify an environment have been removed; the sequence of reasoning has not.

---

[← Chapter 17 — Security Is Platform Work](17-security-is-platform-work.md) · [Contents](../README.md) · [Chapter 19 — When the Safe Decision Is to Stop →](19-when-the-safe-decision-is-to-stop.md)
