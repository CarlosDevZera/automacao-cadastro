import pandas as pd
from faker import Faker
import random

# Inicializa o Faker para gerar dados fictícios (use 'pt_BR' para dados em português do Brasil)
fake = Faker('pt_BR')

# Número de linhas (registros) que queremos na planilha
num_registros = 500

# Listas para armazenar os dados gerados
id = []
nome = []
email = []
telefone = []
estado = []
produtos_interesse = []
valores_compra = []
data_cadastro = []
status = []

# Gerando os dados fictícios
for i in range(1, num_registros + 1):
    id.append(i)
    nome.append(fake.name())
    email.append(fake.email())
    telefone.append(fake.phone_number())
    estado.append(fake.state_abbr())  # Sigla do estado (SP, RJ, MG, etc.)


    produtos = ['Celular', 'Notebook', 'Tablet', 'Fone de Ouvido', 'TV', 'Smartwatch']
    produtos_interesse.append(random.choice(produtos))

    # Gera um valor de compra entre 100.00 e 5000.00
    valores_compra.append(round(random.uniform(100.00, 5000.00), 2))

    # Gera uma data de cadastro nos últimos 365 dias
    data_cadastro.append(fake.date_between(start_date='-1y', end_date='today'))

    # Escolha um status aleatório
    status_opcoes = ['Ativo', 'Inativo', 'Pendente']
    status.append(random.choice(status_opcoes))

# Cria um dicionário com os dados
dados = {
    'ID_Cliente': id,
    'Nome_Completo': nome,
    'Email': email,
    'Telefone': telefone,
    'Estado': estado,
    'Produto': produtos_interesse,
    'Valor_Ultima_Compra': valores_compra,
    'Data_Cadastro': data_cadastro,
    'Status_Cliente': status
}

# Cria um DataFrame do pandas
df = pd.DataFrame(dados)

# Define o nome do arquivo Excel
nome_arquivo_excel = 'dados_ficticios_500.xlsx'

# Salva o DataFrame em um arquivo Excel
df.to_excel(nome_arquivo_excel, index=False)

print(f"Planilha '{nome_arquivo_excel}' com {num_registros} dados fictícios criada com sucesso!")

