from repositories.disciplina_repository import DisciplinaRepository
from repositories.curso_repository import CursoRepository
from models.disciplina import Disciplina

class DisciplinaService:
    @staticmethod
    def criar_disciplina(data):
        if not data.get('nome'):
            raise ValueError("Nome é obrigatório")
        if not data.get('codigo'):
            raise ValueError("Código é obrigatório")
        if not data.get('curso_id'):
            raise ValueError("Curso é obrigatório")
        
        curso = CursoRepository.find_by_id(data['curso_id'])
        if not curso:
            raise ValueError("Curso não encontrado")
        
        return DisciplinaRepository.create(Disciplina.from_dict(data))
    
    @staticmethod
    def listar_disciplinas():
        return DisciplinaRepository.find_all()
    
    @staticmethod
    def listar_disciplinas_por_curso(curso_id):
        return DisciplinaRepository.find_by_curso(curso_id)
    
    @staticmethod
    def buscar_disciplina(disciplina_id):
        disc = DisciplinaRepository.find_by_id(disciplina_id)
        if not disc:
            raise ValueError("Disciplina não encontrada")
        return disc
    
    @staticmethod
    def atualizar_disciplina(disciplina_id, data):
        disc = DisciplinaRepository.find_by_id(disciplina_id)
        if not disc:
            raise ValueError("Disciplina não encontrada")
        
        if 'curso_id' in data:
            curso = CursoRepository.find_by_id(data['curso_id'])
            if not curso:
                raise ValueError("Curso não encontrado")
        
        disc.nome = data.get('nome', disc.nome)
        disc.codigo = data.get('codigo', disc.codigo)
        disc.carga_horaria = data.get('carga_horaria', disc.carga_horaria)
        disc.curso_id = data.get('curso_id', disc.curso_id)
        
        return DisciplinaRepository.update(disc)
    
    @staticmethod
    def excluir_disciplina(disciplina_id):
        disc = DisciplinaRepository.find_by_id(disciplina_id)
        if not disc:
            raise ValueError("Disciplina não encontrada")
        return DisciplinaRepository.delete(disciplina_id)