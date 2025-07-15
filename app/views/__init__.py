from flask import Blueprint
from app.views.user.contact_view import ContactView

user_bp = Blueprint("user", __name__, template_folder="../templates/user")

contact_view = ContactView.as_view("contact")
user_bp.add_url_rule("/contact" \
                    , view_func=contact_view \
                    , methods=["GET", "POST"])