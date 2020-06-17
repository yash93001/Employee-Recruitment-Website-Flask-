from ...Model import con
from flask import session, flash

cur_user_crud = con.cursor()


def fetch_user_detail():
    cur_user_crud.execute(
        "Select id, email, first_name, last_name, phone_no, created_time, role_id from user_table order by id")
    query_result = [dict(line) for line in
                    [zip([column[0] for column in cur_user_crud.description], row) for row in cur_user_crud.fetchall()]]
    return query_result


def r_detail():
    cur_user_crud.execute("Select rolename, roleid from user_table, role where role_id = roleid")
    query_result = [dict(line) for line in
                    [zip([column[0] for column in cur_user_crud.description], row) for row in cur_user_crud.fetchall()]]
    return query_result


def fetch_role_details():
    cur_user_crud.execute("Select rolename, roleid from role")
    query_result = [dict(line) for line in
                    [zip([column[0] for column in cur_user_crud.description], row) for row in cur_user_crud.fetchall()]]
    return query_result


def insert_user(uemail, ufn, uln, uphone, time, urid, created_by, code):
    st = "Insert into user_table( email, first_name, last_name, phone_no, created_time, role_id, created_by, url_code) VALUES( %s, %s, %s, %s, %s, %s, %s, %s)"
    cur_user_crud.execute(st, (uemail, ufn, uln, uphone, time, urid, created_by, code,))
    con.commit()


def select_user_by_id(uemail):
    ste = "Select id, email, first_name, last_name, phone_no, created_time, role_id from user_table where id= %s"
    cur_user_crud.execute(ste, (uemail,))
    query_result = [dict(line) for line in
                    [zip([column[0] for column in cur_user_crud.description], row) for row in cur_user_crud.fetchall()]]
    return query_result


def update_user_list(useremail, ufn, uln, uphone, urid, id, time):
    st = "Update user_table set email = %s, first_name = %s, last_name= %s, phone_no= %s, role_id = %s, modified_on = %s where id = %s"
    cur_user_crud.execute(st, (useremail, ufn, uln, uphone, urid, time, id,))
    con.commit()


def delete_user(detail):
    cur_user_crud.execute("delete from user_table where id = %s", (detail,))
    con.commit()


def select_user_by_code(code):
    ste = "Select id, email, first_name, last_name, phone_no, created_time, role_id from user_table where url_code= %s"
    cur_user_crud.execute(ste, (code,))
    query_result = [dict(line) for line in
                    [zip([column[0] for column in cur_user_crud.description], row) for row in cur_user_crud.fetchall()]]
    return query_result


def set_passowrd_db(password, code):
    st = "Update user_table set password = %s where url_code = %s"
    cur_user_crud.execute(st, (password, code,))
    con.commit()


def delete_url_code(code):
    st = "Update user_table set url_code = null  where url_code = %s"
    cur_user_crud.execute(st, (code,))
    con.commit()


def fetch_detail_byemail(email):
    st = "Select id, email, first_name, last_name, phone_no, created_time, role_id from user_table where email= %s"
    cur_user_crud.execute(st, (email,))
    query_result = [dict(line) for line in
                    [zip([column[0] for column in cur_user_crud.description], row) for row in cur_user_crud.fetchall()]]
    return query_result


def update_user_personal(details, password, email):
    st = "Update user_table set first_name = %s, last_name= %s, phone_no= %s, password= %s where email = %s"
    try:
        cur_user_crud.execute(st, (details[4], details[0], details[3], password, email,))
        con.commit()
    except:
        flash('Error')
        con.rollback()


def update_user_personal_nop(details, email):
    st = "Update user_table set first_name = %s, last_name= %s, phone_no= %s where email = %s"
    try :
        cur_user_crud.execute(st, (details[4], details[0], details[3], email,))
        con.commit()
    except:
        flash('Error')
        con.rollback()


def get_password():
    st = "Select password from user_table where email = %s"
    cur_user_crud.execute(st, (session['email_ad'], ))
    query_result = [dict(line) for line in
                    [zip([column[0] for column in cur_user_crud.description], row) for row in cur_user_crud.fetchall()]]
    return query_result


def set_password_mail(pass_hash):
    st = "Update user_table set password = %s where email = %s"
    cur_user_crud.execute(st, (pass_hash, session['email_ad'],))
    con.commit()
