<div dir="rtl">

# المراجع وقراءات إضافية

الإطار المعروض في هذا الكتاب هو خلاصة المؤلّف لتجربته التشغيلية. وتثبّت المراجع أدناه الملاحظات التقنية في الوثائق الأوّلية؛ فهي تدعم الحقائق التقنية، لا إطار التشغيل نفسه. يتطوّر OpenStack باستمرار، وتتغيّر حالة الإصدارات والوثائق وتفاصيل المشاريع بعد النشر. في قرارات دورة الحياة، ارجع دائمًا إلى وثائق الإصدار والمشروع الحالية بدل عبارة في هذا الكتاب.

## الهندسة المعمارية والخدمات

- وثائق OpenStack، البوّابة المركزية. https://docs.openstack.org/
- Nova، *Nova System Architecture* (المكوّنات ومسؤولياتها؛ الفصل 5). https://docs.openstack.org/nova/latest/user/architecture.html
- Nova، *Cells v2* (قواعد بيانات الخلايا، واكتشاف المضيفين؛ الفصل 5). https://docs.openstack.org/nova/latest/admin/cells.html
- وثائق Nova. https://docs.openstack.org/nova/latest/
- وثائق Neutron، ومنها المادة المرجعية عن الوكلاء وOVN المستخدمة في الفصل 1. https://docs.openstack.org/neutron/latest/
- وثائق Cinder. https://docs.openstack.org/cinder/latest/
- وثائق Glance. https://docs.openstack.org/glance/latest/
- وثائق Keystone. https://docs.openstack.org/keystone/latest/
- وثائق Placement. https://docs.openstack.org/placement/latest/
- مراجع واجهات برمجة تطبيقات OpenStack. https://docs.openstack.org/api-ref/

## العمليات

- Nova، *Configure live migrations* (المتطلّبات المسبقة، والتخزين المشترك، وترحيل الكتل؛ الفصل 20). https://docs.openstack.org/nova/latest/admin/configuring-migrations.html
- Nova، *Live-migrate instances*. https://docs.openstack.org/nova/latest/admin/live-migration-usage.html
- Nova، *Migrate instances* (الترحيل البارد؛ الفصل 20). https://docs.openstack.org/nova/latest/admin/migration.html
- Nova، *Evacuate instances* (الفصلين 10 و20). https://docs.openstack.org/nova/latest/admin/evacuate.html
- Nova، *CPU topologies* (سياسة المعالجات المخصّصة، و`cpu_dedicated_set`، وسياسة خيوط المحاكي؛ الفصل 15). https://docs.openstack.org/nova/latest/admin/cpu-topologies.html
- Nova، *nova-manage* (تدقيق Placement وإصلاحه، وأرشفة الصفوف المحذوفة؛ الفصلين 6 و10). https://docs.openstack.org/nova/latest/cli/nova-manage.html
- oslo.messaging، *RabbitMQ driver* (طوابير النصاب والخيارات ذات الصلة؛ الفصل 10). https://docs.openstack.org/oslo.messaging/latest/admin/rabbit.html
- RabbitMQ، *Quorum Queues* (شرط الأغلبية، وإزالة النسخ الكلاسيكي المُعكوس في 4.0؛ الفصل 10). https://www.rabbitmq.com/docs/quorum-queues
- RabbitMQ، *Clustering and Network Partitions* (معالجة الانقسامات؛ الفصلين 10 و19). https://www.rabbitmq.com/docs/partitions
- RabbitMQ، *Monitoring* (الفصل 8). https://www.rabbitmq.com/docs/monitoring
- وثائق Galera Cluster، *Weighted Quorum* (النصاب والحالة non-Primary؛ الفصل 10). https://galeracluster.com/library/documentation/weighted-quorum.html
- وثائق Galera Cluster، *Crash Recovery* (الـbootstrap من العقدة الأكثر تقدّمًا؛ الفصل 10). https://galeracluster.com/library/documentation/crash-recovery.html
- وثائق Galera Cluster، *Monitoring the Cluster* (الفصل 8). https://galeracluster.com/library/documentation/monitoring-cluster.html
- وثائق Large Scale SIG، ومنها *The Scaling Journey* (الفصل 5). https://docs.openstack.org/large-scale/
- OpenStack Operations Guide. آخر تحديث جوهري له في 2017؛ ذو قيمة تاريخية، ولم يعد محدَّثًا. https://docs.openstack.org/operations-guide/

## الترقيات ودورة الحياة

- OpenStack Releases: حالة السلاسل، وتسمية SLURP، والتواريخ (الفصل 14). https://releases.openstack.org/
- OpenStack Project Team Guide، *Stable Branches* (معايير النقل الخلفي (backport)، وحالات Maintained / Unmaintained / End of Life؛ الفصل 14). https://docs.openstack.org/project-team-guide/stable-branches.html
- Nova، *Upgrades* (تسلسل الترقية المتدرّجة دون انقطاع، وتوافق إصدارات الخدمات، وترحيلات البيانات أثناء التشغيل؛ الفصل 14). https://docs.openstack.org/nova/latest/admin/upgrades.html
- Neutron، *Upgrade strategy* (مرحلتا التوسيع والتقليص؛ الفصل 14). https://docs.openstack.org/neutron/latest/contributor/internals/upgrade.html
- `nova-status upgrade check`. https://docs.openstack.org/nova/latest/cli/nova-status.html
- `neutron-status upgrade check`. https://docs.openstack.org/neutron/latest/cli/neutron-status.html
- `cinder-status upgrade check`. https://docs.openstack.org/cinder/latest/cli/cinder-status.html
- `placement-status upgrade check`. https://docs.openstack.org/placement/latest/cli/placement-status.html
- ملاحظات إصدار Nova، Train (20.0.0): الترحيل الحيّ الواعي بـNUMA (الفصل 15). https://docs.openstack.org/releasenotes/nova/train.html
- فهرس ملاحظات إصدار المشاريع. https://docs.openstack.org/releasenotes/
- تحليلات OpenStack User Survey، لتوزّع الإصدارات الموجودة فعلًا في الإنتاج (الفصل 14). https://www.openstack.org/analytics

## الأمن

- التنبيهات الأمنية لـOpenStack (OSSA)، التي يصدرها فريق إدارة الثغرات (الفصل 17). https://security.openstack.org/ossalist.html
- OpenStack Technical Committee، *Consistent and Secure Default RBAC* (الشخصيات، و`enforce_new_defaults`، و`enforce_scope`، والمراحل؛ الفصل 17). https://governance.openstack.org/tc/goals/selected/consistent-and-secure-rbac.html
- Keystone، *Fernet — Frequently Asked Questions* (تدوير المفاتيح؛ الفصل 17). https://docs.openstack.org/keystone/latest/admin/fernet-token-faq.html
- OpenStack Security Guide. لم يُحدَّث الدليل تحديثًا جوهريًا منذ عدّة إصدارات؛ استخدمه للمفاهيم، لا للإعداد الخاصّ بإصدار بعينه. https://docs.openstack.org/security-guide/

## الأصول

- Google، *Site Reliability Engineering* (2016) و*The Site Reliability Workbook* (2018)، في اختبار التعافي من الكوارث، وثقافة تحليل ما بعد الحادث، ومعاملة العمل التشغيلي بوصفه عملًا هندسيًا. https://sre.google/books/
- دورة «خطّط – نفّذ – تحقّق – صحّح» (Deming) وحلقة «راقب – توجّه – قرّر – نفّذ» (Boyd) بوصفهما سلفَي حلقة التحكّم في الفصل 4.

## العلامات التجارية

- معلومات العلامة والعلامة التجارية لـOpenStack. https://www.openstack.org/brand/

---

[الملحق و — المسرد →](appendix-f-glossary.md) · [المحتويات](../README.md)

</div>
