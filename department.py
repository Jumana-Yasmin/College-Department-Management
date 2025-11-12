from flask import *
from database import *
import uuid

department=Blueprint('department',__name__)

@department.route('/dept_home')
def dept_home():
    return render_template("department_home.html")

@department.route('/dept_manage_staff',methods=['get','post'])
def dept_manage_staff():
    data={}
    s="select * from faculty where dept_id='%s'"%(session['dept_id'])
    res=select(s)
    data['fac']=res
    if 'submit' in request.form:
        uname=request.form['uname']
        pwd=request.form['pwd']
        name=request.form['name']
        adrs=request.form['adr']
        phone=request.form['phone']
        mail=request.form['mail']
        qualification=request.form['qualification']
     
    
        q="insert into login values(null,'%s','%s','faculty')"%(uname,pwd)
        lid=insert(q)
        r="insert into faculty values(null,'%s','%s','%s','%s','%s','%s','%s')"%(lid,session['dept_id'],name,adrs,phone,mail,qualification)
        insert(r)
        flash("Faculty Added")
    
        return redirect(url_for('department.dept_manage_staff'))

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']

    else:
        action=None

    if action=='delete':
        q="delete from faculty where fac_id='%s'"%(id)
        delete(q)
        flash("faculty Removed")
        return redirect(url_for('department.dept_manage_staff'))

    if action=='update':
        q="select * from faculty where fac_id='%s'"%(id)
        print(q)
        res=select(q)
        print(res)
        data['res']=res
    
    if 'edit' in request.form:
        
        name=request.form['name']
        adrs=request.form['adr']
        phone=request.form['phone']
        mail=request.form['mail']
        qualification=request.form['qualification']
     
      
        q="update faculty set f_name='%s',f_address='%s',f_phone='%s',f_mail='%s',f_qualification='%s' where fac_id='%s'"%(name,adrs,phone,mail,qualification,id)
        update(q)
        flash("Faculty updated")
        return redirect(url_for('department.dept_manage_staff'))
    
    return render_template("dept_manage_staff.html",data=data)


@department.route('/dept_manage_subject',methods=['get','post'])
def dept_manage_subject():
    data={}
    fid=request.args['id']
    s="select * from subject where fac_id='%s'"%(fid)
    data['res']=select(s)
    if 'submit' in request.form:
        subject=request.form['sbj']
        q="insert into subject values(null,'%s','%s')"%(subject,fid)
        insert(q)
        flash("Assigned Subject")
        return redirect(url_for('department.dept_manage_staff'))
    return render_template("dept_manage_subject.html",data=data)


@department.route('/dept_manage_student',methods=['get','post'])
def dept_manage_student():
    data={}
    s="select * from student where dept_id='%s'"%(session['dept_id'])
    res=select(s)
    data['std']=res
    if 'submit' in request.form:
        uname=request.form['uname']
        pwd=request.form['pwd']
        name=request.form['name']
        adrs=request.form['adr']
        phone=request.form['phone']
        mail=request.form['mail']
    
        q="insert into login values(null,'%s','%s','student')"%(uname,pwd)
        lid=insert(q)
        r="insert into student values(null,'%s','%s','%s','%s','%s','%s')"%(lid,name,adrs,phone,mail,session['dept_id'])
        insert(r)
        flash("Student Added")
    
        return redirect(url_for('department.dept_manage_student'))

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']

    else:
        action=None

    if action=='delete':
        q="delete from student where stud_id='%s'"%(id)
        delete(q)
        flash("Student Removed")
        return redirect(url_for('department.dept_manage_student'))

    if action=='update':
        q="select * from student where stud_id='%s'"%(id)
        print(q)
        res=select(q)
        print(res)
        data['res']=res
    
    if 'edit' in request.form:
        
        name=request.form['name']
        adrs=request.form['adr']
        phone=request.form['phone']
        mail=request.form['mail']
     
     
      
        q="update student set s_name='%s',s_address='%s',s_phone='%s',s_mail='%s' where stud_id='%s'"%(name,adrs,phone,mail,id)
        update(q)
        flash("Student updated")
        return redirect(url_for('department.dept_manage_student'))
    
    return render_template("dept_manage_student.html",data=data)


@department.route('/dept_view_leave',methods=['get','post'])
def dept_view_leave():
    data={}
    # s="(SELECT CONCAT(`student`.`s_name`,'(student)')AS `user`,`date`,reason,`status`,`leave_id`,`sender_id` FROM `leave` INNER JOIN student ON student.`login_id`=`leave`.`sender_id` WHERE `user_type`='student')UNION(SELECT CONCAT(`faculty`.`f_name`,'(faculty)')AS `user`,`date`,reason,`status`,`leave_id`,`sender_id` FROM `leave` INNER JOIN faculty ON faculty.`login_id`=`leave`.`sender_id` WHERE `user_type`='faculty')"
    s="SELECT student.s_name as user,`date`,reason,`status`,leave_id,sender_id,user_type,d_name FROM `leave` INNER JOIN student ON leave.sender_id=student.login_id inner join department using(dept_id) WHERE user_type='student' AND dept_id='%s' UNION SELECT faculty.f_name as user,`date`,reason,`status`,leave_id,sender_id,user_type,d_name FROM `leave` INNER JOIN faculty ON leave.sender_id=faculty.login_id inner join department using(dept_id) WHERE user_type='faculty' AND dept_id='%s'"%( session['dept_id'], session['dept_id'])
    res=select(s)
    data['res']=res
   
    if 'action' in request.args:
        action=request.args['action']
        lv_id=request.args['lv_id']
    else:
        action=None
    if action=='approve':
        q="UPDATE `leave` SET `status` = 'approved' WHERE leave_id='%s'"%(lv_id)
        update(q)
        return redirect(url_for('department.dept_view_leave'))
    if action=='reject':
        q="UPDATE `leave` SET `status` = 'reject' WHERE leave_id='%s'"%(lv_id)
        update(q)
        return redirect(url_for('department.dept_view_leave'))

    return render_template("dept_view_leave.html",data=data)

@department.route('/dept_manage_stu_attendance',methods=['get','post'])
def dept_manageattendance():
    data={}
    s="select * from student where dept_id='%s'"%(session['dept_id'])
    data['res']=select(s)
    s2="select * from attendance inner join student using (stud_id) where dept_id='%s' order by attendance_id"%(session['dept_id'])
    data['view']=select(s2)
    if 'submit' in request.form:
        st=request.form['student']
        dt=request.form['date']
        atd=request.form['attendance']
        pd=request.form['pd']
        qry="insert into attendance values(null,'%s','%s','%s','%s')"%(st,atd,dt,pd)
        insert(qry)
        return redirect(url_for('department.dept_manageattendance'))
    return render_template("dept_manage_st_attendance.html",data=data)

@department.route('/dept_add_result',methods=['get','post'])
def dept_add_result():
    data={}
    qry="select * from student where dept_id='%s'"%(session['dept_id'])
    res=select(qry)
    data['stud']=res
    qry="        SELECT sub_name FROM SUBJECT INNER JOIN faculty USING(fac_id) INNER JOIN department USING(dept_id) where dept_id='%s'"%(session['dept_id'])
    res=select(qry)
    data['sub']=res


    if 'submit' in request.form:
        st=request.form['student']
        sb=request.form['sub']
        ma=request.form['ma']
        gt=request.form['gt']
        result=request.form['result']
        qry="insert into result values(null,'%s','%s','%s','%s','%s')"%(st,sb,ma,gt,result)
        insert(qry)
        return redirect(url_for('department.dept_add_result'))
    return render_template("dept_add_result.html",data=data)

@department.route("/view_complaint",methods=['get','post'])
def viewcomplaint():
    data={}
    # qry="select * from complaint where sender_id='%s'"%(session['stud_id'])
    qry="SELECT student.s_name AS `user`, sender_id,complaint,reply,`date`,d_name,complaint_id FROM complaint INNER JOIN student ON student.login_id = complaint.sender_id INNER JOIN department USING(dept_id) WHERE dept_id='%s' UNION SELECT faculty.f_name AS `user`, sender_id,complaint,reply,`date`,d_name,complaint_id FROM complaint INNER JOIN faculty ON faculty.login_id = complaint.sender_id INNER JOIN department USING(dept_id) WHERE dept_id='%s'"%(session['dept_id'],session['dept_id'])
    res=select(qry)
    data['res']=res
  
    

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None
    if action=='reply':
        data['check']=0
    if 'replay' in request.form:
        reply=request.form['reply']

        q="update complaint set reply='%s' where complaint_id='%s'"%(reply,id)
        update(q)
        flash("Reply sent")
        return redirect(url_for('department.viewcomplaint'))
    return render_template("depart_view_complaint.html",data=data)



# for i in range (1,len(res)+1):
#         print(i)
#         if 'submit'+str(i) in request.form:
#             print('hell')
#             reply=request.form['reply'+str(i)]
#             id=request.form['id'+str(i)]
#             q="UPDATE `complaint` SET `reply`='%s' WHERE `complaint_id`='%s'"%(reply,id)
#             update(q)
#             flash('REPLY DELIVERED')

    #  {% if row['reply']=='pending'%}
	# 			<td><input type="text" class="form-control" name="reply{{loop.index}}">
	# 				<input type="hidden" name="id{{loop.index}}" value="{{row['complaint_id']}}">
	# 				<input class="btn btn-info" type="submit" name="submit{{loop.index}}"></td>
	# 				{% else %}
	# 			<td>{{row['reply']}}</td>
	# 			{% endif %}




