import re
import pandas as pd
import numpy as np

def extrair_data_padronizada(string):
    string = str(string).strip()
    
    match = re.search(r'(\d{1,2})/(\d{1,2})/(\d{4})', string)
    if match:
        dia, mes, ano = match.groups()
        return f"{int(dia):02d}/{int(mes):02d}/{ano}"
    return pd.nan

# Limpa qualquer sufixo de hora e segundos
def limpar_hora(string):
    
    string = str(string).strip()
    return re.sub(r'\s+\d{1,2}(:\d{2}){1,2}\s*[APapMm]*', '', string)

# Função principal para aplicar em cada valor
def normalizar_data(string):
    string_limpo = limpar_hora(string)
    return extrair_data_padronizada(string_limpo)
