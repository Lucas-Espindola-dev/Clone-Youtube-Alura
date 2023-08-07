from app import ma
from ..models import categoria_model
from marshmallow import fields
from ..schemas import video_schema


class CategoriaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = categoria_model.Categoria
        load_instance = True
        fields = ('id', 'titulo', 'cor', 'videos')

    titulo = fields.String(required=True)
    cor = fields.String(required=True)
    videos = fields.List(fields.Nested(video_schema.VideoSchema, only=('titulo', 'url')))
