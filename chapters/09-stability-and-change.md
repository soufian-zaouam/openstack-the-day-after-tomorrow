*Part III — Operating with Control*

# Chapter 9 — Stability and Change

Stability means protecting what already works while retaining the ability to change. This is a particular concern in OpenStack because changes cross service and infrastructure boundaries: a compute-host maintenance involves live migration; a TLS change affects the control-plane services and the agents that run on every compute node; an upgrade alters assumptions across several services at once. Stability therefore rests on three things: trusted states, controlled degradation and capacity.

Repeated recovery is not stability. If the same workaround is applied every week, the organization has not restored control; it is repeating a temporary response. Business criticality determines what stability means: the organization may decide that critical workloads require live migration while less critical workloads can tolerate a restart during operating-system patching, because the consequences differ even when the technical operation is the same. And stability depends on operational capacity. A platform with no spare capacity cannot execute every maintenance strategy as though capacity were unlimited.

## Stabilize before transforming

When a platform is already unstable, adding major architectural change makes diagnosis harder and increases the blast radius of every problem. The objective is to reach a state in which change can again be deliberate, not to freeze the platform indefinitely. I hold this as a general rule, with one caveat that experience forces me to add: there are platforms so far behind, on unmaintained releases with unpatched vulnerabilities, where the transformation *is* the only available stabilization, and waiting for calm is itself the risk. The rule is “do not stack uncertainty”, not “never move while things are difficult”. Chapters 14 and 18 return to that judgement.

Stability sometimes requires rejecting technically valid work. A feature may work correctly while being inappropriate for the current operating state. An upgrade may be necessary eventually while being unsafe this month because recovery capability or capacity is insufficient. That is sequencing, not resistance to progress. A stable platform needs enough operational capacity to absorb the next change, and if that capacity does not exist, the organization should improve the condition before increasing the load.

## Stability is a property of transitions

The most important stability questions arise before and after changes. Before a change: what state are we starting from? During it: how will we know that the platform is still within acceptable boundaries? After it: what evidence tells us that the new state is trusted? Stability is the quality of the transitions between operating states rather than a static status, and it needs explicit boundaries to be more than an intention: capacity limits, workload-migration rates, maintenance scope, API restrictions and the conditions under which a rollout stops.

A platform should not inherit its previous stability assumptions after an upgrade or an architectural change. Dependencies, performance characteristics and recovery procedures may all have changed. The new state has to earn trust through observation and verification. Consumers, for their part, should understand what the platform can safely guarantee: if compute capacity is temporarily constrained, teams may need to prioritize their migrations; if a control-plane maintenance can temporarily suspend resource creation, consumers should know what to expect. This does not mean exposing internal detail; it means aligning technical operating conditions with the business expectations built on top of the platform.

## Understand before you change

A symptom is not a diagnosis. A failed VM creation says what the user experienced; it does not say which of the services and dependencies in the provisioning chain caused it. Operational reasoning should distinguish facts, which are observed; hypotheses, which explain facts; and assumptions, which are beliefs not yet demonstrated. The distinction matters because familiar fixes are attractive. Engineers remember what worked last time, and a known fix applied to a different failure mode can introduce new risk.

OpenStack failures produce plausible explanations in abundance. A scheduling problem looks like a Nova problem, a network timeout looks like a Neutron problem, a slow operation looks like a capacity problem, and the architecture makes each of these plausible without making any of them true. Good investigation therefore tries to disprove hypotheses as well as confirm them. This is one reason cross-service knowledge matters: engineers do not need to master every component equally, but they need enough understanding of the dependency chain to recognize when a local explanation is insufficient.

Investigation is sometimes treated as an informal prelude to real work. In complex OpenStack environments it *is* the work: it requires hypotheses, evidence, dependency knowledge, controlled experiments and explicit stop conditions, and a team that invests in it avoids making several risky changes because one of them looked plausible. The best investigation is often smaller than the platform. Can the behaviour be reproduced in a test environment? Can one compute host be isolated? Can one workload pattern be compared with another? Can one dependency be observed without changing anything else? Reducing the experimental surface increases the value of every observation.

## Evidence proportional to consequence

A harmless diagnostic command needs little evidence. A production database intervention needs much more. The burden of proof should rise with blast radius and irreversibility, and this principle matters most during incidents, when urgency compresses reasoning time. A prepared organization compensates with known decision paths, stop conditions and recovery procedures established in advance. Sometimes the safest action is to wait: if uncertainty is high and the business impact of waiting is limited, collecting evidence is safer than changing the platform. Uncertainty is a risk signal in its own right.

Do not stack uncertainty. Changing the operating system, the deployment tooling, the network configuration and the OpenStack release simultaneously makes unexpected behaviour impossible to attribute. And challenge the proposed solution: a request is not a diagnosis. “Automate this”, “move these VMs”, “change this network”, “upgrade this component” should each be translated back into the problem it is meant to solve before anyone acts on it.

## Verification is part of the change

A change is not complete when the command finishes. If the objective was to restore VM creation, a successful configuration change is not enough; the organization must verify that VM creation works, that the relevant dependency remains healthy and that nothing new has broken. Verification must be designed before execution, or the team discovers too late that it has no reliable way to determine success. Stop conditions, likewise, should be defined before significant changes rather than improvised in the middle of them. Approval alone does not make a decision controlled.

Investigation has diminishing returns. At some point the organization knows enough to choose a safe action even though uncertainty remains, and the decision should state explicitly what remains unknown and why the residual uncertainty is acceptable. That is more honest than pretending the problem is fully understood. Technical decisions become business decisions at this boundary: the technical team provides evidence and consequences, business owners provide criticality, and the designated accountable owner arbitrates when risks conflict. Understanding is therefore part of governance.

> **Principle.** Before changing a mission-critical OpenStack platform, understand enough to know what you are risking, how you will detect failure, and how you will recover if you are wrong. A stable platform is one that can change without unnecessarily losing control of what already works.

---

[← Chapter 8 — Visibility Before Action](08-visibility-before-action.md) · [Contents](../README.md) · [Chapter 10 — Recovery Is a Feature →](10-recovery-is-a-feature.md)
