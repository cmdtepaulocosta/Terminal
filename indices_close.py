import yfinance as yf
from datetime import datetime, timedelta

# Lista de símbolos e nomes dos índices
indices = {
    '^GSPC': 'SP500',
    '^DJI': 'Dow Jones',
    '^IXIC': 'Nasdaq',
    '^GDAXI': 'DAX',
    '^FTSE': 'FTSE100',
    '^BVSP': 'Ibovespa'
}

# Obtendo os dados dos índices
data_atual = datetime.now()
data_inicial = data_atual - timedelta(days=12)
dados_indices = yf.download(list(indices.keys()), start=data_inicial, end=data_atual)['Close']

# Verificar se há dados suficientes para calcular a variação percentual
if dados_indices.empty or len(dados_indices) < 2:
    print("Dados insuficientes para calcular a variação percentual.")
else:
    # Última linha (dia atual) e penúltima linha (dia anterior)
    ultima_linha = dados_indices.iloc[-1]
    penultima_linha = dados_indices.iloc[-2]

    # Imprimir o título dos principais índices em âmbar
    print("\n\033[33m INTRADAY\033[0m\n")

    # Exibir o último valor cotado e a variação percentual em relação ao dia anterior para cada índice
    for indice, nome in indices.items():
        if indice in ultima_linha and indice in penultima_linha:
            valor = ultima_linha[indice]
            valor_anterior = penultima_linha[indice]
            variacao_percentual = ((valor - valor_anterior) / valor_anterior) * 100
            seta = '▲' if variacao_percentual >= 0 else '▼'
            cor_variacao = '\033[92m' if variacao_percentual >= 0 else '\033[91m'
            cor_seta = '\033[92m' if variacao_percentual >= 0 else '\033[91m'
            cor_valor = '\033[92m' if variacao_percentual >= 0 else '\033[91m'
            cor_nome_indice = '\033[92m' if variacao_percentual >= 0 else '\033[91m'
            valor_formatado = f"{valor:.2f}"
            print(f"{cor_nome_indice}{nome:<10}\033[0m: {cor_valor}{valor_formatado:>8}\033[0m  {cor_variacao}{variacao_percentual:>6.2f}% {cor_seta}{seta}\033[0m")

    # Obter hora atual
    hora_atual = datetime.now().strftime('%H:%M:%S')

    # Incluir descrição dos índices em âmbar, centralizada, com a hora atual
    print(f"\n\033[33m{'X CmdtePaulo':^78}\033[0m")
    print(f"\033[33m{'às: ' + hora_atual:^78}\033[0m")
