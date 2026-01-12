from database.db_connection import get_connection
from models.matricula import Matricula

class MatriculaRepository:
    @staticmethod
    def create(matricula):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO matriculas (aluno_id, turma_id, status)
            VALUES (?, ?, ?)
        ''', (matricula.aluno_id, matricula.turma_id, matricula.status))
        matricula.id = cursor.lastrowid
        conn.commit()
        conn.close()
        return matricula
    
    @staticmethod
    def find_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT m.*, a.nome as aluno_nome, t.codigo as turma_codigo
            FROM matriculas m
            JOIN alunos a ON m.aluno_id = a.id
            JOIN turmas t ON m.turma_id = t.id
            ORDER BY m.data_matricula DESC
        ''')
        rows = cursor.fetchall()
        conn.close()
        
        matriculas = []
        for row in rows:
            m = Matricula.from_db_row(row)
            m_dict = m.to_dict()
            m_dict['aluno_nome'] = row['aluno_nome']
            m_dict['turma_codigo'] = row['turma_codigo']
            matriculas.append(m_dict)
        return matriculas
    
    @staticmethod
    def find_by_aluno(aluno_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT m.*, t.codigo as turma_codigo, d.nome as disciplina_nome
            FROM matriculas m
            JOIN turmas t ON m.turma_id = t.id
            JOIN disciplinas d ON t.disciplina_id = d.id
            WHERE m.aluno_id = ?
        ''', (aluno_id,))
        rows = cursor.fetchall()
        conn.close()
        
        matriculas = []
        for row in rows:
            m = Matricula.from_db_row(row)
            m_dict = m.to_dict()
            m_dict['turma_codigo'] = row['turma_codigo']
            m_dict['disciplina_nome'] = row['disciplina_nome']
            matriculas.append(m_dict)
        return matriculas
    
    @staticmethod
    def find_by_turma(turma_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT m.*, a.nome as aluno_nome, a.email as aluno_email
            FROM matriculas m
            JOIN alunos a ON m.aluno_id = a.id
            WHERE m.turma_id = ? AND m.status = 'ativa'
        ''', (turma_id,))
        rows = cursor.fetchall()
        conn.close()
        
        alunos = []
        for row in rows:
            alunos.append({
                'matricula_id': row['id'],
                'aluno_id': row['aluno_id'],
                'aluno_nome': row['aluno_nome'],
                'aluno_email': row['aluno_email'],
                'data_matricula': row['data_matricula']
            })
        return alunos
    
    @staticmethod
    def delete(matricula_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM matriculas WHERE id = ?', (matricula_id,))
        deleted = cursor.rowcount > 0
        conn.commit()
        conn.close()
        return deleted
    
    @staticmethod
    def existe_matricula(aluno_id, turma_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id FROM matriculas 
            WHERE aluno_id = ? AND turma_id = ? AND status = 'ativa'
        ''', (aluno_id, turma_id))
        row = cursor.fetchone()
        conn.close()
        return row is not None