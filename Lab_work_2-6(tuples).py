#Lab. work 2-6 (tuples and sets)

#Generate two sets with not unique numbers and few symbols
a = set('abcde823eemnl3')
b = {'V', '2', 'i', 'l', 'l', 'a', '7', '4', '8'}

#Print 1st set
print('The first set is "a": {}'.format(a))
print('The second set is "b": {}'.format(b))

#Create tuple from intersection of first and second set
t1 = tuple(a&b)
print('Intersection t1: {}'.format(t1))

#Create tuple from difference first and second set
t2 = tuple(a-b)
print('Unique value from "a" t2: {}'.format(t2))

#Create tuple from difference second and first set (additional)
t3 = tuple(b-a)
print('Unique value from "b" t3: {}'.format(t3))

#Slice first 3 symbols from first tuple
print('First 3 symbols from "Intersection t1": {}'.format(t1[:3]))

#Print only symbols with numbers from second set
for s in b:
    try:
        print(int(s))
    except ValueError:
        pass

#Reverse tuple using slice
t1 = t1[::-1]
t2 = t2[::-1]

print('Reversed t1: {}'.format(t1))
print('Reversed t2: {}'.format(t2))

#Convert both tuples into list
l1 = list(t1)
l2 = list(t2)

print('List of t1: {}'.format(l1))
print('List of t2: {}'.format(l2))