from flask_restful import Resource
from app import api
from ..schemas import categoria_schema
from flask import request, make_response, jsonify
from ..entidades import categoria
from ..services import categoria_service


class CategoriasList(Resource):
    def get(self):
        categorias = categoria_service.listar_categorias()
        cs = categoria_schema.CategoriaSchema(many=True)
        return make_response(cs.jsonify(categorias), 200)

    def post(self):
        cs = categoria_schema.CategoriaSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            titulo = request.json['titulo']
            cor = request.json['cor']

            nova_categoria = categoria.Categoria(titulo=titulo, cor=cor)
            resultado = categoria_service.cadastrar_categoria(nova_categoria)
            x = cs.jsonify(resultado)
            return make_response(x, 201)


class CategoriaDetail(Resource):
    def get(self, id):
        categoria = categoria_service.listar_categoria_id(id)
        if categoria is None:
            return make_response(jsonify('Categoria não encontrada!'), 404)
        cs = categoria_schema.CategoriaSchema()
        return make_response(cs.jsonify(categoria), 200)

    def put(self, id):
        categoria_bd = categoria_service.listar_categoria_id(id)
        if categoria_bd is None:
            return make_response(jsonify('Categoria não foi encontrada!'), 404)
        cs = categoria_schema.CategoriaSchema()
        validate = cs.validate(request.json)
        if validate:
            make_response(jsonify(validate), 400)
        else:
            titulo = request.json['titulo']
            cor = request.json['cor']
            nova_categoria = categoria.Categoria(titulo=titulo, cor=cor)
            categoria_service.atualiza_categoria(categoria_bd, nova_categoria)
            video_atualizado = categoria_service.listar_categoria_id(id)
            return make_response(cs.jsonify(video_atualizado), 200)

    def delete(self, id):
        categoria_bd = categoria_service.listar_categoria_id(id)
        if categoria_bd is None:
            return make_response(jsonify('Categoria não encontrada!'), 404)
        categoria_service.remove_categoria(categoria_bd)
        return make_response(jsonify('Categoria excluida com sucesso!'), 204)


api.add_resource(CategoriasList, '/categorias')
api.add_resource(CategoriaDetail, '/categorias/<int:id>')
