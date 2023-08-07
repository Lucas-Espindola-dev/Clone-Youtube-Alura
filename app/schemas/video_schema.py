from app import ma
from ..models import video_model
from marshmallow import fields


class VideoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = video_model.Video
        load_instance = True
        fields = ('id', 'titulo', 'descricao', 'url', 'categoria')

    titulo = fields.String(required=True)
    descricao = fields.String(required=True)
    url = fields.String(required=True)
    categoria = fields.String(required=True)
