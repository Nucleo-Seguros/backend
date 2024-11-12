from flask import Blueprint, request, jsonify
from models import Usuario 
from models import db 

usuario_bp = Blueprint('usuarios', __name__)

@usuario_bp.route('/usuario-register', methods=['POST'])
def registrar_usuario():
    data = request.json
    novo_usuario = Usuario(
        usuario_email = data['usuario_email'],
        usuario_nome = data['usuario_nome'], 
        usuario_senha = data['usuario_senha'],
        pergunta_usuario = data['pergunta_usuario'],
        palavra_chave = data['palavra_chave']
                           )
    
    #if novo_usuario.usuario_senha == novo_usuario.usuario_confirmaSenha:
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify({'message': "Usuario cadastrado com sucesso!",
                    'usuario_id': novo_usuario.usuario_id,
                    'usuario_nome': novo_usuario.usuario_nome}), 201
    #else:
        #return jsonify({'error': 'Senhas não conferem'}), 400*/

@usuario_bp.route('/usuario', methods=['GET'])
def listar_usuarios():
    usuarios = Usuario.query.all()
    list_usuarios = [{'usuario_id': usuario.usuario_id, 'usuario_nome': usuario.usuario_nome, 'usuario_email': usuario.usuario_email} for usuario in usuarios]
    return jsonify(list_usuarios)

#Para buscar por email: GET /usuario?email=usuario@example.com
#Para buscar por ID: GET /usuario?id=1
@usuario_bp.route('/usuario-unico', methods=['GET'])
def buscar_usuario_unico():
    email = request.args.get('email')
    nome = request.args.get('nome')
    usuario_id = request.args.get('usuario_id')
    
    if usuario_id:
        usuario = Usuario.query.filter_by(id=id).first()
        return jsonify({'usuario_id': usuario.usuario_id, 'usuario_nome': usuario.usuario_nome, 'usuario_email': usuario.usuario_email})
    elif email:
        usuario = Usuario.query.filter_by(usuario_email=email).first()
        return jsonify({'usuario_id': usuario.usuario_id, 'usuario_nome': usuario.usuario_nome, 'usuario_email': usuario.usuario_email})
    elif nome:
        usuario = Usuario.query.filter_by(usuario_nome=nome).first()
        return jsonify({'usuario_id': usuario.usuario_id, 'usuario_nome': usuario.usuario_nome, 'usuario_email': usuario.usuario_email})
    else:
        return jsonify({'error': 'Parâmetros inválidos'}), 400
    
@usuario_bp.route('/usuario/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    data = request.json
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({'error': 'Usuario não encontrado'}), 404
    
    campos_para_atualizar = [
        'usuario_email', 
        'usuario_nome', 
        'usuario_senha', 
        'pergunta_usuario', 
        'palavra_chave'
    ]

    for campo in campos_para_atualizar:
        if campo in data and data[campo] is not None:
            setattr(usuario, campo, data[campo])
    
    db.session.commit()
    return jsonify({'id': usuario.usuario_id, 'nome': usuario.usuario_nome, 'email': usuario.usuario_email}), 200
    

@usuario_bp.route('/usuario/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    usuario = Usuario.query.get(id)
    
    if not usuario:
        return jsonify({'error': 'Usuario não encontrado'}), 404
    
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'message': 'Usuario deletado com sucesso'}), 204


@usuario_bp.route('/usuario-login', methods=['POST'])
def login():
    data = request.json
    email = data.get('usuario_email')
    senha = data.get('usuario_senha')
    
    # Consulta o banco de dados para obter os usuários diretamente
    usuarios = Usuario.query.all()
    
    for usuario in usuarios:
        if usuario.usuario_email == email and usuario.usuario_senha == senha:
            return jsonify({
                'message': 'Login realizado com sucesso!',
                'usuario_id': usuario.usuario_id,
                'usuario_nome': usuario.usuario_nome
            }), 200
    
    # Se o loop terminar e não encontrar correspondência
    return jsonify({'error': 'Email ou senha inválidos'}), 401
