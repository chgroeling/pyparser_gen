class AstExpression:
    def __init__(self, expression):
        self.expression = expression

    def __repr__(self):
        return str(self.expression)

class AstParameterConnect:
    def __init__(self, parameter , expression):
        self.parameter = parameter
        self.expression = expression

class AstParameterConnectWithOptionalComment:
    def __init__(self, parameter , expression, comment):
        self.parameter = parameter
        self.expression = expression
        self.comment = comment

    def __repr__(self):
        return f"{self.parameter[1]} <-- {self.expression}"

def shape_expression_to_ast(parse_tree):
    expr = AstExpression(parse_tree)
    return expr 

def shape_parameter_connect_to_ast(parse_tree):
    terminal, expr = parse_tree

    _ = expr[0]
    expression = expr[1]
    expr = AstParameterConnect(terminal, expression)
    return expr

def shape_parameter_connect_with_optional_comment_to_ast(parse_tree):
    expr, terminal = parse_tree
    parameter_connect = expr
    comment = terminal
    return AstParameterConnectWithOptionalComment(parameter_connect.parameter, parameter_connect.expression, comment)

def simplify_statements(parse_tree):
    if len(parse_tree)==1:
        if parse_tree[0][0] == "NEWLINE":
            return parse_tree[0]
        if parse_tree[0][0] == "COMMENT":
            return parse_tree[0]
        
    if len(parse_tree)==2:
        assert(type(parse_tree[0]) == AstParameterConnectWithOptionalComment)
        if parse_tree[1][0] == "NEWLINE":
            return parse_tree[0]
    
    return parse_tree

def simplify_statement_list(parse_tree):
    statements, eof = parse_tree
    res = []

    for i in statements:
        if type(i) == AstParameterConnectWithOptionalComment:
            res.append(i)
    return (res, eof)