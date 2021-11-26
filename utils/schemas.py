from marshmallow import Schema, fields


class UsuarioSchema(Schema):
    __tablename__ = "usuarios"

    id = fields.Str(required=True)
    nome = fields.Str(required=True)
    senha = fields.Str(required=True)
    premium = fields.Bool(required=True)


class PlantaSchema(Schema):
    __tablename__ = "plantas"

    id = fields.Str(required=True)
    descricao = fields.Str(required=True)
    especie = fields.Str(required=True)
    temperatura_maxima = fields.Str(required=True)
    temperatura_minima = fields.Str(required=True)
    temperatura_ideal = fields.Str(required=True)
    umidade_solo_ideal = fields.Str(required=True)
    umidade_ar_ideal = fields.Str(required=True)
    luminosidade_ideal = fields.Str(required=True)
    regas = fields.Integer(required=True)
    preco = fields.Decimal(required=True, as_string=True)


class MedicaoSchema(Schema):
    __tablename__ = "usuarios"

    id = fields.Str(required=True)
    id_usuario_planta = fields.Str(required=True)
    temperatura = fields.Str(required=True)
    umidade_solo = fields.Str(required=True)
    umidade_ar = fields.Str(required=True)
    luminosidade = fields.Str(required=True)
    created_at = fields.Str(required=True)


class UsuarioPlantaSchema(Schema):
    __tablename__ = "usuarios_plantas"

    id = fields.Str(required=True)
    id_planta = fields.Str(required=True)
    id_usuario = fields.Str(required=True)
    nome = fields.Str(required=True)
    temperatura_maxima = fields.Str(required=True)
    temperatura_minima = fields.Str(required=True)
    temperatura_ideal = fields.Str(required=True)
    umidade_ideal = fields.Str(required=True)
    luminosidade_ideal = fields.Str(required=True)
    regas = fields.Int(required=True)
    usuario = fields.Nested(UsuarioSchema)
    planta = fields.Nested(PlantaSchema)
    medicoes = fields.Nested(MedicaoSchema, many=True)


class SolicitacoesRegaSchema(Schema):
    __tablename__ = "solicitacoes_rega"

    id = fields.Str(required=True)
    id_usuario_planta = fields.Str(required=True)
    hora = fields.Str(required=True)
    completo = fields.Bool(required=True)