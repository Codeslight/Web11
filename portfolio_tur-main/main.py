# Import
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# SQLite'ı bağlama
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Veri tabanı oluşturma
db = SQLAlchemy(app)
# Tablo oluşturma
class User(db.Model):
    # Sütunları oluşturma
     # kimlik
    email=db.Column(db.String(100), nullable=False)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text=db.Column(db.String(100), nullable=False)


# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler

@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_db = request.form.get('button_db')
    button_html = request.form.get('button_html')
    return render_template('index.html', button_python=button_python,button_discord=button_discord,button_db=button_db,button_html=button_html)

@app.route('/form_create', methods=["POST"])
def form_create():
    if request.method == 'POST':
        email=request.form["email"]
        text =  request.form['text']
        if email:

            # Veri tabanına gönderilecek bir nesne oluşturma
            user = User(email=email, text=text)

            db.session.add(user)
            db.session.commit()
            return redirect('/index')
    

if __name__ == "__main__":
    with app.app_context():
         db.create_all()
    app.run(debug=True)
