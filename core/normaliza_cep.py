import pandas as pd
import numpy as np
import re
from core.normaliza_numeros import normalizar_numeros


def verificar_cep(cep) -> str:
    cep = str(cep)
    cep = normalizar_numeros(cep)
    if len(cep)<8 or len(cep)>9:
        return "CEP invalido"
    return cep

