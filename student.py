from flask import *
from database import *
import uuid

student=Blueprint('student',__name__)

@student.route('/stud_home')
def stud_home():
    return render_template("student_home.html")




@student.route('/stud_apply_leave',methods=['get','post'])
def stud_apply_leave():
    data={}
    s="select * from `leave` where sender_id='%s'"%(session['lid'])
    data['res']=select(s)
    if 'submit' in request.form:
        dt=request.form['date']
        rsn=request.form['reason']
        qry="insert into `leave` values(null,'%s','%s','%s','pending','student')"%(session['lid'],dt,rsn)
        insert(qry)
        return redirect(url_for('student.stud_apply_leave'))
    return render_template("stud_apply_leave.html",data=data)

@student.route('/stud_complaint',methods=['get','post'])
def stud_complaint():
    data={}
    s="select * from complaint where sender_id='%s'"%(session['stud_id'])
    res=select(s)
    data['res']=res
    if 'submit' in request.form:
        a=request.form['complaint']
        q="insert into complaint values(null,'%s','%s','pending',now())"%(session['stud_id'],a)
        print(q)
        insert(q)
        return redirect(url_for('student.stud_complaint'))
    return render_template("stud_complaint.html",data=data)

@student.route('/stud_feedback',methods=['get','post'])
def stud_feedback():

    if 'fd' in request.form:
        feedback=request.form['feed']

        qry="insert into feedback values(null,'%s','%s',curdate())"%(session['stud_id'],feedback)
        insert(qry)

    # data={}
    # s="select * from feedback where student_id='%s'"%(session['stud_id'])
    # res=select(s)
    # data['res']=res
    # if 'fd' in request.form:
    #     fd=request.form['feed']
    #     q="insert into complaint values(null,'%s','%s','pending',now())"%(session['lid'],fd)
    #     print(q)
    #     insert(q)
    #     return redirect(url_for('student.stud_feedback'))
    return render_template("stud_feedback.html")

@student.route('/stud_scholarship')
def stud_scholarship():
    data={}
    s="select * from scholarship"
    data['sch']=select(s)

    
    return render_template("stud_scholarship.html",data=data)


@student.route('/stud_apply_scholar',methods=['get','post'])
def stud_apply_scholar():
    schlr_id=request.args['schid']
    if 'submit' in request.form:
        doc=request.files['docs']
        path='static/'+str(uuid.uuid4())+doc.filename
        doc.save(path)
        qry="insert into request_scholarship values(null,'%s','%s','%s','pending','%s')"%(session['stud_id'],session['sdpt'],path,schlr_id)
        insert(qry)
        return redirect(url_for('student.stud_apply_scholar'))

    return render_template("stud_apply_scholar.html")

@student.route('/stud_faculties')
def stud_faculties():
    data={}
    s="select * from faculty inner join subject using(fac_id) where dept_id='%s'"%(session['sdpt'])

 
    
    data['res']=select(s)

    return render_template("stud_faculties.html",data=data)

@student.route('/stud_result')
def stud_result():
    data={}
    s="select * from result inner join subject using(sub_id) where stud_id='%s' order by result_id desc"%(session['stud_id'])
    data['res']=select(s)

    return render_template("stud_result.html",data=data)

@student.route('/stud_attendance')
def stud_attendance():
    data={}
    s="select * from attendance where stud_id='%s' order by attendance_id desc"%(session['stud_id'])
    data['res']=select(s)
    return render_template("stud_attendance.html",data=data)

@student.route('/stud_fee')
def stud_fee():
    data={}
    s="select * from fee where dept_id='%s'"%(session['sdpt'])
    data['res']=select(s)
    return render_template("stud_fee.html",data=data)



