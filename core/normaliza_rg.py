import pandas as pd
import re
import numpy as np

def verificar_rg(rg) -> str:
    rg = str(rg)
    if len(rg) < 7 or len(rg)>9:
        return "RG Invalido"
    return rg