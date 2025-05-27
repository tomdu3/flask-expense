from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FloatField, SubmitField
from wtforms.validators import DataRequired

class UserInputForm(FlaskForm):
    type = SelectField(
        'Type', validators=[DataRequired()],
        choices = [
            ('income', 'income'),
            ('expense', 'expense')
            ]
        )
    
    category = SelectField(
        'Category', validators=[DataRequired()],
        choices = [
            ('salary', 'salary'),
            ('rent', 'rent'),
            ('transport', 'transport'),
            ('food', 'food'),
            ('other', 'other')
            ]
        )
    description = StringField('Description', validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired()])
    submit = SubmitField('Submit')
