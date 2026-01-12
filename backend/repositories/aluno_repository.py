from database.db_connection import get_connection
from models.aluno import Aluno

class AlunoRepository:
    """Camada de acesso a dados para Alunos"""
    
    @staticmethod
    def create(aluno):
        """Cria um novo aluno no banco"""
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO alunos (nome, cpf, email, telefone, data_nascimento)
            VALUES (?, ?, ?, ?, ?)
        ''', (aluno.nome, aluno.cpf, aluno.email, aluno.telefone, aluno.data_nascimento))
        
        aluno.id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return aluno
    
    @staticmethod
    def find_all():
        """Retorna todos os alunos"""
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM alunos ORDER BY nome')
        rows = cursor.fetchall()
        conn.close()
        
        return [Aluno.from_db_row(row) for row in rows]
    
    @staticmethod
    def find_by_id(aluno_id):
        """Busca um aluno por ID"""
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM alunos WHERE id = ?', (aluno_id,))
        row = cursor.fetchone()
        conn.close()
        
        return Aluno.from_db_row(row) if row else None
    
    @staticmethod
    def find_by_cpf(cpf):
        """Busca um aluno por CPF"""
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM alunos WHERE cpf = ?', (cpf,))
        row = cursor.fetchone()
        conn.close()
        
        return Aluno.from_db_row(row) if row else None
    
    @staticmethod
    def update(aluno):
        """Atualiza um aluno existente"""
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE alunos 
            SET nome = ?, cpf = ?, email = ?, telefone = ?, data_nascimento = ?
            WHERE id = ?
        ''', (aluno.nome, aluno.cpf, aluno.email, aluno.telefone, 
              aluno.data_nascimento, aluno.id))
        
        conn.commit()
        conn.close()
        
        return aluno
    
    @staticmethod
    def delete(aluno_id):
        """Deleta um aluno"""
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM alunos WHERE id = ?', (aluno_id,))
        deleted = cursor.rowcount > 0
        
        conn.commit()
        conn.close()
        
        return deleted