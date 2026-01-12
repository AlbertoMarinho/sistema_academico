from repositories.curso_repository import CursoRepository
from models.curso import Curso

class CursoService:
    @staticmethod
    def criar_curso(data):
        if not data.get('nome'):
            raise ValueError("Nome é obrigatório")
        if not data.get('codigo'):
            raise ValueError("Código é obrigatório")
        if not data.get('carga_horaria'):
            raise ValueError("Carga horária é obrigatória")
        
        return CursoRepository.create(Curso.from_dict(data))
    
    @staticmethod
    def listar_cursos():
        return CursoRepository.find_all()
    
    @staticmethod
    def buscar_curso(curso_id):
        curso = CursoRepository.find_by_id(curso_id)
        if not curso:
            raise ValueError("Curso não encontrado")
        return curso
    
    @staticmethod
    def atualizar_curso(curso_id, data):
        curso = CursoRepository.find_by_id(curso_id)
        if not curso:
            raise ValueError("Curso não encontrado")
        
        curso.nome = data.get('nome', curso.nome)
        curso.codigo = data.get('codigo', curso.codigo)
        curso.carga_horaria = data.get('carga_horaria', curso.carga_horaria)
        curso.descricao = data.get('descricao', curso.descricao)
        
        return CursoRepository.update(curso)
    
    @staticmethod
    def excluir_curso(curso_id):
        curso = CursoRepository.find_by_id(curso_id)
        if not curso:
            raise ValueError("Curso não encontrado")
        return CursoRepository.delete(curso_id)