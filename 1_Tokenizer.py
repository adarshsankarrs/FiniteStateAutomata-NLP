from dataclasses import dataclass
import string

"""
# The transition states for our Finite State Machine placed in numerical order
"""

REJECT = 0
INTEGER = 1
DECIMAL = 2
NEGATIVE = 3
OPERATOR = 4
STRING = 5
UNKNOWN = 6
SPACE = 7

"""
The Finite State Machine transition state table. The first row (index 0) 
represents a place holder, so the row in the array starts on row 1 instead 
of 0.

This table to make the states accept or reject different parameters, thus 
changing its behavior. More states can be added to this table.
"""

stateTable=[
            [0, INTEGER,  DECIMAL,  NEGATIVE, OPERATOR,  STRING, UNKNOWN,  SPACE],
            [INTEGER,  INTEGER,  DECIMAL,   UNKNOWN, REJECT,   REJECT,  REJECT,  REJECT], # STATE 1
            [DECIMAL,  DECIMAL,  UNKNOWN, UNKNOWN, REJECT,   REJECT,  REJECT,  REJECT], # STATE 2
            [NEGATIVE,  NEGATIVE,  NEGATIVE, UNKNOWN, REJECT,   REJECT,  REJECT,  REJECT], # STATE 3
            [OPERATOR,  REJECT, REJECT,  UNKNOWN, REJECT,   STRING,  REJECT,  REJECT], # STATE 4
            [STRING,    STRING, REJECT,  REJECT, STRING,   STRING,  REJECT,  REJECT], # STATE 5
            [UNKNOWN,  UNKNOWN, UNKNOWN, UNKNOWN,  UNKNOWN, UNKNOWN, UNKNOWN, REJECT], # STATE 6
            [SPACE,     REJECT, REJECT,  REJECT, REJECT,   REJECT,  REJECT,  REJECT] # STATE 7
        ] 

def Lexer(expression):
    #TokenType access
    #access = TokenType("", 0, "")
    access = []
    #tokens = TokenType("", 0, "")
    tokens = []

    currentChar = ' '
    col = REJECT
    currentState = REJECT
    prevState = REJECT
    currentToken = ""

    #print(expression)
    for x in range(0, len(expression)):
        currentChar = expression[x]

        # Get the column number for the current character
        col = Get_FSM_Col(currentChar)
        
        # print(type(col))
        # print(type(currentState))

        # Get the current state of the expression
        currentState = stateTable[currentState][col]

        if(currentState == REJECT):
            if(prevState != SPACE): # Whitespace is not considered
                token = currentToken
                lexeme = prevState
                lexemeName = GetLexemeName(lexeme)
                access = [token, lexeme, lexemeName]

                #print("The current access:", access)

                # Appending to the list of tokens
                tokens.append(access)
            
            # Resetting current token
            currentToken = ""
        
        else: # Moving on to the next character
            currentToken += currentChar
            x = x+1
        prevState = currentState
        #print("The token in this iteration is: ", tokens)

    if(currentState != SPACE and currentToken != ""):
    # Whitespace is not considered
        token = currentToken
        lexeme = currentState
        lexemeName = GetLexemeName(lexeme)
        access = [token, lexeme, lexemeName]

        # Appending to the list of tokens
        tokens.append(access)

    return tokens

def Get_FSM_Col(currentChar):
    
    if(currentChar.isspace()):
        return SPACE

    # Check for integer numbers
    elif(currentChar.isdigit()):
        return INTEGER

    # Check for real numbers
    elif(currentChar == '.'):
        return DECIMAL
    
    # Check if the number is negative
    elif(currentChar == '-'):
        return NEGATIVE

    # Check for characters
    elif(currentChar.isalpha()):
        return STRING

    # Check for operators
    elif(ispunct(currentChar)):
        return OPERATOR
    
    # Return UNKOWN if not identified
    return UNKNOWN

def ispunct(ch):
    # Function to check if punctuation
    return ch in string.punctuation

def GetLexemeName(lexeme):
        if lexeme == INTEGER:
           return "INTEGER"
        elif lexeme == DECIMAL:
           return "DECIMAL"
        elif lexeme == NEGATIVE:
           return "NEGATIVE"
        elif lexeme == OPERATOR:
           return "OPERATOR"
        elif lexeme == STRING:
           return "STRING"
        elif lexeme == UNKNOWN:
           return "UNKNOWN"
        elif lexeme == SPACE:
           return "SPACE"
        else:
           return "ERROR"

def main():
 
    #print("\nPlease enter the name of the file: ")
    fileName = str(input("\nPlease enter the name of the file: "))
    #f = open(fileName, "r")

    # Opening the file
    with open(fileName, 'r', encoding='utf-8') as infile:
        # Reading each line from the file
        for line in infile:
            #print(line)
            tokens = Lexer(line)
            for i in tokens:
                print(i[2]+ " " + i[0])
                #print(i)
            print("\n")
            
    #print(tokens)

if __name__ == "__main__":
    main()