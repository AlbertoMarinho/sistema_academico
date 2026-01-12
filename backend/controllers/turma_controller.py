from flask import Blueprint, request, jsonify
from services.turma_service import TurmaService
from services.matricula_service import MatriculaService

turma_bp = Blueprint('turma', __name__)

@turma_bp.route('', methods=['GET'])
def listar_turmas():
    try:
        turmas = TurmaService.listar_turmas()
        return jsonify(turmas), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@turma_bp.route('/<int:id>', methods=['GET'])
def buscar_turma(id):
    try:
        turma = TurmaService.buscar_turma(id)
        return jsonify(turma.to_dict()), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@turma_bp.route('/<int:id>/alunos', methods=['GET'])
def listar_alunos_turma(id):
    try:
        alunos = MatriculaService.listar_alunos_por_turma(id)
        return jsonify(alunos), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@turma_bp.route('', methods=['POST'])
def criar_turma():
    try:
        data = request.get_json()
        turma = TurmaService.criar_turma(data)
        return jsonify(turma.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@turma_bp.route('/<int:id>', methods=['PUT'])
def atualizar_turma(id):
    try:
        data = request.get_json()
        turma = TurmaService.atualizar_turma(id, data)
        return jsonify(turma.to_dict()), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@turma_bp.route('/<int:id>', methods=['DELETE'])
def excluir_turma(id):
    try:
        TurmaService.excluir_turma(id)
        return jsonify({'message': 'Turma excluída com sucesso'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500