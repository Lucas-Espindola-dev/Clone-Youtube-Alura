from flask_restful import Resource
from app import api
from ..schemas import video_schema
from flask import request, make_response, jsonify
from ..entidades import video
from ..services import video_service, categoria_service
from ..paginate import paginate
from ..models.video_model import Video
from flask_jwt_extended import jwt_required


class VideosList(Resource):
    @jwt_required()
    def get(self):
        vs = video_schema.VideoSchema(many=True)
        return paginate(Video, vs)

    @jwt_required()
    def post(self):
        vs = video_schema.VideoSchema()
        validate = vs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            titulo = request.json['titulo']
            descricao = request.json['descricao']
            url = request.json['url']
            categoria = request.json['categoria']
            categoria_video = categoria_service.listar_categoria_id(categoria)
            if categoria_video is None:
                return make_response(jsonify('Categoria não encontrada!'), 404)

            novo_video = video.Video(titulo=titulo, descricao=descricao,
                                     url=url, categoria=categoria_video)
            resultado = video_service.cadastrar_video(novo_video)
            x = vs.jsonify(resultado)
            return make_response(x, 201)


class VideoDetail(Resource):
    @jwt_required()
    def get(self, id):
        video = video_service.listar_videos_id(id)
        if video is None:
            return make_response(jsonify('Vídeo não foi encontrado!'), 404)
        vs = video_schema.VideoSchema()
        return make_response(vs.jsonify(video), 200)

    @jwt_required()
    def put(self, id):
        video_bd = video_service.listar_videos_id(id)
        if video_bd is None:
            return make_response(jsonify('Vídeo não foi encontrado!'), 404)
        vs = video_schema.VideoSchema()
        validate = vs.validate(request.json)
        if validate:
            make_response(jsonify(validate), 400)
        else:
            titulo = request.json['titulo']
            descricao = request.json['descricao']
            url = request.json['url']
            categoria = request.json['categoria']
            categoria_video = categoria_service.listar_categoria_id(categoria)
            if categoria_video is None:
                return make_response(jsonify('Categoria não encontrada!'), 404)
            novo_video = video.Video(titulo=titulo, descricao=descricao,
                                     url=url, categoria=categoria_video)
            video_service.atualiza_video(video_bd, novo_video)
            video_atualizado = video_service.listar_videos_id(id)
            return make_response(vs.jsonify(video_atualizado), 200)

    @jwt_required()
    def delete(self, id):
        video_bd = video_service.listar_videos_id(id)
        if video_bd is None:
            return make_response(jsonify('Vídeo não encontrado!'), 404)
        video_service.remove_video(video_bd)
        return make_response(jsonify('Vídeo excluido com sucesso!'), 204)


api.add_resource(VideosList, '/videos')
api.add_resource(VideoDetail, '/videos/<int:id>')
