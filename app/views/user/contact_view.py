from flask import jsonify, render_template
from flask.views import MethodView
from app.services.user.contact_service import ContactService
from app.forms.user.contact_form import ContactForm

class ContactView(MethodView):
    form = None

    def dispatch_request(self, *args, **kwargs):
        self.form = ContactForm()
        return super().dispatch_request(*args, **kwargs)

    def get(self):
        context = {"form": self.form}
        return render_template("contact.html", **context)

    def post(self):
        data = None
        try:
            if self.form.validate_on_submit():
                data = self.form.data
            else:
                raise ValueError("Invalid form submission")

            ContactService.register(data)
            ContactService.send(data)
            return jsonify({"message": "Sended mail"})
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
