<div dir="rtl">

# OpenStack، بعد غد

### تشغيل منصّات OpenStack الحرجة

**المؤلّف: سفيان زعوام**

[![تنزيل PDF](https://img.shields.io/badge/%D8%AA%D9%86%D8%B2%D9%8A%D9%84-PDF%20(%D8%A2%D8%AE%D8%B1%20%D8%A5%D8%B5%D8%AF%D8%A7%D8%B1)-2ea44f?style=for-the-badge)](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/releases/latest)
[![الإصدار](https://img.shields.io/github/v/release/soufian-zaouam/openstack-the-day-after-tomorrow?label=version&style=for-the-badge)](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/releases)
[![الرخصة: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey?style=for-the-badge)](../LICENSE)

هذه هي الطبعة العربية من كتاب *OpenStack, the Day After Tomorrow*، وتُحفظ في المستودع نفسه الذي يضمّ الطبعة الإنجليزية الأصلية ([README بالإنجليزية](../README.md)) والطبعة الفرنسية ([README بالفرنسية](../fr/README.md)). تتبع النصّ الإنجليزي فصلًا فصلًا؛ وتحمل الطبعات كلّها رقم الإصدار نفسه وتُنشر معًا.

**الطبعة العربية مشروع مجتمعي قيد الإنجاز.** يترجمها ويراجعها متطوّعون من مجتمع OpenStack بإشراف المؤلّف، فصلًا فصلًا. الفصول المترجمة تُقرأ هنا مباشرة؛ وحالة كلّ فصل (لم يبدأ، في المراجعة، مُترجم، مسودّة) في [TRANSLATIONS.md](../TRANSLATIONS.md)؛ وطريقة المشاركة في الترجمة أو المراجعة أو التصحيح — مع Git أو من دونه — في [CONTRIBUTING.md](CONTRIBUTING.md). المنهج والمصطلحات في [STYLE.md](STYLE.md). المساهمون في [CONTRIBUTORS.md](../CONTRIBUTORS.md).

يُنشر الكتاب بحرّية، بصيغة **PDF** (انظر [التنزيل](#التنزيل)) وبصيغة **Markdown، ملفّ لكلّ فصل، يُقرأ مباشرة على GitHub** (انظر [قراءة الكتاب على GitHub](#قراءة-الكتاب-على-github)). وهو **مساهمة مستقلّة وشخصية في مجتمع OpenStack**. ليس منشورًا لمؤسّسة OpenStack Foundation (OpenInfra Foundation)، ولا لناشر أو ربّ عمل أو عميل، ولا يصف منصّة أيّ مؤسّسة بعينها.

---

## عن الكتاب

تتوقّف معظم المواد عن OpenStack حيث يبدأ العمل الحقيقي: المنصّة منشورة، والخدمات تستجيب، والمستأجرون الأوائل على متنها. هذا الكتاب عمّا يأتي بعد ذلك: السنوات التي يجب أن تبقى فيها المنصّة مستقرّة، وقابلة للملاحظة، وقابلة للترقية، وآمنة، وقبل كلّ شيء مفهومة لدى من يشغّلونها.

أطروحته المركزية أنّ تشغيل OpenStack في الإنتاج ليس مشكلة تقنية فحسب. إنّه أيضًا مشكلة رؤية واستقرار وتنظيم وحوكمة وإدارة مخاطر. يمكن لمنصّة أن تعمل بكامل وظائفها وتبقى مع ذلك صعبة التشغيل، وصعبة التطوير، وصعبة التأمين، وصعبة التسليم.

إنّه تجربة مشغّل واحد ووجهة نظره، لا معيار ولا مرجع. وحيث يعتمد الجواب الصحيح على طريقة النشر أو على الواجهة الخلفية، يقول النصّ ذلك.

يستند الكتاب إلى أكثر من خمس سنوات من تشغيل منصّات OpenStack في الإنتاج (عمليات اليوم الثاني، الموثوقية، الترقيات، معالجة الحوادث، بناء الفرق). عُمِّمت التجربة الحقيقية في أنماط ومبادئ؛ ولا يوصف أيّ عميل أو ربّ عمل أو مشروع أو بيئة، ولا يمكن تمييز أيّ منها.

**ما ستجده في الداخل** (20 فصلًا في ستّة أجزاء، مع ملاحق)

- *فهم المشكلة* — لماذا لا ينتهي OpenStack عند النشر، ولماذا العدوّ الحقيقي هو فقدان التحكّم، وحلقة التحكّم التي تخترق الكتاب كلّه
- *تقييم التحكّم* — كيف نقيّم ونقيس مقدار التحكّم الذي تملكه المؤسّسة فعلًا في منصّتها، وماذا نفعل حين يكون مفقودًا بالفعل
- *التشغيل بتحكّم* — الرؤية قبل الفعل، والاستقرار والتغيير، والاستعادة بوصفها ميزة لا فكرة لاحقة
- *التنظيم خلف المنصّة* — التوثيق بوصفه ذاكرة تشغيلية، وبناء الفريق، وحقوق القرار
- *التطوّر دون فقدان التحكّم* — الترقيات والنقل الخلفي والمواءمة مع المنبع؛ التعقيد والدين التقني والتبسيط؛ الأتمتة؛ الأمن بوصفه عملًا من أعمال المنصّة
- *قرارات من الميدان* — قراران مفصّلان تصادمت فيهما الأدلّة التقنية والأثر على الأعمال والقيود التشغيلية
- الملاحق: إطار قرار التحكّم، وورقة عمل تقييم التحكّم، وسجلّ قرار تغيير بالحدّ الأدنى، وأسئلة مراجعة التحكّم، ومبادئ التشغيل في لمحة، ومسرد

على امتداد النصّ، تفصل أُطر *ملاحظة تقنية* و*مبدأ* و*من الميدان* بين سلوك OpenStack الموثَّق، ومبادئ التشغيل التي يراها المؤلّف، والمواقف المستمدّة من عمليات حقيقية.

## قراءة الكتاب على GitHub

يُنشر النصّ الكامل للكتاب في هذا المستودع بصيغة Markdown، **ملفّ لكلّ فصل**، ليُقرأ مباشرة على GitHub، ويُبحث فيه، ويُربط به، ويُقتبس منه بالقسم. النصّ هو نصّ PDF الذي يُولَّد من هذه الملفّات نفسها؛ والأشكال الخمسة متاحة بصيغة SVG في [`assets/figures/ar/`](../assets/figures/ar/).

ابدأ بـ[كيف تقرأ هذا الكتاب](chapters/00-how-to-read-this-book.md)، ثمّ اتبع روابط *السابق / المحتويات / التالي* في أسفل كلّ فصل. يبقى PDF متاحًا للقراءة دون اتّصال (انظر [التنزيل](#التنزيل)). الفصول التي لم تُترجم بعد مذكورة بلا رابط؛ يمكنك قراءتها [بالإنجليزية](../README.md#read-the-book-on-github) أو [بالفرنسية](../fr/README.md)، أو [المساعدة في ترجمتها](CONTRIBUTING.md).

| | الفصل |
| --- | --- |
| | [الصفحات التمهيدية](chapters/00-front-matter.md) |
| | [كيف تقرأ هذا الكتاب](chapters/00-how-to-read-this-book.md) |
| | [المقدّمة](chapters/00-introduction.md) |
| **الجزء الأول — فهم المشكلة** | |
| 1 | [OpenStack لا ينتهي عند النشر](chapters/01-openstack-doesnt-end-at-deployment.md) |
| 2 | [العدوّ هو فقدان التحكّم](chapters/02-the-enemy-is-loss-of-control.md) |
| 3 | [لماذا تصبح المنصّات الجيّدة صعبة التشغيل](chapters/03-why-good-platforms-become-difficult-to-operate.md) |
| 4 | [حلقة التحكّم](chapters/04-the-control-loop.md) |
| **الجزء الثاني — تقييم التحكّم** | |
| 5 | [تقييم التحكّم في المنصّة](chapters/05-assessing-platform-control.md) |
| 6 | [قياس التحكّم](chapters/06-measuring-control.md) |
| 7 | [عندما يكون التحكّم مفقودًا بالفعل](chapters/07-when-control-is-already-lost.md) |
| **الجزء الثالث — التشغيل بتحكّم** | |
| 8 | [الرؤية قبل الفعل](chapters/08-visibility-before-action.md) |
| 9 | [الاستقرار والتغيير](chapters/09-stability-and-change.md) |
| 10 | [الاستعادة ميزة](chapters/10-recovery-is-a-feature.md) |
| **الجزء الرابع — التنظيم خلف المنصّة** | |
| 11 | [التوثيق هو الذاكرة التشغيلية](chapters/11-documentation-is-operational-memory.md) |
| 12 | [بناء الفريق خلف المنصّة](chapters/12-building-the-team-behind-the-platform.md) |
| 13 | [حقوق القرار](chapters/13-decision-rights.md) |
| **الجزء الخامس — التطوّر دون فقدان التحكّم** | |
| 14 | [الترقيات والنقل الخلفي والمواءمة مع المنبع](chapters/14-upgrades-backports-and-upstream-alignment.md) |
| 15 | [التعقيد والدين التقني والتبسيط](chapters/15-complexity-technical-debt-and-simplification.md) |
| 16 | [الأتمتة والتعقيد التشغيلي](chapters/16-automation-and-operational-complexity.md) |
| 17 | [الأمن عمل من أعمال المنصّة](chapters/17-security-is-platform-work.md) |
| 18 | [تطوير منصّة حرجة](chapters/18-evolving-a-mission-critical-platform.md) |
| **الجزء السادس — قرارات من الميدان** | |
| 19 | [عندما يكون القرار الآمن هو التوقّف](chapters/19-when-the-safe-decision-is-to-stop.md) |
| 20 | [الأمن والسعة والأهمية الحرجة للأعمال](chapters/20-security-capacity-and-business-criticality.md) |
| | [الخاتمة: إبقاء OpenStack تحت التحكّم](chapters/21-conclusion-keeping-openstack-under-control.md) |
| **الملاحق** | |
| أ | [إطار قرار التحكّم](appendices/appendix-a-the-control-decision-framework.md) |
| ب | [ورقة عمل تقييم التحكّم](appendices/appendix-b-the-control-assessment-worksheet.md) |
| ج | [سجلّ قرار تغيير بالحدّ الأدنى](appendices/appendix-c-a-minimum-change-decision-record.md) |
| د | [أسئلة مراجعة التحكّم](appendices/appendix-d-control-review-questions.md) |
| هـ | [مبادئ التشغيل في لمحة](appendices/appendix-e-operating-principles-at-a-glance.md) |
| و | [المسرد](appendices/appendix-f-glossary.md) |
| | [المراجع وقراءات إضافية](appendices/references-and-further-reading.md) |

**مسار قصير للمديرين والرعاة** (كما يقترحه *كيف تقرأ هذا الكتاب*): [المقدّمة](chapters/00-introduction.md)، والفصول من [1](chapters/01-openstack-doesnt-end-at-deployment.md) إلى [3](chapters/03-why-good-platforms-become-difficult-to-operate.md)، والفصل [7](chapters/07-when-control-is-already-lost.md)، والقسم الأخير من الفصل [12](chapters/12-building-the-team-behind-the-platform.md)، والفصلان [13](chapters/13-decision-rights.md) و[14](chapters/14-upgrades-backports-and-upstream-alignment.md) حتى أوّل ملاحظة تقنية، والفصلان [19](chapters/19-when-the-safe-decision-is-to-stop.md) و[20](chapters/20-security-capacity-and-business-criticality.md)، و[الخاتمة](chapters/21-conclusion-keeping-openstack-under-control.md)، والملحقان [د](appendices/appendix-d-control-review-questions.md) و[هـ](appendices/appendix-e-operating-principles-at-a-glance.md).

### تنظيم الطبعة العربية في المستودع

```text
openstack-the-day-after-tomorrow/
├── README.md              تقديم الطبعة الإنجليزية وفهرسها
├── chapters/, appendices/ النصّ الإنجليزي، ملفّ Markdown لكلّ فصل
├── fr/                    الطبعة الفرنسية
├── assets/figures/        أشكال الطبعة الإنجليزية (SVG)
│   └── ar/                الأشكال نفسها بتسميات عربية، معكوسة لتُقرأ من اليمين إلى اليسار
├── ar/
│   ├── README.md          هذه الصفحة: التقديم والفهرس بالعربية
│   ├── STYLE.md           منهج الطبعة العربية وقواعدها ومسرد مصطلحاتها
│   ├── CONTRIBUTING.md    كيف تشارك في الترجمة والمراجعة والتصحيح
│   ├── chapters/          الصفحات التمهيدية والمقدّمة والفصول 1–20 والخاتمة (الأسماء الإنجليزية نفسها)
│   └── appendices/        الملاحق أ–و والمراجع
├── TRANSLATIONS.md        حالة كلّ فصل في كلّ لغة
├── CONTRIBUTORS.md        المترجمون والمراجعون
├── tools/pdf/             توليد ملفّات PDF (pandoc + XeLaTeX / LuaLaTeX)، كلّ الطبعات
├── tools/figures/         ترجمة الأشكال (خرائط التسميات في tools/figures/ar/)
└── tools/check_editions.py  التحقّق من تطابق الطبعات المترجمة مع الأصل
```

يحمل كلّ ملفّ عربي اسم الملفّ الإنجليزي المقابل نفسه (الجدول الكامل في [`STYLE.md`](STYLE.md)). وعلى امتداد النصّ، تُعرض ثلاثة أنواع من الأُطر الموجودة في PDF على شكل اقتباسات: **ملاحظة تقنية** (حقائق قابلة للتحقّق عن OpenStack، مع مرجع)، و**مبدأ** (قاعدة تشغيل يوصي بها الكتاب)، و**من الميدان** (موقف تشغيلي والقرار الذي اقتضاه).

## موارد مرافقة

- **[الدليل الموجز (Short Guide)](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow-guide)** — أفكار الكتاب في 18 صفحة مصوّرة، فكرة وشكل في كلّ صفحة (بالإنجليزية). أسرع مدخل، ومرجع مشترك للفرق والرعاة.
- **[OpenStack Production Guide](https://github.com/soufian-zaouam/openstack-production-guide)** — الرفيق العملي (بالإنجليزية): استكشاف الأخطاء بحسب العرَض والأمر ورسالة الخطأ، وسلسلة *One Command, One Investigation* (20 حلقة)، وستّ حالات حوادث مجهّلة بصيغة تحليل السبب الجذري. عدّة فقرات *من الميدان* في الكتاب مفصّلة هناك مع ملفّها التقني.

## لمن هذا الكتاب

- للمهندسين وفرق المنصّات الذين يشغّلون منصّة OpenStack أو على وشك أن يرثوها
- للمعماريين وقادة المنصّات المسؤولين عن موثوقية سحابة خاصّة وتطويرها
- للمديرين التقنيين ومديري نظم المعلومات وقادة البرامج الذين يحتاجون إلى فهم ما يعنيه «تشغيل OpenStack» فعلًا من التزامات

يفترض الكتاب معرفة عملية بـOpenStack. ليس دليل تثبيت ولا يحلّ محلّ الوثائق الرسمية.

## لماذا يوجد هذا الكتاب

النشر بداية الرحلة التشغيلية لا نهايتها. دروس عمليات اليوم الثاني المكتسبة بشقّ الأنفس نادرًا ما تُكتب، وحين تُكتب تتناثر بين تقارير الحوادث والمعرفة القَبَلية ومحاضرات المؤتمرات. هذا الكتاب محاولة لتجميعها في نصّ متماسك وصريح وعملي، وردّها إلى المجتمع الذي جعل المنصّة ممكنة.

**لماذا يُنشر بحرّية.** OpenStack مفتوح المصدر، ومعظم ما أعرفه عن تشغيله تعلّمته من وثائق وشفرة ونقاشات اختار آخرون مشاركتها. نشر هذا الكتاب بحرّية هو أقصر طريق أملكه لردّ شيء ممّا أخذت، ولأن يُناقَش محتواه ويُصحَّح ويُحسَّن على أيدي من يشغّلون هذه المنصّات كلّ يوم.

**لماذا طبعة عربية.** تُشغَّل منصّات OpenStack في كثير من البلدان العربية، وفي الإدارات والجامعات والمشغّلين، وقليل من أدبيات تشغيلها متاح بالعربية. الطبعة العربية طبعة كاملة، يترجمها مجتمع القرّاء والمشغّلين بإشراف المؤلّف، تتبع الطبعة الإنجليزية فصلًا فصلًا وتتطوّر معها. وهي مفتوحة لمن يريد أن يترجم فصلًا أو يراجعه أو يحسّن مصطلحًا.

## التنزيل

| | |
|---|---|
| **الإصدار** | الإصدار نفسه الذي تحمله الطبعة الإنجليزية (انظر [CHANGELOG.md](../CHANGELOG.md)) |
| **الصيغة** | PDF (عربي) حين تكتمل الترجمة · Markdown (هذا المستودع) |
| **التنزيل** | **[آخر إصدار ←](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/releases/latest)** |

تُوزَّع ملفّات PDF حصريًا عبر صفحة [Releases](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/releases) في هذا المستودع؛ وكلّ إصدار موسوم ومؤرَّخ ومصحوب بملاحظات إصدار. **ملفّ PDF العربي يُنشر مع الإصدارات ما إن تكتمل ترجمة الفصول كلّها**؛ وإلى ذلك الحين، يبني سير العمل في GitHub معاينة من الفصول المترجمة عند كلّ تغيير ويحتفظ بها كأرشيف (artifact) لسير العمل، يمكن للمراجعين تنزيلها من صفحة *Actions*.

يُولَّد ملفّ PDF **تلقائيًا من مصادر Markdown** في هذا المستودع ([`ar/chapters/`](chapters/)، [`ar/appendices/`](appendices/)، [`assets/figures/ar/`](../assets/figures/ar/)) بالمحرّك LuaLaTeX، الذي يتولّى الكتابة من اليمين إلى اليسار والنصّ المختلط عربيًا ولاتينيًا؛ انظر [`tools/pdf/README.md`](../tools/pdf/README.md) لسلسلة التوليد ولبنائه محلّيًا (`bash tools/pdf/build.sh ar`).

## الإبلاغ عن الأخطاء والمشاركة

التصويبات والاعتراضات التقنية والاقتراحات مرحّب بها، وكذلك المشاركة في الترجمة والمراجعة.

- **خطأ؟** (خطأ تقني، خطأ مطبعي، فقرة غامضة، مرجع مكسور، ترجمة غير دقيقة) ← [افتح issue من نوع *Errata*](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/issues/new?template=errata.yml) أو [*Translation feedback*](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/issues/new?template=translation-feedback.yml)
- **اقتراح أو سؤال عن المحتوى؟** ← [افتح issue من نوع *Suggestion*](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/issues/new?template=suggestion.yml)
- **تريد ترجمة فصل أو مراجعته؟** ← اختر فصلًا حرًّا في [TRANSLATIONS.md](../TRANSLATIONS.md)، و[احجزه](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/issues/new?template=translate-chapter.yml)، واتبع [STYLE.md](STYLE.md)؛ الخطوات كاملة في [CONTRIBUTING.md](CONTRIBUTING.md)
- **مصطلح يبدو لك خاطئًا؟** ← [افتح issue من نوع *Terminology*](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/issues/new?template=terminology.yml)

اذكر إصدار الكتاب والطبعة (العربية) والصفحة (PDF) أو ملفّ الفصل والقسم (Markdown). التصويبات المؤكَّدة تُدرج في [سجلّ التغييرات](../CHANGELOG.md) وتُدمج في الإصدار التالي. التصويب الجوهري يُجرى أوّلًا في الطبعة الإنجليزية ثمّ يُنقل إلى هنا.

## الرخصة

حقوق النشر © 2026 سفيان زعوام.

يُنشر الكتاب برخصة [المشاع الإبداعي نَسب المُصنَّف – غير تجاري – منع الاشتقاق 4.0 دولي](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.ar) (CC BY-NC-ND 4.0). لك أن تقرأه وتنزّله وتشاركه وتعيد توزيعه، على أيّ وسيط، شريطة نسبته إلى مؤلّفه، وعدم استخدامه تجاريًا، وعدم توزيع نسخة معدَّلة منه. انظر [LICENSE](../LICENSE).

الترجمة نسخة معدَّلة بتعبير الرخصة، ولذلك لا توجد ترجمات الكتاب إلّا في هذا المستودع: الطبعة العربية يترجمها مساهمون يدمج المؤلّف عملهم وينشره بالرخصة نفسها، مع ذكر أسمائهم في [CONTRIBUTORS.md](../CONTRIBUTORS.md). شروط قبول المساهمات في [CONTRIBUTING.md](CONTRIBUTING.md). وللاستخدامات التي لا تغطّيها الرخصة — طبعة منفصلة، مقتطفات لموادّ تدريبية، إدراج في عرض تجاري — افتح issue أو تواصل مع المؤلّف.

## الاستشهاد بالكتاب

> Zaouam, S. (2026). *OpenStack، بعد غد: تشغيل منصّات OpenStack الحرجة* (الطبعة العربية من *OpenStack, the Day After Tomorrow*، ترجمة مجتمعية). https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow

استشهاد قابل للقراءة آليًا في [CITATION.cff](../CITATION.cff).

## عن المؤلّف

سفيان زعوام مهندس منصّات متخصّص في عمليات اليوم الثاني وموثوقية منصّات OpenStack الحرجة وحوكمتها. هذا الكتاب أوّل سلسلة مخطّطة من الأعمال عن تشغيل OpenStack في الإنتاج.

[LinkedIn](https://www.linkedin.com/in/soufian-zaouam) · [GitHub](https://github.com/soufian-zaouam)

---

*OpenStack علامة تجارية مسجّلة لمؤسّسة OpenInfra Foundation. هذا الكتاب وهذا المستودع مستقلّان عن مؤسّسة OpenInfra Foundation ولا تقرّهما.*

</div>
