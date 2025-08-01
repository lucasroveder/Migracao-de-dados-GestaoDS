import pandas as pd
import numpy as np
import re
from core.normaliza_strings import normalizar_strings

def verificar_sexo(sexo) -> str:
    sexo = str(sexo)
    sexo = normalizar_strings(sexo)
    if sexo == 'M' or sexo == 'F':
        return sexo
    return "Sexo invalido"