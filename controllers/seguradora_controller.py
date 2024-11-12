from flask import Blueprint, request, jsonify
from models import db, Seguradora

seguradora_bp = Blueprint('seguradoras', __name__)

@seguradora_bp.route('/seguradora', methods=['POST'])
def criar_seguradora():
    data = request.json
    nova_seguradora = Seguradora(seguradora_nome = data['seguradora_nome'])
    db.session.add(nova_seguradora)
    db.session.commit()
    return jsonify({'id': nova_seguradora.seguradora_id, 'seguradora_nome': nova_seguradora.seguradora_nome}), 201

@seguradora_bp.route('/seguradora', methods=['GET'])
def listar_seguradoras():
    seguradoras = Seguradora.query.all()
    lista_seguradoras = [{'id': seguradora.seguradora_id, 'nome': seguradora.seguradora_nome} for seguradora in seguradoras]
    return jsonify(lista_seguradoras)

@seguradora_bp.route('/seguradora-unica',methods = ['GET'])
def listar_seguradora():
    id = request.args.get('id')
    nome = request.args.get('nome')
    if id:
       seguradora = Seguradora.query.filter_by(id=id).first() 
       return jsonify(seguradora)
    elif nome:
        seguradora = Seguradora.query.filter_by(seguradora_nome=nome).first()
        return jsonify(seguradora)
    else:
        return jsonify({'error': 'Parâmetros inválidos'}), 400

@seguradora_bp.route('/seguradora/<int:id>', methods=['PUT'])
def atualizar_seguradora(id):
    data = request.json
    seguradora = Seguradora.query.get(id)
    if not seguradora:
        return jsonify({'error': 'Seguradora não encontrado'}), 404
    #Parei aqui
    seguradora.produto_nome = data['produto_nome']
    db.session.commit()
    return jsonify({'id': seguradora.produto_id, 'nome': seguradora.produto_nome}), 200

@seguradora_bp.route('/produtos/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    produto = Produto.query.get(id)
    
    if not produto:
        return jsonify({'error': 'Produto não encontrado'}), 404
    
    db.session.delete(produto)
    db.session.commit()
    return jsonify({'message': 'Produto deletado com sucesso'}), 204