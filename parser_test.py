import pprint

import langparser.langparser as langparser
import langparser.cacos_lexer as cacos_lexer

commands = None
with open("translation_table.csc") as fp:
    commands = fp.read()

lexer  = cacos_lexer.CacosLexer()

# remove whitespace
tokens = []
for i in lexer.tokenize(commands):
    if i.token_type == "WHITESPACE":
        continue
    tokens.append(i)

parser=langparser.LangParser(tokens)
result = parser.program()

pprint.pprint(result,width=1)