import pandas as pd
import matplotlib.pyplot as plt
class Student:
    def __init__(self, name, department):
        self.name = name
        self.department = department
class TimeTableGenerator:
    def __init__(self):
        self.subjects = {}
    def add_subject(self, subject, priority):
        if priority.lower() == "high":
            weight = 3
        elif priority.lower() == "medium":
            weight = 2
        else:
            weight = 1
        self.subjects[subject] = weight
    def generate_timetable(self):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        weighted_subjects = []
        for subject, weight in self.subjects.items():
            for i in range(weight):
                weighted_subjects.append(subject)
        while len(weighted_subjects) < 25:
            weighted_subjects.extend(weighted_subjects)
        weighted_subjects = weighted_subjects[:25]
        timetable = {}
        index = 0
        for day in days:
            periods = []
            for p in range(5):
                periods.append(weighted_subjects[index])
                index += 1
            timetable[day] = periods
        df = pd.DataFrame(timetable)
        df.index = ["Period 1", "Period 2", "Period 3", "Period 4", "Period 5"]
        return df
class AIReport:
    def generate_report(self, student, subjects):
        print("\n" + "=" * 50)
        print("AI STUDY REPORT")
        print("=" * 50)
        high_subjects = []
        for subject, weight in subjects.items():
            if weight == 3:
                high_subjects.append(subject)
        print(f"Student Name : {student.name}")
        print(f"Department   : {student.department}")
        print("\nFocus More On:")
        for subject in high_subjects:
            print("✓", subject)
        print("\nSuggestion:")
        print(f"\nHello {student.name}, " f"focus more on {', '.join(high_subjects)} " f"because they are marked as High Priority.")
class Visualizer:
    def pie_chart(self, subjects):
        plt.figure(figsize=(7,7))
        plt.pie(subjects.values(), labels=subjects.keys(), autopct="%1.1f%%")
        plt.title("Subject Priority Distribution")
        plt.show()
print("=" * 55)
print("INTELLIGENT TIMETABLE GENERATOR")
print("=" * 55)
name = input("Enter Name : ")
department = input("Enter Department : ")
student = Student(name, department)
generator = TimeTableGenerator()
n = int(input("\nHow Many Subjects? : "))
for i in range(n):
    print(f"\nSubject {i+1}")
    subject = input("Enter Subject Name : ")
    priority = input("Priority (High/Medium/Low) : ")
    generator.add_subject(subject, priority)
df = generator.generate_timetable()
print("\n===== INTELLIGENT TIMETABLE =====\n")
print(df)
report = AIReport()
report.generate_report(student, generator.subjects)
visual = Visualizer()
visual.pie_chart(generator.subjects)