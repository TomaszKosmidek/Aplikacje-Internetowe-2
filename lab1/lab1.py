# Hello World
print("Hello, World!")

# Printing
a = '  |  |\n'
print(a, a, a, sep='--------\n', end='\n')

# Printing #2
for i in range(1, 18):
    if i % 6 == 0:
        print('========+========+========')
    elif i % 2 == 0:
        print('--+--+--H--+--+--H--+--+--')
    else:
        print('  |  |  H  |  |  H  |  |  ')

# Fizz, Buzz, FizzBuzz!
x = 0
for i in range(1, 1001):
    if i % 3 == 0 or i % 5 == 0:
        x = x + i
print(x)

# Collatz Sequence
def collatz(number):
    x = number
    counter = 1
    while x != 1:
        if x % 2 == 0:
            x = x/2
            counter += 1
        else:
            x = 3*x+1
            counter += 1
    return counter, number

def find(border):
    max = (0,0)
    while border != 1:
       test = collatz(border)
       if test > max:
           max = test
       border -= 1
    return max

i = find(1000000)
print('Ilość stanów:', i[0], '  liczba:', i[1])

# Fahrenheit-to-Celsius converter
fahrenheit = input('Temperature F? ')
print("It is ", round((float(fahrenheit) - 32) * 5/9, 2), " degrees Celsius.")
