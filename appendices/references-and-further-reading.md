# References and Further Reading

The framework in this book is the author’s synthesis of operational experience. The references below anchor the technical notes in primary documentation; they support the technical facts, not the operating framework itself. OpenStack evolves continuously, and release status, documentation and project details change after publication. For lifecycle decisions, always consult the current release and project documentation rather than a statement in this book.

## Architecture and services

- OpenStack Documentation, central portal. https://docs.openstack.org/
- Nova, *Nova System Architecture* (components and their responsibilities; Chapter 5). https://docs.openstack.org/nova/latest/user/architecture.html
- Nova, *Cells v2* (cell databases, host discovery; Chapter 5). https://docs.openstack.org/nova/latest/admin/cells.html
- Nova documentation. https://docs.openstack.org/nova/latest/
- Neutron documentation, including the agent and OVN reference material used in Chapter 1. https://docs.openstack.org/neutron/latest/
- Cinder documentation. https://docs.openstack.org/cinder/latest/
- Glance documentation. https://docs.openstack.org/glance/latest/
- Keystone documentation. https://docs.openstack.org/keystone/latest/
- Placement documentation. https://docs.openstack.org/placement/latest/
- OpenStack API references. https://docs.openstack.org/api-ref/

## Operations

- Nova, *Configure live migrations* (prerequisites, shared storage and block migration; Chapter 20). https://docs.openstack.org/nova/latest/admin/configuring-migrations.html
- Nova, *Live-migrate instances*. https://docs.openstack.org/nova/latest/admin/live-migration-usage.html
- Nova, *Migrate instances* (cold migration; Chapter 20). https://docs.openstack.org/nova/latest/admin/migration.html
- Nova, *Evacuate instances* (Chapters 10 and 20). https://docs.openstack.org/nova/latest/admin/evacuate.html
- Nova, *CPU topologies* (dedicated CPU policy, `cpu_dedicated_set`, emulator thread policy; Chapter 15). https://docs.openstack.org/nova/latest/admin/cpu-topologies.html
- Nova, *nova-manage* (placement audit and repair, archiving of deleted rows; Chapters 6 and 10). https://docs.openstack.org/nova/latest/cli/nova-manage.html
- oslo.messaging, *RabbitMQ driver* (quorum queues and related options; Chapter 10). https://docs.openstack.org/oslo.messaging/latest/admin/rabbit.html
- RabbitMQ, *Quorum Queues* (majority requirement, removal of classic mirroring in 4.0; Chapter 10). https://www.rabbitmq.com/docs/quorum-queues
- RabbitMQ, *Clustering and Network Partitions* (partition handling; Chapters 10 and 19). https://www.rabbitmq.com/docs/partitions
- RabbitMQ, *Monitoring* (Chapter 8). https://www.rabbitmq.com/docs/monitoring
- Galera Cluster documentation, *Weighted Quorum* (quorum and the non-Primary state; Chapter 10). https://galeracluster.com/library/documentation/weighted-quorum.html
- Galera Cluster documentation, *Crash Recovery* (bootstrapping from the most advanced node; Chapter 10). https://galeracluster.com/library/documentation/crash-recovery.html
- Galera Cluster documentation, *Monitoring the Cluster* (Chapter 8). ht tps://galeracluster.com/library/documentation/monitoring-cluster. html
- Large Scale SIG documentation, including *The Scaling Journey* (Chapter 5). https://docs.openstack.org/large-scale/
- OpenStack Operations Guide. Last substantially updated in 2017; historically valuable, no longer current. https://docs.openstack.org/operations-guide/

## Upgrades and lifecycle

- OpenStack Releases: series status, SLURP designation and dates (Chapter 14). https://releases.openstack.org/
- OpenStack Project Team Guide, *Stable Branches* (backport criteria, Maintained / Unmaintained / End of Life; Chapter 14). https://docs.openstack.org/project-team-guide/stable-branches.html
- Nova, *Upgrades* (rolling upgrade sequence, service version compatibility, online data migrations; Chapter 14). https://docs.openstack.org/nova/latest/admin/upgrades.html
- Neutron, *Upgrade strategy* (expand and contract phases; Chapter 14). https://docs.openstack.org/neutron/latest/contributor/internals/upgrade.html
- `nova-status upgrade check`. https://docs.openstack.org/nova/latest/cli/nova-status.html
- `neutron-status upgrade check`. https://docs.openstack.org/neutron/latest/cli/neutron-status.html
- `cinder-status upgrade check`. https://docs.openstack.org/cinder/latest/cli/cinder-status.html
- `placement-status upgrade check`. https://docs.openstack.org/placement/latest/cli/placement-status.html
- Nova release notes, Train (20.0.0): NUMA-aware live migration (Chapter 15). https://docs.openstack.org/releasenotes/nova/train.html
- Project release notes index. https://docs.openstack.org/releasenotes/
- OpenStack User Survey analytics, for the distribution of releases actually in production (Chapter 14). https://www.openstack.org/analytics

## Security

- OpenStack Security Advisories (OSSA), published by the Vulnerability Management Team (Chapter 17). https://security.openstack.org/ossalist.html
- OpenStack Technical Committee, *Consistent and Secure Default RBAC* (personas, `enforce_new_defaults`, `enforce_scope`, phases; Chapter 17). https://governance.openstack.org/tc/goals/selected/consistent-and-secure-rbac.html
- Keystone, *Fernet — Frequently Asked Questions* (key rotation; Chapter 17). https://docs.openstack.org/keystone/latest/admin/fernet-token-faq.html
- OpenStack Security Guide. The guide has not been substantially updated for several releases; use it for concepts, not for release-specific configuration. https://docs.openstack.org/security-guide/

## Lineage

- Google, *Site Reliability Engineering* (2016) and *The Site Reliability Workbook* (2018), for disaster-recovery testing, postmortem culture and the treatment of operational work as engineering. https://sre.google/books/
- The plan–do–check–act cycle (Deming) and the observe–orient–decide–act loop (Boyd) as the ancestors of the control loop in Chapter 4.

## Trademarks

- OpenStack brand and trademark information. https://www.openstack.org/brand/

---

[← Appendix F — Glossary](appendix-f-glossary.md) · [Contents](../README.md)
