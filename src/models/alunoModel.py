from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AlunoModel(db.Model):
    __tablename__ = 'aluno'
   
    
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(100))
    cpf = db.Column(db.String(11), unique = True)
    matricula = db.Column(db.String(11), unique = True)
    ano = db.Column(db.Integer)
    turma =db.Column(db.String(2))
    
    
    def __init__(self, cpf, name, matricula, ano, turma):
        self.name = name
        self.cpf = cpf
        self.matricula = matricula
        self.ano = ano
        self.turma = turma
    def __repr__(self):
        return f"{self.id}:{self.name}:{self.matricula}:{self.ano}-{self.turma}"