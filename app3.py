import heapq
from general import Student

class Approach3LazyCache:
    def __init__(self, students):
        self.stud_emails = {s.m_email: s for s in students}
        self.groups = {}
        for s in students:
            if s.m_group in self.groups:
                self.groups[s.m_group][0] += s.m_rating
                self.groups[s.m_group][1] += 1
            else:
                self.groups[s.m_group] = [s.m_rating, 1]
        self.top_cache = []
        self.best_cache = []
        self.top_valid = False
        self.best_valid = False

    def top100(self) -> list[Student]:
        if not self.top_valid:
            self.top_cache = heapq.nlargest(100, self.stud_emails.values(), key=lambda s: s.m_rating)
            self.top_valid = True
        return self.top_cache.copy()

    def change_rate(self, email: str, new_rating: float) -> bool:
        if email not in self.stud_emails:
            return False
        student = self.stud_emails[email]
        old_rating = student.m_rating
        self.groups[student.m_group][0] += (new_rating - old_rating)
        top_min = self.top_cache[-1].m_rating if (self.top_valid and len(self.top_cache) == 100) else 0.0
        student.m_rating = new_rating
        self.best_valid = False
        if not self.top_valid or old_rating >= top_min or new_rating >= top_min:
            self.top_valid = False

        return True

    def best_groups(self) -> list[str]:
        if not self.best_valid:
            averages = {g: stats[0] / stats[1] for g, stats in self.groups.items()}
            max_avg = max(averages.values())
            self.best_cache = sorted([g for g, avg in averages.items() if abs(avg-max_avg)<=1e-9])
            self.best_valid = True
        return self.best_cache.copy()
