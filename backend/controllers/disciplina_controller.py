from flask import Blueprint, request, jsonify
from services.disciplina_service import DisciplinaService

disciplina_bp = Blueprint('disciplina', __name__)

@disciplina_bp.route('', methods=['GET'])
def listar_disciplinas():
    try:
        disciplinas = DisciplinaService.listar_disciplinas()
        return jsonify([d.to_dict() for d in disciplinas]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@disciplina_bp.route('/curso/<int:curso_id>', methods=['GET'])
def listar_disciplinas_por_curso(curso_id):
    try:
        disciplinas = DisciplinaService.listar_disciplinas_por_curso(curso_id)
        return jsonify([d.to_dict() for d in disciplinas]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@disciplina_bp.route('/<int:id>', methods=['GET'])
def buscar_disciplina(id):
    try:
        disciplina = DisciplinaService.buscar_disciplina(id)
        return jsonify(disciplina.to_dict()), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@disciplina_bp.route('', methods=['POST'])
def criar_disciplina():
    try:
        data = request.get_json()
        disciplina = DisciplinaService.criar_disciplina(data)
        return jsonify(disciplina.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@disciplina_bp.route('/<int:id>', methods=['PUT'])
def atualizar_disciplina(id):
    try:
        data = request.get_json()
        disciplina = DisciplinaService.atualizar_disciplina(id, data)
        return jsonify(disciplina.to_dict()), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@disciplina_bp.route('/<int:id>', methods=['DELETE'])
def excluir_disciplina(id):
    try:
        DisciplinaService.excluir_disciplina(id)
        return jsonify({'message': 'Disciplina excluída com sucesso'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500