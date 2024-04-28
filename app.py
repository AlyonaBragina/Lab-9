from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////project.db'
db = SQLAlchemy(app)

class WorkHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(80), nullable=False)
    term = db.Column(db.Integer, nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        company = request.form['company']
        term = request.form['term']
        work_history = WorkHistory(company=company, term=term)
        db.session.add(work_history)
        db.session.commit()
    work_history_list = WorkHistory.query.all()
    return render_template('index.html', work_history_list=work_history_list)

if __name__ == '__main__':
    app.run(debug=True)
