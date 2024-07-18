# Define a function hello with the parameter name
def hello(name):
    '''A super simple function'''
    print(f'Hello, {name}')

# Call the function hello
hello('Kitty')

# Define the addition function
def add(x=1, y=[], /, *, z):
    # Add the number 100 to the list y
    y.append(100)
    print(y)

    # Calculate the sum of the numbers contained in x, y, and z
    num = 0
    for i in y:
        num += i

    return x + num + z

# z can only be used as a keyword parameter
print(add(z=1))
# x is used as a positional parameter
print(add(1, z=3))

# Define the multiplication function
def mlp(*nums, **info):
    # Show keyword parameters
    print(info)

    # Calculate the positional parameters contained in nums
    num = 1
    for i in nums:
        num *= i

    return num

# Pass multiple numbers for multiplication
print(mlp(2, 3, 4, 5, tip='Here is a little hint'))

# This function will be overridden by the wait function defined later
def wait(seconds):
    print(f'Wait {seconds} second(s)')

# The first defined wait function is called
wait(3)

# This function overrides the previously defined wait function
def wait(hours, minutes=5):
    print(f'Wait {hours} hour(s) {minutes} minute(s)')

# The last defined wait function is called
wait(3)

# Define the variable message in the module
message = 'I am a module variable'

# The show function defines its own message
def show():
    # This does not modify the message defined by the module
    message = 'I am a variable in the function'
    print(message)

# The show_again function uses the message variable defined by the module
def show_again():
    print(message)

show()
show_again()

# A simple function
def simple(a: int = 1) -> None:
    '''A simple function~~~!

    Sure enough, it's easy.
    '''

# Sums all numbers less than or equal to 10 in a tuple
def add_list(*l):
    # Nested function check, checks a number, returns 0 if greater than 10
    def check(i):
        return 0 if i > 10 else i

    # Call check to ignore numbers greater than 10 in a tuple
    num = 0
    for i in l:
        num += check(i)

    return num

print(add_list(4, 2, 11, 3))

# Define an anonymous functions
div = lambda a, b: a / b

print(div(9, 3))