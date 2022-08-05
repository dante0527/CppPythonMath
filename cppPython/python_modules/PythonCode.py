import re
import string


def printsomething():
    print("Hello from python!")

def PrintMe(v):
    print("You sent me: " + v)
    return 100;

def SquareValue(v):
    return v * v

def MultiplicationTable(num):
    for i in range(10):
        print(f"{num} X {i+1} = {num*(i+1)}")
    return num

def DoubleValue(v):
    return v * 2