# Algorithmic Complexity

## Big O

Determine the "Big O" for the problems below:

1. double each number in an array of n numbers.
2. given a number between 0 to 6, return Sunday for 0, Monday for 1, Tuesday for 2, Wednesday for 3, Thursday for 4, Friday for 5, and Saturday for 6.
3. find the result of multiplying each number in an array of n numbers.
4. calculate the multiplication table for the numbers between 0 to n.
5. given an array of basketball players that are sorted by average points per game, find the player who scored exactly 10 points per game, if he exists.
6. find the player in an array whose first name is "LeBron".

## Array Sorting

Choose one of the array sorting algorithms:

* bubble sort
* selection sort
* merge sort
* quick sort

and implement it. You will use Python's lists and pretend they are arrays but you are not allow to use:

1. append()
2. insert()
3. del
4. slicing
5. any other weird stuff other than arr[i], arr[i] = value, and len(arr).

Your function will take in an array argument, and it will sort that array in-place - as in, it will modify the array that is being sorted. For example:

>>> arr = [45, 3, 8, 2, 9, 10, 11]
>>> bubble_sort(arr)
>>> arr
[2, 3, 8, 9, 10, 11, 45]

We will have a competition for who can implement the fastest sort!

## Linked Lists

You will implement code for working with a linked list. The following operations are need to work with a linked list:

1. inserting a node to the head of the list (ll_insert)
2. removing a node from the head of the list (ll_remove)
3. traversing each node in the list (ll_traverse)

You will represent each linked-list node using this class:

class LLNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "LLNode(%r)" % self.data

class LinkedList(object):
    def __init__(self):
        # head will initially point to nothing
        # but will normally point to the first LLNode
        self.head = None

    def insert(self, data):
        "you will implement this"

    def remove(self):
        "you will implement this"

    def traverse(self, fn):
        "you will implement this"

This class is used as follows:

>>> ll = LinkedList()
>>> ll.insert(1)
>>> ll.insert(2)
>>> ll.insert(3)

Now we have a linked list that looks like (the -> represents the link stored by the "next" attribute):

head
   \
   LLNode(3) -> LLNode(2) -> LLNode(1) -> None

### insert

The insert method will insert a new node into the list, after the specified node:

ll.insert(4)

### traverse

The traverse method will traverse each be used as follows:

>>> def print_node(data):
...   print data

>>> ll.traverse(print_node)
4
3
2
1

### remove

The remove method will remove a node for the head (the beginning) of the list:

>>> removed_item = ll.remove()
>>> removed_item
4

Now only the first 3 items remain:

>>> ll.traverse(print_node)
3
2
1

## Hash Tables

You will implement a hash table using an array and linked-lists as its internal data structures. You hash table class will look like this:

class HashTable(object):
    def __init__(self, size=5):
        self.array = [None] * size

    # the hash function: returns an index to the internal array
    # given a string key. This method is used only internally to this class
    # by the get and set methods.
    def hash(self, string):
        "you will implement this"

    # returns the current value for a specified key
    def get(self, key):
        "you will implement this"

    # sets the value for the specified key
    def set(self, key, value):
        "you will implement this"

The hash table is to be used as follows:

table = HashTable()
table.set('Igor', '83837478383')
table.set('Juan', '38473893238')
table.set('Barbara', '78237463743')
table.set('Jordan', '2345718934')
table.set('Derek', '56752934737')
table.set('Manny', '537323323')
table.set('Jorge', '473737438')

print 'Igor', table.get('Igor')
print 'Juan', table.get('Juan')
print 'Barbara', table.get('Barbara')
print 'Jordan', table.get('Jordan')
print 'Derek', table.get('Derek')
print 'Manny', table.get('Manny')
print 'Jorge', table.get('Jorge')

### Bonus: Dictionary-like Syntax

Allow your hash table to be accessed using the same syntax as a dictionary:

table = HashTable()
table['Igor'] = '83837478383'
print 'Igor', table['Igor']

Hint: implement the __getitem__ and __setitem__ methods.
