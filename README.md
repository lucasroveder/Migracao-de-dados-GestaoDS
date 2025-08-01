Esse é um desafio pratico para estágio de migração de dados.

## Por dentro do projeto
Nesse desafio usei a biblioteca pandas, re (regex) e numpy para resolver o desafio prático de migração de dados da GestãoDS.

## 🧠 Funcionalidades
Normalização de CEP: Remove caracteres inválidos e padroniza o formato.

Normalização de CPF/RG: Formata e valida campos.

Datas: Converte múltiplos formatos para um padrão.

E-mails: Limpeza e validação de estrutura.

Normalização de Telefones: Padroniza números com ou sem DDD.

Normalização de Strings: Corrige capitalização e formatação de campos textuais.

Transferência de Dados: Realiza o mapeamento e transformação entre tabelas de origem e destino.

## 📓 Detalhes
Dentro da pasta core, coloquei os arquivos modulados com as funções de verificação, limpeza e normalização dos dados. Além da função de transferência .

Dentro da pasta data, coloquei os arquivos excel que serão analizados, intruções e exemplo de saída.

Dentro da pasta utils, coloquei as constants como caminho do diretorio do arquivo alvo e dicionários de colunas.

## 🚀 Como Executar
Certifique-se de ter o Python 3.10+ instalado.

Clone este repositório ou baixe os arquivos.

Para este projeto é necessario ter instalado a biblioteca pandas.

```bash
pip install pandas
```

Execute o script principal:
```bash
python main.py
```

Ao executar, serão criados 2 arquivos xlsx com o resultados da migração, um nomeado Resultado Exemplo.xlsx e outro Resultado Lucas.xlsx

## 📌 Observações
O projeto está estruturado para fácil expansão. Novos tipos de normalização podem ser adicionados no diretório core/.

O foco é a manipulação de dados sujos, simulando um cenário de migração ou saneamento de base de dados.

Alguns dados inválidos podem ser corrigidos conforme as regras de negócio da empresa, essa implementação pode ser facilmente adicionada
no diretório core/ do devido elemento (CPF, RG, CEP...).

## 💬 Comentários
Para chegar no resultado, observei as diferenças entre as duas tabelas e as possiveis irregularidades nos dados passados com os dados esperados.

Utilizei a biblioteca pandas, para fazer a leitura e ter acesso ao arquivo como um data frame (estrutura de dado).

Utilizei ReGex para identificar padrões nas strings e, com as funções modulares, corrigir essas irregularidades.

Fiz o uso de dicionarios (no arquivo constants.py) para percorrer e o codigo ficar mais limpo. Além disso, caso queira fazer modificações de ordem de tabelas, poderia só mexer nessa variável.

Separei as funções por categorias em arquivos para que o código se torne mais legivel e, caso necessária alteração, altera apenas um arquivo, impedindo erros ou que diversas alterações sejam feitas.
