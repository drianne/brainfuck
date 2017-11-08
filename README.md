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

Este repositório apresenta uma atividade apresentada como avaliação parcial da disciplina de Compiladores do curso de Engenharia de software da UnB. O objetivo é compilar um código escrito em brainfuck obtendo como saída um código em C.

Para rodar o programa basta executar o seguinte comando:

```shell
$ python3 brainf_ck.py arquivo.bf -o saida.c
```

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
