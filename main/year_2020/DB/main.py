from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_urlsafe(16)
Bootstrap(app)


class GoodsForm(FlaskForm):
    good_type = StringField('Type:', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    submit = SubmitField('Save')


@app.route('/', methods=['POST', 'GET'])
def index():
    form = GoodsForm()
    if form.validate_on_submit():
        good_type = form.good_type.data
        price = form.price.data
        print(f'Type: {good_type} Price: {price}')
        return 'SUPER'
    else:
        return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)

