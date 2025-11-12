from flask import *
from database import *
import uuid

faculty=Blueprint('faculty',__name__)


@faculty.route('/fac_home')
def fac_home():
    return render_template("faculty_home.html")


@faculty.route('/fac_leave',methods=['get','post'])
def fac_leave():
    data={}
    s="select * from `leave` where sender_id='%s'"%(session['lid'])
    data['res']=select(s)
    if 'submit' in request.form:
        dt=request.form['date']
        rsn=request.form['reason']
        qry="insert into `leave` values(null,'%s','%s','%s','pending','faculty')"%(session['lid'],dt,rsn)
        insert(qry)
        return redirect(url_for('faculty.fac_leave'))
    return render_template("fac_leave.html",data=data)

@faculty.route('/fac_subj')
def fac_subj():
    data={}
    s="select * from subject where fac_id='%s'"%(session['fac_id'])
    data['res']=select(s)
    return render_template("fac_subj.html",data=data)

@faculty.route('/fac_complaint',methods=['get','post'])
def fac_complaint():
    data={}
    s="select * from complaint where sender_id='%s'"%(session['lid'])
    res=select(s)
    data['res']=res
    if 'submit' in request.form:
        a=request.form['complaint']
        q="insert into complaint values(null,'%s','%s','pending',now())"%(session['lid'],a)
        print(q)
        insert(q)
        return redirect(url_for('faculty.fac_complaint'))
    return render_template("fac_complaint.html",data=data)