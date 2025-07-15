from flask import request, jsonify, render_template
from flask.views import MethodView
from app.services.user_service import UserService
from app.forms.login_form import LoginForm

class LoginView(MethodView):
    form = None

    def dispatch_request(self, *args, **kwargs):
        self.form = LoginForm()
        return super().dispatch_request(*args, **kwargs)

    def get(self):
        context = {"form": self.form}
        return render_template("login.html", **context)

    def post(self):
        data = None
        try:
            if self.form.validate_on_submit():
                data = self.form.data
            else:
                raise ValueError("Invalid form submission")

            user = UserService.login(data.get("username"), data.get("password"))
            return jsonify({"message": "Logged in", "user": user})
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
