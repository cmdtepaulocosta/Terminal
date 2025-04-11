import yfinance as yf
from datetime import datetime

# Lista de símbolos e nomes das commodities
commodities = {
    'ZS=F': 'Soja',
    'ZC=F': 'Milho',
    'LE=F': 'Boi Gordo',
    'SB=F': 'Açúcar',
    'KC=F': 'Café Arabica',
    'GC=F': 'Ouro',
    'ZW=F': 'Trigo'
}

# Obtendo os dados das commodities
dados_commodities = yf.download(list(commodities.keys()), period='2d')['Close']

# Última linha (dia atual) e penúltima linha (dia anterior)
ultima_linha_commodities = dados_commodities.iloc[-1]
penultima_linha_commodities = dados_commodities.iloc[-2]

# Imprimir o título das commodities
print("\n\033[33m Commodities\033[0m\n")

# Exibir o último valor cotado e a variação percentual em relação ao dia anterior
for symbol, nome in commodities.items():
    if symbol not in dados_commodities.columns:
        print(f"Não foi possível obter dados para {nome}")
        continue
    valor = ultima_linha_commodities[symbol]
    valor_anterior = penultima_linha_commodities[symbol]
    variacao_percentual = ((valor - valor_anterior) / valor_anterior) * 100 if valor_anterior != 0 else 0
    seta = '▲' if variacao_percentual >= 0 else '▼'
    cor_variacao = '\033[92m' if variacao_percentual >= 0 else '\033[91m'
    cor_seta = '\033[92m' if variacao_percentual >= 0 else '\033[91m'
    cor_valor = '\033[92m' if variacao_percentual >= 0 else '\033[91m'
    print(f"{nome:<10}: {cor_valor}{valor:.2f}\033[0m  {cor_variacao}{variacao_percentual:.2f}% {cor_seta}{seta}\033[0m")

# Obter hora atual
hora_atual = datetime.now().strftime('%H:%M:%S')

# Incluir descrição das commodities, centralizada, com a hora atual
print(f"\n\033[33m{'@cmdte.paulo':^78}\033[0m")
print(f"\033[33m{'às: ' + hora_atual:^78}\033[0m")
