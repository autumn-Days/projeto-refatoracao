# Descrição
Esse repositório é dedicado a refatoração do repositório `https://github.com/Warrioravi/GUI-scientific-calculator-using-python/blob/master/calculator.py` para o primeiro projeto de `reuso de software`.

# Objetivos
1. Expansão pré-eliminar da aplicação para que ela encorpore também uma calculadora científica e trigonométrica, à medida em que os vícios no projeto são mantidos
2. Refatoração pelo uso dos seguintes padrões de projeto: Factory, Observer e o Builder.

# Descrição dos padrões de projeto

## Factory
Uma vez que a aplicação incorporará 3 tipos de calculadora, as quais são básica, científica e trigonométrica, é conveniente usar o padrão Factory para que haja a abstração da seleção de qual objeto instacializar para fora da classe principal.

## Observer
Esse padrão vai ser usado para que a interface gráfica seja notificada de alguma mudança deestado e seja atualizada.

## Builder

Servirá para que os
