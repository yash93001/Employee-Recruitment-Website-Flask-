from flask import redirect, url_for


def redirect_loginpage ():
    return redirect(url_for('start'))