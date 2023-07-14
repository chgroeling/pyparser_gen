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
    