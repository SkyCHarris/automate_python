# Elements of Flow Control

# -Flow control statements often start with a 'condition' and are followed by a block of code called the 'clause'

# Conditions

# -Conditions are basically expressions, and always evaluate down to a Boolean value: True or False

# Blocks of Code

# -Lines of python code can be grouped together in blocks. Three rules:

# 1. Blockcs begin when the indentation increases
# 2. Blockcs can contain other blocks
# 3. Blocks end when the indentation decreases to zero ro to a containing block's indentation

name = 'Mary'
password = 'swordfish'
if name == 'Mary' :
    print('Hello, Mary')
    if password == 'swordfish':
        print('Access granted.')
    else:
        print('Wrong password.')

# Program Execution

# -Not all programs execute from top to bottom

# Flow Control Statements

# if Statements

# -An if statement's clause will execute if the statement's condition is True, and skipped if the condition is False
# -An if satement consists of the following:
# 1. The 'if' keyword
# 2. A condition (an expression that evalutes to True or False)
# 3. A colon
# 4. Starting on the next line, an indented block of code (the if clause)

if name == 'Alice':
    print('Hi, Alice.')

# else Statements

# -An if clause can optionally be followed by an else statement. It only executes when the if statement's condition is False
# -else statements always consist of the following:
# 1. The else keyword
# 2. A colon
# 3. Starting on the next line, an indented block of code (the else clause)

if name == 'Alice':
    print('Hello, Alice')
else:
    print('Hello, stranger.')

# elif Statements

# -You may have a case where you want one of many possible clauses to execute
# -The elif statement (else if statement) always follows an if or another elif statement.
# -It provides another condition that is checked only if all previous conditions were False.
# -elif statements always consist of the following:
# 1. The elif keyword
# 2. A condition (an expression that evalutes to True or False)
# 3. A colon
# 4. Starting on the next line, an indented block fo code (the elif clause)

if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')

# -When there is a chain of elif statements, only one or none of the clauses will be executed
# -When one of the statements' conditions is found to be True, the rest of the elif clauses are automatically skipped

name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')

# -Optionally, you can have an else statement after the last elif statement

name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')
