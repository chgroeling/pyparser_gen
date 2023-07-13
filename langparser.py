import terminals

class LangParser:
    def __init__(self, tokens):
        self._current = 0
        self._tokens = tokens

    def isAtEnd(self):
        return self.peek()[0] == terminals.EOF

    def peek(self):
        return self._tokens[self._current]

    def previous(self):
        return self._tokens[self._current - 1]

    def check(self, token_type):
        token = self.peek()
        token_type_r = token[0]
        return token_type == token_type_r

    def advance(self):
        self._current+=1
        return self.previous()
  
    def match(self,token_type):
        if self.check(token_type):
          self.advance()
          return True
 
        return False

    # ===================================================
    # Rules
    # ===================================================    
    
    def primary(self):
        """ primary -> 
               ID | 
               REAL
        """
        
        if self.match(terminals.ID): 
            terminal = self.previous()
            return terminal
        
        if self.match(terminals.REAL): 
            terminal = self.previous()
            return terminal
        
        raise Exception("Rule primary doesn't match")

    def expression(self):
        """ expression -> primary (MULTIPLY primary)*
        """
        res = list()

        expr = self.primary()
        res.append(expr)

        while self.match(terminals.MULTIPLY):
            terminal = self.previous()
            res.append(terminal)
            
            expr = self.primary()
            res.append(expr)

        return res

     
    def connect(self):
        """ connect -> CONNECT expression 
        """

        if self.match(terminals.CONNECT):
            terminal = self.previous()
            expr = self.expression()
            return (terminal, expr)
        else:
            raise Exception()

            
    def parameter(self):
        """ parameter -> PARAMETER connect 
        """

        if self.match(terminals.PARAMETER):
            terminal = self.previous()
            expr = self.connect()
            return (terminal, expr)
        else:
            raise Exception()

            
    def parameter_with_comment(self):
        """ parameter_with_comment -> parameter COMMENT? 
        """
        expr = self.parameter()
        
        if self.match(terminals.COMMENT):
            terminal = self.previous()
            return (expr, terminal)
        else:
            return (expr, None)

    def use_table(self):
        """ use_table -> ID
        """
        if self.match(terminals.ID):
            terminal = self.previous()
            return terminal
        else:
            raise Exception()

    def statement(self):
        """ statement -> 
               NEWLINE | 
               COMMENT |
               USE_TABLE use_table NEWLINE |
               parameter_with_comment NEWLINE
        """
        
        if self.match(terminals.NEWLINE): 
            terminal = self.previous()
            return terminal
        
        if self.match(terminals.COMMENT): 
            terminal = self.previous()
            return terminal
        
        if self.match(terminals.USE_TABLE): 
            terminal_0 = self.previous()
            expr = self.use_table() 
            if self.match(terminals.NEWLINE):
                terminal_1 = self.previous() 
            else:
                raise Exception("Rule statement doesn't match")
                
            return (terminal_0, expr, terminal_1)
        
        expr = self.parameter_with_comment()
        if self.match(terminals.NEWLINE):
            terminal = self.previous() 
            return (expr, terminal)
        raise Exception("Rule statement doesn't match")

    def program(self):
        """ program -> statement* EOF
        """
        res = list()
        if self.match(terminals.EOF):
            terminal = self.previous()
            return ([], terminal)

        expr = self.statement()
        res.append(expr)

        while not self.match(terminals.EOF):
            expr = self.statement()
            res.append(expr)
        terminal = self.previous()
        return (res, terminal)

     

if __name__ == "__main__":
    pass