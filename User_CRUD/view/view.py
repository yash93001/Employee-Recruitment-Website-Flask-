from flask import redirect, render_template, url_for


def view_user_list(detail, user_rname):
    return render_template('/User_CRUD/templates/index_user.html', detail= detail, user_rname =user_rname)


def view_user_create(user_rname):
    return render_template('/User_CRUD/templates/user_create.html', user_rname=user_rname)


def redirect_user_list():
    return redirect(url_for('controller_user_crud.userlist'))


def view_user_edit(detail, user_rname):
    return render_template('/User_CRUD/templates/user_edit.html', user_id=detail[0]['id'], user_email=detail[0]['email'], user_fn=detail[0]['first_name'],
                           user_ln=detail[0]['last_name'], user_phoneno=detail[0]['phone_no'], user_rname1=user_rname)


def view_set_password_user(detail, code):
    return render_template('/User_CRUD/templates/set_password.html', detail = detail, code = code)


def redirect_dashboard():
    return redirect(url_for('controller1.initial'))

def view_user_setting(detail):
    return render_template('/User_CRUD/templates/user_setting.html',detail = detail)

def redirect_user_setting():
    return redirect(url_for('controller_user_crud.user_setting'))


def view_change_user_password():
    return render_template('/User_CRUD/templates/user_change_password.html')