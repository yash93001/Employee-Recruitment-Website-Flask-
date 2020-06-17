from ...Model import con
cursor = con.cursor()


def user_login_data():
    cursor.execute("Select email, password from user_table")
    query_result = [dict(line) for line in [ zip([ column[0] for column in cursor.description ], row) for row in cursor.fetchall() ] ]

    return query_result


def user_fetch_dashboardinf(ema):
    emi = "Select first_name, last_name, rolename from user_table, role where roleid = role_id and email = %s "

    cursor.execute(emi, (ema,))
    all_detail = cursor.fetchall()
    return all_detail


