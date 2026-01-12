from repositories.turma_repository import TurmaRepository
from repositories.disciplina_repository import DisciplinaRepository
from repositories.professor_repository import ProfessorRepository
from models.turma import Turma

class TurmaService:
    @staticmethod
    def criar_turma(data):
        if not data.get('codigo'):
            raise ValueError("Código é obrigatório")
        if not data.get('disciplina_id'):
            raise ValueError("Disciplina é obrigatória")
        if not data.get('professor_id'):
            raise ValueError("Professor é obrigatório")
        if not data.get('periodo'):
            raise ValueError("Período é obrigatório")
        if not data.get('ano'):
            raise ValueError("Ano é obrigatório")
        
        disc = DisciplinaRepository.find_by_id(data['disciplina_id'])
        if not disc:
            raise ValueError("Disciplina não encontrada")
        
        prof = ProfessorRepository.find_by_id(data['professor_id'])
        if not prof:
            raise ValueError("Professor não encontrado")
        
        return TurmaRepository.create(Turma.from_dict(data))
    
    @staticmethod
    def listar_turmas():
        return TurmaRepository.find_all()
    
    @staticmethod
    def buscar_turma(turma_id):
        turma = TurmaRepository.find_by_id(turma_id)
        if not turma:
            raise ValueError("Turma não encontrada")
        return turma
    
    @staticmethod
    def atualizar_turma(turma_id, data):
        turma = TurmaRepository.find_by_id(turma_id)
        if not turma:
            raise ValueError("Turma não encontrada")
        
        if 'disciplina_id' in data:
            disc = DisciplinaRepository.find_by_id(data['disciplina_id'])
            if not disc:
                raise ValueError("Disciplina não encontrada")
        
        if 'professor_id' in data:
            prof = ProfessorRepository.find_by_id(data['professor_id'])
            if not prof:
                raise ValueError("Professor não encontrado")
        
        turma.codigo = data.get('codigo', turma.codigo)
        turma.disciplina_id = data.get('disciplina_id', turma.disciplina_id)
        turma.professor_id = data.get('professor_id', turma.professor_id)
        turma.periodo = data.get('periodo', turma.periodo)
        turma.ano = data.get('ano', turma.ano)
        turma.vagas = data.get('vagas', turma.vagas)
        
        return TurmaRepository.update(turma)
    
    @staticmethod
    def excluir_turma(turma_id):
        turma = TurmaRepository.find_by_id(turma_id)
        if not turma:
            raise ValueError("Turma não encontrada")
        return TurmaRepository.delete(turma_id)