import pandas as pd
import numpy as np

def transferir_dados(dict, res_df, df):
    for res_col, (src_col, func) in dict.items():
        # Se src_col for lista, trata como especial (ex: Nome Completo)
        if isinstance(src_col, list):
            res_df[res_col] = df[src_col].apply(func, axis=1)
        else:
            if src_col == ' ':
                res_df[res_col] = None
            elif func is None:
                res_df[res_col] = df[src_col]
            else:
                res_df[res_col] = df[src_col].apply(func)