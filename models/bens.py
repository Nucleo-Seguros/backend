from sqlalchemy import ForeignKey
from app import db

class Bens(db.Model):
    
    __tablename__ = 'bens'
    
    id_bens = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_beneficiario = db.Column(db.String(36), ForeignKey('beneficarios.id_beneficiario'), nullable=False)
    beneficiario = db.relationship('Beneficiaro', backref='bens')