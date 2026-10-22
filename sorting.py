import csv

def sort_builtin(students):
    return sorted(students,key=lambda s: s.m_rating)


class BSTNode:
    def __init__(self, student):
        self.key = student.m_rating
        self.students = [student]
        self.left = None
        self.right = None


def sort_custom(students):
    if not students:
        return []

    root = BSTNode(students[0])
    for student in students[1:]:
        key = student.m_rating
        curr = root
        while True:
            if key == curr.key:
                curr.students.append(student)
                break
            elif key < curr.key:
                if curr.left is None:
                    curr.left = BSTNode(student)
                    break
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = BSTNode(student)
                    break
                curr = curr.right
    sorted_students = []
    stack = []
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            sorted_students.extend(curr.students)
            curr = curr.right

    return sorted_students


def save_students_csv(students, path):
    if not students:
        with open(path, mode='w', encoding='utf-8') as f:
            pass
        return
    keys = list(vars(students[0]).keys())
    headers = keys

    with open(path, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for student in students:
            writer.writerow(list(vars(student).values()))
