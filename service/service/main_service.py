import time
import json
from loguru import logger
from service.constants import mensagens
import pandas as pd

import pickle


class RegressaoService():

    def __init__(self):
        logger.debug(mensagens.INICIO_LOAD_SERVICO)
        self.load_model()

    def load_model(self):
        """"
        Carrega o modelo de regressão a ser usado
        """

        self.model = pickle.load(open('./service/Models/regressao_linear.pkl', 'rb'))
        self.scaler = pickle.load(open('./service/Models/scaler.pkl', 'rb'))

        logger.debug(mensagens.FIM_LOAD_MODEL)

    def executar_rest(self, texts):
        response = {}

        logger.debug(mensagens.INICIO_PREDICT)
        start_time = time.time()

        response_predicts = self.buscar_predicao(texts)

        logger.debug(mensagens.FIM_PREDICT)
        logger.debug(f"Fim de todos os cálculos em {time.time()-start_time}")

        df_response = pd.DataFrame(columns=['Numero'])
        df_response['predict'] = response_predicts

        df_response = df_response.drop(columns=['Numero'])

        response = json.loads(df_response.to_json(orient='records', force_ascii=False))

        return response

    def buscar_predicao(self, texts):
        """
        Pega o modelo carregado e aplica nos dados
        """
        logger.debug('Iniciando a predição...')

        response = []

        idade = int(texts['Idade'][0])
        imc = float(texts['IMC'][0])
        filhos = int(texts['Filhos'][0])
        fumante = int(texts['Fumante'][0])
        sexo = int(texts['Sexo'][0])

        dados = [[idade, imc, filhos, fumante, sexo, 1, 1, 1]]

        dados_request = self.scaler.transform(dados)
        dados_request = dados_request[:,:-3]

        predicao = self.model.predict(dados_request)

        response.append(predicao)

        return response
