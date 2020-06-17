from flask import render_template, redirect, url_for


def user_login():
    return render_template('/login/templates/ff.html')


def user_login_redirect():
    return redirect(url_for('controller1.initial'))


def view_forgot_password_page():
    return render_template('/login/templates/forgot_password.html')


def set_password(url_code):
    return render_template('/login/templates/password_set.html', url_code = url_code)
