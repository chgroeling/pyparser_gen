class AstExpression:
    def __init__(self, expression):
        self.expression = expression

    def __repr__(self):
        return str(self.expression)

    def __getitem__(self, item):
        if item == 0:
            return "AstExpression"
        raise Exception("Index out of bounds!")

class AstId:
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return f"AstId({self.id})"

    def __getitem__(self, item):
        if item == 0:
            return "AstId"
        raise Exception("Index out of bounds!")

class AstReal:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"AstReal({self.value})"

    def __getitem__(self, item):
        if item == 0:
            return "AstReal"
        raise Exception("Index out of bounds!")
    


class AstBinOp:
    def __init__(self, lhs, op, rhs):
        self.lhs = lhs
        self.op = op
        self.rhs = rhs

    def __repr__(self):
        return f"AstBinOp({self.lhs} {self.op} {self.rhs})"

    def __getitem__(self, item):
        if item == 0:
            return "AstBinOp"

        raise Exception("Index out of bounds!")


class AstParameterConnect:
    def __init__(self, parameter, expression):
        self.parameter = parameter
        self.expression = expression

    def __getitem__(self, item):
        if item == 0:
            return "AstParameterConnect"
        raise Exception("Index out of bounds!")


class AstConnect:
    def __init__(self, parameter, expression, comment):
        self.parameter = parameter
        self.expression = expression
        self.comment = comment

    def __repr__(self):
        return f"AstConnect({self.parameter[1]} <-- {self.expression})"

    def __getitem__(self, item):
        if item == 0:
            return "AstConnect"
        raise Exception("Index out of bounds!")


class AstUseTable:
    def __init__(self, table):
        self.table = table

    def __repr__(self):
        return f"AstUseTable('{self.table}')"

    def __getitem__(self, item):
        if item == 0:
            return "AstUseTable"
        raise Exception("Index out of bounds!")
    
def shape_primary_to_ast(parse_tree):
    if parse_tree[0][0]=="ID":
        return AstId(parse_tree[0].value)
    
    if parse_tree[0][0]=="REAL":
        return AstReal(parse_tree[0].value)

    raise Exception(f"Primary unknown")

def shape_add_to_ast(parse_tree):
    if len(parse_tree) == 1:
        if (parse_tree[0][0] == "AstId") or (parse_tree[0][0] == "AstBinOp"):  
            return parse_tree[0]
        raise Exception(f"Only ID allowed {parse_tree}")
    else:
        for i in range(0, len(parse_tree), 3):
            expr = AstBinOp(parse_tree[0], parse_tree[1], parse_tree[2])
    return expr


def shape_mul_to_ast(parse_tree):
    if len(parse_tree) == 1:
        if parse_tree[0][0] == "AstId":
            return parse_tree[0]
        raise Exception(f"Only ID allowed {parse_tree}")
    else:
        for i in range(0, len(parse_tree), 3):
            expr = AstBinOp(parse_tree[0], parse_tree[1], parse_tree[2])
    return expr


def shape_parameter_connect_to_ast(parse_tree):
    terminal, expr = parse_tree
    connect = expr[0]
    assert (connect[0], "CONNECT")
    expression = expr[1]
    expr = AstParameterConnect(terminal, expression)
    return expr


def shape_use_table(parse_tree):
    return AstUseTable(parse_tree[0][1])


def shape_parameter_connect_with_optional_comment_to_ast(parse_tree):
    expr, terminal = parse_tree
    parameter_connect = expr
    comment = terminal
    return AstConnect(
        parameter_connect.parameter, parameter_connect.expression, comment
    )


def simplify_statements(parse_tree):
    assert len(parse_tree) > 0
    if len(parse_tree) == 1:
        if parse_tree[0][0] == "NEWLINE":
            return parse_tree[0]
        if parse_tree[0][0] == "COMMENT":
            return parse_tree[0]

    if len(parse_tree) == 2:
        assert (parse_tree[0][0]) == "AstConnect"
        if parse_tree[1][0] == "NEWLINE":
            return parse_tree[0]

    if len(parse_tree) == 3:
        assert (parse_tree[0][0]) == "USE_TABLE"
        if parse_tree[1][0] == "AstUseTable":
            return parse_tree[1]

    return parse_tree


def simplify_statement_list(parse_tree):
    statements, eof = parse_tree
    res = []

    for i in statements:
        if i[0] != "NEWLINE" and i[0] != "COMMENT":
            res.append(i)
    return (res, eof)
