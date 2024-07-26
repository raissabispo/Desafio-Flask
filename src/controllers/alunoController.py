from flask import Blueprint, render_template, request, redirect, abort
from models.alunoModel import AlunoModel, db
 
aluno_blueprint = Blueprint('aluno', __name__)
 
@aluno_blueprint.route('/')
def index():
    return render_template('mainpage.html')

@aluno_blueprint.route('/consulta_matricula', methods=["GET", "POST"])
def consulta_matricula():
    if request.method == "POST":
        matricula = request.form.get('matricula')
        if matricula:
            return redirect(f'/data/matricula/{matricula}')
        else:
            return "Matrícula não informada", 400
    return render_template("consulta_matricula.html")


 
@aluno_blueprint.route('/create', methods=["GET", "POST"])
def create():
   
    if request.method == 'GET':
        return render_template('createpage.html')
   
    if request.method == 'POST':
        name = request.form['name']
        cpf = request.form['cpf']
        matricula = request.form['matricula']
        ano = request.form['ano']
        turma = request.form['turma']
        aluno = AlunoModel(name = name, cpf = cpf, matricula = matricula, ano = ano, turma = turma ) 
        db.session.add(aluno)
        db.session.commit()
        return redirect('/data')
   
@aluno_blueprint.route('/data')
def DataView():
    aluno = AlunoModel.query.all()
    return render_template('datalist.html', aluno=aluno)


@aluno_blueprint.route('/data/matricula/<string:matricula>')
def mostrar_aluno_matricula(matricula):
    aluno = AlunoModel.query.filter_by(matricula=matricula).first()
    return render_template("mostrar_aluno.html", aluno=aluno)


@aluno_blueprint.route('/data/<int:matricula>')
def findAluno(matricula):
    # buscar pelo numero da matricula
    aluno = AlunoModel.query.filter_by(matricula = matricula).first()
    if aluno:
        return render_template("data.html", aluno=aluno)
    else:
        return f"Aluno(a) com o número da matrícula{matricula} não existe"
    
    
@aluno_blueprint.route('/data/<int:matricula>/update', methods=["GET","POST"])
# editar o usuario
def update(matricula):
    aluno =AlunoModel.query.get(matricula)
    if not aluno:
        return "Aluno(a) com o número da matrícula{matricula} não existe"
    if request.method == 'POST':
        aluno.name = request.form["name"]
        aluno.cpf = request.form["cpf"]
        aluno.matricula= request.form["matricula"]
        aluno.ano= request.form["ano"]
        aluno.turma= request.form["turma"]
        db.session.commit()
        return redirect(f"/data/{matricula}")
    return render_template("update.html", aluno=aluno)

@aluno_blueprint.route('/data/<int:id>/delete', methods=["GET", "POST"])
def delete(id):
    aluno = AlunoModel.query.get(id)
    if not aluno:
        return "Aluno(a) com id={id} não existe", 404
    if request.method == 'POST':
        db.session.delete(aluno)
        db.session.commit()
        return redirect('/data')
    return render_template('delete.html', aluno=aluno)
