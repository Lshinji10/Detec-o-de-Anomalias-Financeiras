# Detec-o-de-Anomalias-Financeiras

# 🛡️ FinGuard: Detecção de Anomalias Financeiras

Este projeto utiliza Machine Learning para identificar transações suspeitas em tempo real, visando reduzir fraudes e perdas operacionais.

## 🚀 Tecnologias Utilizadas
* Python 3.11
* Scikit-Learn (Isolation Forest)
* Pandas & Numpy
* Matplotlib & Seaborn

## 📈 O Problema de Negócio
Instituições financeiras perdem bilhões anualmente com transações fraudulentas. O desafio é identificar esses padrões em meio a milhões de transações legítimas sem gerar atrito excessivo para o cliente.

## 🛠️ Como o Modelo Funciona
Utilizamos o algoritmo **Isolation Forest**, que é extremamente eficiente para dados não rotulados. Ele isola anomalias (outliers) baseando-se em características como:
* Valor da transação desproporcional.
* Horário da operação (ex: transações de alto valor na madrugada).
* Desvios no score de crédito do cliente.

## 📊 Resultados
O modelo foi capaz de identificar [X]% das anomalias simuladas, apresentando uma visualização clara para a equipe de monitoramento de riscos.
