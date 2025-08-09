import pandas as pd
import numpy as np

#codigo abaixo esta puxando um arquivo de dados csv do github para a analise usando o pandas no formato de dataframe
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

def projeto_alura05(df):
    print(df.head(10))
    
    #metodo para listar campos nulos
    nulo = df.isnull().sum()
    print(nulo) 
    
    print()
    campo_unico = df['work_year'].unique()  #mostra os anos unicos do campo work_year
    print(campo_unico)
    print()

    print(df[df.isnull().any(axis=1)])  #mostra as linhas que tem algum campo nulo
#projeto_alura05(df)

def projeto_alura06():
    #criando dataframe com valores nulos
    df_salarios = pd.DataFrame({
        'nome': ['Ana', 'Beatriz', 'Carlos', 'Daniel','val'],
        'salario': [4000, np.nan, 5000, np.nan, 100000]
    })
    #metodo para preencher os valores nulos com a media dos valores da coluna salario
    df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))
    
    #metodo para preencher os valores nulos com a mediana dos valores da coluna salario
    df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median())
    print(df_salarios)
#projeto_alura06()

def projeto_alura07():
    #criando dataframe com valores nulos
    df_salarios = pd.DataFrame({
        'nome': ['Ana', 'Beatriz', 'Carlos', 'Daniel','val'],
        'salario': [4000, 5000, np.nan, np.nan, 100000]
    })
    #metodo para preencher os valores nulos com o valor anterior
    df_salarios['salario_completar'] = df_salarios['salario'].fillna(df_salarios['salario'].ffill())
    
    print(df_salarios)
    
#projeto_alura07()

def projeto_alura08():
    #criando dataframe com valores nulos
    df_salarios = pd.DataFrame({
        'nome': ['Ana', 'Beatriz', 'Carlos', 'Daniel','val'],
        'salario': [4000, 5000, np.nan, np.nan, 100000]
    })
    #metodo para preencher os valores nulos com o valor posterior
    df_salarios['salario_completar_back'] = df_salarios['salario'].bfill()

    print(df_salarios)
#projeto_alura08()

def projeto_alura09():
    #criando dataframe com valores nulos
    df_salarios = pd.DataFrame({
        'nome': ['Ana', 'Beatriz', 'Carlos', 'Daniel','val'],
        'salario': [4000, 5000, np.nan, np.nan, 100000],
        'cidade': ['SP', 'RJ', 'SP', np.nan, 'MG']
        
    })
    #metodo para preencher os valores nulos com o valor posterior
    df_salarios['salario_completar_back'] = df_salarios['salario'].bfill()

    #preenche os valores nulos da coluna cidade com 'Não informado'
    df_salarios['cidade_preenchida'] = df_salarios['cidade'].fillna('Não informado')  

    print(df_salarios)
#projeto_alura09()

def projeto_alura10(df):
    df_limpo = df.dropna()
    
    print(df_limpo.isnull().sum())  #verifica se ainda existem campos nulos
    
    print(df_limpo.head())  #mostra os primeiros 10 registros do dataframe limpo
    print()
    
    print(df_limpo.info())  #mostra as informações do dataframe limpo
    
    df_limpo = df_limpo.assign(work_year = df_limpo['work_year'].astype('int64'))  #converte a coluna work_year para int
    
    print()
    print(df_limpo.info())  #mostra as informações do dataframe limpo após a conversão
    print()
    print(df_limpo.head(10))  #mostra os primeiros 10 registros do dataframe limpo após a conversão
projeto_alura10(df)