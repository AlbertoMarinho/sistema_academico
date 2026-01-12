class Disciplina:
    def __init__(self, id=None, nome=None, codigo=None, carga_horaria=None,
                 curso_id=None, created_at=None):
        self.id = id
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria
        self.curso_id = curso_id
        self.created_at = created_at
    
    def to_dict(self):
        return {
            'id': self.id, 'nome': self.nome, 'codigo': self.codigo,
            'carga_horaria': self.carga_horaria, 'curso_id': self.curso_id,
            'created_at': self.created_at
        }
    
    @staticmethod
    def from_dict(data):
        return Disciplina(
            id=data.get('id'), nome=data.get('nome'), codigo=data.get('codigo'),
            carga_horaria=data.get('carga_horaria'), curso_id=data.get('curso_id')
        )
    
    @staticmethod
    def from_db_row(row):
        return Disciplina(
            id=row['id'], nome=row['nome'], codigo=row['codigo'],
            carga_horaria=row['carga_horaria'], curso_id=row['curso_id'],
            created_at=row['created_at']
        )