import yfinance as yf
from datetime import datetime

# Lista de símbolos e nomes dos índices futuros
futuros = {
    'ES=F': 'S&P 500',
    'YM=F': 'Dow Jones',
    'NQ=F': 'Nasdaq',
    '^GDAXI': 'DAX30'  # Símbolo para o índice DAX Cash
}

# Obtendo os dados dos índices futuros
dados_futuros = yf.download(list(futuros.keys()), period='2d')['Close']

# Última linha (dia atual) e penúltima linha (dia anterior)
ultima_linha = dados_futuros.iloc[-1]
penultima_linha = dados_futuros.iloc[-2]

# Imprimir o título dos principais índices futuros em âmbar, centralizado
print("\n\033[33m INTRADAY\033[0m\n")

# Exibir o último valor cotado e a variação percentual em relação ao dia anterior
for futuro, nome in futuros.items():
    valor = ultima_linha[futuro]
    valor_anterior = penultima_linha[futuro]
    variacao_percentual = ((valor - valor_anterior) / valor_anterior) * 100
    seta = '▲' if variacao_percentual >= 0 else '▼'
    cor_variacao = '\033[92m' if variacao_percentual >= 0 else '\033[91m'
    cor_seta = '\033[92m' if variacao_percentual >= 0 else '\033[91m'
    cor_valor = '\033[92m' if variacao_percentual >= 0 else '\033[91m'
    cor_nome_futuro = '\033[92m' if variacao_percentual >= 0 else '\033[91m'
    print(f"{cor_nome_futuro}{nome:<10}\033[0m: {cor_valor}{valor:>8.2f}\033[0m  {cor_variacao}{variacao_percentual:>6.2f}% {cor_seta}{seta}\033[0m")

# Obter hora atual
hora_atual = datetime.now().strftime('%H:%M:%S')

# Incluir descrição dos índices futuros em âmbar, centralizada, com a hora atual
print(f"\n\033[33m{'@cmdte.paulo':^78}\033[0m")
print(f"\033[33m{'às: ' + hora_atual:^78}\033[0m")
