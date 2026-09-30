*Part III — Operating with Control*

# Chapter 8 — Visibility Before Action

OpenStack generates a large amount of operational information. Nova, Neutron, Cinder, Glance, Keystone and Placement each expose logs, notifications and API state; the message bus, the databases, storage, networking and the infrastructure beneath them generate more. More data does not create visibility. Visibility begins with operational questions: why can users not create VMs, which capabilities are affected, which dependencies are shared, is the problem new, what changed, who owns the affected capability.

A useful dashboard is one that helps an operator follow that dependency chain, rather than one that shows whether each service process is running. Symptoms must be separated from state: a service can be running while unhealthy. RabbitMQ processes can be present while messaging is degraded; Nova processes can be active while scheduling or port binding prevents every provisioning request from succeeding. Baselines are more useful than arbitrary thresholds, because operators need to know what normal looks like before deviations become meaningful.

## Visibility must follow dependencies

OpenStack’s service boundaries create misleading operational views. A Nova alarm may reflect Placement state. A provisioning problem may originate in Neutron. A service that appears healthy may be blocked by messaging or database behaviour. Visibility should therefore represent dependency paths: for each critical capability, operators should know which services and external dependencies participate in the transaction, which signals indicate degradation, and which team owns each dependency. This is more useful than a collection of independent per-service dashboards, and it is why correlation matters more than volume. An engineer facing a provisioning failure needs to connect the user symptom with scheduling, allocations, port binding, messaging and database state; another isolated graph does not help. OpenStack gives that correlation a handle: every API request carries a request identifier that the services propagate in their logs, and a platform whose logs are searchable by request id can follow one failed boot across Nova, Placement, Neutron and Glance in minutes. A platform whose logs are not is reduced to guessing by timestamp.

> **Technical note — the signals that matter on the shared components.** Without prescribing a monitoring stack, some signals belong on every production platform’s first screen because they describe the shared dependencies on which every capability rests. For the Galera cluster: `wsrep_cluster_size` and `wsrep_cluster_status` (a value other than *Primary* means the node will refuse writes) and `wsrep_flow_control_paused` (the fraction of time replication has stalled the node). For RabbitMQ: the number of messages ready and unacknowledged per queue, the number of consumers, and whether a memory or disk alarm or a partition is in effect; a queue whose messages accumulate while its consumers vanish is a service that has stopped processing, whatever its process list says. For OpenStack itself: the liveness of every compute service and network agent as the services report it (`openstack compute service list`, `openstack network agent list`), API latency and error rates at the load balancer, the number of instances in a transitional state (BUILD, deleting, migrating) for longer than an operation should take, and the difference between what Placement believes is allocated and what the hypervisors actually run. Two more signals prevent the outages that are most embarrassing afterwards: the expiry dates of every TLS certificate on the control plane, and the age of the Keystone Fernet keys. See the Galera monitoring documentation and the RabbitMQ monitoring documentation.

## Change must be visible

The platform’s state is only half of the picture. Operators also need to know what recently changed: a deployment, a configuration modification, host maintenance, a certificate rotation, a network change. Change context is what distinguishes a platform that is naturally degraded from one that has just been altered, and in my experience the question “what changed?” resolves more incidents than any single metric.

## Business context and human signals

A capacity alert is not equally urgent when it concerns a test environment and when it concerns a business capability with severe continuity requirements. Business context changes the meaning of a signal, and so do people. User reports, support tickets and consumer feedback often reveal degradation before infrastructure metrics do: a consumer reporting that VMs take unusually long to boot may be the first indication of a performance problem; a service team reporting intermittent connectivity may reveal an issue that aggregate network metrics hide. User feedback should enter the same evidence chain as technical telemetry, with correlation rather than blame as the objective.

## Ownership, boundaries and failure

A signal without an owner is information without action, so ownership should be visible alongside the signal. Visibility should also survive team boundaries. If an important signal exists only inside another team’s monitoring system, the platform operator may not have enough information to make a timely decision; critical dependencies need shared operational visibility even when their ownership remains distributed. This does not require one giant dashboard. It requires enough common evidence for the teams involved in a decision to see the same situation.

Finally, visibility should be designed for failure rather than for healthy operation. A dashboard that is informative when everything works can be useless during an incident. Operators need to know what degraded, when it changed, which dependencies are involved and whether the state is improving or deteriorating, and the only reliable way to know whether the tooling provides that is to evaluate it during realistic failure exercises.

> **Principle.** The purpose of observability is to make the platform understandable enough to support the right decision at the right time.

---

[← Chapter 7 — When Control Is Already Lost](07-when-control-is-already-lost.md) · [Contents](../README.md) · [Chapter 9 — Stability and Change →](09-stability-and-change.md)
