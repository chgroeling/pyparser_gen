import langparser
import terminals
import pprint

import cacos_lexer


token_list = [
    (terminals.NEWLINE, "singular newline"),
    (terminals.USE_TABLE, "table"),
    (terminals.ID, "table_abc"),
    (terminals.NEWLINE, "newline"),
    (terminals.PARAMETER, "parameter"),
    (terminals.CONNECT, "-->"),
    (terminals.ID, "identifier_1"),
    (terminals.PLUS, "+"),
    (terminals.ID, "identifier_2"),
    (terminals.COMMENT, "bla bla"),
    (terminals.NEWLINE, "newline"),
    (terminals.EOF, "EOF")
]

parser=langparser.LangParser(token_list)
#result = parser.program()

#pprint.pprint(result,width=1)

commands = None
with open("translation_table copy.csc") as fp:
    commands = fp.read()

lexer  = cacos_lexer.CacosLexer()

# remove whitespace
tokens = []
for i in lexer.tokenize(commands):
    if i.token_type == "WHITESPACE":
        continue

    tokens.append(i)

pprint.pprint(tokens)

parser=langparser.LangParser(tokens)
result = parser.program()

pprint.pprint(result,width=1)