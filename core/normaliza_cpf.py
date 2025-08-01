import pandas as pd
import re
import numpy as np
from core.normaliza_numeros import normalizar_numeros

def verificar_cpf(cpf) -> str:
    str(cpf)
    cpf = normalizar_numeros(cpf)

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return "CPF invalido"

    # Validação dos dígitos verificadores
    for i in range(9, 11):
        soma = sum(int(cpf[num]) * ((i+1) - num) for num in range(0, i))
        digito = ((soma * 10) % 11) % 10
        if digito != int(cpf[i]):
            return "CPF invalido"
    return cpf