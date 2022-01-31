# RPG Pô

*Um jogo de RPG no estilo Jo-Ken-Pô*

## As regras são simples

Cada um dos 2 jogadores deve escolher uma das 3 opções para uma batalha épica: 

- [Ladino](https://pt.wikipedia.org/wiki/Ladino_(classe_de_personagem))
- [Guerreiro](https://pt.wikipedia.org/wiki/Guerreiro_(classe_de_personagem))
- ou [Mago](https://pt.wikipedia.org/wiki/Mago_(classe_de_personagem))

### Que vença o melhor

Ladino ganha de Guerreiro, porque apesar de forte, o Guerreiro é pouco astuto e toma golpes sem nem saber de onde vêm.

Guerreiro ganha de Mago, porque apesar de sábio, o Mago morre com a força de uma simples machadada.

E Mago ganha de Ladino, porque apesar de esperto, o Ladino não resiste às bruxarias.

## Como jogar

A [versão alfa](https://pt.wikipedia.org/wiki/Vers%C3%A3o_alfa) do jogo funciona por linha de comando através do terminal do seu computador. Os únicos pré-requisitos é ter o  [Python](https://pt.wikipedia.org/wiki/Python) instalado [(dowload)](https://www.python.org/downloads/) no seu computador e a linha de comando, onde ocorre o jogo atualmente.

### Para rodar

Baixe o código fonte e rode no terminal a partir do diretório baixado o comando `python game/rpg_po.py`

## Se você quiser programar alguma evolução

Ele é de [código aberto](https://pt.wikipedia.org/wiki/C%C3%B3digo_aberto) , então fique a vontade para implementar o que quiser!

Estamos buscando seguir as a sabedoria do [Testivus](https://www.artima.com/weblogs/viewpost.jsp?thread=203994#:~:text=%20The%20Way%20of%20Testivus%20%201%20If,no%20test.%2010%20Good%20tests%20fail.%20More%20), e incentivamos muito você tentar aceitar e internalizar *o Karma dos testes de unidade*:

> O Karma diz:
>
>"*Faça coisas boas e boas coisas te acontecerão.*
>
>*Faça-as de uma forma que você saiba.*
>
>*Faça-as de uma forma que você goste.*"
> 
> **O Karma é flexível. Testes precisam de flexibilidade.
> 
> O Karma prospera com criatividade. Testes precisam de criatividade."**

### Botando a mão na massa

Comece pelos testes.

1. Escreva um novo teste que mostre que uma nova boa ideia ainda não está implementada (buscando o vermelho).

> Ainda de acordo com o [Testivus](https://www.artima.com/weblogs/viewpost.jsp?thread=203994#:~:text=%20The%20Way%20of%20Testivus%20%201%20If,no%20test.%2010%20Good%20tests%20fail.%20More%20), em tradução livre:
>
> *"Se todos os seus testes passam o tempo todo, você precisa escrever melhores testes"*

2. Rode os testes (incluindo esse seu) com o comando `python -m unittest discover"` (não selecione o loop.)

3. Veja o teste recém escrito falhar, já que você ainda não implementou o código que resolve o que está sendo testado

4. Implemente o código mais simples possível para fazer os testes passarem

5. Quando todos os testes estiverem passando, busque melhorar o código, sem alterar seu comportamento

6. Volte ao item 1


## Para o futuro

Temos muitas ideias, mas o que queremos mesmo é a diversão. Não só de quem joga, mas de quem desenvolve o jogo também.

Se você também tem alguma ideia, feedback ou sugestão, manda uma mensagem no [Twitter](https://twitter.com/lulacode)

