from ...Model import con
from flask import session
from datetime import datetime

cur_leads = con.cursor()


def fetch_lead_detail():
    cur_leads.execute(
        "Select name, email, city, status, created_on from leads order by created_on")
    query_result = [dict(line) for line in
                    [zip([column[0] for column in cur_leads.description], row) for row in cur_leads.fetchall()]]
    return query_result


def fetch_user_name():
    cur_leads.execute(
        "Select first_name, last_name, id from user_table where role_id = 4")
    query_result = [dict(line) for line in
                    [zip([column[0] for column in cur_leads.description], row) for row in cur_leads.fetchall()]]
    return query_result


def insert_leads(detail):
    st = "Insert into leads(name, email, phone_no, interested_in, city, user_id, assigned_on, created_on, created_by, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    date = datetime.now()
    cur_leads.execute(st, (
    detail[6], detail[5], detail[3], detail[4], detail[0], detail[2], date, date, session['email_ad'], detail[1],))
    con.commit()


def delete_lead(email):
    st = "delete from leads where email = %s"
    cur_leads.execute(st, (email,))
    con.commit()


def fetch_lead_detail_email(email):
    st = "Select name, email, city, status, created_on, phone_no, interested_in, user_id from leads  where email = %s"
    cur_leads.execute(st, (email,))
    query_result = [dict(line) for line in
                    [zip([column[0] for column in cur_leads.description], row) for row in cur_leads.fetchall()]]
    return query_result


def update_leads(details, email):
    st = "Update leads set name = %s, email= %s, phone_no= %s, interested_in= %s, city= %s, user_id= %s where email = %s "
    cur_leads.execute(st, (details[6], details[5], details[3], details[4], details[0], details[2], email))
    con.commit()


def fetch_lead_owner(id):
    st = "Select first_name, last_name from user_table, leads where user_id = id and user_id = %s"
    cur_leads.execute(st, (id, ))
    query_result = [dict(line) for line in
                    [zip([column[0] for column in cur_leads.description], row) for row in cur_leads.fetchall()]]
    return query_result
