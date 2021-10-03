# %%
import numpy as np
# %%
x = np.arange(2, 11).reshape(3, 3)
y = 3
answer = np.floor(np.divide(x, y))

# %%


# Defining functions
def get_floor(numerator, denomiator):
    f = np.floor(np.divide(numerator, denomiator))
    return f
    print(f)


# Show how things change if we alternate between
# print and return functions
get_floor(x, y)
test = get_floor(x, y)
print(test)

# %%
# Function with a default value


def get_floor(numerator, denomiator=5):
    f = np.floor(np.divide(numerator, denomiator))
    return f
    print(f)


test = get_floor(x, y)
test2 = get_floor(x)

print(test)
print(test2)
# %%
# Adding docstrings


def get_floor2(numerator, denomiator=5):
    """ This is my function

    here are some more longer words about my function

    numerator - is a numpy array
    denomiator - a single number I want to divide by
    """
    f = np.floor(np.divide(numerator, denomiator))
    return f


help(get_floor2)
test = get_floor2(x)
print(test)

# %%
# Function with two outputs


def divide_two_ways(numerator, denomiator=5):
    f_divide = np.floor(np.divide(numerator, denomiator))
    reg_divide = np.divide(numerator, denomiator)
    return f_divide, reg_divide


# Getting the outputs as two separate variables
first, second = divide_two_ways(x, y)

# Getting the outputs as one variable and separating after
both = divide_two_ways(x, y)
first = both[0]
second = both[1]

# %%
