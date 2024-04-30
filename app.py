from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(80), unique=True)
    term = db.Column(db.Integer)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        company_name = request.form['company']
        term = request.form['term']
        new_company = Company(company_name=company_name, term=term)
        db.session.add(new_company)
        db.session.commit()
    companies = Company.query.all()
    return render_template('index.html', companies=companies)

@app.route('/clear', methods=['POST'])
def clear():
    db.session.query(Company).delete()
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
