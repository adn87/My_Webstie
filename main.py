from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///work.db"
db = SQLAlchemy()
db.init_app(app)
Bootstrap5(app)


class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(250), nullable=False)
    company = db.Column(db.String(250), nullable=False)
    duration = db.Column(db.String(250), nullable=False)
    description = db.Column(db.Text, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/work')
def work():
    result = db.session.execute(db.select(Work).order_by(Work.id))
    jobs = result.scalars().all()
    return render_template('work.html', job=jobs)


@app.route('/description/<int:job_id>')
def description(job_id):
    requested_job = db.get_or_404(Work, job_id)
    return render_template('description.html', job=requested_job)


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
