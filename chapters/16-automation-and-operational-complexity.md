*Part V — Evolving Without Losing Control*

# Chapter 16 — Automation and Operational Complexity

Automation reduces manual effort while increasing operational complexity. It introduces software, dependencies, failure modes, versioning and knowledge requirements, and it can scale an error faster than any human operator. The first question is therefore whether automating something will make the platform easier and safer for this organization to operate, which is a different question from whether it can be automated.

## Automation should follow understanding

Automating an unresolved workaround makes the problem happen faster and at greater scale. Automation should follow understanding, and my position, which not every engineering culture shares, is that execution should be automated before judgement. A predictable action can usually be automated safely. A decision that requires business context, uncertain diagnosis or risk acceptance should generally remain under human authority, because automation can determine that a host is available but should not silently determine that a critical workload can be disrupted unless the organization has explicitly delegated that decision. The evacuation example in Chapter 10 is the sharpest form of this: an automation that evacuates on a lost heartbeat without fencing has been delegated a judgement it cannot make. The distinction between execution and judgement is the heart of the matter.

Semi-automation is often the better design. A script can prepare an operation, collect evidence and propose a result while an engineer decides whether to proceed; that preserves judgement without returning the whole process to manual work. There are also legitimate reasons not to automate at all: low-frequency operations, highly contextual decisions and procedures whose automation cost exceeds their value may remain manual or semi-automatic.

## Automation is production software

Once automation can affect production OpenStack resources, it deserves production discipline: an owner, version control, testing, documentation, observability and a recovery path. The fact that its implementation is “only a script” does not reduce its consequence, and a script created as a convenience becomes a production dependency the first time it is used during an incident. The organization needs to know when an automation ran, what it changed, whether it succeeded and how to stop or recover it.

Scope matters. An automation that can affect every compute host needs stronger safeguards than one operating on a single test resource. Where practical, automated actions should have explicit boundaries and recovery paths; an automation that migrates workloads, alters networking or modifies large numbers of resources should not run as an opaque batch, and the more destructive the action, the more important preview, dry run, explicit scope, confirmation, monitoring and stop conditions become. An operator should be able to determine what an automation will do before allowing a high-consequence action.

## Automation can hide complexity and become control debt

A highly automated platform looks simple because humans see fewer commands. The complexity has not disappeared; it has moved into software, pipelines, dependencies and state management, and an operator should be able to explain what an automation does before trusting it during an incident. An automation that only its creator can explain or recover is control debt: it reduced today’s manual work and increased tomorrow’s uncertainty.

The value of automation is therefore a business trade-off rather than simply engineering time saved. It may reduce human error, improve consistency and increase response speed; against that stand development effort, maintenance, failure modes, expertise and lifecycle cost.

> **Principle.** The objective is the right level of automation for the platform the organization can actually operate, which is rarely the maximum.

---

[← Chapter 15 — Complexity, Technical Debt and Simplification](15-complexity-technical-debt-and-simplification.md) · [Contents](../README.md) · [Chapter 17 — Security Is Platform Work →](17-security-is-platform-work.md)
