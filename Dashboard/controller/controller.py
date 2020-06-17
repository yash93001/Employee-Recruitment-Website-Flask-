from flask import Blueprint, request, session, redirect, url_for
from ..model.model import *
from ..view.view import *
from ...login.view.view import *
import hashlib

mod_dashboard = Blueprint('controller', __name__, template_folder=r'C:\Users\YASH\PycharmProjects\projects\project_1\Dashboard\view\templates')


@mod_dashboard.route('/dashboard', methods=['GET', 'POST'])
def user_login1():                                                                                                                                                   

    if request.method == 'POST':
        email_detail = user_login_data()
        password = request.form['password']
        password_hash = hashlib.md5(password.encode())
        tr = password_hash.hexdigest()

        email_ad = request.form['email']
        for i in range(len(email_detail)):
            if email_ad in email_detail[i]['email']:
                if tr in email_detail[i]['password']:
                    session['email_ad'] = email_ad
                    session['logged_in'] = True

        all_detail = user_fetch_dashboardinf(session['email_ad'])
        return view_dashboard(all_detail)

    if request.method == 'GET':
        all_detail_get = user_fetch_dashboardinf(session['email_ad'])
        
        return view_dashboard(all_detail_get)







