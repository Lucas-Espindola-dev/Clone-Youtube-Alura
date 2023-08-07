from app import db


class Categoria(db.Model):
    __tablename__ = 'categoria'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    titulo = db.Column(db.String(50), nullable=False)
    cor = db.Column(db.String(50), nullable=False)
