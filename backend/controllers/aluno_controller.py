from flask import Blueprint, request, jsonify
from services.aluno_service import AlunoService

aluno_bp = Blueprint('aluno', __name__)

@aluno_bp.route('', methods=['GET'])
def listar_alunos():
    try:
        alunos = AlunoService.listar_alunos()
        return jsonify([aluno.to_dict() for aluno in alunos]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@aluno_bp.route('/<int:id>', methods=['GET'])
def buscar_aluno(id):
    try:
        aluno = AlunoService.buscar_aluno(id)
        return jsonify(aluno.to_dict()), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@aluno_bp.route('', methods=['POST'])
def criar_aluno():
    try:
        data = request.get_json()
        aluno = AlunoService.criar_aluno(data)
        return jsonify(aluno.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@aluno_bp.route('/<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    try:
        data = request.get_json()
        aluno = AlunoService.atualizar_aluno(id, data)
        return jsonify(aluno.to_dict()), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@aluno_bp.route('/<int:id>', methods=['DELETE'])
def excluir_aluno(id):
    try:
        AlunoService.excluir_aluno(id)
        return jsonify({'message': 'Aluno excluído com sucesso'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500