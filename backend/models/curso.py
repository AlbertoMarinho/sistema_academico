class Curso:
    def __init__(self, id=None, nome=None, codigo=None, carga_horaria=None,
                 descricao=None, created_at=None):
        self.id = id
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria
        self.descricao = descricao
        self.created_at = created_at
    
    def to_dict(self):
        return {
            'id': self.id, 'nome': self.nome, 'codigo': self.codigo,
            'carga_horaria': self.carga_horaria, 'descricao': self.descricao,
            'created_at': self.created_at
        }
    
    @staticmethod
    def from_dict(data):
        return Curso(
            id=data.get('id'), nome=data.get('nome'), codigo=data.get('codigo'),
            carga_horaria=data.get('carga_horaria'), descricao=data.get('descricao')
        )
    
    @staticmethod
    def from_db_row(row):
        return Curso(
            id=row['id'], nome=row['nome'], codigo=row['codigo'],
            carga_horaria=row['carga_horaria'], descricao=row['descricao'],
            created_at=row['created_at']
        )