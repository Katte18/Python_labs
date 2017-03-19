#Lab. work 2-4 (lists)

#Generate list with lowercase and uppercase alphabet plus numbers
y = ['r','a','d','a','r','L','E','V','E','L','7','8','9']

#Print 1st symbol of list
a = (y[0])
print('The first symbol from list is {}'.format(a))

#Print last symbol
b = (y[-1])
print('The last symbol is {}'.format(b))

#Print 3rd from start and 3rd from the end
c = (y[2])
d = (y[-3])
print('The third symbol from start is {}'.format(c))
print('The third symbol from end is {}'.format(d))

#Slice first 10 symbols
e = (y[:10])
print('The first 10 symbols are {}'.format(e))

#Print only symbols with index, which divides on 2 without remaining
f = y[2::2]
print('The symbols with index divided on 2 {}'.format(f))

#Print only integer values from list

digits = []
for symbol in y:
     try:
         digits.append(int(symbol))
     except ValueError:
         pass

print('Only numbers: {}'.format(digits))

#Reverse text using slice
h = y[::-1]
print('Reverse text: {}'.format(h))

#Convert base list into string
i = str(y)
print('Convert base list into string: {}'.format(i))