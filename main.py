from flask import  Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask( __name__ )
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/test_db7'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f"Book (author = '{self.author}',title = '{self.title}')"

@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books = books)

@app.route('/add', methods= ['POST'])
def add():
    author = request.form['author']
    title = request.form['title']

    book = Book(author=author, title=title)
    db.session.add(book)
    db.session.commit()
    return redirect('/')

if __name__ == 'main':
    with app.app_context():
        db.create_all()
    app.run(debug = True, port = 8000)