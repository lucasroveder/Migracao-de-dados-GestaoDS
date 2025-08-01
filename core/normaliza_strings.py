import re
import pandas as pd
import numpy as np

preposicoes = {'da', 'de', 'do', 'das', 'dos'}
#Separa Strings coladas diferenciadas por maiusculo (JoaoGabriel -> Joao Gabriel)
def separar_colado(string):
    return re.sub(r'(?<!^)([A-Z])', r' \1', string)

#Caixa alta na primeira casa da string (joao -> Joao)
def cap_string(string):
    return ' '.join([p.lower().capitalize() for p in string.strip().split()])

#Normaliza strings
def normalizar_strings(string):
    if pd.isnull(string) or not str(string).strip():
        return np.nan
    string = str(string).strip()
    if string.isupper():
        string = string.lower()

    # Caso esteja tudo minúsculo ou mal capitalizado
    if string.islower() or string != string.title():
        # Detecta nome colado com maiúsculas internas
        if re.search(r'(?<!^)[A-Z]', string):
            string = separar_colado(string)

        # Padroniza palavras, respeitando preposições
        palavras = string.strip().split()
        palavras_formatadas = [p.lower() if p.lower() in preposicoes else p.lower().capitalize()
                               for p in palavras]
        string = ' '.join(palavras_formatadas)
    return string



