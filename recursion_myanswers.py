#1
def print_numbers(end,start = 1):
    if start <= end:
        print start
        print_numbers (end,start+1)

print_numbers(10)





# 2
list = ['Bruce', 'Clark', 'Diana']
def print_names(names):
    print names
    if names > 1:
        print_names(names - 1)

print_names(list)


#Another way
list = ['Bruce', 'Clark', 'Diana']
def say_hello(list, i=0):
    if i< len(list):
        name = list[i]
        print "Hello, %s!" %name
        say_hello(list, i+1)

say_hello(list)


#3
class LLNode(object):
    def __init__ (self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "LLNode(% r)" % self.data

one = LLNode(1)
two = LLNode(2)
three = LLNode(3)
four = LLNode(4)

one.next = two
two.next = three
three.next = four

def ll_lookup(node, target):
    if node:
        if node.data == target:
            return node
        else:
            return ll_lookup(node.next, target)
print ll_lookup(one, 3)
print ll_lookup(one, 5)
print ll_lookup(three, 1)
