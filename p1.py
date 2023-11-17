# Importando bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np

# Carregando o arquivo CSV com os dados
df = pd.read_csv("CasePositivo.csv", sep=";")

# Criando uma nova coluna para o valor de mercado total diário de cada debênture
df["Total Market Value"] = df["Preço Unitário Indicativo"] * df["Quantidade"]

# Removendo a coluna da taxa de compra
df = df.drop(columns=["Taxa de Compra"])

# Convertendo a coluna de data para o formato datetime
df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y")

# Agrupando os dados pela data e calculando a média das colunas Preço Unitário Indicativo e Taxa Indicativa
df = df.groupby("Data").agg({"Preço Unitário Indicativo": np.mean, "Taxa Indicativa": np.mean})

# Calculando o valor presente diário de um pagamento fictício de R$ 100 milhões daqui a 3 anos
for index, row in df.iterrows():
    rate = row["Taxa Indicativa"]
    pv = 100000000 / ((1 + rate) ** 3)
    df.at[index, "Present Value"] = pv

# Criando um gráfico de linhas com duas escalas y
fig, ax1 = plt.subplots()

# Configurando a escala y para a coluna Preço Unitário Indicativo
color = 'tab:red'
ax1.set_xlabel('Data')
ax1.set_ylabel('Preço Unitário Indicativo', color=color)
ax1.plot(df.index, df["Preço Unitário Indicativo"], color=color)
ax1.tick_params(axis='y', labelcolor=color)

# Criando uma segunda escala y para a coluna Taxa Indicativa
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Taxa Indicativa', color=color)
ax2.plot(df.index, df["Taxa Indicativa"], color=color)
ax2.tick_params(axis='y', labelcolor=color)

# Ajustando o layout para evitar sobreposição
fig.tight_layout()

# Exibindo o gráfico
plt.show()
