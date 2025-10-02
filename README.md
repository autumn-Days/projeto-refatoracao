# Descrição
Esse repositório é dedicado a refatoração do repositório `https://github.com/Warrioravi/GUI-scientific-calculator-using-python/blob/master/calculator.py` para o primeiro projeto de `reuso de software`.

# Objetivos
1. Expansão pré-eliminar da aplicação para que ela encorpore também uma calculadora científica e trigonométrica, à medida em que os vícios no projeto são mantidos
2. Refatoração pelo uso dos seguintes padrões de projeto: Model-View-Controller(MVC), Observer, Strategy e Command.

# Descrição dos padrões de projeto

## Model View Controller (MVC)

Atualmente o sistema está implementando toda a lógica da interface gráfica dentro de um arquivo só. Com o MVC separaremos essa lógica em componentes separados para facilitar a manutenção do código.

## Observer

Esse padrão vai ser usado para que a interface gráfica seja notificada de alguma mudança de estado e seja atualizada.

## Strategy

Possibilitará instacilizar o tipo da calculadora, básica ou científica.

## Command

Vai possibilitar a utilização modelar os botões como classes, o que facilitará a manutenação do código futuramente.
