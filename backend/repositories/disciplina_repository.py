from database.db_connection import get_connection
from models.disciplina import Disciplina

class DisciplinaRepository:
    @staticmethod
    def create(disciplina):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO disciplinas (nome, codigo, carga_horaria, curso_id)
            VALUES (?, ?, ?, ?)
        ''', (disciplina.nome, disciplina.codigo, 
              disciplina.carga_horaria, disciplina.curso_id))
        disciplina.id = cursor.lastrowid
        conn.commit()
        conn.close()
        return disciplina
    
    @staticmethod
    def find_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM disciplinas ORDER BY nome')
        rows = cursor.fetchall()
        conn.close()
        return [Disciplina.from_db_row(row) for row in rows]
    
    @staticmethod
    def find_by_id(disciplina_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM disciplinas WHERE id = ?', (disciplina_id,))
        row = cursor.fetchone()
        conn.close()
        return Disciplina.from_db_row(row) if row else None
    
    @staticmethod
    def find_by_curso(curso_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM disciplinas WHERE curso_id = ?', (curso_id,))
        rows = cursor.fetchall()
        conn.close()
        return [Disciplina.from_db_row(row) for row in rows]
    
    @staticmethod
    def update(disciplina):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE disciplinas 
            SET nome = ?, codigo = ?, carga_horaria = ?, curso_id = ?
            WHERE id = ?
        ''', (disciplina.nome, disciplina.codigo, disciplina.carga_horaria,
              disciplina.curso_id, disciplina.id))
        conn.commit()
        conn.close()
        return disciplina
    
    @staticmethod
    def delete(disciplina_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM disciplinas WHERE id = ?', (disciplina_id,))
        deleted = cursor.rowcount > 0
        conn.commit()
        conn.close()
        return deleted