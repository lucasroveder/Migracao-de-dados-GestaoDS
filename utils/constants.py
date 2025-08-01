import pandas as pd
import numpy as np
import re
from core.normaliza_strings import normalizar_strings
from core.normaliza_email import verificar_email
from core.normaliza_datas import normalizar_data
from core.normaliza_numeros import normalizar_numeros, extrair_ddd, extrair_numero, normalizar_complemento
from core.normaliza_sexo import verificar_sexo
from core.normaliza_rg import verificar_rg
from core.normaliza_cpf import verificar_cpf
from core.normaliza_cep import verificar_cep
from core.transfere_dados import transferir_dados

TARGET_DATA = "data/pacientes.xlsx"

DICIONARIO_COLUNAS = {
    'Codigo do paciente':      ('IdPaciente', None),
    'Nome Completo':           (['Nome', 'Sobrenome'], lambda x: normalizar_strings(x['Nome']) + ' ' + normalizar_strings(x['Sobrenome'])),
    'Email':                   ('Email', verificar_email),
    'Data Nascimento':         ('DataNascimento', normalizar_data),
    'Endereco':                ('Logradouro', normalizar_strings),
    'Complemento':             ('Complemento', normalizar_complemento),
    'Bairro':                  ('Bairro', normalizar_strings),
    'Cidade':                  ('Cidade', normalizar_strings),
    'Cep':                     ('Cep', verificar_cep),
    'Estado':                  ('Estado', normalizar_strings),
    'Telefone Fixo':           ('Telefone2', extrair_numero),
    'Sexo':                    ('Sexo', verificar_sexo),
    #Nao ha na tabela original
    'Ocupação':                (' ', None),
    #Nao ha na tabela original
    'Indicado por':            (' ', None),
    'CPF':                     ('CpfCnpj', verificar_cpf),
    'RG':                      ('RG', verificar_rg),
    #Nao ha na tabela original
    'Convenio':                (' ', None),
    #Nao ha na tabela original
    'Matricula Conveinio':     (' ', None),
    #Nao ha na tabela original
    'Mãe':                     (' ', None),
    'Pai':                     ('Pai', normalizar_strings),
    'DDD':                     ('Telefone1', extrair_ddd),
    'CEL':                     ('Telefone1', extrair_numero),
    'Obs':                     ('DataInclusao', lambda x: "Paciente desde " + normalizar_data(x)),
    #Nao ha na tabela original
    'Responsavel fone':        (' ', None),
    #Nao ha na tabela original
    'Responsavel nome':        (' ', None),
    'Atencao':                 ('Observacoes', None),
    'Numero endereco':         ('Numero', normalizar_numeros),
}

#Resolvi alterar a organização das colunas e adicionar o Status da situação
DICIONARIO_COLUNAS_LUCAS = {
    #Dados Pessoais
    'Codigo do paciente':      ('IdPaciente', None),
    'Status':                  ('Situacao', normalizar_strings),
    'Nome Completo':           (['Nome', 'Sobrenome'], lambda x: normalizar_strings(x['Nome']) + ' ' + normalizar_strings(x['Sobrenome'])),
    'Sexo':                    ('Sexo', verificar_sexo),
    'Data Nascimento':         ('DataNascimento', normalizar_data),
    #Nao ha na tabela original
    'Ocupação':                (' ', None),
    
    #Endereço
    'Endereco':                ('Logradouro', normalizar_strings),
    'Numero endereco':         ('Numero', normalizar_numeros),
    'Complemento':             ('Complemento', normalizar_complemento),
    'Bairro':                  ('Bairro', normalizar_strings),
    'Cidade':                  ('Cidade', normalizar_strings),
    'Cep':                     ('Cep', verificar_cep),
    'Estado':                  ('Estado', normalizar_strings),
    
    #Contato
    'Telefone Fixo':           ('Telefone2', extrair_numero),
    'DDD':                     ('Telefone1', extrair_ddd),
    'CEL':                     ('Telefone1', extrair_numero),
    'Email':                   ('Email', verificar_email),
    
    #Documentos
    'CPF':                     ('CpfCnpj', verificar_cpf),
    'RG':                      ('RG', verificar_rg),
    
    #Informações Familiares
    #Nao ha na tabela original
    'Mãe':                     (' ', None),
    'Pai':                     ('Pai', normalizar_strings),
    #Nao ha na tabela original
    'Responsavel fone':        (' ', None),
    #Nao ha na tabela original
    'Responsavel nome':        (' ', None),
    #Nao ha na tabela original
    'Indicado por':            (' ', None),
    
    #Dados de Convênio
    'Convenio':                (' ', None),
    'Matricula Conveinio':     (' ', None),
    
    #Observações / Outros
    'Obs':                     ('DataInclusao', lambda x: "Paciente desde " + normalizar_data(x)),
    'Atencao':                 ('Observacoes', None),
}