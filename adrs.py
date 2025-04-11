# Importando as bibliotecas necessárias
import yfinance as yf  # Biblioteca para obter dados financeiros
from datetime import datetime  # Biblioteca para trabalhar com datas e horários

# Definindo um dicionário com os símbolos e nomes das ADRs em NY
adrs = {
    'PBR': 'Petrobras',
    'VALE': 'Vale',
    'ITUB': 'Itaú',
    'GGB': 'Gerdau',
    'ABEV': 'Ambev',
    'BRFS': 'BRF',
    'BBD': 'Bradesco'
}

# Obtem os dados das ADRs em NY para os últimos 2 dias
dados_adrs = yf.download(list(adrs.keys()), period='2d')['Close']

# Imprime o título "ADRs em NY"
print("\n\033[33m ADRs em NY\033[0m\n")

# Exibe o último valor cotado e a variação percentual para cada ADR
for symbol, nome in adrs.items():
    # Verifica se os dados da ADR estão disponíveis
    if symbol not in dados_adrs.columns:
        print(f"{nome:<10}: Dados não disponíveis")
        continue

    # Obtém o último valor cotado e o valor anterior
    valor = dados_adrs[symbol].iloc[-1]
    valor_anterior = dados_adrs[symbol].iloc[-2]

    # Calcula a variação percentual
    variacao_percentual = ((valor - valor_anterior) / valor_anterior) * 100 if valor_anterior != 0 else 0

    # Define o símbolo para indicar a tendência (▲ para aumento, ▼ para queda)
    seta = '▲' if valor >= valor_anterior else '▼'

    # Define as cores para formatação do texto (verde para aumento, vermelho para queda)
    cor_variacao = '\033[92m' if valor >= valor_anterior else '\033[91m'
    cor_seta = '\033[92m' if valor >= valor_anterior else '\033[91m'
    cor_valor = '\033[92m' if valor >= valor_anterior else '\033[91m'

    # Imprime a linha com as informações da ADR
    print(f"{nome:<10}: {cor_valor}{valor:.2f}\033[0m  {cor_variacao}{variacao_percentual:.2f}% {cor_seta}{seta}\033[0m")

# Obtém a hora atual
hora_atual = datetime.now().strftime('%H:%M:%S')

# Inclui uma descrição das ADRs em NY, centralizada, com a hora atual
print(f"\n\033[33m{'X  CmdtePaulo':^78}\033[0m")
print(f"\033[33m{'às: ' + hora_atual:^78}\033[0m")
