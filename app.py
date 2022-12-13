from flask import Flask, render_template, request, redirect, url_for
import requests, json

app = Flask(__name__)


@app.route("/")
def index():
    response = requests.get('http://127.0.0.1:5000/api/course').text
    courses =  json.loads(response)

    response = requests.get('http://127.0.0.1:5000/api/student').text
    students =  json.loads(response)

    if students['status'] == 404:
        students["message"] = []

    if courses['status'] == 404:
        courses["message"] = []

    return render_template('index.html',  courses=courses["message"], students=students["message"] )


@app.route("/add_student", methods=['POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        course = request.form['comp_select']

        data = {'name': name, 'email': email, 'course': course}

        response = requests.post('http://127.0.0.1:5000/api/student', data=json.dumps(data)).text
        print(response)
        
    return redirect(url_for('index'))

@app.route("/del_student/<int:id>", methods=['GET'])
def del_student(id):
    if request.method == 'GET':
        response = requests.get(f'http://127.0.0.1:5000/api/student/delete/{id}').text
        print(response)

    return redirect(url_for('index'))

@app.route('/edit_student/<id>', methods=['POST', 'GET'])
def edit_student(id):
    response = requests.get(f'http://127.0.0.1:5000/api/student/{id}').text
    student =  json.loads(response)
    
    response = requests.get('http://127.0.0.1:5000/api/course').text
    courses =  json.loads(response)
    return render_template('edit-student.html', student=student['message'], courses=courses["message"])


@app.route('/update_student/<id>', methods=['POST'])
def update_student(id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        course = request.form['comp_select']
        data = {'name': name, 'email': email, 'course': course}

        response = requests.post(f'http://127.0.0.1:5000/api/student/{id}', data=json.dumps(data)).text
        print(response)

    return redirect(url_for('index'))



@app.route("/add_course", methods=['POST'])
def add_course():
    if request.method == 'POST':
        name = request.form['name']

        data = {'name': name}

        response = requests.post('http://127.0.0.1:5000/api/course', data=json.dumps(data)).text
        print(response)
        
    return redirect(url_for('index'))

@app.route("/del_course/<int:id>", methods=['GET'])
def del_course(id):
    if request.method == 'GET':
        response = requests.get(f'http://127.0.0.1:5000/api/course/delete/{id}').text
        print(response)

    return redirect(url_for('index'))

@app.route('/edit_course/<id>', methods=['POST', 'GET'])
def edit_course(id):
    response = requests.get(f'http://127.0.0.1:5000/api/course/{id}').text
    course =  json.loads(response)

    return render_template('edit-course.html', course=course['message'])


@app.route('/update_course/<id>', methods=['POST'])
def update_course(id):
    if request.method == 'POST':
        name = request.form['name']

        data = {'name': name}

        response = requests.post(f'http://127.0.0.1:5000/api/course/{id}', data=json.dumps(data)).text
        print(response)

    return redirect(url_for('index'))

if __name__ == "__main__":
	app.run(port=5001, debug=True)