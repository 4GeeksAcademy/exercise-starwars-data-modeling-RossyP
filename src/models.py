import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Favorito(Base):
    __tablename__= "favorito"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    personaje_id = Column(Integer, ForeignKey("personaje.id"), nullable=False)
    planeta_id = Column(Integer, ForeignKey("planeta.id"), nullable=False)
    especie_id = Column(Integer, ForeignKey("especie.id"), nullable=False)
    usuarios = relationship("Usuario", backref="favorito", lazy=True)
    personajes = relationship('Personaje', backref='favorito', lazy=True)
    planetas = relationship("Planeta", backref="favorito", lazy=True)
    especies = relationship("Especie", backref="favorito", lazy=True)

class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(120), nullable=False)
    # favorito_id = Column(Integer, ForeignKey('favorito.id'), nullable=False)
    favoritos = relationship("Favorito", backref="usuario", lazy=True)

class Personaje(Base):
    __tablename__ = "personaje"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    planetas = relationship("Planeta", backref="planeta")
    especies = relationship("Especie", backref="especie")
    especie_id = Column(Integer, ForeignKey('especie.id'))
    planeta_id = Column(Integer, ForeignKey('planeta.id'))
    favorito_id = Column(Integer, ForeignKey('favorito.id'), nullable=False)



class Planeta(Base):
    __tablename__="planeta"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    clima = Column(String(100), nullable=False)
    favorito_id = Column(Integer, ForeignKey('favorito.id'), nullable=False)
    # personaje_id = Column(Integer, ForeignKey('personaje.id'), nullable=False)

class Especie(Base):
    __tablename__="especie"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    # planeta = Column(String(100), nullable=False)
    favorito_id = Column(Integer, ForeignKey('favorito.id'), nullable=False)
    personaje_id = Column(Integer, ForeignKey('personaje.id'), nullable=False)
    planeta = relationship("Planeta", backref="especies", lazy=True)

# -----
# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
