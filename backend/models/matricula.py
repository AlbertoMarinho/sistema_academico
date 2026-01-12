class Matricula:
    def __init__(self, id=None, aluno_id=None, turma_id=None,
                 data_matricula=None, status='ativa'):
        self.id = id
        self.aluno_id = aluno_id
        self.turma_id = turma_id
        self.data_matricula = data_matricula
        self.status = status
    
    def to_dict(self):
        return {
            'id': self.id, 'aluno_id': self.aluno_id, 'turma_id': self.turma_id,
            'data_matricula': self.data_matricula, 'status': self.status
        }
    
    @staticmethod
    def from_dict(data):
        return Matricula(
            id=data.get('id'), aluno_id=data.get('aluno_id'),
            turma_id=data.get('turma_id'), status=data.get('status', 'ativa')
        )
    
    @staticmethod
    def from_db_row(row):
        return Matricula(
            id=row['id'], aluno_id=row['aluno_id'], turma_id=row['turma_id'],
            data_matricula=row['data_matricula'], status=row['status']
        )