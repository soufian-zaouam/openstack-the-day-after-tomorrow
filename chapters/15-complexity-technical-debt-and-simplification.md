*Part V — Evolving Without Losing Control*

# Chapter 15 — Complexity, Technical Debt and Simplification

Complexity has a cost. Every component, integration, exception, automation framework and local customization adds something the organization must understand and maintain. Complexity is not sophistication: a sophisticated architecture can be well controlled, and a simple-looking one can hide dependencies nobody understands. Chapter 3 explained how complexity accumulates and why it becomes control debt. This chapter is about deciding what to do with it.

## Complexity should be visible before approval

The question about a proposed capability is whether its value justifies the operational complexity it introduces, not merely whether it works. A new feature may have a small implementation cost and a large lifecycle cost: someone must patch it, monitor it, understand its failure modes, include it in recovery and test it at every upgrade. The test set out in Chapter 3 should therefore be answered in the proposal itself, before the capability enters production, together with two questions the proposal usually omits: what changes during an upgrade, and what happens if the component is unavailable. A useful mental model, again not a formula, is:

**Business value + Risk reduction + Control gained − Complexity introduced**

Architects evaluate complexity through diagrams. Operators experience it through questions: what failed, where do I look, who owns it, what can I safely change, how do I recover, how will this behave at the next upgrade. An architecture that looks clean on paper is operationally difficult if those questions have complicated answers, and every exception extends the time a new engineer needs to become independent. Simplification is an operational investment for that reason alone.

## Technical debt should not automatically be repaid

The presence of a customization or workaround does not determine its risk. A practical assessment asks what capability depends on it, how critical that capability is, who can operate and recover it, what happens if it fails, and whether it makes production changes or upgrades harder. The cost of carrying it matters too: a workaround that repeatedly consumes engineering time, complicates investigation or prevents the platform from following upstream has a growing operational cost. The decision can then be one of four: keep it, reduce it, remove it, or schedule its removal for a defined lifecycle event.

| Situation | Operational consequence | Typical decision |
| --- | --- | --- |
| Low business impact, well understood, no significant lifecycle impact | Limited exposure | Keep and document |
| Moderate impact, stable workaround, recurring operational effort | Consumes capacity | Plan simplification |
| Critical capability, recovery depends on one person | High organizational risk | Prioritize removal or redundancy |
| Customization complicates OpenStack upgrades | Increased lifecycle risk | Remove or replace during a planned event |
| Workaround is currently safer than a large production change | Immediate removal may increase risk | Keep temporarily with an exit condition |
| Debt repeatedly causes incidents | Direct loss of control | Treat as a priority risk |
| No remaining justification | Complexity without value | Remove |

Simplification is not replacement. Sometimes removing one configuration is enough; sometimes the debt can only be removed during an upgrade. And simplification does not always require a project: removing an obsolete exception, consolidating procedures, deleting unused automation, standardizing an operational path or retiring a local patch reduces complexity without changing the architecture, and small reductions matter because each one increases the number of situations in which engineers can rely on known behaviour.

## A debt register that produces decisions

A debt register is useful only if it helps make decisions. Each item should identify what capability it affects, who owns it, why it exists, how it is recovered, how much operational effort it consumes and what lifecycle event could remove it. That turns a list of technical annoyances into a risk-management tool. Retaining debt should be a decision rather than an omission: keeping a workaround can be entirely responsible when removal creates greater immediate risk, provided the organization records the reason, the owner, the review trigger and the exit condition. Controlled debt is fundamentally different from forgotten debt, and the question that separates them is simple: what would make us remove it? The answer may be a future release, a business requirement disappearing, a security change, a team capability change or an increase in operational cost. Without an answer, retained debt becomes forgotten debt.

Simplification must also compete for capacity. Not every debt item should become a project. Prioritize by control improvement per unit of capacity: a small customization that blocks a major upgrade may be worth more than refactoring a large but harmless legacy system, and a critical single-person dependency may deserve attention before a large amount of inert legacy configuration. The weighted model in Chapter 18 can structure that comparison. After removing debt, verify that the expected benefit occurred: did the upgrade become easier, did recovery improve, did onboarding get simpler, did investigation get faster? Otherwise the organization may have replaced one complexity with another without learning anything.

## When the workaround becomes the risk

Workarounds are legitimate operational tools. A production environment cannot always wait for a complete root-cause analysis, and the danger is not the workaround but the moment temporary becomes permanent.

> **From the field.** Virtual machines configured with dedicated CPU pinning began showing CPU steal time, which such instances should not experience. Live-migrating an affected instance to another compute host made the symptom disappear, so live migration became the response. Then the symptom returned, and the team found itself migrating the same workloads repeatedly, each migration carrying its own performance risk for the workload. The decision was to stop the migrations, accept a limited amount of steal on the affected workloads, and investigate the cause instead of relocating the symptom.

> **Technical note — pinned CPUs and live migration.** With `hw:cpu_policy=dedicated`, Nova allocates PCPU resources (the Placement resource class for dedicated host CPUs, as opposed to VCPU for shared ones) and pins each guest vCPU to a host CPU taken from the host’s `cpu_dedicated_set`. What Nova pins is the guest’s vCPUs, nothing else. It does not keep the host’s own kernel threads, interrupt handling, memory deduplication or daemons off those CPUs; that isolation has to be arranged on the host, with kernel isolation options or a tuning profile. And by default the instance’s QEMU emulator thread is allowed to run on the instance’s own pinned CPUs unless `hw:emulator_threads_policy` moves it elsewhere. Those two facts are the usual explanations for steal time on a pinned instance, ahead of overlapping pinning or a mismatch between what Nova believes and what the host does. Relocating the instance may relieve the contention for a while, as the example above shows, but corrects none of them, and a destination host with the same configuration reproduces the symptom. Live migration of instances with a NUMA topology, including pinned CPUs, was only made NUMA-aware in the Train release (Nova 20.0.0). From Stein, Nova refused such migrations unless the operator enabled the `enable_numa_live_migration` workaround; earlier releases, and Stein with the workaround, moved the instance without recalculating the guest-to-host mapping on the destination, which could itself produce overlapping pinning. See the Nova CPU topologies documentation and the Nova Train release notes.

A workaround should have a purpose, an owner, a known scope, known side effects, detection criteria, a recovery method and an exit condition. It consumes a risk budget: it adds manual effort, performance impact, operational complexity or dependency on expertise, and it remains justified only while the risk it removes exceeds the risk it introduces. Repetition is evidence. If the same workaround is applied every week, the organization has learned that the underlying condition is not being removed, and the frequency, effort and side effects should become inputs to the decision about permanent remediation.

Workarounds also become accidental architecture. A manual procedure becomes a script, the script becomes deployment logic, new engineers assume it is required, and the historical reason disappears. The most dangerous workarounds are the ones an engineer performs so often that they no longer feel exceptional; that is exactly the moment to ask whether the action has silently become part of the standard operating model, and if it has, it deserves documentation and lifecycle review like any other debt. Known workarounds should be included in upgrade planning, because an upgrade can remove them, invalidate them or break them.

Not every workaround should be eliminated. If the permanent solution requires a high-risk transformation and the workaround is stable, understood and cheap to operate, retaining it is rational. The distinction that matters is intentional retention versus accidental permanence.

> **Principle.** A workaround is safe only while the risk it introduces remains smaller than the risk it removes.

The goal of all of this is a platform whose remaining debt is visible, justified and controlled, and whose remaining complexity has earned its place; a debt-free architecture is not on offer.

---

[← Chapter 14 — Upgrades, Backports and Upstream Alignment](14-upgrades-backports-and-upstream-alignment.md) · [Contents](../README.md) · [Chapter 16 — Automation and Operational Complexity →](16-automation-and-operational-complexity.md)
