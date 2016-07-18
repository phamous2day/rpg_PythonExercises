def bubbleSort(my_array):
    for pass_number in range(len(my_array)-1,0,-1):
        print "This is pass_number, round: %r" % pass_number

        for i in range(pass_number):
            if my_array[i]>my_array[i+1]:
                temp = my_array[i]
                my_array[i] = my_array[i+1]
                print "my_array[i] is %r" %(my_array[i])
                my_array[i+1] = temp
                
my_array = [54,26,93,17,77,31,44,55,20]
bubbleSort(my_array)
print(my_array)
