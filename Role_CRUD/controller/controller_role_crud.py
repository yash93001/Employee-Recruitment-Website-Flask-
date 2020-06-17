from flask import Blueprint,render_template,redirect, url_for, request,session
from ..model.model import *
from ..view.view import *
from ...login.view.view import *

mod_role_crud = Blueprint('controller_role_crud', __name__, template_folder=r'C:\Users\YASH\PycharmProjects\projects\project_1\Role_CRUD\view\templates')




@mod_role_crud.route('/role')
def role():
    if session.get('logged_in'):
        detail = fetch_role_info()
        return view_role_index(detail)
    else:
        return user_login_redirect()


@mod_role_crud.route('/role/create', methods=['GET', 'POST'])
def role_create():
    if session.get('logged_in'):
        if request.method == "POST":
            rname = request.form['name']
            insert_new_role(rname)
            return redirect_role_index()
        return view_role_create()
    else:
        return user_login_redirect()



@mod_role_crud.route('/role/<details>', methods=['GET', 'POST'])
def rolelist_edit(details):
    if session.get('logged_in'):
        ri_rid, ri_name = details.split('.')
        if request.method == "POST":
            rname = request.form['name']
            update_row_list( rname, ri_rid)
            return redirect_role_index()
        return view_role_edit(ri_rid, ri_name)
    else:
        return user_login_redirect()


@mod_role_crud.route('/role/delete/<detail>')
def dele(detail):
    if session.get('logged_in'):
        delete_role(detail)
        return redirect_role_index()
    else:
        return user_login_redirect()
