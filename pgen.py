import jinja2
import pathlib
import sys
from collections import namedtuple


OrParameter = namedtuple("OrParameter", "terminal nonterminal optionalterminal")
TerminalParameter = namedtuple("TerminalParameter", "terminal")
NonTerminalParameter = namedtuple("NonTerminalParameter", "nonterminal")
NonTerminalTerminalParameter = namedtuple(
    "NonTerminalParameter", "nonterminal, terminal"
)

RULES = [
    [
        "primary",
        "shape_primary_to_ast",
        "or_rule.jinja",
        [OrParameter("ID", None, None), OrParameter("REAL", None, None), None],
    ],
    [
        "multiply",
        "shape_mul_to_ast",
        "nonterminal_list_with_delimiter_rule.jinja",
        [NonTerminalParameter("primary"), TerminalParameter("MULTIPLY")],
    ],
    [
        "expression",
        "shape_add_to_ast",
        "nonterminal_list_with_delimiter_rule.jinja",
        [NonTerminalParameter("multiply"), TerminalParameter("ADD")],
    ],
    [
        "connect",
        None,
        "lhs_unary_rule.jinja",
        [
            TerminalParameter("CONNECT"),
            NonTerminalParameter("expression"),
        ],
    ],
    [
        "parameter",
        "shape_parameter_connect_to_ast",
        "lhs_unary_rule.jinja",
        [
            TerminalParameter("PARAMETER"),
            NonTerminalParameter("connect"),
        ],
    ],
    [
        "parameter_with_comment",
        "shape_parameter_connect_with_optional_comment_to_ast",
        "rhs_optional_terminal.jinja",
        [
            NonTerminalParameter("parameter"),
            TerminalParameter("COMMENT"),
        ],
    ],
    [
        "use_table",
        "shape_use_table",
        "consume_rule.jinja",
        [TerminalParameter("ID")],
    ],
    [
        "statement",
        "simplify_statements",
        "or_rule.jinja",
        [
            OrParameter("NEWLINE", None, None),
            OrParameter("COMMENT", None, None),
            OrParameter("USE_TABLE", "use_table", "NEWLINE"),
            NonTerminalTerminalParameter("parameter_with_comment", "NEWLINE"),
        ],
    ],
    [
        "program",
        "simplify_statement_list",
        "nonterminal_list_rule.jinja",
        [NonTerminalParameter("statement"), TerminalParameter("EOF")],
    ],
]


class TemplateRenderer:
    def __init__(self, template_dir, filters=dict()):
        assert isinstance(template_dir, pathlib.PurePath)

        self._template_loader = jinja2.FileSystemLoader(searchpath=template_dir)
        self._template_env = jinja2.Environment(loader=self._template_loader)

        for key, value in filters.items():
            self._template_env.filters[key] = value

    def get_template(self, template_file):
        assert isinstance(template_file, pathlib.PurePath)

        posix_template_file = template_file.as_posix()
        return self._template_env.get_template(posix_template_file)


if __name__ == "__main__":
    tr = TemplateRenderer(pathlib.PurePath("./templates"))

    template = tr.get_template(pathlib.PurePath("lang_parser.jinja"))

    rules = []
    for i in RULES:
        rule_name = i[0]
        rule_shaper = i[1]
        rule_def = i[2]
        p = i[3]
        rule_template = tr.get_template(pathlib.PurePath(rule_def))
        rules.append(
            rule_template.render(shaper=rule_shaper, rule_name=rule_name, p=p)
        )
    buf = template.render(rules=rules)
    with open("langparser.py", "w") as fp:
        fp.write(buf)
