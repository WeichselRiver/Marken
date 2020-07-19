from flask import Flask, render_template, request, redirect, url_for
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
    michnr = db.Column(db.Integer, nullable=False)
    entwertung = db.Column(db.String(10), nullable=False)
    anzahl = db.Column(db.Integer)


    def __repr__(self):
        return f"{self.gebiet}, MichNr {self.michnr}, {self.entwertung} : {self.anzahl}"


class MyForm(FlaskForm):
    gebiete = [('AD Baden', 'AD Baden'), ('Berlin', 'Berlin') ]
    entwertungen = [('Postfrisch', 'Postfrisch'), ('Falz', 'Falz'), ('Gestempelt', 'Gestempelt')]

    gebiet = SelectField('Gebiet', choices=gebiete)
    michnr = IntegerField('MichNr', validators=[DataRequired()])
    entwertung = SelectField('Entwertung', choices=entwertungen, validators=[DataRequired()])
    anzahl = IntegerField('Anzahl')

@app.route('/', methods =['GET', 'POST'])
def index():
    marken_list = Marke.query.all()
    return render_template('index.html', marken_list = marken_list)



@app.route('/add', methods =['GET', 'POST'])
def add():
    
    form = MyForm()
    if form.validate_on_submit():
        fb_gebiet = form.gebiet.data
        fb_michnr = form.michnr.data
        fb_entwertung = form.entwertung.data
        fb_anzahl = form.anzahl.data
        print(fb_gebiet, fb_michnr, fb_entwertung, fb_anzahl)
        new_marke = Marke(gebiet = fb_gebiet, 
        michnr = fb_michnr, 
        entwertung=fb_entwertung, 
        anzahl=fb_anzahl)
        db.session.add(new_marke)
        db.session.commit()
        return redirect(url_for('index'))
        
    return render_template('add.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)


