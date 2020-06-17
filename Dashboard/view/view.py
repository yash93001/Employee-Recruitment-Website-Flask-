from flask import render_template

def view_dashboard(all_detail):
    return render_template('/Dashboard/templates/new.html', detail=all_detail )