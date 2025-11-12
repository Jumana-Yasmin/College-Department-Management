from flask import *
from public import public
from admin import admin
from department import department
from student import student
from faculty import faculty

app=Flask(__name__)
app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(department)
app.register_blueprint(student)
app.register_blueprint(faculty)


app.secret_key='key'
app.run(debug=True,port=5009)