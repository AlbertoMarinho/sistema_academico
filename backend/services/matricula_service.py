from repositories.matricula_repository import MatriculaRepository
from repositories.aluno_repository import AlunoRepository
from repositories.turma_repository import TurmaRepository
from models.matricula import Matricula

class MatriculaService:
    @staticmethod
    def criar_matricula(data):
        if not data.get('aluno_id'):
            raise ValueError("Aluno é obrigatório")
        if not data.get('turma_id'):
            raise ValueError("Turma é obrigatória")
        
        aluno = AlunoRepository.find_by_id(data['aluno_id'])
        if not aluno:
            raise ValueError("Aluno não encontrado")
        
        turma = TurmaRepository.find_by_id(data['turma_id'])
        if not turma:
            raise ValueError("Turma não encontrada")
        
        if MatriculaRepository.existe_matricula(data['aluno_id'], data['turma_id']):
            raise ValueError("Aluno já matriculado nesta turma")
        
        return MatriculaRepository.create(Matricula.from_dict(data))
    
    @staticmethod
    def listar_matriculas():
        return MatriculaRepository.find_all()
    
    @staticmethod
    def listar_matriculas_por_aluno(aluno_id):
        return MatriculaRepository.find_by_aluno(aluno_id)
    
    @staticmethod
    def listar_alunos_por_turma(turma_id):
        turma = TurmaRepository.find_by_id(turma_id)
        if not turma:
            raise ValueError("Turma não encontrada")
        return MatriculaRepository.find_by_turma(turma_id)
    
    @staticmethod
    def cancelar_matricula(matricula_id):
        return MatriculaRepository.delete(matricula_id)