from flask import Flask
from models.alunoModel import db
from controllers.alunoController import aluno_blueprint

app = Flask(__name__, template_folder="views")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aluno.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(aluno_blueprint, url_prefix='/')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)