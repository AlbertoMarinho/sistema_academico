class Turma:
    def __init__(self, id=None, codigo=None, disciplina_id=None, professor_id=None,
                 periodo=None, ano=None, vagas=30, created_at=None):
        self.id = id
        self.codigo = codigo
        self.disciplina_id = disciplina_id
        self.professor_id = professor_id
        self.periodo = periodo
        self.ano = ano
        self.vagas = vagas
        self.created_at = created_at
    
    def to_dict(self):
        return {
            'id': self.id, 'codigo': self.codigo,
            'disciplina_id': self.disciplina_id, 'professor_id': self.professor_id,
            'periodo': self.periodo, 'ano': self.ano, 'vagas': self.vagas,
            'created_at': self.created_at
        }
    
    @staticmethod
    def from_dict(data):
        return Turma(
            id=data.get('id'), codigo=data.get('codigo'),
            disciplina_id=data.get('disciplina_id'), professor_id=data.get('professor_id'),
            periodo=data.get('periodo'), ano=data.get('ano'), vagas=data.get('vagas', 30)
        )
    
    @staticmethod
    def from_db_row(row):
        return Turma(
            id=row['id'], codigo=row['codigo'],
            disciplina_id=row['disciplina_id'], professor_id=row['professor_id'],
            periodo=row['periodo'], ano=row['ano'], vagas=row['vagas'],
            created_at=row['created_at']
        )