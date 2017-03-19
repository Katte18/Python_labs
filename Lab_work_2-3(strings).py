#Lab. work 2-3 (strings)

#Generate string with lowercase and uppercase alphabet plus numbers
z = 'Vacaciones2017'

#Print 1st symbol of string
a = (z[0])
print('The first symbol is {}'.format(a))

#Print last symbol
b = (z[-1])
print('The last symbol is {}'.format(b))

#Print 3rd from start and 3rd from the end
c = (z[2])
d = (z[-3])
print('The third symbol from start is {}'.format(c))
print('The third symbol from end is {}'.format(d))

#Slice first 8 symbols
e = (z[:8])
print('The first 8 symbols are {}'.format(e))

#Print only symbols with index, which divides on 3 without remaining
f = z[3::3]
print('The symbols with index divided on 3 {}'.format(f))

#Print the symbol of the middle of the string text
g = (z[len(z) // 2])
print('The middle symbol of the string is {}'.format(g))

#Reverse text using slice
h = z[::-1]
print('Reverse text: {}'.format(h))