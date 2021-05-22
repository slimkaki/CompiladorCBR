# Projeto de Compilador
## Lógica da Computação - Engenharia da Computação - Insper 7o Semestre

**Professor:** Maciel Calebe

**Aluno:** Rafael Almada

Nesta APS temos o intuito de criar nossa própria linguagem.

Baseando no código construído ao longo do semestre para a disciplina, foi possível atualizar a linguagem para uma própria criada por mim. 

A linguagem criada é a CBR que mistura a linguagem C com a língua portuguesa. A ideia de se existir uma linguagem assim é fomentar que pessoas que não falam o inglês, possam entender e começar a programar em seu próprio idioma, ajudando futuros novos programadores.

A linguagem foi construída utilizando um sistema AST.

## EBNF - Linguagem _"cbr"_

````
BLOCK = "{", { COMMAND }, "}" ;
COMMAND = ( λ | ASSIGNMENT | PRINT | INPUT | CONDITION | LOOP ), ";" ;
ASSIGNMENT = IDENTIFIER, "=", ( EXPRESSION ) ;
PRINT = "imprimir", "(", EXPRESSION, ")" ;
LOOP = "enquanto", "(", CONDITIONEXP, ")", "{", BLOCK, "}" ;
CONDITION = IF, "{", BLOCK, "}", { ( ELSEIF, ELSE ), "{", BLOCK, "}" } ;
CONDITIONEXP = ( NEG, "" ), ( LESSER | GREATER | LESSEREQ | GREATEREQ | UNEQ | EQEXP ), { ("||", "&&"),  ( NEG, "" ), ( ( LESSER | GREATER | LESSEREQ | GREATEREQ | UNEQ | EQEXP ) ) } ;
IF = "se", "(", CONDITIONEXP, ")" ;
ELSEIF = "caso se", "(", CONDITIONEXP, ")" ;
ELSE = "senao" ;
NEG = "!" ;
LESSER = ( NUMBER | IDENTIFIER ), "<", ( NUMBER | IDENTIFIER ) ;
GREATER = ( NUMBER | IDENTIFIER ), ">", ( NUMBER | IDENTIFIER ) ;
LESSEREQ = ( NUMBER | IDENTIFIER ), "<=", ( NUMBER | IDENTIFIER ) ;
GREATEREQ = ( NUMBER | IDENTIFIER ), ">=", ( NUMBER | IDENTIFIER ) ;
EQEXP = ( NUMBER | IDENTIFIER ), "==", ( NUMBER | IDENTIFIER ) ;
UNEQ = ( NUMBER | IDENTIFIER ), "!=", ( NUMBER | IDENTIFIER ) ;
INPUT = "entrada", "(", ")" ;
EXPRESSION = TERM, { ("+" | "-"), TERM } ;
TERM = FACTOR, { ("*" | "/"), FACTOR } ;
FACTOR = (("+" | "-"), FACTOR) | NUMBER | "(", EXPRESSION, ")" | IDENTIFIER ;
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;
NUMBER = DIGIT, { DIGIT } ;
STRING = ( "'" | """ ) , { LETTER | DIGIT }, ( "'" | """ ) ;
LETTER = ( a | ... | z | A | ... | Z ) ;
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
````

## Para rodar

Para rodar um código utilizando a linguagem, basta baixa-la e no diretório raiz digitar o comando:

```sh
$ python3 main.py <nome-do-seu-código>.cbr
```

> Obs: É importante ressaltar sobre o código necessariamente ser do tipo *.cbr*

## Testes

Por fim, os testes unitários podem ser facilmente encontrados no arquivo *test_issues.py*.

Para rodar os testes basta rodar também no diretório raiz:

```sh
$ pytest
```