from flask_app import app
from flask import session,render_template,redirect,request
from flask_app.models.order import Order

@app.route('/cookies')
def index():
    return render_template('show_all.html', all_orders=Order.show_all())

@app.route('/cookies/new')
def new():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    if not Order.vald_order(request.form):
        return redirect('/cookies/new')
    Order.create(request.form)
    return redirect('/cookies')

@app.route('/cookies/edit/<int:id>')
def edit(id):
    session['id'] = id
    return render_template('edit.html',order=Order.show_one(id))

@app.route('/cookies/update', methods=['POST'])
def update():
    if not Order.vald_order(request.form):
        return redirect("/cookies/edit/" + str(session['id']))
    Order.update_cookie(request.form)
    return redirect('/cookies')
