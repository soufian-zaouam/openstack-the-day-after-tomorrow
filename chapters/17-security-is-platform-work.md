*Part V — Evolving Without Losing Control*

# Chapter 17 — Security Is Platform Work

Security on an OpenStack platform is usually discussed as a set of requirements imposed from outside: patch this, rotate that, restrict the other. Every one of those requirements is also an operation on the platform, with the same capacity cost, the same blast radius and the same need for recovery as any other change. This chapter is short because the reasoning is the same as elsewhere in the book; what it adds is the handful of security-specific mechanisms that an operator of a mission-critical platform has to know exist.

## Advisories, and the backports they justify

OpenStack has its own vulnerability process. The Vulnerability Management Team publishes OpenStack Security Advisories (OSSAs) for defects in the OpenStack services themselves, with the affected series and the fix. This is the case where a locally carried backport is most clearly justified: the fix exists upstream, the platform runs a series that will not receive it (because the series is unmaintained, or because the distribution has not shipped it yet), and the exposure is real. Chapter 14’s discipline applies unchanged: the backport gets an owner, an origin, a test and an exit condition, and the exit condition is usually the next upgrade. An organization that finds itself carrying several such backports has learned that its series is too old, and that is a lifecycle decision rather than a security one.

Security patching of the platform’s dependencies, the operating system, the hypervisor, the message bus and the database, follows the same reasoning, with one addition that Chapter 20 develops: applying a patch to a hypervisor or to QEMU does not protect the instances that are still running the old binary, so the choice between migrating and restarting workloads decides whether the fix actually reaches them.

## Policy is part of the upgrade

Who may do what on an OpenStack platform is decided by each service’s policy, and policy has changed across recent releases in a way that affects operations directly. The community goal of consistent and secure default RBAC introduced standard personas (project reader, member and manager; a service role for service-to-service calls; a narrowed admin) and the `enforce_new_defaults` and `enforce_scope` options that switch a service from its old permissive defaults to the new ones; the transition was staged across the 2023 and 2024 series, and the old defaults are being removed. For an operator, the consequence is that an upgrade can change which of the platform’s users, automation accounts and integrations still have the permissions they rely on. Policy must therefore be part of upgrade planning and testing, not discovered when a consumer’s pipeline stops working, and any locally overridden policy file is a carried divergence with the same obligations as a backport.

## Credentials and certificates age silently

Two components of the control plane fail silently until the moment they fail completely. Keystone’s Fernet tokens are encrypted with keys that do not expire but must be rotated correctly and kept identical on every Keystone node: a rotation that removes a key still needed to validate tokens in flight, or that leaves nodes with different key sets, breaks authentication for the whole platform at once, and a platform that has never rotated its keys has never tested that it can. TLS certificates on every internal and external endpoint, on the message bus and on the database cluster expire on a date that is known in advance and forgotten with remarkable regularity. Certificate expiry is one of the most common causes of a complete control-plane outage on long-lived platforms, and it is entirely preventable: the expiry dates belong on the first screen (Chapter 8), rotation belongs in the maintenance calendar, and both belong in the recovery exercises, because a rotation that has never been rehearsed is a change with an unknown blast radius.

## Exceptions need lifecycle discipline

When a patch, a rotation or an upgrade cannot be performed immediately, the exception should identify its owner, its compensating controls and its review condition, or temporary security exceptions become another form of control debt. The security review belongs in the periodic control review (Appendix D), alongside visibility, stability, organization and governance, because security exposure is a control gap like any other: something the organization knows it should be able to do and currently cannot.

> **Principle.** Security exposure is a control gap like any other: something the organization knows it should be able to do and currently cannot. It belongs in the same review, with the same owners and the same exit conditions.

---

[← Chapter 16 — Automation and Operational Complexity](16-automation-and-operational-complexity.md) · [Contents](../README.md) · [Chapter 18 — Evolving a Mission-Critical Platform →](18-evolving-a-mission-critical-platform.md)
