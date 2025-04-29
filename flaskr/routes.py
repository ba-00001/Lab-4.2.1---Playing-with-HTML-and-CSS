from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html', title='Home')

@bp.route('/about')
def about():
    return render_template('about.html', title='About')

@bp.route('/data')
def data():
    # Sample data for visualization
    labels = ['January', 'February', 'March', 'April', 'May']
    values = [10, 25, 18, 30, 22]
    return render_template('data.html', title='Data', labels=labels, values=values)