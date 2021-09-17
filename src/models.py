import datetime

from sqlalchemy import DECIMAL, Column, DateTime, ForeignKey, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class Base(object):
    created_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        nullable=False
    )


DeclarativeBase = declarative_base(cls=Base)


class Usuario(DeclarativeBase):
    __tablename__ = "usuarios"

    id = Column(String, primary_key=True)
    nome = Column(String, nullable=False)
    senha = Column(String, nullable=False)


class Planta(DeclarativeBase):
    __tablename__ = "plantas"

    id = Column(String, primary_key=True)
    especie = Column(String, nullable=False)
    temperatura = Column(String, nullable=False)
    regas = Column(Integer, nullable=False)


class UsuarioPlanta(DeclarativeBase):
    __tablename__ = "usuarios_plantas"

    id = Column(String, primary_key=True)
    id_planta = Column(
        String,
        ForeignKey("plantas.id", name="fk_id_planta_usuarios_plantas"),
        nullable=False
    )
    id_usuario = Column(
        String,
        ForeignKey("usuarios.id", name="fk_id_usuario_usuarios_plantas"),
        nullable=False
    )
    nome = Column(String, nullable=False)
    temperatura_maxima = Column(String, nullable=False)
    umidade_minima = Column(String, nullable=False)
    luminosidade_ideal = Column(String, nullable=False)
    usuario = relationship("Usuario", uselist=False)
    planta = relationship("Planta", uselist=False)
    medicoes = relationship("Medicao")


class Medicao(DeclarativeBase):
    __tablename__ = "medicoes"

    id = Column(String, primary_key=True)
    id_usuario_planta = Column(
        String,
        ForeignKey("usuarios_plantas.id", name="fk_id_usuario_planta_medicoes"),
        nullable=False
    )
    temperatura = Column(String, nullable=False)
    umidade = Column(String, nullable=False)
    luminosidade = Column(String, nullable=False)
