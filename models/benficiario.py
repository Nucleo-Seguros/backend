from app import db


class Beneficiario(db.Model):
    
    __tablename__ = 'beneficiario'
    
    id_beneficiario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_beneficiario = db.Column(db.String(100), nullable=False)
    email_beneficiario = db.Column(db.String(100), nullable=False)
    telefone_beneficiario = db.Column(db.String(20), nullable=False)
    cpf_cnpj = db.Column(db.String(14), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    
        
        
        