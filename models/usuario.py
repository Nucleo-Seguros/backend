from . import db

class Usuario(db.Model):
    
    __tablename__ = 'usuarios'
    
    usuario_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_email = db.Column(db.String(100), nullable=False)
    usuario_nome = db.Column(db.String(100), nullable=False)
    usuario_senha = db.Column(db.String(20), nullable=False)
    pergunta_usuario = db.Column(db.String(200), nullable=False)
    palavra_chave = db.Column(db.String(100), nullable=False)
    
    
   