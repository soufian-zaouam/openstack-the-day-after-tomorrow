*Appendices*

# Appendix A — The Control Decision Framework

The framework is intended to make operational judgement explicit without pretending that complex decisions reduce to a formula. A significant decision can be structured as follows; the structure should become lighter for routine decisions and more explicit as consequence grows.

1. **Situation** — What is happening?
2. **Business objective** — What are we trying to protect, restore or improve?
3. **Evidence** — What do we actually know?
4. **Uncertainty** — What remains unproven?
5. **Constraints** — What limits the available options?
6. **Business impact** — What happens if the situation deteriorates?
7. **Options** — What realistic actions are available?
8. **Trade-offs** — What risk and complexity does each option introduce?
9. **Decision rights** — Who provides evidence, who owns the capability, who accepts the consequence, who decides?
10. **Controlled action** — How will the selected option be executed?
11. **Verification** — How will success and unintended effects be established?
12. **Learning** — What should change because of the outcome?

## Decision gates

Weighted scoring must not override fundamental safety constraints. Before scoring, verify that each option has an acceptable business impact, a credible recovery path, sufficient technical evidence, a defined owner, appropriate decision authority, a bounded blast radius, and no violation of mandatory security or regulatory requirements. If one of these is absent, improve the condition before comparing options.

## Weighted scoring model

When several options remain credible after the gates, a weighted model structures the comparison. Six dimensions are scored from 1 to 5 for each option, with 5 always the preferable end of the scale (for transition risk and operational complexity, 5 means the lowest), and each score is multiplied by the dimension’s weight: business value or risk reduction (25 %), control improvement (25 %), transition risk (20 %), operational complexity (10 %), lifecycle and upstream alignment (10 %) and organizational readiness (10 %). The result lies between 1 and 5. The baseline weights are illustrative and should change with context: a security-driven decision may weight risk reduction more heavily, an unstable platform may weight transition risk more heavily, a team in transition may weight readiness more heavily. Chapter 18 contains a worked example on a realistic situation, and shows the model pointing to a recovery exercise rather than to an upgrade.

Whatever the result, the questions that matter are: Why is the transition risk a 1 rather than a 3? What evidence supports the readiness score? Which assumption is most uncertain? What event would change the ranking? Is there a non-negotiable constraint that rejects an option regardless of score?

## The model is a conversation tool

The strongest value of weighted scoring is not the final number but disagreement made visible. Two engineers may agree on the options and disagree strongly on transition risk. A business owner may assign a higher criticality to a workload than the platform team expected. A platform lead may see that a technically attractive option creates excessive lifecycle divergence. The model forces those differences into the open, and it makes later review easier: when the decision is revisited after an incident, an upgrade or a team change, the organization can identify which assumptions changed rather than starting from memory.

***Good decisions are not decisions without uncertainty. They are decisions in which uncertainty, consequence and accountability are made visible.***

---

[← Conclusion: Keeping OpenStack Under Control](../chapters/21-conclusion-keeping-openstack-under-control.md) · [Contents](../README.md) · [Appendix B — The Control Assessment Worksheet →](appendix-b-the-control-assessment-worksheet.md)
