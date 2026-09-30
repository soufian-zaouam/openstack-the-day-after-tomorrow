*Appendices*

# Appendix F — Glossary

**Backport** — In upstream OpenStack, a fix cherry-picked from the master branch to a stable branch under the stable branch policy. In this book, more broadly, any change carried by the deployed platform that is not part of the release it runs (Chapter 14).

**Blast radius** — The extent of the platform, and of the workloads on it, that a failure of a given change or component would reach.

**Business capability** — An outcome or service the organization depends on, as distinct from a technical component.

**Capability accountability** — Accountability for keeping a technical capability operable, maintainable, changeable and recoverable over time.

**Change capacity** — The finite ability of the organization to execute production changes safely without overwhelming operations.

**Conductor** — The Nova service that coordinates multi-step operations such as builds and migrations and mediates database access on behalf of the compute services.

**Control** — The organization’s ability to understand, decide, intervene, recover and evolve the OpenStack platform deliberately.

**Control debt** — Loss of organizational ability caused by undocumented dependencies, concentrated expertise, uncontrolled complexity, weak recovery or other conditions that reduce operational control. Distinct from technical debt: the same artefact can be one, the other or both (Chapter 3).

**Control plane / data plane** — The control plane is the set of OpenStack API services, schedulers, conductors, message bus and databases that accept and execute requests; the data plane is the hypervisors, storage and network paths on which instances actually run, together with the agents that run on them. The two fail separately (Chapter 1).

**Control theatre** — A mechanism that creates the appearance of control without materially improving decision quality or operational capability.

**Controlled degradation** — A deliberate, temporary reduction in capability intended to protect more important capabilities or prevent broader instability.

**Day 1 / Day 2** — Day 1 is the building of the platform; Day 2 is everything that follows once workloads depend on it: operation, maintenance, incidents, upgrades, recovery and the organization around them.

**Decision rights** — The explicit authority to make a decision and accept its consequence.

**Maintained / Unmaintained / End of Life** — The phases of an upstream OpenStack release series. Distinct from vendor support (Chapter 14).

**OSSA** — OpenStack Security Advisory, published by the OpenStack Vulnerability Management Team for defects in the OpenStack services (Chapter 17).

**Operational accountability** — Accountability for whether an operation was performed correctly (Chapter 12).

**Operational capacity** — The finite people, time, environments, maintenance windows and attention available to operate and change the platform safely.

**PCPU / VCPU** — The Placement resource classes for dedicated (pinned) and shared host CPUs respectively (Chapter 15).

**Platform technical accountability** — Accountability for the technical coherence of the OpenStack platform across its services and dependencies.

**Port binding** — The step in which Neutron’s mechanism driver and the agent or OVN controller on a compute host wire an instance’s port; Nova waits for Neutron’s confirmation before completing a boot (Chapter 5).

**Quorum queue** — A RabbitMQ queue type replicated across a majority of cluster nodes, now recommended by oslo.messaging in place of classic mirrored queues, which RabbitMQ 4.0 removed (Chapter 10).

**SLURP** — Skip Level Upgrade Release Process: the upstream designation of every other release series as a release from which an upgrade to the next SLURP series is supported (Chapter 14).

**Services named in this book** — Keystone (identity and the service catalogue), Nova (compute), Neutron (networking), Cinder (block storage), Glance (images), Placement (resource inventory and allocation). Beneath them: RabbitMQ (the message bus), MariaDB Galera (the database cluster), memcached (caching, notably of tokens), and a load balancer holding the API virtual IP.

**Technical debt** — A deliberate or accumulated technical compromise whose consequences must be carried by the platform over time.

**Trusted state** — A platform state whose relevant behaviour, dependencies and recovery characteristics are sufficiently known to be relied upon (Chapter 1).

**Upstream alignment** — The degree to which the platform remains reasonably close to maintained OpenStack releases and behaviour.

**Weighted decision model** — A decision-support technique that compares options against explicitly weighted criteria. It is not a substitute for judgement or for mandatory safety constraints.

---

[← Appendix E — Operating Principles at a Glance](appendix-e-operating-principles-at-a-glance.md) · [Contents](../README.md) · [References and Further Reading →](references-and-further-reading.md)
