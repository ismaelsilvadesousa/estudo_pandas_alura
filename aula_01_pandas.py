import pandas as pd

#para comentar rapido : Ctrl + ;
#lembrar de remover os comentarios de baixo da função a ser executada para o teste

teste = "ola"

def funcao_teste():
    print(teste)
#funcao_teste()

def criar_dataframe():
    data = {
        "calories": [420, 380, 390],
        "duration": [50, 40, 45]
        }

    #load data into a DataFrame object:
    df = pd.DataFrame(data)

    print(df)     
#criar_dataframe()

#codigo abaixo esta puxando um arquivo de dados csv do github para a analise usando o pandas no formato de dataframe
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

def projeto_alura01(df):
    dados = df.head(10)
    #metodos de listas o conteudo do arquivo:
    print(dados) 
    #print(df.to_string())    
#projeto_alura01(df)

def projeto_alura02(df):
    #metodo para listar metadados como colunas, quantidade e tipos de dados
    df.info()     
#projeto_alura02(df)

def projeto_alura03(df):
    #metodo para realizar uma analise de dados numerica rapida
    dados = df.describe() 
    print(dados)
#projeto_alura03(df)

def projeto_alura04(df):
    #metodo para mostras quantidade de linhas e numero de colunas
    dados = df.shape 
    print(dados)
    
    linhas = df.shape[0]
    colunas = df.shape[1]
    print("quantidade de linhas do arquivo: ", linhas)
    print("quantidade de colunas do arquivo: ", colunas)
    print()
    
    nome_colunas = df.columns
    print("nome das colunas: ", nome_colunas)
    print()
    
    #metodo para renomear as colunas do dataframe
    #o atributo inplace=true faz com que a alteração feita seja permanente no dataframe original
    renomear_colunas = {
        'work_year': 'ano_trabalho',
        'experience_level': 'nível_experiência',
        'employment_type': 'tipo_contrato',
        'job_title': 'cargo',
        'salary': 'salário',
        'salary_currency': 'moeda_salário',
        'salary_in_usd': 'salário_em_usd',
        'employee_residence': 'residência_funcionário',
        'remote_ratio': 'percentual_remoto',
        'company_location': 'local_empresa',
        'company_size': 'porte_empresa'
    }
    
    df.rename(columns=renomear_colunas, inplace=True)
    print(df.columns)
    print()
    
    #metodo para mostrar a frequencia dos tipos de dados de cada coluna selecionada
    print(df['nível_experiência'].value_counts())
    
    # Criar um dicionário para mapear as abreviações para os nomes completos
    mapeamento_nivel = {
        'SE': 'Senior',
        'MI': 'Mid-level',
        'EN': 'Entry-level',
        'EX': 'Executive'
    }

    # Usar o método replace() para renomear os valores na coluna
    df['nível_experiência'] = df['nível_experiência'].replace(mapeamento_nivel)

    # Imprimir novamente a contagem de valores para verificar a mudança
    print()
    print(df['nível_experiência'].value_counts())
    
    print()
    print(df.describe(include='object'))  # Inclui colunas de tipo objeto (strings) na análise descritiva?

projeto_alura04(df)

