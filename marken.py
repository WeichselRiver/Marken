from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = "secretkey"

db = SQLAlchemy(app)

class Marke(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gebiet = db.Column(db.String(120), nullable=False)


    def __repr__(self):
        return f"{self.gebiet}, MichNr"


class MyForm(FlaskForm):
    entwertungen = ['Postfrisch','Falz', 'Gestempelt']

    gebiet = StringField('Gebiet', validators=[DataRequired()])
    michnr = IntegerField('MichNr', validators=[DataRequired()])
    entwertung = SelectField('Entwertung',choices=entwertungen)

@app.route('/', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        print(form.gebiet.data)
        return redirect('/')
    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)


