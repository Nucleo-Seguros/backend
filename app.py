from flask import Flask
from models import db
from config import Config
from controllers import usuario_bp
from flask import Flask
from flask_cors import CORS


def criar_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)

    db.init_app(app)
   
    with app.app_context():
        db.create_all()
    
    app.register_blueprint(usuario_bp)
    
    app.run(debug=True)


if __name__ == '__main__':
    app = criar_app()