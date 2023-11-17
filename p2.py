# Importando bibliotecas necessárias
import pandas as pd
import statsmodels.api as sm

# Carregando o arquivo CSV com os dados
df = pd.read_csv("NTNBIFIX.csv", sep=";")

# Convertendo a coluna de data para o formato datetime
df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y")

# Convertendo a coluna "Taxa Indicativa NTN-B 760199 20350515" para float, substituindo vírgulas por pontos
df["Taxa Indicativa NTN-B 760199 20350515"] = df["Taxa Indicativa NTN-B 760199 20350515"].str.replace(',', '.').astype(float)

# Definindo variáveis X e y para a análise de regressão logística
X = df["Taxa Indicativa NTN-B 760199 20350515"]
y = (df["Dividend Yield"] > 0).astype(int)

# Adicionando uma constante à variável independente X
X = sm.add_constant(X)

# Criando e treinando o modelo de regressão logística
model = sm.Logit(y, X)
result = model.fit()

# Exibindo um resumo estatístico do modelo
print(result.summary())
