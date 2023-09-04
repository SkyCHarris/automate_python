# Flow Control

# -'Flow control statements' can decide which Python instructions to execute under which conditions

# Boolean Values

# -Only has two values- 'True' and 'False'

spam = True
print(spam)

true
# >>> Error
True = 2 + 2
# >>> Error

# 1. Boolean values are used in expressions and can be stored in variables
# 2. Python will give you an error message for not using the proper case or for using True/False for variable names

# __________________


# Comparison Operators

# -Comparison operators, also called 'relational operators', compare two values and evaluate down to a single Boolean value

42 == 42
# >>> True
42 == 99
# >>> False
2 != 3
# >>> True
2 != 2
# >>> False

# -The == and != operators can work with values of any data type

'hello' == 'hello'
# >>> True
'hello' == 'Hello'
# >>> False
'dog' != 'cata'
# >>> True
True == True
# >>> True
True != False
# >>> True
42 == 42.0
# >>> True
42 == '42'
# >>> False

# Note: An integer or floating-point value will always be unequal to a string value. 
# -The <, >, <=, and >= operators work properly only with integer and floating-point values

42 < 100
# >>> True
42 > 100
# >>> False
42 < 42
# >>> False
eggCount = 42
eggCount <= 42
# >>> True
myAge = 29
myAge >= 10
# >>> True

# -The == operator (equal to) asks whether two values are the same as each other
# -The = operator (assignment) puts the value on the right into the variable on the left

# _________________

# Boolean Operators

# -The three Boolean operators('and', 'or', 'not') are used to compare Boolean values.
# -Like comparison operators, they evaluate these expressions down to a Boolean value.

# Binary Boolean Operators

# -'and' and 'or' always take two Boolean values (or expressions) and so are considered 'binary' operators
# -'and' operator evaluates an expression to 'True' if both Boolean values are True, otherwise evalutes to False

True and True
# >>> True
True and False
# >>> False

# -'or' operator evalutes an expression to True if either of the two Boolean values is True. If both are False, it evaluates to False

False or True
# >>> True
False or False
# >>> False

# The 'not' Operator

# -The 'not' operator operates on only one Boolean value (or expression). It is a unary operator.
# -'not' operates to the opposite Boolean value

not True
# >>> False
not not not not True
# >>> True

# Mixing Boolean and Comparison Operators

# -Since comparison operators evalute to boolean values, you can use them in expressions with Boolean operators

(4 < 5) and (5 < 6)
# >>> True
(4 < 5) and (9 < 6)
# >>> False
(1 == 2) or (2 == 2)
# >>> True

# -You can use multiple Boolean operators in an expression, along with comparison operators:

2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2
# >>> True

# Boolean Order of Operations:

# 1. not | 2. and | 3. or

# __________________
