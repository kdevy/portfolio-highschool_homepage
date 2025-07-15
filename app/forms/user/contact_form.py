from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    last_name = StringField(
        '姓',
        validators=[DataRequired()],
        render_kw={"placeholder": "例）日本"}
    )
    first_name = StringField(
        '名',
        validators=[DataRequired()],
        render_kw={"placeholder": "例）太郎"}
    )
    last_name_kana = StringField(
        'セイ',
        validators=[DataRequired()],
        render_kw={"placeholder": "例）ニホン"}
    )
    first_name_kana = StringField(
        'メイ',
        validators=[DataRequired()],
        render_kw={"placeholder": "例）タロウ"}
    )
    email = StringField(
        'メールアドレス',
        validators=[DataRequired()],
        render_kw={"placeholder": "例）nihontarou@gmail.com"}
    )
    email_confirmation = StringField(
        'Email Confirmation',
        validators=[DataRequired()],
        render_kw={"placeholder": "※ご確認のため再度ご入力ください"}
    )
    tell = StringField(
        '電話番号',
        validators=[DataRequired()],
        render_kw={"placeholder": "例）080-1234-5678"}
    )
    address = StringField(
        '住所',
        validators=[DataRequired()],
        render_kw={"placeholder": "例）2390831 神奈川県横須賀市久里浜1-2-3"}
    )
    content = TextAreaField(
        'お問い合わせ内容',
        validators=[DataRequired()],
        render_kw={"placeholder": "Content"}
    )
    submit = SubmitField('Submit')