from ...Model import con
cur_login = con.cursor()


def insert_code(email, code):
    st = "Update user_table set url_code = %s, where email = %s"
    cur_login.execute(st, ( code, email, ))
    con.commit()


