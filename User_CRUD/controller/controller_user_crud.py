from ..view.view import *
from ..model.model import *
from ...login.view.view import *
from flask import Blueprint, request, session, flash
from datetime import datetime
from random import randint
import os
from sendgrid import SendGridAPIClient
import hashlib


mod_user_crud = Blueprint('controller_user_crud', __name__, template_folder=r'C:\Users\YASH\PycharmProjects\projects\project_1\User_CRUD\view\templates')


@mod_user_crud.route('/userlist')
def userlist():
    if session.get('logged_in'):

        detail = fetch_user_detail()
        user_rname = r_detail()
        return view_user_list(detail , user_rname)
    else:
        return user_login_redirect()



@mod_user_crud.route('/userlist/create', methods=['GET', 'POST'])
def user_create():
    if session.get('logged_in'):

        user_rname = fetch_role_details()
        if request.method == "POST":
            urid = request.form['manu']
            uemail = request.form['uemail']
            ufn = request.form['ufname']
            uln = request.form['ulname']
            uphone = request.form['uno']
            time = str(datetime.now())
            url_code = randint(100000000000,999999999999)
            insert_user(uemail, ufn, uln, uphone, time, urid, session['email_ad'], url_code)
            body = render_template('/email/password_set.html', url_code = url_code)
            message = {
                'personalizations': [
                    {
                        'to': [
                            {
                                'email': uemail
                            }
                        ],
                        'subject': 'Password Set'
                    }
                ],
                'from': {
                    'email': 'tusharnema16@gmail.com'
                },
                'content': [
                    {
                        'type': 'text/html',
                        'value': body
                    }
                ]
            }


            try:
                sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
                print(e.message)

            return redirect_user_list()
        return view_user_create(user_rname)
    else:
        return user_login_redirect()


@mod_user_crud.route('/userlist/<details>', methods=['GET', 'POST'])
def userlist_edit(details):
    details_id = details
    if session.get('logged_in'):
        detail = select_user_by_id(details_id)
        user_rname = fetch_role_details()
        if request.method == "POST":
            urid = request.form['manu']
            useremail = request.form['uemail']
            ufn = request.form['ufname']
            uln = request.form['ulname']
            uphone = request.form['uno']
            time = str(datetime.now())
            update_user_list(useremail, ufn, uln, uphone, urid, details_id, time)
            return redirect_user_list()
        return view_user_edit(detail,user_rname)
    else:
        return user_login_redirect()


@mod_user_crud.route('/userlist/delete/<detail>')
def dele(detail):
    if session.get('logged_in'):

        delete_user(detail)
        return redirect_user_list()
    else:
        return user_login_redirect()


@mod_user_crud.route('/user/password/<item>', methods=['GET', 'POST'])
def set_password(item):
    detail = select_user_by_code(item)
    if request.method == "POST":
        password = request.form['password']
        result = hashlib.md5(password.encode())
        tr = result.hexdigest()
        set_passowrd_db(tr, item)
        delete_url_code(item)

        return redirect_dashboard()
    return view_set_password_user(detail, item)


@mod_user_crud.route('/user/setting', methods=['GET', 'POST'])
def user_setting():
    detail = fetch_detail_byemail(session['email_ad'])

    if request.method == "POST":
        det = request.form.values()

        user_password = get_password()
        current_pas = request.form['cp']
        new_pas = request.form['np']

        if current_pas == '':
            update_user_personal_nop(det, session['email_ad'])
            return redirect_user_setting()
        else:

            result = hashlib.md5(current_pas.encode())
            tr = result.hexdigest()
            if tr == user_password[0]['password']:
                res = hashlib.md5(new_pas.encode())
                tr1 = res.hexdigest()
                update_user_personal(det, tr1, session['email_ad'])
                return redirect_user_setting()
            else:
                flash('Enter correct password')
                return redirect_user_setting()

    return view_user_setting(detail)
