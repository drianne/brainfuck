import click

@click.command()
@click.argument('brainf_ck',type=click.File('r'))
@click.option('-o', nargs=1, type=click.File('w'))

def cGenerator(brainf_ck, o):

	parseDictionary = {">": "  ++ptr; \n",
	            "<": "  --ptr; \n",
	            "+": "  ++(*ptr); \n",
	            "-": "  --(*ptr); \n",
	            ".": """    printf("%c \\n",(*ptr)); \n""",
	            ",": """    scanf("%c",ptr); \n""",
	            "[": """  while(*ptr) { \n""",
	            "]": " \n}\n"}

	c_file = """
#include<stdio.h>
int main(){
char *tape = malloc(sizeof(char)*40000);
char *pointer = &tape[0];
"""

	source = brainf_ck.read()
	for data in source:
		if data in parseDictionary:
			c_file = c_file + parseDictionary[data]
	c_file = c_file + "return 0;\n"

	o.write(c_file)
	o.flush()

if __name__ == "__main__":
    op = cGenerator()
