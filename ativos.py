import yfinance as yf
from datetime import datetime

# Lista de símbolos e nomes dos índices
indices = {
    '^GSPC': 'SP500',
    '^IXIC': 'Nasdaq',
    '^DJI': 'Dow Jones',
    '^GDAXI': 'DAX30',
    '^BVSP': 'Ibovespa'
}

# Obtendo os dados dos índices
dados_indices = yf.download(list(indices.keys()), period='2d')['Close']

# Última linha (dia atual) e penúltima linha (dia anterior)
ultima_linha = dados_indices.iloc[-1]
penultima_linha = dados_indices.iloc[-2]

# Imprimir o título dos principais índices em âmbar
print("\n\033[33m INTRADAY\033[0m\n")

# Exibir o último valor cotado e a variação percentual em relação ao dia anterior
for indice, nome in indices.items():
    valor = ultima_linha[indice]
    valor_formatado = f"{valor:.2f}"[:-1]  # Remover o último número decimal
    valor_anterior = penultima_linha[indice]
    variacao_percentual = ((valor - valor_anterior) / valor_anterior) * 100
    seta = '▲' if variacao_percentual >= 0 else '▼'
    cor_variacao = '\033[92m' if variacao_percentual >= 0 else '\033[91m'
    cor_seta = '\033[92m' if variacao_percentual >= 0 else '\033[91m'
    cor_valor = '\033[92m' if variacao_percentual >= 0 else '\033[91m'
    cor_nome_indice = '\033[92m' if variacao_percentual >= 0 else '\033[91m'
    print(f"{cor_nome_indice}{nome:<10}\033[0m: {cor_valor}{valor_formatado:>8}\033[0m  {cor_variacao}{variacao_percentual:>6.2f}% {cor_seta}{seta}\033[0m")

# Obter hora atual
hora_atual = datetime.now().strftime('%H:%M:%S')

# Incluir descrição dos índices em âmbar, centralizada, com a hora atual
print(f"\n\033[33m{'@cmdte.paulo':^78}\033[0m")
print(f"\033[33m{'às: ' + hora_atual:^78}\033[0m")
