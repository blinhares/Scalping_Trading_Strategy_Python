# Realizando uma Analise para Scalping Trading Strategy

## Intro

Navegando na internet vi um artigo que dizia que este metodo no qual vamos analisar abaixo era efetivo em 74% das vezes, o que chamou atencao, como pode um metodo tao simples ser tao efetivo, é a chance de qualquer pessoa ficar rica...Pensei.

[Eis o link](https://medium.datadriveninvestor.com/creating-a-scalping-strategy-in-python-with-a-74-win-rate-53a17662ff03)

Mas não é bem assim... Vejamos.

`Scalping Trading Strategy` consiste em uma estrategia simples de compra de venda de acoes baseada em condicoes simples que sao listadas abaixo:

- Nos `entramos no jogo` quando: O pregão abre com um aumento de 1% em relação ao preço de fechamento do `dia anterior`.

- Nos `saimos do jogo` quando: Existir um aumento de mais de 1% sobre o valor de compra. Se a aç~ao falhar em subir 1% sobre o valor de compra nos saimos ao final do dia.

Enfim, a meta é não criar estrategias mirabolantes...

Vamos tentar analisar se essa estrategia é vantajosa, se sua simplicidade nos daria algum retorno financeiro e vamos mais alem tentando mostrar, quanto seria esse retorno financeiro.

Siga lendo no arquivo `.ipynb` de nome : `scalping`. La tratamos com mais detalhes.
