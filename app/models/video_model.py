from app import db
from ..models import categoria_model


class Video(db.Model):
    __tablename__ = 'video'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    titulo = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(50), nullable=False)

    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))
    categoria = db.relationship(categoria_model.Categoria, backref=db.backref("videos", lazy='dynamic'))
