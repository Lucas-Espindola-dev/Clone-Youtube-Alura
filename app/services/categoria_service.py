from ..models import categoria_model
from app import db


def cadastrar_categoria(categoria):
    categoria_bd = categoria_model.Categoria(titulo=categoria.titulo, cor=categoria.cor)
    db.session.add(categoria_bd)
    db.session.commit()
    return categoria_bd


def listar_categorias():
    categorias = categoria_model.Categoria.query.all()
    return categorias


def listar_categoria_id(id):
    categoria = categoria_model.Categoria.query.filter_by(id=id).first()
    return categoria


def atualiza_categoria(categoria_anterior, nova_categoria):
    categoria_anterior.titulo = nova_categoria.titulo
    categoria_anterior.descricao = nova_categoria.descricao
    categoria_anterior.url = nova_categoria.url
    db.session.commit()


def remove_categoria(categoria):
    db.session.delete(categoria)
    db.session.commit()
