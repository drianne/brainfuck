import click

@click.command()
@click.argument('brainf_ck')
@click.argument('-o', nargs=1)

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

}
