import pandas as pd

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
projeto_alura05(df)