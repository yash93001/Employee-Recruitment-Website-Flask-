from ..view.view import *
from ..model.model import *
from ...login.view.view import *
from flask import Blueprint, request, session, flash


mod_leads = Blueprint('controller_leads', __name__, template_folder=r'C:\Users\YASH\PycharmProjects\projects\project_1\User_CRUD\view\templates')


@mod_leads.route('/leads')
def leads_index():
    if session.get('logged_in'):
        detail = fetch_lead_detail()
        return view_lead_lsit(detail)
    else:
        return user_login_redirect()


@mod_leads.route('/leads/create', methods=['GET', 'POST'])
def lead_create():
    if session.get('logged_in'):

        user_name = fetch_user_name()
        if request.method == "POST":
            details = request.form.values()
            insert_leads(details)
            return redirect_lead_profile(details[5])
        return view_leads_create(user_name)
    else:
        return user_login_redirect()


@mod_leads.route('/lead/profile/<email>')
def lead_profile(email):
    if session.get('logged_in'):
        detail = fetch_lead_detail_email(email)
        lead_owner = fetch_lead_owner(detail[0]['user_id'])
        return view_lead_profile(detail, lead_owner)
    else:
        return user_login_redirect()


@mod_leads.route('/leads/delete/<email>')
def lead_delete(email):
    if session.get('logged_in'):
        delete_lead(email)
        return redirect_index()
    else:
        return user_login_redirect()


@mod_leads.route('/leads/edit/<email>', methods=['GET', 'POST'])
def lead_edit(email):
    if session.get('logged_in'):
        user_name = fetch_user_name()
        user_name.sort()

        detail = fetch_lead_detail_email(email)


        if request.method == "POST":
            details = request.form.values()
            update_leads(details , email)
            return redirect_lead_profile(details[5])

        return view_lead_profile_edit(detail, user_name)
    else:
        return user_login_redirect()