from flask import Blueprint, render_template

static_page_bp = Blueprint('static_page', __name__, template_folder='../templates/user')

@static_page_bp.route('/')
def index():
    return render_template('index.html')

@static_page_bp.route('/about')
def about():
    return render_template('about.html')

@static_page_bp.route('/accessibility_policy')
def accessibility_policy():
    return render_template('accessibility_policy.html')

@static_page_bp.route('/personal_policy')
def personal_policy():
    return render_template('personal_policy.html')

@static_page_bp.route('/overview')
def overview():
    return render_template('overview.html')

@static_page_bp.route('/greeting')
def greeting():
    return render_template('greeting.html')

@static_page_bp.route('/philosophy')
def philosophy():
    return render_template('philosophy.html')

@static_page_bp.route('/history')
def history():
    return render_template('history.html')

@static_page_bp.route('/facility')
def facility():
    return render_template('facility.html')

@static_page_bp.route('/access')
def access():
    return render_template('access.html')