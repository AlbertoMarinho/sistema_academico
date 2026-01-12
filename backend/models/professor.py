class Professor:
    def __init__(self, id=None, nome=None, cpf=None, email=None, 
                 telefone=None, especializacao=None, created_at=None):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.especializacao = especializacao
        self.created_at = created_at
    
    def to_dict(self):
        return {
            'id': self.id, 'nome': self.nome, 'cpf': self.cpf,
            'email': self.email, 'telefone': self.telefone,
            'especializacao': self.especializacao, 'created_at': self.created_at
        }
    
    @staticmethod
    def from_dict(data):
        return Professor(
            id=data.get('id'), nome=data.get('nome'), cpf=data.get('cpf'),
            email=data.get('email'), telefone=data.get('telefone'),
            especializacao=data.get('especializacao')
        )
    
    @staticmethod
    def from_db_row(row):
        return Professor(
            id=row['id'], nome=row['nome'], cpf=row['cpf'],
            email=row['email'], telefone=row['telefone'],
            especializacao=row['especializacao'], created_at=row['created_at']
        )