from . import ast

def shape_primary_to_ast(parse_tree):
    if parse_tree[0][0]=="ID":
        return ast.AstId(parse_tree[0].value)
    
    if parse_tree[0][0]=="REAL":
        return ast.AstReal(parse_tree[0].value)

    raise Exception(f"Primary unknown")

def shape_add_to_ast(parse_tree):
    if len(parse_tree) == 1:
        if (parse_tree[0][0] == "AstId") or (parse_tree[0][0] == "AstBinOp"):  
            return parse_tree[0]
        raise Exception(f"Only ID allowed {parse_tree}")
    else:
        for i in range(0, len(parse_tree), 3):
            expr = ast.AstBinOp(parse_tree[0], parse_tree[1], parse_tree[2])
    return expr


def shape_mul_to_ast(parse_tree):
    if len(parse_tree) == 1:
        if parse_tree[0][0] == "AstId":
            return parse_tree[0]
        raise Exception(f"Only ID allowed {parse_tree}")
    else:
        for i in range(0, len(parse_tree), 3):
            expr = ast.AstBinOp(parse_tree[0], parse_tree[1], parse_tree[2])
    return expr


def shape_parameter_connect_to_ast(parse_tree):
    terminal, expr = parse_tree
    connect = expr[0]
    assert connect[0], "CONNECT"
    expression = expr[1]
    expr = ast.AstParameterConnect(terminal, expression)
    return expr


def shape_use_table(parse_tree):
    return ast.AstUseTable(parse_tree[0][1])


def shape_parameter_connect_with_optional_comment_to_ast(parse_tree):
    expr, terminal = parse_tree
    parameter_connect = expr
    comment = terminal
    return ast.AstConnect(
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
