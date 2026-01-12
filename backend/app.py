from flask import Flask
from flask_cors import CORS
from database.db_connection import init_db
from controllers.aluno_controller import aluno_bp
from controllers.professor_controller import professor_bp
from controllers.curso_controller import curso_bp
from controllers.disciplina_controller import disciplina_bp
from controllers.turma_controller import turma_bp
from controllers.matricula_controller import matricula_bp

app = Flask(__name__)
CORS(app)

# Registrar blueprints
app.register_blueprint(aluno_bp, url_prefix='/api/alunos')
app.register_blueprint(professor_bp, url_prefix='/api/professores')
app.register_blueprint(curso_bp, url_prefix='/api/cursos')
app.register_blueprint(disciplina_bp, url_prefix='/api/disciplinas')
app.register_blueprint(turma_bp, url_prefix='/api/turmas')
app.register_blueprint(matricula_bp, url_prefix='/api/matriculas')

@app.route('/')
def index():
    return {'message': 'API Sistema Acadêmico', 'status': 'online'}

@app.route('/api/health')
def health():
    return {'status': 'healthy'}

if __name__ == '__main__':
    init_db()
    print("🚀 Servidor iniciado em http://localhost:5000")
    print("📚 API Sistema Acadêmico")
    app.run(debug=True, port=5000)