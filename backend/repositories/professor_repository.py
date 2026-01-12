from database.db_connection import get_connection
from models.professor import Professor

class ProfessorRepository:
    @staticmethod
    def create(professor):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO professores (nome, cpf, email, telefone, especializacao)
            VALUES (?, ?, ?, ?, ?)
        ''', (professor.nome, professor.cpf, professor.email, 
              professor.telefone, professor.especializacao))
        professor.id = cursor.lastrowid
        conn.commit()
        conn.close()
        return professor
    
    @staticmethod
    def find_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM professores ORDER BY nome')
        rows = cursor.fetchall()
        conn.close()
        return [Professor.from_db_row(row) for row in rows]
    
    @staticmethod
    def find_by_id(professor_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM professores WHERE id = ?', (professor_id,))
        row = cursor.fetchone()
        conn.close()
        return Professor.from_db_row(row) if row else None
    
    @staticmethod
    def find_by_cpf(cpf):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM professores WHERE cpf = ?', (cpf,))
        row = cursor.fetchone()
        conn.close()
        return Professor.from_db_row(row) if row else None
    
    @staticmethod
    def update(professor):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE professores 
            SET nome = ?, cpf = ?, email = ?, telefone = ?, especializacao = ?
            WHERE id = ?
        ''', (professor.nome, professor.cpf, professor.email, 
              professor.telefone, professor.especializacao, professor.id))
        conn.commit()
        conn.close()
        return professor
    
    @staticmethod
    def delete(professor_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM professores WHERE id = ?', (professor_id,))
        deleted = cursor.rowcount > 0
        conn.commit()
        conn.close()
        return deleted