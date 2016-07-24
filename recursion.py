# -*- coding: utf-8 -*-









# ██████╗ ███████╗ ██████╗██╗   ██╗██████╗ ███████╗██╗ ██████╗ ███╗   ██╗
# ██╔══██╗██╔════╝██╔════╝██║   ██║██╔══██╗██╔════╝██║██╔═══██╗████╗  ██║
# ██████╔╝█████╗  ██║     ██║   ██║██████╔╝███████╗██║██║   ██║██╔██╗ ██║
# ██╔══██╗██╔══╝  ██║     ██║   ██║██╔══██╗╚════██║██║██║   ██║██║╚██╗██║
# ██║  ██║███████╗╚██████╗╚██████╔╝██║  ██║███████║██║╚██████╔╝██║ ╚████║
# ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
#














# Recursion is a bit like loops, they can go on indefinitely.

def go():
    go()

go()













# Actually, you'll get this:
#
#   File "recursion.py", line 32, in go
#     go()
#   File "recursion.py", line 32, in go
#     go()
#   File "recursion.py", line 32, in go
#     go()
#   File "recursion.py", line 32, in go
#     go()
#   File "recursion.py", line 32, in go
#     go()
#   File "recursion.py", line 32, in go
#     go()
#   File "recursion.py", line 32, in go
#     go()
#   File "recursion.py", line 32, in go
#     go()
#   File "recursion.py", line 32, in go
#     go()
#   File "recursion.py", line 32, in go
#     go()
#   File "recursion.py", line 32, in go
#     go()
#   File "recursion.py", line 32, in go
#     go()
#   File "recursion.py", line 32, in go
#     go()
#   File "recursion.py", line 32, in go
#     go()
#   File "recursion.py", line 32, in go
#     go()
# RuntimeError: maximum recursion depth exceeded











# ╔═╗┌┬┐┌─┐┌─┐┌─┐┬┌┐┌┌─┐  ╔═╗┌─┐┌┐┌┌┬┐┬┌┬┐┬┌─┐┌┐┌
# ╚═╗ │ │ │├─┘├─┘│││││ ┬  ║  │ ││││ │││ │ ││ ││││
# ╚═╝ ┴ └─┘┴  ┴  ┴┘└┘└─┘  ╚═╝└─┘┘└┘─┴┘┴ ┴ ┴└─┘┘└┘


def go_n_times(times):
    if times > 0:
        go_n_times(times - 1)



















def hello_n_times(times):
    print "Hello"
    if times > 1:
        hello_n_times(times - 1)

hello_n_times(5)













#
# ╔═╗┬┌┐ ┌─┐┌┐┌┌─┐┌─┐┌─┐┬
# ╠╣ │├┴┐│ ││││├─┤│  │  │
# ╚  ┴└─┘└─┘┘└┘┴ ┴└─┘└─┘┴

# Here is an example of the fibinacci sequence

def fib(n):
    return fib(n - 1) + fib(n - 2)

# except it will run into an infinite loop













# We need a stopping condition, or we get a SO

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)














# Loop through a list using recursion instead of a loop
def print_items(lst, i = 0):
    if i < len(lst):
        print "print_items %r" % lst[i]
        print_items(lst, i + 1)

print_items([1, 2, 3])


# Another example of optional parameters in Python
def hello(subject = 'world'):
    print "Hello, %s!" % subject

hello('Bob')
hello()















class LLNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

# Create the nodes
one = LLNode(1)
two = LLNode(2)
three = LLNode(3)
four = LLNode(4)

# Link the nodes together
one.next = two
two.next = three
three.next = four

def ll_print_items_loop(llnode):
    curr_node = llnode
    while curr_node:
        print "ll_print_items_loop %r" % curr_node.data
        curr_node = curr_node.next

ll_print_items_loop(one)











def ll_print_items(llnode):
    if llnode:
        print "ll_print_items %r" % llnode.data
        ll_print_items(llnode.next)

ll_print_items(one)















class BTreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Create the nodes
two = BTreeNode(2)
one = BTreeNode(1)
three = BTreeNode(3)

# Link them up
two.left = one
two.right = three

def bt_print_items(node):
    if node:
        print "bt_print_items %r" % node.data
        bt_print_items(node.left)
        bt_print_items(node.right)

bt_print_items(two)





#
