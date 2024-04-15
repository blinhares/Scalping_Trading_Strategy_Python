
import pandas as pd
import matplotlib.pyplot as plt
from termcolor import colored as cl
import numpy as np
import yfinance as yf
from pathlib import Path
import csv
ROOT_DIR = Path(__file__).parent
ROOT_DIR_FILES = ROOT_DIR / 'src'

CSV_PATH = ROOT_DIR_FILES / 'list_acoes_br'/ 'lista_de_acoes.csv'
print(CSV_PATH)

PERIODO_ACAO_YFINAN = '2y'

#ESTE É O PERCENTUAL EM QUE CONSIDERAMOS PARA ENTRAR NO JOGO
var_p_close_p_open = .5 # %

#ESTE É O PERCENTUAL EM QUE SE VENDERIA AS ACOES...NO CASO DELA SUBIR X% EM RELACAO AO 
#PRECO DE ABERTURA
VAR_P_CHANGE = .5 # %


def filtrar_dados(stock:pd.DataFrame,var_percentua_abertura:float):
    """ 
    Filtrar valores de acordo com o percentual fornecido.
    O data frame retornado sera os que Percentual de abertura do dia for maio que 

    Args:
        stock (pd.DataFrame): _description_
    """
    stock['p_close_open'] = np.nan # criando uma coluna NAN

    for i in range(1, len(stock)):
        diff = (stock['Close'].iloc[i-1] - stock['Open'].iloc[i])
        # avg = (stock['Close'].iloc[i-1] + stock['Open'].iloc[i])/2
        avg = stock['Close'].iloc[i-1]
        
        pct_change = (diff / avg) * 100
        #armazena o vlaor encontrado
        stock.loc[stock.index[i] ,'p_close_open'] = pct_change

    # filtra os resultados caso o % encontrado dia anterior valor de abertura for igual ao desejado
    #no caso do exemplo 1%
    stock = stock[stock['p_close_open'] > var_percentua_abertura]
    stock = stock[stock['Open'] > 0]

    return stock

def calcular_var_percentual_dia(stock:pd.DataFrame):
    '''Inclui no DF a variação percentual do dia'''
    for i in range(1, len(stock)):

        diff = (stock['High'].iloc[i] - stock['Open'].iloc[i])
        
        pct_change = (diff / stock['Open'].iloc[i]) * 100
        # print(f"Max: {stock['High'].iloc[i]} , Open: {stock['Open'].iloc[i]} , % {pct_change}")
        #armazena o vlaor encontrado
        stock.loc[stock.index[i] ,'aum_percentual_dia'] = pct_change
    return stock


def main():
    cont = 0

    df_saida = pd.DataFrame(
        columns=[
            'titulo',f'n_abertur_{var_p_close_p_open}',
            f'n_ganhos_{var_p_close_p_open + VAR_P_CHANGE }',
            f'porc_ganho_{VAR_P_CHANGE}',
            'n_ganho_qualquer',
            f'porc_ganho']
                                    )

    with open(CSV_PATH, newline='') as csv_file:
        file = csv.DictReader(csv_file, delimiter=';')
        for lin in file:
            cont += 1
            titulo = (lin['Símbolo'])
            print(f'Verificando arquivo {cont} - {titulo}')

            if titulo:
                titulo += '.SA'
            
            #coletar dados
            stock = pd.DataFrame(yf.Ticker(titulo).history(period = PERIODO_ACAO_YFINAN))
            

            stock = filtrar_dados(stock,var_p_close_p_open)

            n_vezes_p_abertura_maior = stock['p_close_open'].count()

            stock['aum_percentual_dia'] = np.nan # criando uma coluna NAN
            
            stock = calcular_var_percentual_dia(stock)

            n_vezes_p_abertura_plus = stock[stock['aum_percentual_dia'] > var_p_close_p_open + VAR_P_CHANGE ]['aum_percentual_dia'].count()

            n_vezes_ganho = stock[stock['Close'] > stock['Open']]['Close'].\
                count()
            
            perc_ganhos_superiores = n_vezes_p_abertura_plus / n_vezes_p_abertura_maior * 100

            perc_ganhos_qualquer = n_vezes_ganho / n_vezes_p_abertura_maior * 100
            
            
            if  perc_ganhos_superiores > 70 and perc_ganhos_qualquer > 60 :
                df_saida.loc[len(df_saida.index)] = [
                    titulo,
                    n_vezes_p_abertura_maior,
                    n_vezes_p_abertura_plus,
                    perc_ganhos_superiores,
                    n_vezes_ganho,
                    perc_ganhos_qualquer
                    ]

                print('-'*80)   
                print(f'Informação para o titulo {titulo}')
                print(f'Numero de DIAS que valor de abertura maior que {var_p_close_p_open}% : {n_vezes_p_abertura_maior}')
                print(f'Numero de DIAS com VALOR MAX maior que {var_p_close_p_open + VAR_P_CHANGE }% : {n_vezes_p_abertura_plus}')
                print(f'Uma porcentagem de {perc_ganhos_superiores :.2f}%')
                print(f'Numero de DIAS que houve um ganho quaquer no valor de fechamento : {n_vezes_ganho}')
                print(f'Uma porcentagem de {perc_ganhos_qualquer :.2f}%')
                print('-'*80)

    print(df_saida)
    df_saida.to_parquet(ROOT_DIR_FILES / 'df_saida.parquet')

if __name__ == '__main__':
    main()