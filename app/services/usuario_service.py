from ..models import usuario_model
from app import db


def cadastrar_usuario(usuario):
    usuario_bd = usuario_model.Usuario(nome=usuario.nome, email=usuario.email, senha=usuario.senha)
    usuario_bd.encriptar_senha()
    db.session.add(usuario_bd)
    db.session.commit()
    return usuario_bd


def listar_usuario_email(email):
    return usuario_model.Usuario.query.filter_by(email=email).first()
