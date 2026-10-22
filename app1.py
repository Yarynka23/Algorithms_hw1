from general import Student

class Approach1Naive:
    def __init__(self, students):
        self.students=students
    def top100(self) -> list[Student]:
        new=sorted(self.students, key=lambda student: student.m_rating, reverse=True)
        return new[:100].copy()

    def change_rate(self, email: str, new_rating: float) -> bool:
        for s in self.students:
            if s.m_email==email:
                s.m_rating=new_rating
                return True
                break
        else:
            return False

    def best_groups(self) -> list[str]:
        groups={}
        for s in self.students:
            if s.m_group in groups:
                groups[s.m_group][0]+=s.m_rating
                groups[s.m_group][1]+=1
            else:
                groups[s.m_group]=[s.m_rating,1]
        averages = {group: a[0]/a[1] for group, a in groups.items()}
        max_avg = max(averages.values())
        return sorted([group for group, avg in averages.items() if abs(avg-max_avg)<=1e-9]).copy()
