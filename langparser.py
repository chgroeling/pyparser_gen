import terminals
import shapers

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
            return (terminal)
        
        if self.match(terminals.REAL): 
            terminal = self.previous()
            return (terminal)
        
        raise Exception("Rule 'primary' does not match")

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
        return shapers.shape_expression_to_ast(res)
        
    def connect(self):
        """ connect -> CONNECT expression 
        """

        if self.match(terminals.CONNECT):
            terminal = self.previous()
            expr = self.expression()
            return (terminal, expr)
        else:
            raise Exception("Rule 'connect' does not match")

            
    def parameter(self):
        """ parameter -> PARAMETER connect 
        """

        if self.match(terminals.PARAMETER):
            terminal = self.previous()
            expr = self.connect()
            return shapers.shape_parameter_connect_to_ast((terminal, expr))
        else:
            raise Exception("Rule 'parameter' does not match")

            
    def parameter_with_comment(self):
        """ parameter_with_comment -> parameter COMMENT? 
        """
        expr = self.parameter()
        
        if self.match(terminals.COMMENT):
            terminal = self.previous()
            return shapers.shape_parameter_connect_with_optional_comment_to_ast((expr, terminal))
        else:
            return shapers.shape_parameter_connect_with_optional_comment_to_ast((expr, None))
            

    def use_table(self):
        """ use_table -> ID
        """
        if self.match(terminals.ID):
            terminal = self.previous()
            return shapers.shape_use_table((terminal,))
        else:
            raise Exception("Rule '{rule_name}' does not match!")

    def statement(self):
        """ statement -> 
               NEWLINE | 
               COMMENT |
               USE_TABLE use_table NEWLINE |
               parameter_with_comment NEWLINE
        """
        
        if self.match(terminals.NEWLINE): 
            terminal = self.previous()
            return shapers.simplify_statements((terminal,))
        
        if self.match(terminals.COMMENT): 
            terminal = self.previous()
            return shapers.simplify_statements((terminal,))
        
        if self.match(terminals.USE_TABLE): 
            terminal_0 = self.previous()
            expr = self.use_table() 
            if self.match(terminals.NEWLINE):
                terminal_1 = self.previous() 
            else:
                raise Exception("Rule statement doesn't match")
            return shapers.simplify_statements((terminal_0, expr, terminal_1))
        
        expr = self.parameter_with_comment()
        if self.match(terminals.NEWLINE):
            terminal = self.previous()
            return shapers.simplify_statements((expr, terminal))
        raise Exception("Rule 'statement' does not match")

    def program(self):
        """ program -> statement* EOF
        """
        res = list()
        if self.match(terminals.EOF):
            terminal = self.previous()
            return shapers.simplify_statement_list((tuple(), terminal))

        expr = self.statement()
        res.append(expr)

        while not self.match(terminals.EOF):
            expr = self.statement()
            res.append(expr)
        terminal = self.previous()
        return shapers.simplify_statement_list((res, terminal))

     

if __name__ == "__main__":
    pass