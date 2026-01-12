from repositories.aluno_repository import AlunoRepository
from models.aluno import Aluno
from utils.validators import validar_cpf, validar_email

class AlunoService:
    """Camada de lógica de negócio para Alunos"""
    
    @staticmethod
    def criar_aluno(data):
        """Cria um novo aluno com validações"""
        if not data.get('nome'):
            raise ValueError("Nome é obrigatório")
        
        if not data.get('cpf'):
            raise ValueError("CPF é obrigatório")
        
        if not validar_cpf(data['cpf']):
            raise ValueError("CPF inválido")
        
        if not data.get('email'):
            raise ValueError("Email é obrigatório")
        
        if not validar_email(data['email']):
            raise ValueError("Email inválido")
        
        aluno_existente = AlunoRepository.find_by_cpf(data['cpf'])
        if aluno_existente:
            raise ValueError("CPF já cadastrado")
        
        aluno = Aluno.from_dict(data)
        return AlunoRepository.create(aluno)
    
    @staticmethod
    def listar_alunos():
        return AlunoRepository.find_all()
    
    @staticmethod
    def buscar_aluno(aluno_id):
        aluno = AlunoRepository.find_by_id(aluno_id)
        if not aluno:
            raise ValueError("Aluno não encontrado")
        return aluno
    
    @staticmethod
    def atualizar_aluno(aluno_id, data):
        aluno = AlunoRepository.find_by_id(aluno_id)
        if not aluno:
            raise ValueError("Aluno não encontrado")
        
        if 'cpf' in data and data['cpf'] != aluno.cpf:
            if not validar_cpf(data['cpf']):
                raise ValueError("CPF inválido")
            
            aluno_existente = AlunoRepository.find_by_cpf(data['cpf'])
            if aluno_existente:
                raise ValueError("CPF já cadastrado")
        
        if 'email' in data and not validar_email(data['email']):
            raise ValueError("Email inválido")
        
        aluno.nome = data.get('nome', aluno.nome)
        aluno.cpf = data.get('cpf', aluno.cpf)
        aluno.email = data.get('email', aluno.email)
        aluno.telefone = data.get('telefone', aluno.telefone)
        aluno.data_nascimento = data.get('data_nascimento', aluno.data_nascimento)
        
        return AlunoRepository.update(aluno)
    
    @staticmethod
    def excluir_aluno(aluno_id):
        aluno = AlunoRepository.find_by_id(aluno_id)
        if not aluno:
            raise ValueError("Aluno não encontrado")
        
        return AlunoRepository.delete(aluno_id)