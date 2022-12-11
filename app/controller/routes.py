from app import app, db
from flask import request, json
from app.moldel.tables import Student


@app.route("/api/student/create", methods=['POST'])
def createStudent():
    response = {"status": 400, "message": "Student not created"}

    student_data = json.loads(request.data)
    try:
        name = student_data["name"]
        email = student_data["email"]
        course = student_data["course"]

        student = Student(name=name, email=email, course=course)
        db.session.add(student)
        db.session.commit()

        response["status"] = 201
        response["message"] = "Student created successfully"

        return response, response["status"]
    except Exception as e:
        print(f"Error: {e}")

    return response, response["status"]


@app.route("/api/student", methods=['GET'])
def getStudents():
    response = {"status": 404, "message": "Students not available"}

    students = Student.query.all()
    if students:
        list_students = []
        for student in students:
            student_dic = {
                "id": student.id,
                "name": student.name,
                "email": student.email,
                "course": student.course
            }
            list_students.append(student_dic)

        response["status"] = 200
        response["message"] = list_students

        return response, response["status"]

    return response, response["status"]


@app.route("/api/student/<int:student_id>", methods=['GET'])
def getStudent(student_id):
    response = {"status": 404, "message": "Student not found"}

    student = Student.query.filter_by(id=student_id).first()
    if student:
        student_dic = {
            "id": student.id,
            "name": student.name,
            "email": student.email,
            "course": student.course
        }

        response["status"] = 200
        response["message"] = student_dic

        return response, response["status"]

    return response, response["status"]


@app.route("/api/student/update/<int:student_id>", methods=['POST'])
def updateStudent(student_id):
    response = {"status": 404, "message": "Users not available"}

    student = Student.query.filter_by(id=student_id).first()
    if student:
        student_data = json.loads(request.data)
        student.name = student_data["name"]
        student.email = student_data["email"]
        student.course = student_data["course"]

        db.session.commit()

        response["status"] = 200
        response["message"] = "Student updated successfully"

        return response, response["status"]

    return response, response["status"]


@app.route("/api/student/delete/<int:student_id>", methods=['GET'])
def deleteStudent(student_id):
    response = {"status": 404, "message": "Users not available"}

    student = Student.query.filter_by(id=student_id).first()
    if student:
        db.session.delete(student)
        db.session.commit()

        response["status"] = 200
        response["message"] = "Student deleted successfully"

        return response, response["status"]

    return response, response["status"]

