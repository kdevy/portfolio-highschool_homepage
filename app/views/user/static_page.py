from flask import render_template
from app.views import user_bp

@user_bp.route('/')
def index():
    return render_template('index.html')

@user_bp.route('/about')
def about():
    return render_template('about.html')

@user_bp.route('/accessibility_policy')
def accessibility_policy():
    return render_template('accessibility_policy.html')

@user_bp.route('/personal_policy')
def personal_policy():
    return render_template('personal_policy.html')

@user_bp.route('/overview')
def overview():
    return render_template('overview.html')

@user_bp.route('/greeting')
def greeting():
    return render_template('greeting.html')

@user_bp.route('/philosophy')
def philosophy():
    return render_template('philosophy.html')

@user_bp.route('/history')
def history():
    return render_template('history.html')

@user_bp.route('/facility')
def facility():
    return render_template('facility.html')

@user_bp.route('/access')
def access():
    return render_template('access.html')