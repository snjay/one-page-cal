import ast
import pprint

tree = ast.parse(open('foo.py').read())
# pprint.pprint(ast.dump(tree))  # dumps the whole tree

# get the function from the tree body (i.e. from the file's content)

f = tree.body[0]

# get the function argument names
arguments = [a.arg for a in f.args.args]
print('the functions is: %s(%s)' % (f.name, ', '.join(arguments)))
