# program PairedSpecialCharacterCounter
# author Ray Arias
# date 05 September 2020
# description This program opens a text file and counts the paired special characters in it (that is, parentheses,
#             brackets, braces, and quotation marks in the file to see if the open characters (such as "(," ")," "[,"
#             "]," "{," and "}" match up with each other, and if there is an even number of quotation marks, which
#             usually means the quotation marks match up with each other.

# declaration and initialization of all variables
openParentheses = 0
closeParentheses = 0
openBrackets = 0
closeBrackets = 0
openBraces = 0
closeBraces = 0
quotationMarks = 0
totalCount = 0
doubleLessThan = 0
doubleGreaterThan = 0
prevLessThan = False
prevGreaterThan = False
quotesEven = False
ParenthesesMatched = False
BracketsMatched = False
BracesMatched = False
dLTdGTmatched = False
character = "#"

# input and processing
print ("\n")
print ("Welcome to the Paired Special Character Counter by Ray Arias. \n")
filename = input("Enter name of file to read: ")
f = open(filename, 'rt')
while character:
    character = f.read(1)
    totalCount += 1
    if character != '<':
        prevLessThan = False
    if character != '>':
        prevGreaterThan = False
    if character == chr(34):
        quotationMarks += 1
    elif character == '(':
        openParentheses += 1
    elif character == ')':
        closeParentheses += 1
    elif character == '[':
        openBrackets += 1
    elif character == ']':
        closeBrackets += 1
    elif character == '{':
        openBraces += 1
    elif character == '}':
        closeBraces += 1
    elif character == '<':
        if prevLessThan:
            doubleLessThan += 1
            prevLessThan = False
        else:
            prevLessThan = True
    elif character == '>':
        if prevGreaterThan:
            doubleGreaterThan += 1
            prevGreaterThan = False
        else:
            prevGreaterThan = True

# concluding processing
f.close()
quotesEven = (quotationMarks % 2 == 0)
parenthesesMatched = (openParentheses == closeParentheses)
bracketsMatched = (openBrackets == closeBrackets)
bracesMatched = (openBraces == closeBraces)
dLTdGTmatched = (doubleLessThan == doubleGreaterThan)

# output on screen
print ("\n")
print ("File \"" + filename + "\" counted and contains each of the following:")
print ("Total characters in file: " + str(totalCount))
print ("\n         Quotation Marks: " + str(quotationMarks))
if quotesEven:
    print ("      VERY LIKELY MATCH! \n")
else:
    print ("   VERY LIKELY DO NOT MATCH. \n")
print ("       Open parentheses: " + str(openParentheses))
print ("      Close parentheses: " + str(closeParentheses))
if parenthesesMatched:
    print ("     PARENTHESES MATCH! \n")
else:
    print ("    PARENTHESES DO NOT MATCH. \n")
print ("          Open brackets: " + str(openBrackets))
print ("         Close brackets: " + str(closeBrackets))
if bracketsMatched:
    print ("      BRACKETS MATCH! \n")
else:
    print ("    BRACKETS DO NOT MATCH. \n")
print ("            Open braces: " + str(openBraces))
print ("           Close braces: " + str(closeBraces))
if bracesMatched:
    print ("       BRACES MATCH! \n")
else:
    print ("     BRACES DO NOT MATCH. \n")
print ("   Double Less Than << : " + str(doubleLessThan))
print ("Double Greater Than >> : " + str(doubleGreaterThan))
if dLTdGTmatched:
    print ("DOUBLE < AND DOUBLE > MATCH! \n")
else:
    print ("DOUBLE < AND DOUBLE > DO NOT MATCH. \n")

print ("Thank you for using the Paired Special Character Counter by Ray Arias. \n")



