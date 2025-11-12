from flask import *
from database import *
import uuid

admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():
    return render_template("admin_home.html")



@admin.route('/admin_manage_department',methods=['get','post'])
def admin_manage_department():
   
    data={}
    s="select * from department"
    res=select(s)
    data['dpt']=res
    if 'submit' in request.form:
        uname=request.form['name']
        pwd=request.form['pwd']
        name=request.form['name']
        phone=request.form['phone']
        mail=request.form['mail']
     
    
        q="insert into login values(null,'%s','%s','department')"%(uname,pwd)
        lid=insert(q)
        r="insert into department values(null,'%s','%s','%s','%s')"%(lid,name,phone,mail)
        insert(r)
        flash("Department Added")
    
        return redirect(url_for('admin.admin_manage_department'))

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
        lid=request.args['lid']

    else:
        action=None

    if action=='delete':
        q="delete from department where dept_id='%s'"%(id)
        delete(q)
        r="delete from login where login_id='%s'"%(lid)
        delete(r)
        flash("Department Removed")
        return redirect(url_for('admin.admin_manage_department'))

    if action=='update':
        q="select * from department where dept_id='%s'"%(id)
        print(q)
        res=select(q)
        print(res)
        data['res']=res
    
    if 'edit' in request.form:
        name=request.form['name']
        phone=request.form['phone']
        mail=request.form['mail']
     
      
        q="update department set d_name='%s',d_phone='%s',d_mail='%s' where dept_id='%s'"%(name,phone,mail,id)
        update(q)
        flash("Department updated")
        return redirect(url_for('admin.admin_manage_department'))
    
    return render_template("admin_manage_department.html",data=data)




@admin.route('/admin_view_faculties',methods=['get','post'])
def admin_view_faculties():
    d_id=request.args['id']
    data={}
    s="select * from faculty where dept_id='%s'"%(d_id)
    res=select(s)
    data['res']=res
    return render_template("admin_view_faculties.html",data=data)




# @admin.route('/admin_view_student',methods=['get','post'])
# def admin_view_student():
#     data={}
    
#     d="select * from department"
#     data['view']=select(d)
#     s="select * from student inner join department using (dept_id)"
#     res=select(s)
#     data['res']=res
#     return render_template("admin_view_student.html",data=data)


@admin.route('/admin_view_student',methods=['get','post'])
def admin_view_student():
    data={}
    d="select * from department"
    data['view']=select(d)
    
    if 'submit' in request.form:
        dept=request.form['dept']
        print(dept,"//////////////////////////")
        
        a="select * from student inner join department using(dept_id) where dept_id='%s'"%(dept)
        data['res']=select(a)
    return render_template("admin_view_student.html",data=data)








@admin.route('/admin_viewcomplaint',methods=['get','post'])
def admin_viewcomplaint():
    data={}
    s="(SELECT CONCAT(`student`.`s_name`,'(student)')AS `user`,`complaint`,reply,`date`,`complaint_id`,`sender_id` FROM `complaint` INNER JOIN student ON `complaint`.`sender_id` = student.`login_id` INNER JOIN login USING(login_id) WHERE `usertype`='student') UNION (SELECT CONCAT(`faculty`.`f_name`,'(faculty)')AS `user`,`complaint`,reply,`date`,`complaint_id`,`sender_id` FROM `complaint` INNER JOIN faculty ON faculty.`login_id`=`complaint`.`sender_id`  INNER JOIN login USING(login_id) WHERE `usertype`='faculty')"
    res=select(s)
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
        return redirect(url_for('admin.admin_viewcomplaint'))
        
    return render_template("admin_viewcomplaint.html",data=data)




@admin.route('/admin_view_leave',methods=['get','post'])
def admin_view_leave():
    data={}
    d="select * from department"
    data['view']=select(d)
    
    if 'submit' in request.form:
        dept=request.form['dept']
        print(dept,"//////////////////////////")

        a="(SELECT CONCAT(`student`.`s_name`,'(student)')AS `user`,`date`,reason,`status`,`leave_id`,`sender_id` FROM `leave` INNER JOIN student ON student.`login_id`=`leave`.`sender_id` WHERE `user_type`='student' AND `dept_id`='%s')UNION(SELECT CONCAT(`faculty`.`f_name`,'(faculty)')AS `user`,`date`,reason,`status`,`leave_id`,`sender_id` FROM `leave` INNER JOIN faculty ON faculty.`login_id`=`leave`.`sender_id` WHERE `user_type`='faculty' AND `dept_id`='%s')"%(dept,dept)


        data['res']=select(a)
    return render_template("admin_view_leave.html",data=data)



@admin.route('/admin_manage_fee',methods=['get','post'])
def admin_manage_fee():
    data={}
    q="select dept_id,d_name from department"
    data['dpt']=select(q)
    s="select * from fee inner join department using(dept_id)"
    res=select(s)
    data['res']=res
 
    if 'submit' in request.form:
        dpt=request.form['dept']
        fee=request.form['fee']
        if dpt not in data['res']:
            y="insert into fee values(null,'%s','%s')"%(dpt,fee)
            insert(y)
            flash("Fee added")
        return redirect(url_for('admin.admin_manage_fee'))
        
    return render_template("admin_manage_fee.html",data=data)

@admin.route('/admin_manage_scholarship',methods=['get','post'])
def admin_managescholarship():
    data={}
    s="select * from scholarship order by scholarship_id desc"
    res=select(s)
    data['res']=res

    if 'submit' in request.form:
        scholar=request.form['scholar']
        dtails=request.form['details']
       
        q="insert into scholarship values(null,'%s','%s')"%(scholar,dtails)
        insert(q)
      
        flash("Scholarship Added")
    
        return redirect(url_for('admin.admin_managescholarship'))

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']

    else:
        action=None

    if action=='delete':
        q="delete from scholarship where scholarship_id='%s'"%(id)
        delete(q)
        flash("scholarship Removed")
        return redirect(url_for('admin.admin_managescholarship'))

    if action=='update':
        q="select * from scholarship where scholarship_id='%s'"%(id)
        print(q)
        res=select(q)
        print(res)
        data['upd']=res
    
    if 'edit' in request.form:
        dtails=request.form['details']
     
      
        q="update scholarship set details='%s' where scholarship_id='%s'"%(dtails,id)
        update(q)
        flash("Scholarship updated")
        return redirect(url_for('admin.admin_managescholarship'))
    
    return render_template("admin_manage_scholarship.html",data=data)

# @admin.route('/admin_view_scholarship_appln',methods=['get','post'])
# def admin_view_scholarship_appln():
#     data={}
#     s="select * from request_scholarship inner join student using(stud_id) inner join department on department.dept_id=request_scholarship.dept_id"
#     res=select(s)
#     data['res']=res
#     return render_template("admin_view_scholarship_appln.html",data=data)
    

@admin.route('/adminviewfeedback',methods=['get','post'])
def adminviewfeed():
    data={}
    qry="select * from feedback inner join student using(stud_id)"
    res=select(qry)
    data['view']=res

    return render_template("admin_view_feedback.html",data=data)