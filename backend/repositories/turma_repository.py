from database.db_connection import get_connection
from models.turma import Turma

class TurmaRepository:
    @staticmethod
    def create(turma):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO turmas (codigo, disciplina_id, professor_id, periodo, ano, vagas)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (turma.codigo, turma.disciplina_id, turma.professor_id,
              turma.periodo, turma.ano, turma.vagas))
        turma.id = cursor.lastrowid
        conn.commit()
        conn.close()
        return turma
    
    @staticmethod
    def find_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT t.*, d.nome as disciplina_nome, p.nome as professor_nome
            FROM turmas t
            JOIN disciplinas d ON t.disciplina_id = d.id
            JOIN professores p ON t.professor_id = p.id
            ORDER BY t.ano DESC, t.periodo
        ''')
        rows = cursor.fetchall()
        conn.close()
        
        turmas = []
        for row in rows:
            turma = Turma.from_db_row(row)
            turma_dict = turma.to_dict()
            turma_dict['disciplina_nome'] = row['disciplina_nome']
            turma_dict['professor_nome'] = row['professor_nome']
            turmas.append(turma_dict)
        return turmas
    
    @staticmethod
    def find_by_id(turma_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM turmas WHERE id = ?', (turma_id,))
        row = cursor.fetchone()
        conn.close()
        return Turma.from_db_row(row) if row else None
    
    @staticmethod
    def update(turma):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE turmas 
            SET codigo = ?, disciplina_id = ?, professor_id = ?, 
                periodo = ?, ano = ?, vagas = ?
            WHERE id = ?
        ''', (turma.codigo, turma.disciplina_id, turma.professor_id,
              turma.periodo, turma.ano, turma.vagas, turma.id))
        conn.commit()
        conn.close()
        return turma
    
    @staticmethod
    def delete(turma_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM turmas WHERE id = ?', (turma_id,))
        deleted = cursor.rowcount > 0
        conn.commit()
        conn.close()
        return deleted