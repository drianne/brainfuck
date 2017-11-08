import click

@click.command()
@click.argument('brainf_ck',type=click.File('r'))
@click.option('-o', nargs=1, type=click.File('w'))

# O comando click usado pra obter argumentos na linha de comando

def cGenerator(brainf_ck, o):

# Dicionário analisador entre brainf_ck e c 

	parseDictionary = {">": "  ++ptr;",
	            "<": "  --ptr;",
	            "+": "  ++(*ptr);",
	            "-": "  --(*ptr);",
	            ".": """  printf("%c \\n",(*ptr));""",
	            ",": """  scanf("%c",ptr);""",
	            "[": """  while(*ptr) {""",
	            "]": " }"}

# Convertendo de brainfuck para código c

	c_file = """#include<stdio.h>
int main(){
	char *tape = malloc(sizeof(char)*40000);
	char *pointer = &tape[0];
"""
	line = '\n'

	source = brainf_ck.read()
	for data in source:
		if data in parseDictionary:
			c_file = c_file + parseDictionary[data] + line
	c_file = c_file + "return 0;"

	numBits = o.write(c_file)	
	if numBits != 0:
		print('C file was generated')
	print('Bits number : {}' .format(numBits))
	o.flush()

if __name__ == "__main__":
    cGenerator()
    
