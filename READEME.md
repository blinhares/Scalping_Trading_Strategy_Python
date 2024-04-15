# Realizando um Scrip Python para Scalping Trading Strategy

## Intro

A intencao desse script é automatizar a compra e venda de acoes com a estrategia `Scalping Trading Strategy` usando dados da API [FinancialModelingPrep’s (FMP)](https://site.financialmodelingprep.com/developer/).

`Scalping Trading Strategy` consiste em uma estrategia simples de compra de venda de acoes baseada em condicoes simples que sao listadas abaixo:

- Nos `entramos no jogo` quando: O pregão abre com um aumento de 1% em relação ao preço de fechamento do `dia anterior`.

- Nos `saimos do jogo` quando: Existir um aumento de mais de 1% sobre o valor de compra. Se a aç~ao falhar em subir 1% sobre o valor de compra nos saimos ao final do dia.

Enfim, a meta é não criar estrategias mirabolantes...

https://medium.datadriveninvestor.com/creating-a-scalping-strategy-in-python-with-a-74-win-rate-53a17662ff03

## Importando Bibliotecas

```pyhton

import requests
import pandas as pd
import matplotlib.pyplot as plt
from termcolor import colored as cl
import numpy as np
import math
```

## Extraindo Dados

Extrair os dados sera muito importante para o que pretendemos fazer aqui e como ja comentado, vamos utilizar a API [FinancialModelingPrep’s (FMP)](https://site.financialmodelingprep.com/developer/).