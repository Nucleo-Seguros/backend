from app import db

class Seguradora(db.Model):
    __tablename__ = 'seguradoras'
    
    seguradora_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    seguradora_nome = db.Column(db.String(100), nullable=False)
    