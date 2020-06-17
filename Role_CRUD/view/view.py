from flask import render_template, redirect, url_for


def view_role_index (detail):
    return render_template('/Role_CRUD/templates/index.html', detail = detail)


def redirect_role_index():
    return redirect(url_for('controller_role_crud.role'))


def view_role_create():
    return render_template('/Role_CRUD/templates/rolecreate.html')


def view_role_edit(ri_rid, ri_name):
    return render_template('/Role_CRUD/templates/rolelist_edit.html', ri_rid = ri_rid, ri_name = ri_name )