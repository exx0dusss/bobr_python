from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, SelectField
from wtforms.validators import DataRequired

c = [('red', 'Red'), ('blue', 'Blue'), ('green', 'Green'),
     ('yellow', 'Yellow'), ('black', 'Black'), ('white', 'White')]
s = [('xs', 'XS'),('s', 'S'),('m', 'M'),
     ('l', 'L'),('xl', 'XL'),('xxl', 'XXL')]


class GoodsFormClass(FlaskForm):
    brand = StringField('Brand:', validators=[DataRequired()])
    price = FloatField('Price:', validators=[DataRequired()])
    color = SelectField('Color:', choices=[*c])
    size = SelectField('Size:', choices=[*s])
    submit = SubmitField('Save:')
