*Part II — Assessing Control*

# Chapter 6 — Measuring Control

Measurement should focus on capability, not activity. Ticket counts, numbers of dashboards, changes, automations and documents describe activity without proving control. The better question is whether the organization has become more capable, and that can be examined capability by capability.

For **visibility**, measure how many critical capabilities are covered by meaningful observability, how long detection takes, and how many recurring events remain unexplained. For **stability**, examine incident recurrence, capacity margin, the use of controlled degradation and how often recovery requires improvisation. For **organization**, examine single-expert dependencies, onboarding time, knowledge-transfer coverage, ownership gaps and the concentration of operational workload. For **governance**, measure whether significant decisions have clear owners, explicit risk acceptance and recorded reasoning. Three cross-cutting measures matter as much: for **recovery**, the proportion of critical capabilities with demonstrated recovery, recovery success and duration, and the number of dependencies included in recovery validation; for **change quality**, whether significant changes have credible recovery strategies, explicit risk, stop conditions and post-change verification; for **upstream alignment**, the number of significant local modifications, the maintenance status of the running series, and the effort required to reconcile local changes at each upgrade.

## Measures the platform can produce itself

Most of these measures are organizational and have to be collected by hand. Some can be read from OpenStack, and those deserve to be on the review because they do not depend on anyone’s memory: the number of hosts whose compute service is disabled and why; the count of allocations that Placement holds for instances that no longer exist, reported by `nova-manage placement audit`; the number of instances that have sat in BUILD, ERROR or a deleting state for more than a day; the age of the running series relative to its maintenance status on releases.openstack.org; the number of locally carried patches in the deployment repository; the date of the last recovery exercise for each shared component. None of these is a control score. Each is a fact that makes a conversation about control harder to avoid.

## No single score

No single control score should become the objective. A score hides differences: an organization may have excellent observability and poor recovery, and combining them into one number conceals the weakness. Trends matter more than absolute values. The useful question is whether each capability is becoming stronger or weaker over time, and measurement should lead to decisions: if single-expert dependency increases, the response may be knowledge transfer; if recovery coverage falls, recovery exercises become a priority; if upstream divergence grows, the next upgrade should include simplification.

## Metrics need a decision owner

A useful metric is connected to an action. If recurring Nova scheduling failures increase, someone should know who investigates and who decides whether the response is tuning, capacity expansion, defect remediation or an upgrade. If recovery coverage falls because a dependency changed, the metric should trigger a review. Without an owner, a metric is another dashboard element.

## Measure the concentration of capability

One of the most revealing operational measures is not technical at all: how concentrated is critical knowledge? If one engineer is the only person able to diagnose a Neutron routing problem, the organization has a measurable dependency; if three can perform the recovery independently, the dependency is materially lower. This is best measured by demonstration rather than declaration. The same applies to change capability: if only one person can execute a particular upgrade, the upgrade is an organizational bottleneck as well as a technical task.

## Measure the cost of uncertainty, and watch the leading indicators

Recurring incidents that remain unexplained deserve particular attention. An incident resolved quickly but never understood may be more dangerous than a longer incident that produced durable knowledge, because the first consumes capacity repeatedly. A useful trend is the proportion of recurring events for which the organization has a documented explanation, mitigation and owner; it connects measurement directly to learning.

Some measures describe failures after they occur. Others show that the organization is becoming less prepared: the number of critical capabilities with only one knowledgeable engineer, or the number of recovery procedures not exercised recently. These leading indicators can be more valuable than incident counts because they expose weakening capability before a failure.

## Rhythm, and proof of improvement

Measurements become useful when someone reviews trends and asks what changed. A monthly review may suit critical capabilities; a major lifecycle event justifies a deeper one. The rhythm should match the speed at which the underlying risk changes, and the review must lead to a conversation about action, or it is reporting. A control programme should also be able to prove that its work reduced risk. If a customization was removed, can the organization show that upgrade complexity decreased? If knowledge was transferred, can another engineer now perform the recovery? If observability improved, are incidents detected earlier? Improvement should be visible in capability, not in completed tasks.

Control is a capability whose condition must remain visible throughout the life of the platform, not something an organization measures once.

---

[← Chapter 5 — Assessing Platform Control](05-assessing-platform-control.md) · [Contents](../README.md) · [Chapter 7 — When Control Is Already Lost →](07-when-control-is-already-lost.md)
