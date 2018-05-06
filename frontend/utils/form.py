from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired

class urlForm(FlaskForm):
    url = StringField('URL', validators=[DataRequired()])
    submit = SubmitField('Submit')

class formData():
    def __init__(self):
        self.url = ""
        self.header = ""
        self.body = ""
        self.verdict = ""
    
    def set_url(self, url):
        self.url = url

    def set_header(self, head):
        self.header = head

    def set_body(self, body):
        self.body =body
    
    def set_verdict(self, judgement):
        self.verdict = judgement