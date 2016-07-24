#1
def print_numbers(start, end):
    print end
    if end > 1:
        print_numbers (start, (end-1))

print_numbers(1, 10)





# 2
list = ['Bruce', 'Clark', 'Diana']
def print_names(names):
    print names
    if names > 1:
        print_names(names - 1)

print_names(list)
