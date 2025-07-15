from flask import Blueprint
from app.views.user.contact_view import ContactView
from app.views.admin.login_view import LoginView as AdminLoginView

user_bp = Blueprint("user", __name__, template_folder="../templates/user")
admin_bp = Blueprint("admin", __name__, template_folder="../templates/admin")

contact_view = ContactView.as_view("contact")
user_bp.add_url_rule("/contact" , view_func=contact_view , methods=["GET", "POST"])

admin_login_view = AdminLoginView.as_view("login")
admin_bp.add_url_rule("/", view_func=admin_login_view, methods=["GET", "POST"])
admin_bp.add_url_rule("/login", view_func=admin_login_view, methods=["GET", "POST"])