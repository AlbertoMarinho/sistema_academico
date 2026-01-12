from flask import Blueprint, request, jsonify
from services.professor_service import ProfessorService

professor_bp = Blueprint('professor', __name__)

@professor_bp.route('', methods=['GET'])
def listar_professores():
    try:
        professores = ProfessorService.listar_professores()
        return jsonify([p.to_dict() for p in professores]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@professor_bp.route('/<int:id>', methods=['GET'])
def buscar_professor(id):
    try:
        professor = ProfessorService.buscar_professor(id)
        return jsonify(professor.to_dict()), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@professor_bp.route('', methods=['POST'])
def criar_professor():
    try:
        data = request.get_json()
        professor = ProfessorService.criar_professor(data)
        return jsonify(professor.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@professor_bp.route('/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    try:
        data = request.get_json()
        professor = ProfessorService.atualizar_professor(id, data)
        return jsonify(professor.to_dict()), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@professor_bp.route('/<int:id>', methods=['DELETE'])
def excluir_professor(id):
    try:
        ProfessorService.excluir_professor(id)
        return jsonify({'message': 'Professor excluído com sucesso'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500