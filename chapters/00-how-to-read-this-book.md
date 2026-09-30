# How to Read This Book

This is a book about operating reasoning, not a deployment guide. Most of it is argument: why control over a platform erodes, how to assess it, how to keep it while the platform, its workloads and its people change. To keep that argument honest, the text distinguishes four kinds of statement, and marks three of them explicitly.

**Technical notes** state facts about OpenStack that can be checked against project documentation: what a service does, what upstream maintains, what a command verifies. They are the parts of the book most likely to age, which is why each one names its source and the references at the end give the location.

> **Technical note.** Boxes like this one contain verifiable OpenStack facts, with a reference.

**Principles** are the operating rules the book argues for. Most are practices widely shared among people who run long-lived platforms; a few are my own position, and the surrounding text says so. A principle is a recommendation, not a fact, and a reader with a different platform and a different organization may legitimately weigh it differently.

> **Principle.** Boxes like this one state an operating rule the book recommends.

**From the field** passages describe situations I have encountered or worked through, abstracted enough that no environment can be identified. They are evidence of what happened in one context, not proof of what will happen in yours.

> **From the field.** Boxes like this one describe an operational situation and the decision it required.

Everything else in the book is reasoning: the argument that connects the facts, the principles and the experience. Where I state an opinion that competent engineers may reject, I say so in the first person.

The book owes a debt to earlier work that it does not repeat. The operating loop in Chapter 4 belongs to the same family as Deming’s plan–do–check–act cycle and the observe–orient–decide–act loop; the recovery exercises of Chapter 10 descend from the disaster-recovery testing practised by large web operators and described in the site reliability engineering literature; decision records and change discipline have a long history in IT service management. What the book adds is the application of those ideas to a platform with OpenStack’s particular shape: many services, many shared dependencies, a long life, and an organization that changes underneath it.

## Three readers, three paths

The book is written for the engineer who operates the platform, the architect who changes it, and the manager who is accountable for it. Reading in order is the intended path. Part I sets out the problem. Part II shows how to assess and measure control. Part III covers the operating disciplines. Part IV covers the organization. Part V covers evolution: upgrades, debt, automation, security and transformation. Part VI works through two decisions from the field in detail. The appendices contain the tools.

An engineer new to production OpenStack will get the most from the technical notes, from Chapters 5, 8, 10 and 14, and from the field passages, then from the rest. A manager or sponsor with no OpenStack background can take a shorter path: the Introduction, Chapters 1 to 3, Chapter 7, the last section of Chapter 12, Chapters 13 and 14 up to the first technical note, Chapters 19 and 20, the Conclusion, and Appendices D and E. That path explains why operating the platform is hard, what the business risks are, and which questions to ask the platform team; the glossary explains the service names the text uses.

---

[← Front matter](00-front-matter.md) · [Contents](../README.md) · [Introduction →](00-introduction.md)
