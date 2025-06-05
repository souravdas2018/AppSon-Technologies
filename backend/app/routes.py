from flask import Blueprint, request, jsonify
from app import db
from app.models import Course, Student

main = Blueprint('main', __name__)

@main.route('/courses', methods=['POST'])
def create_course():
    try:
        data = request.json
        name = data.get('name')
        duration = data.get('duration')
        fee = data.get('fee')

        if not all([name, duration, fee]):
            return jsonify({'error': 'Missing required fields'}), 400

        course = Course(name=name, duration=duration, fee=fee)
        db.session.add(course)
        db.session.commit()

        return jsonify({'message': 'Course created'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to create course', 'details': str(e)}), 500

@main.route('/courses', methods=['GET'])
def get_courses():
    try:
        courses = Course.query.all()
        result = [
            {
                'id': c.id,
                'name': c.name,
                'duration': c.duration,
                'fee': c.fee
            }
            for c in courses
        ]
        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': 'Failed to fetch courses', 'details': str(e)}),


@main.route('/students', methods=['POST'])
def register_student():
    try:
        data = request.json
        required_fields = ['first_name', 'last_name', 'dob', 'address', 'course_id']

        # Check for missing fields
        if not all(field in data and data[field] for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400

        student = Student(
            first_name=data['first_name'],
            last_name=data['last_name'],
            dob=data['dob'],
            address=data['address'],
            course_id=data['course_id']
        )
        db.session.add(student)
        db.session.commit()

        return jsonify({'message': 'Student registered'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to register student', 'details': str(e)}), 500

@main.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    result = []
    for s in students:
        result.append({
            'id': s.id,
            'first_name': s.first_name,
            'last_name': s.last_name,
            'dob': s.dob,
            'address': s.address,
            'course': s.course.name,
            'course_id': s.course.id
        })
    return jsonify(result)

@main.route('/students/<int:id>', methods=['PUT'])
def edit_student(id):
    data = request.json
    student = Student.query.get_or_404(id)
    student.first_name = data['first_name']
    student.last_name = data['last_name']
    student.dob = data['dob']
    student.address = data['address']
    student.course_id = data['course_id']
    db.session.commit()
    return jsonify({'message': 'Student updated'})

@main.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Student deleted'})

# @main.route('/report', methods=['GET'])
# def report():
#     courses = Course.query.all()
#     result = []
#     for c in courses:
#         print(c.fee)
#         print(type(c.fee))
#         count = len(c.students)
#         total_fee = count * c.fee
#         result.append({
#             'course': c.name,
#             'count': count,
#             'total_fee': total_fee
#         })
#     return jsonify(result)


@main.route('/report', methods=['GET'])
def report():
    courses = Course.query.all()
    result = []
    for c in courses:
        try:
            fee = int(c.fee)  # Convert string to integer
        except ValueError:
            fee = 0  # Default if fee is not convertible

        count = len(c.students)
        total_fee = count * fee

        result.append({
            'course': c.name,
            'count': count,
            'total_fee': total_fee
        })
    return jsonify(result)

# Edit course
@main.route('/courses/<int:id>', methods=['PUT'])
def edit_course(id):
    data = request.get_json()
    course = Course.query.get(id)
    if not course:
        return jsonify({'error': 'Course not found'}), 404

    course.name = data['name']
    course.duration = data['duration']
    course.fee = data['fee']
    db.session.commit()
    return jsonify({'message': 'Course updated successfully'}), 200

# Delete course
from sqlalchemy.exc import IntegrityError

@main.route('/courses/<int:id>', methods=['DELETE'])
def delete_course(id):
    course = Course.query.get(id)
    if not course:
        return jsonify({'error': 'Course not found'}), 404

    try:
        db.session.delete(course)
        db.session.commit()
        return jsonify({'message': 'Course deleted successfully'}), 200

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Cannot delete course assigned to students'}), 400