import time
import random
import json

class GrandchildCell:
    def __init__(self, parent_id):
        # تعريف الخلية مع معرف فريد، الوالد، والخصائص الأساسية
        self.id = f"GRANDCHILD_{random.randint(1000, 9999)}"
        self.parent_id = parent_id
        self.status = "active"
        self.tasks = []
        self.creation_time = time.time()
        self.energy_level = 1.0  # يبدأ بطاقة كاملة
        self.completed_tasks = 0
        self.chromosomes = self.initialize_chromosomes()
        self.layers = self.initialize_layers()

    def initialize_chromosomes(self):
        """تهيئة الجينات الخاصة بالأداء، التطور، والتعلم."""
        return {
            "performance_genes": random.uniform(0.5, 1.0),
            "evolution_genes": random.uniform(0.5, 1.0),
            "learning_genes": random.uniform(0.5, 1.0)
        }

    def initialize_layers(self):
        """تهيئة الطبقات التي تتحكم في تصرفات الخلية."""
        return {
            "genetic_layer": self.chromosomes,
            "behavioral_layer": {"task_priority": 1, "task_behavior": "default"},
            "energy_layer": {"current_energy": self.energy_level, "energy_threshold": 0.3}
        }

    def assign_task(self, task):
        """إسناد مهمة إلى الخلية."""
        self.tasks.append(task)
        print(f"✅ المهمة '{task}' تم إسنادها إلى الخلية {self.id}.")

    def perform_task(self):
        """تنفيذ مهمة بناءً على مستوى الطاقة والجينات."""
        if self.energy_level <= 0:
            print(f"⚠️ الخلية {self.id} لا تمتلك طاقة كافية لتنفيذ المهام!")
            self.status = "resting"
            return
        
        if self.tasks:
            task = self.tasks.pop(0)
            performance_factor = self.chromosomes["performance_genes"]
            print(f"🚀 الخلية {self.id} تقوم بتنفيذ المهمة: {task}.")
            self.energy_level -= 0.1 * performance_factor
            self.completed_tasks += 1

            if self.energy_level <= self.layers["energy_layer"]["energy_threshold"]:
                self.status = "resting"
                print(f"😴 الخلية {self.id} دخلت في وضع الراحة بسبب انخفاض الطاقة.")

            self.log_performance(task, "completed")
        else:
            print(f"⏳ لا توجد مهام حالياً للخلية {self.id}.")

    def self_evolve(self):
        """محاكاة تطور الخلية بناءً على الجينات ومستوى الطاقة."""
        if self.energy_level >= 0.8 and self.chromosomes["evolution_genes"] > 0.7:
            print(f"🔬 الخلية {self.id} تتطور!")
            self.energy_level *= 0.9  # خفض الطاقة بعد التطور
            self.chromosomes["performance_genes"] += 0.05  # تعزيز أداء الخلية بعد التطور
        else:
            print(f"❌ الخلية {self.id} لا تستطيع التطور حالياً.")

    def receive_energy(self, energy_amount):
        """استقبال الطاقة لتشغيل المهام أو التطور."""
        self.energy_level += energy_amount
        self.energy_level = min(self.energy_level, 1.0)  # لا يمكن تجاوز 100%
        print(f"⚡ الخلية {self.id} استلمت طاقة. المستوى الحالي: {self.energy_level}")

    def collaborate_with(self, other_cell):
        """التعاون مع خلية أخرى لتبادل الطاقة."""
        if self.energy_level > 0.3 and other_cell.energy_level < 0.5:
            transfer_energy = min(self.energy_level * 0.2, 0.2)
            self.energy_level -= transfer_energy
            other_cell.energy_level += transfer_energy
            print(f"🤝 الخلية {self.id} شاركت الطاقة مع {other_cell.id}.")
        else:
            print(f"⚠️ لا يمكن التعاون بين {self.id} و {other_cell.id} الآن.")

    def monitor_performance(self):
        """مراقبة أداء الخلية وعرض الإحصائيات."""
        print(f"📊 تقرير الخلية {self.id}:")
        print(f"  🔹 المهام المكتملة: {self.completed_tasks}")
        print(f"  🔹 مستوى الطاقة: {self.energy_level}")
        print(f"  🔹 جين الأداء: {self.chromosomes['performance_genes']}")
        print(f"  🔹 جين التطور: {self.chromosomes['evolution_genes']}")

    def check_status(self):
        """التحقق من الحالة الحالية للخلية."""
        print(f"ℹ️ حالة الخلية {self.id}: {self.status}. الطاقة: {self.energy_level}")

    def log_performance(self, task, status):
        """حفظ سجل أداء الخلية في ملف JSON."""
        log_entry = {
            "cell_id": self.id,
            "task": task,
            "status": status,
            "energy_level": self.energy_level,
            "timestamp": time.time()
        }
        try:
            with open("cell_performance.json", "a") as file:
                json.dump(log_entry, file)
                file.write("\n")
        except Exception as e:
            print(f"⚠️ خطأ في حفظ السجل: {e}")

# 🔥 **تجربة النظام المحسن**
if __name__ == "__main__":
    # إنشاء خليتين
    grandchild1 = GrandchildCell(parent_id="CHILD_1001")
    grandchild2 = GrandchildCell(parent_id="CHILD_1002")

    # إسناد المهام وتنفيذها
    grandchild1.assign_task("تحليل البيئة")
    grandchild1.perform_task()

    grandchild2.assign_task("تنفيذ بروتوكول التكيف")
    grandchild2.perform_task()

    # محاكاة استقبال الطاقة
    grandchild1.receive_energy(0.4)
    grandchild2.receive_energy(0.2)

    # تطور ذاتي
    grandchild1.self_evolve()

    # التعاون بين الخلايا
    grandchild1.collaborate_with(grandchild2)

    # فحص الحالة ومراقبة الأداء
    grandchild1.check_status()
    grandchild2.monitor_performance()
