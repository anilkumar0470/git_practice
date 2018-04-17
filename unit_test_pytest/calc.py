import unittest


def add(x,y):
    """Add two values"""
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if y ==0:
        assert y, "Cannot divide by zero"
