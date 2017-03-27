#Lab. work 3-4 (loops)

#Write a program, which takes a year as input and returns message if this is a leap year or note.
#Please handle the exceptions which may arise is a user will enter non-numeric symbols.

while True:
    try:
        y = int(input('Please enter a year: '))
        break
    except ValueError:
        print("Oops!  That was no valid number. Please try again")

if y%4==0 and y%100!=0 or y%400==0:
    print('This is a leap year {}'.format(y))
else:
    print('It is not a leap year')

