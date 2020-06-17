from ...Model import con

cur_role = con.cursor()


def fetch_role_info():
    cur_role.execute("Select roleid, rolename from role order by roleid")
    query_result = [dict(line) for line in
                    [zip([column[0] for column in cur_role.description], row) for row in cur_role.fetchall()]]
    return query_result


def insert_new_role(rname):
    st = "Insert into role(rolename) VALUES(%s)"
    cur_role.execute(st, (rname,))
    con.commit()



def update_row_list( rname, ri_rid):
    st = "Update role set rolename= %s where roleid= %s"
    cur_role.execute(st, (rname, ri_rid,))
    con.commit()



def delete_role(detail):
    cur_role.execute("delete from role where roleid = %s", (detail,))
    con.commit()



