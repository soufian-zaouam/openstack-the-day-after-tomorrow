*Part IV — The Organization Behind the Platform*

# Chapter 13 — Decision Rights

A technically capable organization can still lose control if nobody knows who has authority to decide.

> **Principle.** Everyone can challenge. Someone must decide.

Expertise is not authority. The person with the deepest technical knowledge is not necessarily the person accountable for the business consequence, and decision rights should follow consequence. Before a significant decision, four questions should have answers: who provides the technical assessment, who owns the affected capability, who is accountable for the outcome, and who has authority to decide. The decision maker should never be isolated from evidence. During incidents, a designated incident leader coordinates the decision process while technical experts provide investigation and consequences, and business criticality must be represented when disruptive actions are considered. During planned changes, the proposal, technical validation, operational impact, capability ownership, recovery readiness, consumer impact and risk acceptance should all be visible. Technical teams assess technical risk. Authorized owners accept the relevant business risk.

The chain runs from action to authority:

**Action** → **Operational accountability** → **Capability ownership** → **Platform accountability** → **Business consequence** → **Decision authority**

Governance is complete only when the final authority is visible.

## Decision rights should be visible before the incident

Incident pressure is a poor time to discover who can authorize a disruptive action. For critical OpenStack capabilities, the organization should identify in advance who can decide to suspend the APIs, isolate a component, restart a dependency, prioritize workload migration or accept temporary degradation. This does not mean a large approval matrix. It means defining the small number of consequential decisions where ambiguity would be dangerous, and making sure the incident leader’s authority operates within predefined boundaries: enough to coordinate rapid action, not so absolute that technical experts cannot challenge an unsafe action or that business impact drops out of view.

## Technical and business authority are different

An engineer may be the best person to determine whether resetting a dependency is technically safe. That does not make the engineer the owner of the business consequence of disabling a service for an hour. Conversely, a business owner may decide that an outage is unacceptable but cannot determine whether a proposed technical action will restore service safely. Good governance connects the two rather than collapsing them into one role.

## Decision rights follow the failure domain

A decision affecting one workload does not require the same authority as a decision affecting the entire control plane. Decision rights should reflect consequence and blast radius, which allows routine operations to remain fast while high-consequence actions receive scrutiny. Decision rights must also survive organizational change: if authority exists only because a particular manager has always made a certain decision, the governance model is fragile.

## Records, rejected options and expiry

Decision records preserve reasoning, accountability and historical context, and the rejected options can be as valuable as the selected one. If an upgrade was postponed because recovery capability was insufficient, that reason should remain visible; otherwise the next team reads the postponement as inertia. Historical decisions prevent organizations from reconsidering the same question repeatedly without learning from the previous answer (Appendix C provides a minimum record).

Risk acceptance should expire. A risk accepted today may not remain acceptable when business criticality, capacity or security exposure change, or when a new OpenStack release offers a better solution. Acceptance should carry a review condition rather than becoming permanent permission to carry debt.

Governance by committee is a temptation to resist; I say this as a preference, and organizations with a strong consensus culture will weigh it differently. Consultation is valuable; collective accountability becomes ambiguity. Good governance does not prevent people from deciding. It makes sure that the right person decides, with the right evidence, and accepts the right consequence.

---

[← Chapter 12 — Building the Team Behind the Platform](12-building-the-team-behind-the-platform.md) · [Contents](../README.md) · [Chapter 14 — Upgrades, Backports and Upstream Alignment →](14-upgrades-backports-and-upstream-alignment.md)
