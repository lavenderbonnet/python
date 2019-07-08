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

leftOp = 256978
rightOp = 349687

rAdd = Add(leftOp,rightOp)
rSub = Sub(leftOp,rightOp)
rMul = Mul(leftOp,rightOp)
rDiv = Div(leftOp,rightOp)
print (rAdd, rSub, rMul, rDiv)

leftOp = 2
rightOp = 3

rAdd = Add(leftOp,rightOp)
rSub = Sub(leftOp,rightOp)
rMul = Mul(leftOp,rightOp)
rDiv = Div(leftOp,rightOp)
print (rAdd, rSub, rMul, rDiv)

leftOp = 123456789009123456745678944545680
rightOp = 234567829578436756789639786789

rAdd = Add(leftOp,rightOp)
rSub = Sub(leftOp,rightOp)
rMul = Mul(leftOp,rightOp)
rDiv = Div(leftOp,rightOp)
print (rAdd, rSub, rMul, rDiv)

leftOp =123456789009123456745678947663467587698790778764565342765987907097889678574654545680
rightOp = 1

rAdd = Add(leftOp,rightOp)
rSub = Sub(leftOp,rightOp)
rMul = Mul(leftOp,rightOp)
rDiv = Div(leftOp,rightOp)
print (rAdd, rSub, rMul, rDiv)

# Special Test by zero
print ( Div(1,0) )
#---------------------------------------------------------------------------------------------------------------
