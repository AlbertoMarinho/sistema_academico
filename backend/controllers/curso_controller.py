from flask import Blueprint, request, jsonify
from services.curso_service import CursoService

curso_bp = Blueprint('curso', __name__)

@curso_bp.route('', methods=['GET'])
def listar_cursos():
    try:
        cursos = CursoService.listar_cursos()
        return jsonify([c.to_dict() for c in cursos]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@curso_bp.route('/<int:id>', methods=['GET'])
def buscar_curso(id):
    try:
        curso = CursoService.buscar_curso(id)
        return jsonify(curso.to_dict()), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@curso_bp.route('', methods=['POST'])
def criar_curso():
    try:
        data = request.get_json()
        curso = CursoService.criar_curso(data)
        return jsonify(curso.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@curso_bp.route('/<int:id>', methods=['PUT'])
def atualizar_curso(id):
    try:
        data = request.get_json()
        curso = CursoService.atualizar_curso(id, data)
        return jsonify(curso.to_dict()), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@curso_bp.route('/<int:id>', methods=['DELETE'])
def excluir_curso(id):
    try:
        CursoService.excluir_curso(id)
        return jsonify({'message': 'Curso excluído com sucesso'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500