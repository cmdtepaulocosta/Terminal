import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Obtendo os dados do fechamento dos últimos 31 dias para PETR4
petr4 = yf.download("PETR4.SA", period="31d", interval="1d")
fechamentos = petr4['Close']

# Último valor de fechamento
ultimo_fechamento = fechamentos.iloc[-1]

# Fechamento do dia anterior
fechamento_anterior = fechamentos.iloc[-2]

# Variação percentual em relação ao fechamento do dia anterior
variacao_percentual = ((ultimo_fechamento - fechamento_anterior) / fechamento_anterior) * 100

# Definindo a cor do título com base na variação percentual
if variacao_percentual >= 0:
    cor_titulo = 'green'
else:
    cor_titulo = 'red'

# Obtendo a data atual
data_atual = datetime.now()

# Criando uma lista de datas para os últimos 30 dias
datas = [(data_atual - timedelta(days=i)).strftime('%d') for i in range(30, -1, -1)]

# Configurando o tamanho do gráfico
plt.figure(figsize=(10, 6))

# Plotando o gráfico de linhas
plt.plot(datas, fechamentos)

# Definindo o título do gráfico com o último fechamento e a variação percentual
titulo = f'PETR4 Diário - R${ultimo_fechamento:.2f} ({variacao_percentual:.2f}%)'
plt.title(titulo, color=cor_titulo)

# Definindo o nome dos eixos
plt.xlabel('Dias')
plt.ylabel('@cmdte.paulocosta Fechamento (R$)')

# Movendo os valores do eixo Y para o lado direito
plt.gca().yaxis.tick_right()

# Formatar os valores do eixo Y para duas casas decimais
plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))

# Exibindo o gráfico
plt.show()



