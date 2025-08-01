import pandas as pd
from core.transfere_dados import transferir_dados
from utils.constants import DICIONARIO_COLUNAS, DICIONARIO_COLUNAS_LUCAS, TARGET_DATA

df = pd.read_excel(TARGET_DATA, sheet_name="relatorio")

#Data frame da tabela igual ao do exemplo-resultado
res_df = pd.DataFrame()

#Data frame da tabela que organizei
res_df2 = pd.DataFrame()

transferir_dados(DICIONARIO_COLUNAS, res_df, df)

transferir_dados(DICIONARIO_COLUNAS_LUCAS, res_df2, df)


print(res_df.head())

#Da um resultado igual ao exemplo
res_df.to_excel("Resultado Exemplo.xlsx", index=False)

#Da um resultado com as minhas alteracoes nas colunas
res_df2.to_excel("Resultado Lucas.xlsx", index=False)