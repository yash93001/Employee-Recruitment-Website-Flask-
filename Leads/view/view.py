from flask import render_template, redirect, url_for


def view_lead_lsit(detail):
    return render_template('/Leads/index.html', detail = detail)


def view_leads_create(user_name):
    return render_template('/Leads/leads_create.html', user_name = user_name)


def redirect_index():
    return redirect(url_for('controller_leads.leads_index'))


def redirect_lead_profile(email):
    return redirect(url_for('controller_leads.lead_profile', email = email))


def view_lead_profile(details, lead_owner):
    return render_template('/Leads/leads_profile.html', details =details, lead_owner= lead_owner)


def view_lead_profile_edit(detail, user_name):
    return render_template('/Leads/leads_edit.html', details = detail, user_name = user_name)