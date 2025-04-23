from flask import Blueprint, jsonify, request
from website.models import *
from .. import db

student_bp = Blueprint('student_bp', __name__)

@student_bp.route('/students', methods=["GET"])
def get_students():
    # Grabs all students from the database
    students = Student.query.all()
    # Jsonify the students
    return jsonify([
        {
            'id': student.id,
            'name': student.name,
            'grade': student.grade,
            'classroom_id': student.classroom_id
        } for student in students
    ]), 200

@student_bp.route('/students', methods=["POST"])
def add_student():
    # Request Variable
    data = request.get_json()

    #Grabs data
    name = data.get('name')
    grade = data.get('grade')
    classroom_id = data.get('classroom_id')

    if not name or grade is None:
        return jsonify({'error': 'Name and grade are required.'}), 400
    
    student = Student(name=name, grade=grade, classroom_id=classroom_id)
    db.session.add(student)
    db.session.commit()
    return jsonify({"message": f"Student {name} has been added."}), 201

@student_bp.route('/students/<int:id>', methods=["GET"])
def get_student(id):
    student = Student.query.get(id)
    if student is not None:
        return jsonify([
        {
            'id': student.id,
            'name': student.name,
            'grade': student.grade,
            'classroom_id': student.classroom_id
        }
    ]), 200
    else:
        return jsonify({"error": "Student not found" }), 404
    
@student_bp.route('/students/<int:id>', methods=["PUT"])
def update_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({'error': 'Student not found'}), 404

    data = request.get_json()
    new_grade = data.get('grade')
    if new_grade is None:
        return jsonify({'error': 'No grade provided'}), 400
    
    student.set_grade(new_grade)
    db.session.commit()
    return jsonify({'message': f'Grade updated to {new_grade}'}), 200

@student_bp.route('/students/<int:id>', methods=["DELETE"])
def remove_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify ({'error': 'Student not found'}), 404
    
    db.session.delete(student)
    db.session.commit()

    return jsonify({'message': f'{student.name} deleted successfully'}), 200

@student_bp.route('/students/class-average', methods = ['GET'])
def get_average():
    students = Student.query.all()
    if not students:
        return jsonify ({'error': 'Students not found'}), 404
    
    total_grade = sum(student.get_grade() for student in students)
    avg_grade = total_grade/len(students)

    return jsonify({'message': f'Student average is {round(avg_grade)}.'})
