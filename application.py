from flask import Flask, render_template, session, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, SelectField
from wtforms.validators import DataRequired, ValidationError
from flask_bootstrap import Bootstrap
from compute import compute

class SearchForm(FlaskForm):
    year = SelectMultipleField('Year', choices=[('2017','2017'),('2018','2018')], validators = [DataRequired()])
    clg_type = SelectField('College Type', choices=[('nit','NIT'),('iiit', 'IIIT'),('gfti', 'GFTI')], validators = [DataRequired()])
    clg_name = StringField("College")
    branch = StringField("Branch")
    gender = SelectField('Gender Category', choices=[('Neut', 'Gender-Neutral'), ('Fem','Female-Only')], validators = [DataRequired()])
    #quota = SelectField('Quota', choices=[('ai','AI'),('hs', 'HS')])
    cat = SelectField('Category', choices=[('OPEN','OPEN'),('OBC', 'OBC-NCL'),('SC', 'SC'),('ST','ST'),('PwD','PwD')], validators = [DataRequired()])
    submit = SubmitField("SUBMIT")


app=Flask(__name__)
app.config['SECRET_KEY'] ="replace_later"
bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    form=SearchForm(request.form)
    #if request.method=='POST' and form.validate():
    if form.validate_on_submit():
        print("Validate!")
        college = form.clg_name.data
        branch = form.branch.data
        sel_years = form.year.data
        cats = form.cat.data
        clg_type = form.clg_type.data
        gen = form.gender.data
        #quota = form.quota.data
        #dur = form.dur.data
        tables = compute(college, branch, sel_years, cats, clg_type, gen) #,dur, quota
    else:
        tables = None

    return render_template('index.html', form=form, tables=tables, years = form.year.data)

@app.route('/about')
def about():
    return redirect('https://josaa-analysis.herokuapp.com/about')

@app.route('/intellitrak_home')
def intellitrak_home():
    return redirect('www.intellitrak.in/josaa')

if(__name__=="__main__"):
    app.run()