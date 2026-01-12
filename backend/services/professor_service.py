from repositories.professor_repository import ProfessorRepository
from models.professor import Professor
from utils.validators import validar_cpf, validar_email

class ProfessorService:
    @staticmethod
    def criar_professor(data):
        if not data.get('nome'):
            raise ValueError("Nome é obrigatório")
        if not data.get('cpf') or not validar_cpf(data['cpf']):
            raise ValueError("CPF inválido")
        if not data.get('email') or not validar_email(data['email']):
            raise ValueError("Email inválido")
        
        if ProfessorRepository.find_by_cpf(data['cpf']):
            raise ValueError("CPF já cadastrado")
        
        return ProfessorRepository.create(Professor.from_dict(data))
    
    @staticmethod
    def listar_professores():
        return ProfessorRepository.find_all()
    
    @staticmethod
    def buscar_professor(professor_id):
        prof = ProfessorRepository.find_by_id(professor_id)
        if not prof:
            raise ValueError("Professor não encontrado")
        return prof
    
    @staticmethod
    def atualizar_professor(professor_id, data):
        prof = ProfessorRepository.find_by_id(professor_id)
        if not prof:
            raise ValueError("Professor não encontrado")
        
        if 'cpf' in data and data['cpf'] != prof.cpf:
            if not validar_cpf(data['cpf']):
                raise ValueError("CPF inválido")
            if ProfessorRepository.find_by_cpf(data['cpf']):
                raise ValueError("CPF já cadastrado")
        
        if 'email' in data and not validar_email(data['email']):
            raise ValueError("Email inválido")
        
        prof.nome = data.get('nome', prof.nome)
        prof.cpf = data.get('cpf', prof.cpf)
        prof.email = data.get('email', prof.email)
        prof.telefone = data.get('telefone', prof.telefone)
        prof.especializacao = data.get('especializacao', prof.especializacao)
        
        return ProfessorRepository.update(prof)
    
    @staticmethod
    def excluir_professor(professor_id):
        prof = ProfessorRepository.find_by_id(professor_id)
        if not prof:
            raise ValueError("Professor não encontrado")
        return ProfessorRepository.delete(professor_id)