import yfinance as yf
from datetime import datetime, timedelta

# Símbolo e nome do índice Bovespa
indice = '^BVSP'
nome = 'Ibovespa'

# Obtendo os dados do índice Bovespa para os últimos 60 dias
data_atual = datetime.now()
data_inicial = data_atual - timedelta(days=6)
dados_indice = yf.download(indice, start=data_inicial, end=data_atual)['Close']

# Verificar se há dados suficientes para calcular a variação percentual
if dados_indice.empty:
    print("Nenhum dado encontrado para o índice Bovespa.")
elif len(dados_indice) < 2:
    print("Dados insuficientes para calcular a variação percentual.")
else:
    # Última linha (dia atual) e penúltima linha (dia anterior)
    ultima_linha = dados_indice.iloc[-1]
    penultima_linha = dados_indice.iloc[-2]

    # Imprimir o título do índice Bovespa em âmbar
    print("\n\033[33m INTRADAY\033[0m\n")

    # Exibir o último valor cotado e a variação percentual em relação ao dia anterior
    valor = ultima_linha
    valor_formatado = f"{valor:.2f}"
    valor_anterior = penultima_linha
    variacao_percentual = ((valor - valor_anterior) / valor_anterior) * 100
    seta = '▲' if variacao_percentual >= 0 else '▼'
    cor_variacao = '\033[92m' if variacao_percentual >= 0 else '\033[91m'
    cor_seta = '\033[92m' if variacao_percentual >= 0 else '\033[91m'
    cor_valor = '\033[92m' if variacao_percentual >= 0 else '\033[91m'
    cor_nome_indice = '\033[92m' if variacao_percentual >= 0 else '\033[91m'
    print(f"{cor_nome_indice}{nome:<10}\033[0m: {cor_valor}{valor_formatado:>8}\033[0m  {cor_variacao}{variacao_percentual:>6.2f}% {cor_seta}{seta}\033[0m")

    # Obter hora atual
    hora_atual = datetime.now().strftime('%H:%M:%S')

    # Incluir descrição do índice Bovespa em âmbar, centralizada, com a hora atual
    print(f"\n\033[33m{'X CmdtePaulo':^78}\033[0m")
    print(f"\033[33m{'às: ' + hora_atual:^78}\033[0m")

