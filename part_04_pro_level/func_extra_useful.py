## What are docstrings function ?
## Docstrings means hidden text about function or any method
## how to write docstrings function
## how to see docstrings
## what is help function ?


def add(a,b):
    '''This is about addition about two value where output will be sum of two given values'''
    ## here about text is docstrings
    return a+b

print(add.__doc__) 
print(len.__doc__)  
print(sum.__doc__) 

### help function...>>using help function we can know  actually any fuction how to work 

print(help(sum))