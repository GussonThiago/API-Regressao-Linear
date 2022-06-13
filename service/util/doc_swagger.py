from flask_restplus import fields
from service.restplus import api

INPUT_MAIN_SERVICE = api.model(
  'input_main_service', {
    'Idade': fields.List(fields.Integer(), required=True, description="idade da pessoa"), 
    'IMC': fields.List(fields.Float(), required=True, description="Índice de massa corporal"),
    'Filhos': fields.List(fields.Integer(), required=True, description="Se possui filhos e quantos"),
    'Fumante': fields.List(fields.Integer(), required=True, description="1 para fumante e 0 para não fumantes"),
    'Sexo': fields.List(fields.Integer(), required=True, description="1 para Mulher e 0 para Homem")
    })
