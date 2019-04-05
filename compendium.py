### Chapter1. The way of the program
#The first program
print("Hello World")        #Hello World
print("Hello","World")     #Hello World
print("no line break",end="")
43+2                        #47
84/2                        #42.0
6^2                         #4     (XOR: 00000110 ^ 00000010 = 00000100)

#Values and types
type(2)                     #<class 'int'>
type(42.0)                  #<class 'float'>
type('text')                #<class 'str'>

### Chapter2. Variables, expressions and statements
#Keywords in Python
False   class       finally     is          return
None    continue    for         lambda      try
True    def         from        nonlocal    while
and     del         global      not         with
as      elif        if          or          yield
assert  else        import      pass
break   except      in          raise

#PEMDAS
#Parentheses have highest precedence
#Exponentiation: 2**3
#Multiplication & Division have higher precedence than Addition & Subtraction

#Strings
"Hello" + " World"          #Hello World
"Spam" * 3                  #SpamSpamSpam

#Comments
#Comments are most useful when they document non-obvious features of the code.
#It is reasonable to assume that the reader can figure out what the code does;
#it is more useful to explain why.

### Chapter 3. Functions
#casting Variables
int(32.7)
float("34")
str(3.3423)

#Math Functions
import math
math.log10(ratio)
math.sin(radius)
math.pi
math.sqrt

#Definition of Functions
#indention convention: 4 empty spaces
def print_lyrics():
	print("This is the content of my first function")

#function ends with new, non indented line

def functionWithPara(para):
	print(para)

def funtionWithReturnValue():
    a = 5
    return a

#the return value can be None, which is != "None"

### Repetition
for i in range(4):
    print(i)

ct=0
for letter in "banana":
    if letter == "a":
        ct = ct + 1
print("banana contains",a , "* a")
