from flask import *
from database import *
import uuid

public=Blueprint('public',__name__)


@public.route('/',methods=['get','post'])
def home():
    return render_template("publichome.html")

@public.route('/log',methods=['get','post'])
def login():
    if 'login' in request.form:
        a=request.form['uname']
        b=request.form['password']
        print(a,b)
        q="select * from login where username='%s' and password='%s'"%(a,b)
        print(q)
        res=select(q)
        if res:
            session['lid']=res[0]['login_id']
            u_type=res[0]['usertype']

            if u_type=="admin":
                flash("Welcome admin")
                return redirect(url_for('admin.admin_home'))
            elif u_type=="student":
                q="select * from student where login_id='%s'"%(session['lid'])
                re=select(q)
                session['stud_id']=re[0]['stud_id']
                session['sdpt']=re[0]['dept_id']
                flash("login success")
                return redirect(url_for('student.stud_home'))
            elif u_type=="department":
                q="select * from department where login_id='%s'"%(session['lid'])
                re=select(q)
                session['dept_id']=re[0]['dept_id']
                flash("login success")
                return redirect(url_for('department.dept_home'))
            elif u_type=="faculty":
                q="select * from faculty where login_id='%s'"%(session['lid'])
                re=select(q)
                session['fac_id']=re[0]['fac_id']
                flash("login success")
                return redirect(url_for('faculty.fac_home'))
        else:
            flash("Invalid username and password")
    return render_template("public_login.html")
