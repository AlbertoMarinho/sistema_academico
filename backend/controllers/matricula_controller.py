from flask import Blueprint, request, jsonify
from services.matricula_service import MatriculaService

matricula_bp = Blueprint('matricula', __name__)

@matricula_bp.route('', methods=['GET'])
def listar_matriculas():
    try:
        matriculas = MatriculaService.listar_matriculas()
        return jsonify(matriculas), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@matricula_bp.route('/aluno/<int:aluno_id>', methods=['GET'])
def listar_matriculas_aluno(aluno_id):
    try:
        matriculas = MatriculaService.listar_matriculas_por_aluno(aluno_id)
        return jsonify(matriculas), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@matricula_bp.route('', methods=['POST'])
def criar_matricula():
    try:
        data = request.get_json()
        matricula = MatriculaService.criar_matricula(data)
        return jsonify(matricula.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@matricula_bp.route('/<int:id>', methods=['DELETE'])
def cancelar_matricula(id):
    try:
        MatriculaService.cancelar_matricula(id)
        return jsonify({'message': 'Matrícula cancelada com sucesso'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500