from database.db_connection import get_connection
from models.curso import Curso

class CursoRepository:
    @staticmethod
    def create(curso):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO cursos (nome, codigo, carga_horaria, descricao)
            VALUES (?, ?, ?, ?)
        ''', (curso.nome, curso.codigo, curso.carga_horaria, curso.descricao))
        curso.id = cursor.lastrowid
        conn.commit()
        conn.close()
        return curso
    
    @staticmethod
    def find_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM cursos ORDER BY nome')
        rows = cursor.fetchall()
        conn.close()
        return [Curso.from_db_row(row) for row in rows]
    
    @staticmethod
    def find_by_id(curso_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM cursos WHERE id = ?', (curso_id,))
        row = cursor.fetchone()
        conn.close()
        return Curso.from_db_row(row) if row else None
    
    @staticmethod
    def update(curso):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE cursos 
            SET nome = ?, codigo = ?, carga_horaria = ?, descricao = ?
            WHERE id = ?
        ''', (curso.nome, curso.codigo, curso.carga_horaria, 
              curso.descricao, curso.id))
        conn.commit()
        conn.close()
        return curso
    
    @staticmethod
    def delete(curso_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM cursos WHERE id = ?', (curso_id,))
        deleted = cursor.rowcount > 0
        conn.commit()
        conn.close()
        return deleted