import re

class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

    def __repr__(self):
        if self.token_type=="NEWLINE": # DO NOT PRINT NEWLINE
            return f"{self.token_type}(\\n)"
        
        return f"{self.token_type}({self.value})"

    def __getitem__(self, item):
         if (item ==0):
             return self.token_type
         elif (item ==1):
             return self.value
         else:
             raise Exception("Index out of bounds!")
         
class Lexer:
    def __init__(self, rules):
        self.rules = rules

    # This lexer adds a special token at the end called EOF
    def tokenize(self, input_string):
        tokens = []
        remaining_string = input_string

        while remaining_string:
            matched = False

            for token_type, regex in self.rules.items():
                match = re.match(regex, remaining_string)
                
                if match:
                    #print(match, token_type)
                    value = match.group(0)
                    tokens.append(Token(token_type, value))
                    remaining_string = remaining_string[len(value):]
                    matched = True
                    break
                #print(remaining_string)
            if not matched:
                raise ValueError(f"Unexpected character: {remaining_string[0]}")
            
        # Add EOF Token to indicate the following parser that the end of the token list was reached
        tokens.append(Token("EOF", "\0"))
        return tokens

class CacosLexer:
    def __init__(self):
        rules = {
            "COMMENT" : r'\#.*',                  # Ignore everything until newline
            "REAL" : r'[+-]?([0-9]*[.])?[0-9]+',
            "MULTIPLY" : r'\*',
            "USE_TABLE": r'USE_TABLE',
            "NEWLINE" : r'\n',
            "DOT": r'\.',
            "PARAMETER": r'P\d+\.\d+\.\d+\.\d+',
            "CONNECT": r'(?:<--)',                    # The arrow indicates a connection
            "ID": r'[A-Za-z]+[A-za-z0-9]*',      # LITERALS .. second char can be a decimal
            "WHITESPACE": r'\s+',
        }

        self.__lexer_inst = Lexer(rules)
        
    def tokenize(self, out):
        return self.__lexer_inst.tokenize(out)