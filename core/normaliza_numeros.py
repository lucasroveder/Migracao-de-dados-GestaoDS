import re
import pandas as pd
import numpy as np

REGEX_DIGITOS = re.compile(r'\d')

#retira caracteres
def normalizar_numeros(string):
    string = str(string).strip()
    return ''.join(REGEX_DIGITOS.findall(string)) or np.nan

def normalizar_grupo_de_numeros(string):
     numeros = re.findall(r'\d+', string)
     return numeros

#extrai o ddd
def extrair_ddd(string) -> str:
        digitos = normalizar_numeros(string)
        #retira o codigo de pais
        if digitos.startswith('55') and len(digitos) > 11:
            digitos = digitos[2:]
        #retira 0 a esquerda
        if digitos[0] == '0':
             digitos = digitos[1:]
        return digitos[:2] if len(digitos) >= 10 else ''

def extrair_numero(string) -> str:
        if pd.isnull(string) or not str(string).strip():
             return np.nan
        digitos = normalizar_numeros(string)
        #retira o codigo de pais
        if digitos.startswith('55') and len(digitos) > 11:
            digitos = digitos[2:]
        #retira o 0 a esquerda
        if digitos[0] == '0':
             digitos = digitos[1:]
        return digitos[2:] if len(digitos) >= 10 else ''

def normalizar_complemento(numeros):
     if pd.isnull(numeros) or not str(numeros).strip():
        return np.nan
     digitos = normalizar_grupo_de_numeros(numeros)
     if len(digitos) > 1:
          return "Apto " + digitos[0] + " Bloco " + digitos[1]
     return "Apto " + digitos[0]

