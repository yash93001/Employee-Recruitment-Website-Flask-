from flask import Blueprint, request
from ..view.view import*
from random import randint
from ..model.model import *
from ...User_CRUD.model.model import *
from ...User_CRUD.view.view import *
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, To
import os

mod = Blueprint('controller1', __name__)




@mod.route('/login')
def initial():
    return user_login()

@mod.route('/forgot_password')
def forpass():
    return view_forgot_password_page()


@mod.route('/reset_password')
def resetpass():
    email = request.form['email']
    url_code = randint(100000000000, 999999999999)
    insert_code(email , url_code)
    message = Mail(
        from_email='tusharnema16@gmail.com',
        to_emails=To(email),
        subject='Set Your Password',
        html_content= set_password(url_code))
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
    return user_login_redirect()
