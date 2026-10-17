<div dir="rtl">

# الطبعة العربية: المنهج والقواعد والمصطلحات

يحدّد هذا الملفّ طريقة العمل في الطبعة العربية من كتاب *OpenStack, the Day After Tomorrow*. وهو ينطبق على كلّ ملفّ في المجلّد `ar/`. تبقى الطبعة الإنجليزية هي النصّ المرجعي: تتبعها الطبعة العربية فصلًا فصلًا، وقسمًا قسمًا، وإطارًا إطارًا، وكلّ تصويب في المضمون يُجرى أوّلًا في الطبعة الإنجليزية ثمّ يُنقل إلى هنا (انظر [`CONTRIBUTING.md`](CONTRIBUTING.md)).

الطبعة العربية **مشروع مجتمعي**: يترجمها ويراجعها متطوّعون من مجتمع OpenStack بإشراف المؤلّف. هذا الملفّ هو العقد المشترك بينهم؛ من يلتزم به تُدمج مساهمته بسرعة، ومن يرى أنّ قاعدة من قواعده خاطئة يقترح تغييرها في issue من نوع «مصطلحات» بدل مخالفتها في صمت.

## المبادئ

1. **البنية نفسها، والمنهج نفسه.** ملفّ Markdown واحد لكلّ فصل، والتنظيم نفسه للأقسام، والأطر نفسها، والأشكال والجداول نفسها، وتذييل التنقّل نفسه. يُنشأ ملفّ PDF العربي بالسلسلة نفسها (`tools/pdf/build.sh ar`) ويُتحقّق منه بالفحوص نفسها؛ وتتحقّق أداة `tools/check_editions.py ar` من تطابق بنية الطبعتين.
2. **طبعة لا ترجمة حرفية.** يُحفظ المعنى والحجج والأمثلة والفروق الدقيقة وصوت المؤلّف كاملة؛ وتُعاد صياغة الجملة العربية حين يكون النقل الحرفي ثقيلًا. لا يُلخَّص شيء، ولا يُحذف شيء، ولا يُضاف شيء إلى المضمون. وإذا ساور المترجم شكّ في معنى عبارة، يترجمها بأمانة ويضع علامة `<!-- للمراجعة: ... -->` ليفصل فيها المراجعون أو المؤلّف، بدل أن يخترع تفسيرًا.
3. **مصطلحات ثابتة.** تبقى الأسماء الرسمية للمشاريع والخدمات والأوامر والخيارات والحالات بالحروف اللاتينية. ولكلّ مفهوم من مفاهيم الكتاب ترجمة واحدة مدرجة في المسرد أدناه. إذا احتاج مصطلح جديد إلى ترجمة، يُقترح في issue «مصطلحات» ويُضاف إلى المسرد قبل تعميمه.
4. **اللغة والأسلوب.** عربية فصحى معاصرة، طبيعية، سلسة، مهنية؛ دون تكلّف ولا عامية. يُخاطب القارئ بصيغة المفرد المذكّر حين يقول الأصل *you* («يمكنك»، «منصّتك»)، ويُحتفظ بضمير المتكلّم حيث يتكلّم المؤلّف عن نفسه. الجمل العربية أقصر من الإنجليزية عادةً: يجوز تقسيم جملة إنجليزية طويلة إلى جملتين، لكن لا يجوز دمج فقرتين أو تقسيم فقرة.
5. **الأرقام والاتجاه.** تُكتب الأرقام بالأرقام العربية الغربية (0-9) كما في الإصدارات والأوامر؛ وتُكتب الملفّات من اليمين إلى اليسار (انظر «اتجاه النصّ» أدناه).

## تطابق الملفّات

تحمل الملفّات العربية **الأسماء الإنجليزية نفسها**: فالأسماء اللاتينية تعمل في كلّ الأدوات والروابط دون نقحرة، ويكفي رقم الفصل أو حرف الملحق لإيجاد المقابل.

| الطبعة الإنجليزية | الطبعة العربية |
| --- | --- |
| `chapters/00-front-matter.md` | `ar/chapters/00-front-matter.md` |
| `chapters/00-how-to-read-this-book.md` | `ar/chapters/00-how-to-read-this-book.md` |
| `chapters/00-introduction.md` | `ar/chapters/00-introduction.md` |
| `chapters/NN-<slug>.md` (من 1 إلى 21) | `ar/chapters/NN-<slug>.md` (الاسم نفسه) |
| `appendices/appendix-X-<slug>.md` | `ar/appendices/appendix-X-<slug>.md` (الاسم نفسه) |
| `appendices/references-and-further-reading.md` | `ar/appendices/references-and-further-reading.md` |
| `assets/figures/figure-N-M.svg` | `assets/figures/ar/figure-N-M.svg` (الرسم نفسه معكوسًا، والتسميات مترجمة) |
| `README.md` | `ar/README.md` |

## اتجاه النصّ (RTL)

- يبدأ كلّ ملفّ عربي بالسطر `<div dir="rtl">` يليه سطر فارغ، وينتهي بسطر فارغ ثمّ `</div>`. هكذا يعرض GitHub الملفّ من اليمين إلى اليسار (محاذاة، نقاط القوائم، أعمدة الجداول). ولا تظهر هذه الأسطر في PDF: مرشّح البناء يزيلها، لأنّ الوثيقة كلّها من اليمين إلى اليسار.
- داخل النصّ لا حاجة إلى أيّ علامات اتجاه: الأسماء اللاتينية والأوامر والأرقام تُكتب كما هي، وتتولّى خوارزمية ثنائية الاتجاه ترتيبها في المتصفّح وفي PDF (LuaLaTeX مع babel).
- في الحلقات والتسلسلات، يُستخدم السهم **←** (لأنّ القراءة من اليمين إلى اليسار) حيث يستخدم الأصل →: `**المراقبة** ← **الفهم** ← …`.
- في تذييل التنقّل، يكون رابط الفصل السابق أوّلًا (فيظهر على اليمين) وينتهي بالسهم →، ويكون رابط الفصل التالي آخرًا (على اليسار) ويبدأ بالسهم ←:

  `[الفصل 3 — … →](03-….md) · [المحتويات](../README.md) · [← الفصل 5 — …](05-….md)`

- يُنشأ ملفّ PDF العربي بمحرّك LuaLaTeX (لا XeLaTeX) بخطّ Amiri للنصّ وNoto Kufi Arabic للعناوين؛ انظر [`tools/pdf/README.md`](../tools/pdf/README.md).

## العلامات البنيوية (يتعرّف عليها مرشّح البناء)

| الإنجليزية | العربية |
| --- | --- |
| `*Part I — Understanding the Problem*` | `*الجزء الأول — فهم المشكلة*` |
| `# Chapter 4 — The Control Loop` | `# الفصل 4 — حلقة التحكّم` |
| `*Appendices*` / `# Appendix A — …` | `*الملاحق*` / `# الملحق أ — …` |
| `# References and Further Reading` | `# المراجع وقراءات إضافية` |
| `> **Technical note.**` / `> **Technical note — title.**` | `> **ملاحظة تقنية.**` / `> **ملاحظة تقنية — عنوان.**` |
| `> **Principle.**` | `> **مبدأ.**` |
| `> **From the field.**` | `> **من الميدان.**` |
| `![Figure 4.1](../assets/figures/figure-4-1.svg)` | `![الشكل 4.1](../../assets/figures/ar/figure-4-1.svg)` |
| `*Figure 4.1: caption.*` | `*الشكل 4.1: التسمية.*` |
| `[← Chapter 3 — …](03-….md) · [Contents](../README.md) · [Chapter 5 — … →](05-….md)` | `[الفصل 3 — … →](03-….md) · [المحتويات](../README.md) · [← الفصل 5 — …](05-….md)` |

الشرطة في العناوين هي الشرطة الطويلة (—) كما في الأصل. أرقام الفصول بالأرقام 0-9. حروف الملاحق بترتيب الأبجد: أ، ب، ج، د، هـ، و (تقابل A إلى F). الإحالات داخل النصّ: «الفصل 19»، «الفصول 5 و8 و10»، «الملحق د».

أسماء الأجزاء: الجزء الأول — فهم المشكلة؛ الجزء الثاني — تقييم التحكّم؛ الجزء الثالث — التشغيل بتحكّم؛ الجزء الرابع — التنظيم خلف المنصّة؛ الجزء الخامس — التطوّر دون فقدان التحكّم؛ الجزء السادس — قرارات من الميدان.

## الإملاء والترقيم

- الفاصلة العربية «،» والفاصلة المنقوطة «؛» وعلامة الاستفهام «؟» بعد الكلمات العربية؛ والنقطتان «:» والنقطة «.» كما هي. لا مسافة قبل علامات الترقيم، ومسافة واحدة بعدها.
- علامتا الاقتباس «…» (بلا مسافات داخلية) للاقتباس والمصطلحات المُستحدثة؛ لا تُستخدم علامات الاقتباس المستقيمة ("…") إطلاقًا خارج الشفرة.
- الهمزة: تُكتب همزة القطع في مواضعها (أنّ، إنّ، أو، إذا) ولا تُكتب في همزة الوصل (استعادة، انتقال، ابن). التاء المربوطة والهاء لا يُخلط بينهما. الألف المقصورة (ى) لا تُكتب ياءً. لا تطويل (ـ) في النصّ إلّا في «هـ» حرف الأبجد.
- التشكيل: يُستخدم باقتصاد، حيث يرفع لبسًا أو يثبّت نطق مصطلح (التحكّم، المنصّة، المُشرف الافتراضي، المُتحكَّم فيه). المسرد يحدّد الصيغة المشكولة لكلّ مصطلح، وتُلتزم كما هي.
- النسب المئوية: «25%»؛ الوحدات: «17 × 24 سم».
- تُكتب الأسماء اللاتينية كما هي من دون تعريف بـ«الـ» الملتصقة ما أمكن: «خدمات Nova» لا «الـNova». أمّا حروف الجرّ والعطف فتُلصق بالاسم اللاتيني بتطويل: «بـOpenStack»، «لـNova»، «وNeutron» (الواو بلا تطويل). وعند الاضطرار إلى جمع اسم لاتيني يُستخدم جمع عربي مسبوق بكلمة عربية («عناقيد Galera»، «أوامر `openstack`»).
- الكلمات الإنجليزية التي تُدرج بين قوسين بعد المصطلح العربي عند أوّل ورود لها في الفصل تُكتب بالحروف اللاتينية، لا بالنقحرة: «الترحيل الحيّ (live migration)».
- ما يُكتب بين `علامات الشفرة` (الأوامر والخيارات والملفّات) يبقى مطابقًا للأصل حرفًا بحرف؛ وتتحقّق الأداة من ذلك.

## المصطلحات

أسماء الخدمات والمكوّنات ثابتة لا تُترجم ولا تُنقحر: Keystone، Nova، Neutron، Cinder، Glance، Placement، RabbitMQ، MariaDB Galera، memcached، OVN، ML2/OVS، libvirt، QEMU، oslo.messaging، Fernet. الحالات في المنبع (**Maintained** و**Unmaintained** و**End of Life** وSLURP) تبقى كما هي مع شرح عربي عند أوّل ورود.

| الإنجليزية | العربية المعتمدة | ملاحظات |
| --- | --- | --- |
| the day after tomorrow | بعد غد | عنوان الكتاب: *OpenStack، بعد غد* |
| Operating Mission-Critical OpenStack Platforms | تشغيل منصّات OpenStack الحرجة | العنوان الفرعي |
| mission-critical | حرجة / بالغة الأهمية للأعمال | «منصّة حرجة» |
| platform | المنصّة | |
| to operate / operations / operational | شغّل / العمليات (التشغيل) / تشغيلي | «عمليات اليوم الثاني»، «فريق التشغيل» |
| operator / operations team / RUN | مشغّل / فريق التشغيل / RUN | |
| Day 1 / Day 2 | اليوم الأول / اليوم الثاني | مع «(Day 2)» عند أوّل ورود في الفصل |
| Day-2 operations | عمليات اليوم الثاني | |
| control / loss of control / under control | التحكّم / فقدان التحكّم / تحت التحكّم | المفهوم المركزي؛ لا «السيطرة» ولا «الضبط» |
| control loop | حلقة التحكّم | |
| control debt / technical debt | دين التحكّم / الدين التقني | |
| control theatre / documentation theatre | مسرح التحكّم / مسرح التوثيق | |
| control gap | فجوة في التحكّم | |
| capability (four capabilities, business capability) | القدرة (القدرات الأربع، قدرة أعمال) | |
| capacity (compute, change, operational, spare) | السعة (سعة الحوسبة، سعة التغيير، السعة التشغيلية، السعة الاحتياطية) | العربية تميّز بين القدرة والسعة |
| Visibility / Stability / Organization / Governance | الرؤية / الاستقرار / التنظيم / الحوكمة | القدرات الأربع |
| Observe → Understand → Prioritize → Decide → Act → Verify → Learn | المراقبة ← الفهم ← ترتيب الأولويات ← القرار ← التنفيذ ← التحقّق ← التعلّم | بصيغة المصدر؛ في النصّ الجاري تُصرَّف الأفعال |
| Discover → Protect → Assess → Stabilize → Recover Knowledge → Simplify → Establish Control → Evolve | الاكتشاف ← الحماية ← التقييم ← التثبيت ← استرجاع المعرفة ← التبسيط ← إرساء التحكّم ← التطوير | الفصل 7 |
| Unknown → Visible → Understood → Controlled → Recoverable → Sustainable | مجهول ← مرئي ← مفهوم ← مُتحكَّم فيه ← قابل للاستعادة ← مستدام | الفصل 5 |
| Context / Signal / Uncertainty / Business risk / Options / Decision / Trade-off / Outcome / Lesson | السياق / الإشارة / عدم اليقين / مخاطر الأعمال / الخيارات / القرار / المفاضلة / النتيجة / الدرس | الفصلان 19 و20 |
| control plane / data plane | مستوى التحكّم / مستوى البيانات | |
| trusted state | الحالة الموثوقة | |
| controlled degradation | التدهور المُتحكَّم فيه | |
| blast radius | نطاق التأثير | |
| stop condition / exit condition / review condition | شرط التوقّف / شرط الخروج / شرط المراجعة | |
| guardrail | حاجز أمان | |
| recovery / to recover / recoverable / recoverability | الاستعادة / استعاد / قابل للاستعادة / قابلية الاستعادة | «التعافي من الكوارث» لـdisaster recovery |
| recovery exercise | تمرين استعادة | |
| rebuild | إعادة البناء | |
| incident / incident review / postmortem | حادث (ج. حوادث) / مراجعة الحادث / تحليل ما بعد الحادث | |
| incident leader | قائد الحادث | |
| runbook | كتيّب الإجراءات (runbook) | «إجراء» لـprocedure |
| workaround | حلّ التفافي | |
| backport / to backport | النقل الخلفي (backport) / نقل خلفيًا | مع الكلمة الإنجليزية عند أوّل ورود |
| upstream / upstream alignment | المنبع (upstream) / المواءمة مع المنبع | «البقاء أقرب ما يمكن إلى المنبع» |
| divergence | الانحراف (عن المنبع) | |
| distribution / vendor / supplier | التوزيعة / المورّد / المزوّد | |
| release / release series / series | الإصدار / سلسلة إصدارات / السلسلة | |
| maintained / unmaintained / end of life | Maintained / Unmaintained / End of Life | حالات المنبع تبقى كما هي |
| upgrade / rolling upgrade | الترقية / الترقية المتدرّجة دون انقطاع | |
| patch / patching / local patch | التصحيح / تطبيق التصحيحات / تصحيح محلّي | |
| live migration / cold migration / evacuation / to evacuate | الترحيل الحيّ / الترحيل البارد / الإخلاء / أخلى | |
| fencing / to fence | العزل القسري (fencing) / عزل قسرًا | |
| compute host / compute node / hypervisor | مضيف الحوسبة / عقدة الحوسبة / المُشرف الافتراضي (hypervisor) | |
| compute service | خدمة الحوسبة | `nova-compute` |
| scheduler / conductor (Nova) | المجدوِل (scheduler) / المنسّق (conductor) | مع الكلمة الإنجليزية عند أوّل ورود |
| message bus | ناقل الرسائل | |
| database cluster / quorum | عنقود قواعد البيانات / النصاب | |
| port binding | ربط المنفذ (port binding) | |
| scheduling / to schedule / to place | الجدولة / جدول / وضع | |
| allocation / resource provider / inventory | التخصيص / resource provider / المخزون | Placement |
| workload / instance / VM | حِمل العمل (ج. أحمال العمل) / المثيل (ج. المثيلات) / الآلة الافتراضية | |
| tenant / consumer / consuming team | المستأجر (tenant) / المستهلك / الفريق المستهلك | |
| user / engineer / platform engineer | المستخدم / المهندس / مهندس المنصّات | |
| platform team / platform lead / sponsor | فريق المنصّة / قائد المنصّة / الراعي | |
| first-line operations / escalation | الدعم من المستوى الأول / التصعيد | |
| ownership / owner | الملكية / المالك | «المسؤول» حين يكون «المالك» ملتبسًا |
| accountability / accountable | المساءلة / مساءَل (مسؤول أمام) | الفصل 12: الملكية ≠ المساءلة |
| operational / capability / platform technical accountability | المساءلة التشغيلية / المساءلة عن قدرة / المساءلة التقنية عن المنصّة | |
| decision rights / decision authority / decision owner | حقوق القرار / سلطة القرار / صاحب القرار | |
| decision record / change decision record | سجلّ القرار / سجلّ قرار التغيير | |
| debt register | سجلّ الدين | |
| weighted scoring model / weighted decision model | نموذج التقييم المرجّح / نموذج القرار المرجّح | |
| decision gate | بوابة القرار | |
| business impact / risk / criticality / owner / value | الأثر على الأعمال / مخاطر الأعمال / الأهمية الحرجة للأعمال / مالك الأعمال / قيمة الأعمال | |
| the business | جهة الأعمال / المؤسّسة | حسب السياق |
| business continuity | استمرارية الأعمال | |
| maintenance window / change window | نافذة الصيانة / نافذة التغيير | |
| handover / onboarding / knowledge transfer | التسليم / الإدماج / نقل المعرفة | |
| single-expert dependency / single point of failure | الاعتماد على خبير وحيد / نقطة فشل وحيدة | |
| redundancy of knowledge | تكرار المعرفة (توزيعها) | |
| heroics | البطولات الفردية | |
| observability / signal / baseline / threshold | قابلية الملاحظة / الإشارة / خطّ الأساس / العتبة | |
| dashboard / monitoring stack | لوحة المتابعة / منظومة المراقبة | |
| health check / "everything is green" | فحص الصحّة / «كلّ شيء أخضر» | |
| request id | معرّف الطلب | |
| security advisory (OSSA) | تنبيه أمني (OSSA) | |
| policy (RBAC) / persona | سياسة التفويض (policy) / الشخصية (persona) | |
| certificate rotation / key rotation | تدوير الشهادات / تدوير المفاتيح | |
| credentials | بيانات الاعتماد | |
| steal time / CPU pinning / pinned CPU | وقت الاستيلاء (steal time) / تثبيت المعالجات (pinning) / معالج مثبَّت | |
| roadmap / horizon / target state | خارطة الطريق / الأفق / الحالة المستهدفة | |
| transition / lifecycle event / lifecycle | الانتقال / حدث دورة الحياة / دورة الحياة | |
| simplification | التبسيط | |
| automation / semi-automation / dry run | الأتمتة / شبه الأتمتة / التشغيل التجريبي (dry run) | |
| evidence / assumption / hypothesis / fact | الأدلّة / الافتراض / الفرضية / الحقيقة | «الأدلّة» بمعنى ما يُلاحَظ |
| the field / from the field | الميدان / من الميدان | |
| disruptive (action, decision) | مُعطِّل (إجراء مُعطِّل) | |
| liveness / heartbeat | إشارة الحياة (liveness) / النبضة (heartbeat) | |
| resumption / to resume (a stopped change) | الاستئناف / استأنف | يختلف عن الاستعادة |
| sustainable workload (of a team) | عبء عمل محتمَل (للفريق) | يختلف عن حِمل العمل المستضاف |
| network fabric | نسيج الشبكة (fabric) | |
| endpoint | نقطة النهاية (endpoint) | |
| load balancer / virtual IP (VIP) | موزّع الحمل / عنوان IP الافتراضي (VIP) | |
| rollback | التراجع | |
| primary / secondary (knowledge) | الأساسي / الاحتياطي | الفصل 12 |
| bootstrap (Galera) | bootstrap | يبقى كما هو |
| quorum queue / classic mirrored queue | طابور النصاب (quorum queue) / الطابور الكلاسيكي المُعكوس | |
| mechanism driver / resource provider / scaling journey | تبقى بالإنجليزية | أسماء مفاهيم OpenStack |
| failure domain | نطاق الفشل | |
| capacity planning | تخطيط السعة | |
| cherry-pick | *cherry-pick* | يبقى كما هو، بخطّ مائل |
| to discard (transactions, messages) | أسقط / تجاهل | |
| Contents (navigation) | المحتويات | |
| Front matter | الصفحات التمهيدية | |
| How to Read This Book / Introduction / Conclusion | كيف تقرأ هذا الكتاب / المقدّمة / الخاتمة | |
| Glossary / References and Further Reading | المسرد / المراجع وقراءات إضافية | |

### عناوين الفصول والملاحق

| | الإنجليزية | العربية |
| --- | --- | --- |
| 1 | OpenStack Doesn’t End at Deployment | OpenStack لا ينتهي عند النشر |
| 2 | The Enemy Is Loss of Control | العدوّ هو فقدان التحكّم |
| 3 | Why Good Platforms Become Difficult to Operate | لماذا تصبح المنصّات الجيّدة صعبة التشغيل |
| 4 | The Control Loop | حلقة التحكّم |
| 5 | Assessing Platform Control | تقييم التحكّم في المنصّة |
| 6 | Measuring Control | قياس التحكّم |
| 7 | When Control Is Already Lost | عندما يكون التحكّم مفقودًا بالفعل |
| 8 | Visibility Before Action | الرؤية قبل الفعل |
| 9 | Stability and Change | الاستقرار والتغيير |
| 10 | Recovery Is a Feature | الاستعادة ميزة |
| 11 | Documentation Is Operational Memory | التوثيق هو الذاكرة التشغيلية |
| 12 | Building the Team Behind the Platform | بناء الفريق خلف المنصّة |
| 13 | Decision Rights | حقوق القرار |
| 14 | Upgrades, Backports and Upstream Alignment | الترقيات والنقل الخلفي والمواءمة مع المنبع |
| 15 | Complexity, Technical Debt and Simplification | التعقيد والدين التقني والتبسيط |
| 16 | Automation and Operational Complexity | الأتمتة والتعقيد التشغيلي |
| 17 | Security Is Platform Work | الأمن عمل من أعمال المنصّة |
| 18 | Evolving a Mission-Critical Platform | تطوير منصّة حرجة |
| 19 | When the Safe Decision Is to Stop | عندما يكون القرار الآمن هو التوقّف |
| 20 | Security, Capacity and Business Criticality | الأمن والسعة والأهمية الحرجة للأعمال |
| | Conclusion: Keeping OpenStack Under Control | الخاتمة: إبقاء OpenStack تحت التحكّم |
| أ | The Control Decision Framework | إطار قرار التحكّم |
| ب | The Control Assessment Worksheet | ورقة عمل تقييم التحكّم |
| ج | A Minimum Change Decision Record | سجلّ قرار تغيير بالحدّ الأدنى |
| د | Control Review Questions | أسئلة مراجعة التحكّم |
| هـ | Operating Principles at a Glance | مبادئ التشغيل في لمحة |
| و | Glossary | المسرد |

## الأشكال

تُنتَج الأشكال العربية من الأشكال الإنجليزية بالأداة `tools/figures/translate_figure.py` وخرائط التسميات في `tools/figures/ar/` (ملفّ JSON لكلّ شكل). يُعكس الرسم أفقيًا (`"mirror": true`) حتى تُقرأ التدفّقات من اليمين إلى اليسار، وتُكتب التسميات بخطّ Noto Sans Arabic؛ وتصف محاذاة التسميات (`anchor`) الشكل الأصلي كما في الخرائط الفرنسية، فما كان محاذًى إلى اليسار في الأصل يصبح محاذًى إلى اليمين في الشكل المعكوس على الحافّة نفسها. لتعديل تسمية: عدّل الخريطة ثمّ أعد التوليد:

```bash
python3 tools/figures/translate_figure.py assets/figures/figure-4-1.svg tools/figures/ar/figure-4-1.json assets/figures/ar/figure-4-1.svg
```

يتحقّق سير العمل من أنّ الأشكال العربية المودعة هي بالضبط ما تنتجه الخرائط.

## خطوات ترجمة فصل

1. اختر فصلًا حالته «لم يبدأ» في [`TRANSLATIONS.md`](../TRANSLATIONS.md) وأعلن عنه في issue من نوع «ترجمة فصل» (أو علّق على الـissue القائمة) حتى لا يعمل اثنان على الفصل نفسه.
2. انطلق من الملفّ الإنجليزي المحدَّث (`git log -1 -- chapters/NN-….md`)؛ واذكر في رسالة الـcommit المراجعة الإنجليزية المتَّبعة.
3. انسخ الملفّ الإنجليزي إلى `ar/` بالاسم نفسه، ولفّه بـ`<div dir="rtl">` … `</div>`، ثمّ ترجم فقرة فقرة، من دون دمج الفقرات أو تقسيمها، مع إبقاء كلّ إطار وقائمة وجدول وشكل في موضعه.
4. طبّق المصطلحات والإملاء أعلاه. ضع `<!-- للمراجعة: … -->` حيث تشكّ.
5. نفّذ `python3 tools/check_editions.py ar` (تطابق البنية، الروابط، الترقيم)، وإن كانت الأدوات متاحة لديك `bash tools/pdf/build.sh ar` ثمّ `python3 tools/pdf/verify_pdf.py build/openstack-the-day-after-tomorrow-ar.pdf build/openstack-the-day-after-tomorrow-ar.log`. سير العمل في GitHub ينفّذ الفحوص نفسها على كلّ pull request.
6. أعد قراءة الفصل بالعربية وحدها، من دون الأصل، للتأكّد من سلاسته.
7. أرسل pull request واحدة للفصل، وحدّث سطره في `TRANSLATIONS.md` إلى «في المراجعة». يراجعه قارئ ثانٍ على الأقلّ قبل الدمج (انظر [`CONTRIBUTING.md`](CONTRIBUTING.md)).

</div>
