from flask import Flask, render_template, session, redirect, url_for
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from wtforms import FloatField, SubmitField
from wtforms.validators import InputRequired, DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess my string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(Form):
    valeur1 = FloatField('valeur 1 : ', validators=[InputRequired("Entrez une valeur")])
    valeur2 = FloatField('valeur 2 : ', validators=[InputRequired("Entrez une valeur")])
    submit = SubmitField('Calculer')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        value_format= "{:.2f}".format(form.valeur1.data / form.valeur2.data)
        session['result'] = value_format
        return redirect(url_for('index'))
    return render_template('index.html', form=form, result=session.get('result'))


if __name__ == '__main__':
    manager.run()
