# ---------------------------------------------------------------------------------------------------------------
# 8th July,2019
# LW
# Basic Calculations
# ---------------------------------------------------------------------------------------------------------------
# Functions

def Add(leftOp,rightOp):
    return leftOp + rightOp

def Sub(leftOp,rightOp):
    return leftOp - rightOp

def Neg(op):
    return Mul(-1,op)

def Mul(leftOp,rightOp):
    return leftOp * rightOp

def Div(dividend,divisor):
    # TODO : Check for zero
    return dividend / divisor
    
# ---------------------------------------------------------------------------------------------------------------
# Tests
# Addition

Ans = Add(256978,349687)
print (Ans)

Ans = Add(2,3)
print (Ans)

Ans = Add(123456789009123456745678944545680,234567829578436756789639786789)
print (Ans)


Ans = Add(123456789009123456745678947663467587698790778764565342765987907097889678574654545680,1)
print (Ans)


#---------------------------------------------------------------------------------------------------------------
