from . import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), unique=False)
    grade = db.Column(db.Integer, unique=False)
    classroom_id = db.Column(db.Integer, db.ForeignKey('classroom.id'))

    def get_grade(self):
        return self.grade
    
    def set_grade(self, grade):
        self.grade = grade

    def set_class(self, class_id):
        self.classroom_id = class_id