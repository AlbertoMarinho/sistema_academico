class Aluno:
    """Classe Model para Aluno"""
    
    def __init__(self, id=None, nome=None, cpf=None, email=None, 
                 telefone=None, data_nascimento=None, created_at=None):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.data_nascimento = data_nascimento
        self.created_at = created_at
    
    def to_dict(self):
        """Converte o objeto para dicionário"""
        return {
            'id': self.id,
            'nome': self.nome,
            'cpf': self.cpf,
            'email': self.email,
            'telefone': self.telefone,
            'data_nascimento': self.data_nascimento,
            'created_at': self.created_at
        }
    
    @staticmethod
    def from_dict(data):
        """Cria um objeto Aluno a partir de um dicionário"""
        return Aluno(
            id=data.get('id'),
            nome=data.get('nome'),
            cpf=data.get('cpf'),
            email=data.get('email'),
            telefone=data.get('telefone'),
            data_nascimento=data.get('data_nascimento')
        )
    
    @staticmethod
    def from_db_row(row):
        """Cria um objeto Aluno a partir de uma linha do banco"""
        return Aluno(
            id=row['id'],
            nome=row['nome'],
            cpf=row['cpf'],
            email=row['email'],
            telefone=row['telefone'],
            data_nascimento=row['data_nascimento'],
            created_at=row['created_at']
        )