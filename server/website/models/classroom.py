from . import db

class Classroom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(150), unique=False)
    class_average = db.Column(db.String(3))
    students = db.relationship('Student')

    def  list_students(self):
        if not self.students:
            print("No students found.")
        return "\n".join(str(student) for student in self.students)
    
    def get_class_avg(self):
        if not self.students:
            print("No students found.")
        else:
            total_grade = sum(student.get_grade() for student in self.students)
            avg_grade = total_grade / len(self.students)
            self.class_average = avg_grade
            return round(avg_grade)