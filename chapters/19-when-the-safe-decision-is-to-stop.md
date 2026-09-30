*Part VI — Decisions from the Field*

# Chapter 19 — When the Safe Decision Is to Stop

Operational teams are measured by their ability to restore service and keep work moving. That creates a bias toward action, and in mission-critical environments continuing to act is not always the safest option. Sometimes stopping is the decision that preserves control.

## Context

A production OpenStack platform running business workloads, with a highly available control plane: clustered RabbitMQ and a Galera database cluster.

## Signal

Users reported that they could no longer create virtual machines. Existing instances were running normally. The first signal was therefore a loss of one capability, provisioning, rather than an outage.

## Uncertainty

Investigation showed that the control plane’s shared infrastructure was unhealthy: RabbitMQ could no longer complete RPC exchanges reliably, and the MariaDB cluster was affected as well. What was *not* known at that point was why, which requests had been partially applied, and what would happen to the platform’s state if the APIs kept accepting operations while the message bus and the database were in this condition.

## Business risk

The immediate business impact was bounded: no new VMs could be created, and consumers could be told so. The larger risk was invisible. An unstable control plane that continues to accept API operations makes its own condition worse, creating orphaned allocations, half-built instances and records that disagree between Nova, Placement and Neutron, and every such record makes recovery slower and less certain. The workloads already running were not at risk from the control-plane condition itself; they were at risk from an uncontrolled attempt to fix it.

## Options

The immediate objective appeared to be restoring VM creation as fast as possible, which meant repairing the message bus and the database while the APIs kept accepting requests. The alternative was to stop accepting requests first, restart the shared infrastructure, verify, and only then reopen.

## Decision

The team deliberately stopped the OpenStack APIs, restarted the RabbitMQ cluster after purging its queues, and then restarted MariaDB before reopening the platform. The organization accepted a temporary and explicit loss of one capability in order to protect the platform state and the workloads that were already operating. Stopping the APIs first meant that no new requests arrived while the message bus and the database were being brought back; purging the queues meant that the backlog of RPC messages accumulated during the degradation was discarded rather than replayed against a database that had just been restarted. Stopping the APIs does not silence a platform entirely: the conductors, schedulers and agents keep their own work going, and when RabbitMQ returns every agent on every host reconnects at once, which on a large platform is itself a load to expect. The purge accepted that some in-flight operations would be lost.

## Trade-off

The cost was visible and bounded: provisioning was unavailable for the duration of the recovery, and the stop was a decision nobody could later present as “the platform stayed up”. The benefit was that the recovery took place on a platform whose state was no longer changing, which made every verification meaningful. An unstable control plane left open would have produced consequences that were broader, harder to predict and harder to explain afterwards.

## Outcome

Before the APIs were reopened, the team verified three things: that the Galera cluster was back to full size in Primary state and that the RabbitMQ cluster was whole, with its queues recreated and its consumers connected; that every compute service and network agent was reporting again; and that a test virtual machine could be created, reached and deleted end to end. Only then was provisioning restored. The cause was established afterwards: a network partition within the RabbitMQ cluster, which had split the bus into sides that the services could not agree on.

## Lesson

This is controlled degradation. The unavailable capability was explicit and bounded; the alternative was not. Three things make a decision of this kind possible. One is a technical fact: stopping the APIs does not stop the workloads (Chapter 1). The other two are organizational: knowing, before the incident, who has authority to make a disruptive decision (Chapter 13), and having leadership that will support an engineer who stops an operation for a reason they can explain. A stop decision should also be communicated as a protection decision: what is restricted, why continuing would create greater risk, what remains protected, and what condition will allow the platform to reopen.

The cause carries its own lesson. A RabbitMQ partition is a known failure mode with a known set of mitigations, from the cluster’s partition-handling setting on the versions that still have one to the network design that prevents the split in the first place, and the incident review has to reach that far, or the same situation returns. Chapter 10’s technical note names the settings; Chapter 11’s example shows why the runbook for a partitioned cluster is not the runbook for a node that has left it.

The same principle applies to planned changes. A change may already be under way when unexpected behaviour appears, and the time already invested creates no obligation to continue. Stop conditions should be concrete and, for recurring maintenance, pre-agreed: an expected dependency behaves differently; the blast radius exceeds the approved boundary; monitoring is insufficient; recovery is no longer credible; critical workload performance crosses an unacceptable threshold; required capacity is unavailable; the decision authority is not available. Pre-agreed boundaries reduce the pressure to improvise.

Stopping should create a new decision point rather than an interruption without direction: preserve evidence, establish the current state, communicate the impact, reassess, define the conditions for resumption. And once stopped, a change should not automatically resume. The situation has changed; new evidence may have appeared; the original hypothesis may no longer hold. Resumption is a new decision. Operational leadership should distinguish inactivity from containment, because stopping an API, freezing a rollout or refusing another live migration is an active decision to prevent the failure domain from expanding, and the culture has to match the process. If the formal process says “stop when unsafe” while the culture says “never stop”, the process will lose. The ability to stop safely is an organizational maturity test: a mature team can explain what it stopped, why, what it was protecting and what must become true before it continues.

> **Principle.** Stopping is not giving up control. In the right circumstances, it is how control is preserved.

---

[← Chapter 18 — Evolving a Mission-Critical Platform](18-evolving-a-mission-critical-platform.md) · [Contents](../README.md) · [Chapter 20 — Security, Capacity and Business Criticality →](20-security-capacity-and-business-criticality.md)
