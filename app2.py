import bisect
from general import Student
class Approach2bisect:
    def __init__(self, students):
        self.students=sorted(students, key=lambda student: student.m_rating, reverse=True)
        self.stud_emails = {s.m_email: s for s in students}
        groups = {}
        for s in students:
            if s.m_group in groups:
                groups[s.m_group][0] += s.m_rating
                groups[s.m_group][1] += 1
            else:
                groups[s.m_group] = [s.m_rating, 1]
        self.groups = groups
    def top100(self) -> list[Student]:
        return self.students[:100].copy()

    def change_rate(self, email: str, new_rating: float) -> bool:
        if email not in self.stud_emails:
            return False
        student = self.stud_emails[email]
        old_rating = student.m_rating
        if old_rating == new_rating:
            return True
        self.groups[student.m_group][0] += (new_rating - old_rating)

        self.students.remove(student)
        student.m_rating = new_rating
        idx = bisect.bisect_left(self.students, -new_rating, key=lambda s: -s.m_rating)
        self.students.insert(idx, student)

        return True

    def best_groups(self) -> list[str]:
        averages = {g: stats[0] / stats[1] for g, stats in self.groups.items()}
        max_avg = max(averages.values())
        return sorted([g for g, avg in averages.items() if abs(avg-max_avg)<=1e-9]).copy()
