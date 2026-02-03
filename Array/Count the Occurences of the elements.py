def count_occurence(mylist,x):
    count = 0
    for item in mylist:
        if item == x:
            count += 1
    return ("{} has occured {} times".format(x, count))


mylist = [20, 30, 20, 4, 20]
x = 40
print(count_occurence(mylist,x))

# Using Count
# print("{} has occured {} times".format(x, mylist.count(x)))

# Using counter
# from collections import Counter
# mylist = [20, 30, 20, 4, 20]
# dict=Counter(mylist)
# print(dict)