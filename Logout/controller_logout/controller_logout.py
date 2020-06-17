from flask import Blueprint, redirect,session, url_for
from ..view.view import *

mod_logout = Blueprint('controller_logout', __name__)

@mod_logout.route('/logout')
def logout():
    session.clear()
    return redirect_loginpage()