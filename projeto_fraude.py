import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest

np.random.seed(42)
n_rows = 10000

data = {
    'id_transacao': range(n_rows),
    'valor': np.random.exponential(scale=100, size=n_rows),
    'idade_cliente': np.random.randint(18, 80, size=n_rows),
    'hora_dia': np.random.randint(0, 24, size=n_rows),
    'score_credito': np.random.normal(600, 100, size=n_rows)
}

df = pd.DataFrame(data)

df.loc[0:50, 'valor'] = df.loc[0:50, 'valor'] * 30  
df.loc[51:100, 'hora_dia'] = 3                      

features = ['valor', 'idade_cliente', 'hora_dia', 'score_credito']
X = df[features]

model = IsolationForest(contamination=0.02, random_state=42)

df['anomaly_pred'] = model.fit_predict(X)

df['is_anomaly'] = df['anomaly_pred'].apply(lambda x: 1 if x == -1 else 0)

plt.figure(figsize=(12, 6))

sns.scatterplot(
    data=df, 
    x='hora_dia', 
    y='valor', 
    hue='is_anomaly', 
    palette={0: '#1f77b4', 1: '#d62728'}, 
    alpha=0.6
)

plt.title('Dashboard de Detecção de Fraude: Valor vs Horário')
plt.xlabel('Hora do Dia (0-23h)')
plt.ylabel('Valor da Transação (R$)')
plt.legend(title='Alerta de Fraude', labels=['Normal', 'Suspeita'])
plt.grid(True, linestyle='--', alpha=0.5)

print(f"Sucesso! Foram detectadas {df['is_anomaly'].sum()} transações suspeitas.")
plt.show()