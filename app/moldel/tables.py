from app import db


class Student(db.Model):

    __tablename__ = "student"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    course = db.Column(db.String)

    def __int__(self, name, email, course):
        self.name = name
        self.email = email
        self.course = course


class Course(db.Model):

    __tablename__ = "course"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __int__(self, name):
        self.name = name
