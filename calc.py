# add function
def addition(x,y):
    return x + y

# Subtract function
def subtraction(x,y):
    return x - y

# Multiplies function
def multiplication(x, y):
    return x*y

# Division function
def division(x, y):
    try:
       return x/y
    except Exception as e:
        print("Exception:" + str(e))

def power(x, y):
    return x**y