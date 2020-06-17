from flask import Flask, redirect, url_for, session
import  sys

ap_f1 = Flask(__name__, template_folder = r'C:\Users\yash1\PycharmProjects\project\project_1\templates',static_folder=r"C:\Users\YASH\PycharmProjects\projects\project_1\static")
from .login.controller.controller1 import mod
from .Dashboard.controller.controller import mod_dashboard
from .Logout.controller_logout.controller_logout import mod_logout
from .Role_CRUD.controller.controller_role_crud import mod_role_crud
from .User_CRUD.controller.controller_user_crud import mod_user_crud
from .Leads.controller.controller_leads import mod_leads

ap_f1.register_blueprint(mod_dashboard)
ap_f1.register_blueprint(mod_logout)
ap_f1.register_blueprint(mod)
ap_f1.register_blueprint(mod_role_crud)
ap_f1.register_blueprint(mod_user_crud)
ap_f1.register_blueprint(mod_leads)

sys.setrecursionlimit(999999)

@ap_f1.route('/')
def start():

    if not session.get('logged_in'):
        return redirect(url_for('controller1.initial'))
    else:
        return redirect(url_for('controller.user_login1'))