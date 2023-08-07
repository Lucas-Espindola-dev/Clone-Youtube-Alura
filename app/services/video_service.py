from ..models import video_model
from app import db


def cadastrar_video(video):
    video_bd = video_model.Video(titulo=video.titulo, descricao=video.descricao,
                                 url=video.url, categoria=video.categoria)
    db.session.add(video_bd)
    db.session.commit()
    return video_bd


def listar_videos():
    videos = video_model.Video.query.all()
    return videos


def listar_videos_id(id):
    video = video_model.Video.query.filter_by(id=id).first()
    return video


def atualiza_video(video_anterior, novo_video):
    video_anterior.titulo = novo_video.titulo
    video_anterior.descricao = novo_video.descricao
    video_anterior.url = novo_video.url
    video_anterior.categoria = novo_video.categoria
    db.session.commit()


def remove_video(video):
    db.session.delete(video)
    db.session.commit()
