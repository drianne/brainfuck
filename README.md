<h1>brainfuckCompiler</h4> <br>
<p align="center">    
    <img src="http://i65.tinypic.com/bdways.png" width=130 height=130>
</p>

## Contribuidores
| Nome	| Matrícula	|
|--|--|
| Adrianne Alves da Silva | 16/0047595 |
| Letícia de Souza | 15/0015160 |


## Apresentação

Este repositório apresenta um compilador da linguagem brainfuck desenvolvida em Python. Ele consiste em uma atividade apresentada como avaliação parcial da disciplina de Compiladores do curso de Engenharia de software da Universidade de Brasília (UnB), Campus de Engenharias - Faculdade do Gama (FGA). Objetiva-se, por meio deste, compilar código escrito em brainfuck obtendo como saída código em C.

## Sobre a Linguagem

BrainFuck consiste em uma linguagem de programação hermética minimalista, ela foi criada em 1993 por Urban Müller, em 1993. O objetivo principal de seu desenvolvimento é realmente confundir os programadores, dessa forma, não é uma linguagem tão último para aplicações práticas. O seu alfabeto baseia-se nos seguintes caracteres:

### Caracteres

| Caractere | Significado  |
|---|---|
| > | Incremento do ponteiro  |
| < | Decremento do pronteiro  |
| + | Incremento do byte |
| - | Decremento do byte |
| . | Imprimir o dado |
| , | Entrada de um byte |
| [ | Início de um Laço |
| ] | Fim de um laço de repetição |

### Correspondência dos Comandos em C

| Caractere | Significado  |
|---|---|
| Início do programa | char array[INFINITELY_LARGE_SIZE] = {0};
char *ptr=array; |
| > | ++ptr; |
| < | --ptr; |
| + | ++*ptr; |
| - | --*ptr; |
| . | printf("%c \\n",(*ptr)); |
| , | scanf("%c",ptr); |
| [ | while (*ptr) { |
| ] | } |

## Como Contribuir

Para contribuir com o desenvolvimento, é preciso que o colaborador crie o seu próprio Fork e envie um pull request com a contribuição para a branch master do projeto. As alterações serão analisadas e incorporadas ao compilador em caso de aprovação.
