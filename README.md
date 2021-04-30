# Projeto de Compilador
## Lógica da Computação - Engenharia da Computação - Insper 7o Semestre

**Professor:** Maciel Calebe

**Aluno:** Rafael Almada

Projeto com o intuito de se criar uma nova linguagem.

## EBNF - Linguagem _"Python-br"_

````
BLOCK = { COMMAND } ;
COMMAND = ( λ | ASSIGNMENT | PRINT | INPUT | CONDITION | LOOP ), ";" ;
ASSIGNMENT = IDENTIFIER, "=", ( EXPRESSION | BOOLEAN ) ;
PRINT = "imprimir", "(", EXPRESSION, ")" ;
LOOP = "enquanto", "(", ( OREXP | ANDEXP | EQEXP | BOOLEAN ) , ")", "{", BLOCK, { ( BREAK | CONTINUE ) } "}" ;
BREAK = "parar" ;
CONTINUE  = "continuar" ;
CONDITION = IF, "{", BLOCK, "}", { ELSEIF, "{", BLOCK, "}" },  { ELSE, "{", BLOCK, "}" } ;
IF = "se", "(", ( OREXP | ANDEXP | EQEXP | BOOLEAN ), ")" ;
ELSEIF = "caso se", "(", ( OREXP | ANDEXP | EQEXP | BOOLEAN ), ")" ;
ELSE = "senao" ;
OREXP = ( NUMBER | IDENTIFIER ), "ou", ( NUMBER | IDENTIFIER ) ;
ANDEXP = ( NUMBER | IDENTIFIER ), "e", ( NUMBER | IDENTIFIER ) ;
EQEXP = ( NUMBER | IDENTIFIER ), "==", ( NUMBER | IDENTIFIER ) ;
INPUT = "entrada", "(", ")" ;
EXPRESSION = TERM, { ("+" | "-"), TERM } ;
TERM = FACTOR, { ("*" | "/"), FACTOR } ;
FACTOR = (("+" | "-"), FACTOR) | NUMBER | "(", EXPRESSION, ")" | IDENTIFIER ;
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;
NUMBER = DIGIT, { DIGIT } ;
STRING = ( "'" | """ ) , { LETTER | DIGIT | EXTRACHARS }, ( "'" | """ ) ;
LETTER = ( a | ... | z | A | ... | Z ) ;
EXTRACHARS = ( "!" | "@" | "#" | "$" | "?" | "%" | "^" | "&" | "*" | "(" | ")" | ":" | ";" | "{" | "}" | "[" | "]" | "|" | "<" | ">" | "/" | "\" | "~" | "`" | "=" | "_" | "-" | " " ) ;
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
BOOLEAN = ( Verdadeiro | Falso ) ;
````