#task 3

class Student:
    def __init__(self, name, num_courses, scores):
        self.name = name
        self.num_courses = num_courses
        self.scores = scores
        self.gpa = None
        self.status = None

    def calculateGPA(self):
        total_credits = 0
        weighted_score = 0

        for course, info in self.scores.items():
            score = info['score']
            credits = info['credits']
            total_credits += credits
            weighted_score += score * credits

        if total_credits > 0:
            self.gpa = weighted_score / total_credits
        else:
            self.gpa = 0

    def setStatus(self):
        if self.gpa is not None:
            self.status = 'Passed' if self.gpa >= 1.0 else 'Not Passed'
        else:
            self.status = 'Not Set'

    def showGPA(self):
        if self.gpa is not None:
            print(f'{self.name}\'s GPA: {self.gpa:.2f}')
        else:
            print('GPA not calculated. Call calculateGPA() first.')

    def showStatus(self):
        if self.status is not None:
            print(f'{self.name}\'s Status: {self.status}')
        else:
            print('Status not set. Call setStatus() first.')

# Example Usage:
student_scores = {
    'math': {'score': 4.3, 'credits': 4},
    'chemistry': {'score': 3.3, 'credits': 3},
    'english': {'score': 4.0, 'credits': 4}
}

student = Student(name='John Doe', num_courses=3, scores=student_scores)

# Calculate GPA and set status
student.calculateGPA()
student.setStatus()

# Display GPA and status
student.showGPA()
student.showStatus()
