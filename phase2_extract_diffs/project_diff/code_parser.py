import ast
import re
from itertools import chain
from difflib import SequenceMatcher


class ParseCall(ast.NodeVisitor):
    def __init__(self):
        self.ls = []

    def visit_Attribute(self, node):
        ast.NodeVisitor.generic_visit(self, node)
        self.ls.append(node.attr)

    def visit_Name(self, node):
        self.ls.append(node.id)


class FindFuncs(ast.NodeVisitor):
    def visit_Call(self, node):
        p = ParseCall()
        p.visit(node.func)
        print(".".join(p.ls))
        ast.NodeVisitor.generic_visit(self, node)


# code = 'something = a.b.method(foo() + xtime.time(), var=1) + q.y(x.m())'
# tree = ast.parse(code)
# FindFuncs().visit(tree)


# def func_parser(s, r):
#     t = re.sub(r'\([^()]+\)', '()', s)
#     m = re.findall(r'[\w.]+\(\)', t)
#     t = re.sub(r'[\w.]+\(\)', '', t)
#     if m == r:
#         return
#     for i in chain(m, func_parser(t, m)):
#         yield i
#
#
# def import_similarity(o, n):
#     return SequenceMatcher(None, o, n).ratio()
