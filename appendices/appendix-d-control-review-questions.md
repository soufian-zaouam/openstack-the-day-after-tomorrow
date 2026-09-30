*Appendices*

# Appendix D — Control Review Questions

A periodic control review can use a small set of questions. Its purpose is not to generate another report but to identify where the organization is becoming less capable of controlling its platform.

**Visibility.** Can we explain the important signals? Can we follow critical dependencies? Do we know what changed recently? Does every critical signal have an owner?

**Stability.** What are our trusted operating states? Which capabilities are repeatedly degraded? Where is capacity limiting safe maintenance? Are we protecting existing workloads while changing the platform?

**Organization.** Which capabilities depend on one person? Can new engineers become productive without informal knowledge? Is workload sustainable? Does the team retain a shared identity and purpose?

**Governance.** Who decides during a critical incident? Who accepts business risk? Who owns each technical capability? Are significant decisions recorded?

**Evolution.** How far are we from maintained upstream releases? Which local modifications or backports remain? What debt should be removed at the next lifecycle event? Is the organization ready for the next transition?

**Security.** Which advisories affect the running series, and which fixes are we carrying locally? Did the last upgrade’s policy changes get tested against our users and automation? When do our certificates and Fernet keys expire, and when were they last rotated? Which security exceptions are open, who owns them, and when are they reviewed?

---

[← Appendix C — A Minimum Change Decision Record](appendix-c-a-minimum-change-decision-record.md) · [Contents](../README.md) · [Appendix E — Operating Principles at a Glance →](appendix-e-operating-principles-at-a-glance.md)
