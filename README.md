# Projeto de Compilador
## Lógica da Computação - Engenharia da Computação - Insper 7o Semestre

**Professor:** Maciel Calebe

**Aluno:** Rafael Almada

Projeto com o intuito de se criar uma nova linguagem.

## EBNF

````
BLOCK = { COMMAND } ;
COMMAND = ( λ | ASSIGNMENT | PRINT | CONDITION | LOOP ), ";" ;
ASSIGNMENT = IDENTIFIER, "=", EXPRESSION ;
PRINT = "println", "(", EXPRESSION, ")" ;
CONDITION = IF, "{", BLOCK, "}", { ELSEIF, "{", BLOCK, "}" },  { ELSE, "{", BLOCK, "}" } ;
IF = "if", "(", ( OREXP | ANDEXP | EQEXP ), ")" ;
ELSEIF = "else if", "(", ( OREXP | ANDEXP | EQEXP ), ")" ;
ELSE = "else" ;
OREXP = ( NUMBER | IDENTIFIER ), "||", ( NUMBER | IDENTIFIER ) ;
ANDEXP = ( NUMBER | IDENTIFIER ), "&&", ( NUMBER | IDENTIFIER ) ;
EQEXP = ( NUMBER | IDENTIFIER ), "==", ( NUMBER | IDENTIFIER ) ;
EXPRESSION = TERM, { ("+" | "-"), TERM } ;
TERM = FACTOR, { ("*" | "/"), FACTOR } ;
FACTOR = (("+" | "-"), FACTOR) | NUMBER | "(", EXPRESSION, ")" | IDENTIFIER ;
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;
NUMBER = DIGIT, { DIGIT } ;
LETTER = ( a | ... | z | A | ... | Z ) ;
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
````
