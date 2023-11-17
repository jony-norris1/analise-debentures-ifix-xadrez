import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np

df = pd.read_csv("CasePositivo.csv", sep=";")

df["Total Market Value"] = df["Preço Unitário Indicativo"] * df["Quantidade"]

df = df.drop(columns=["Taxa de Compra"])

df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y")
df = df.groupby("Data").agg({"Preço Unitário Indicativo": np.mean, "Taxa Indicativa": np.mean})

for index, row in df.iterrows():
    rate = row["Taxa Indicativa"]
    pv = 100000000 / ((1 + rate) ** 3)
    df.at[index, "Present Value"] = pv

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Data')
ax1.set_ylabel('Preço Unitário Indicativo', color=color)
ax1.plot(df.index, df["Preço Unitário Indicativo"], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('Taxa Indicativa', color=color)
ax2.plot(df.index, df["Taxa Indicativa"], color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.show()
