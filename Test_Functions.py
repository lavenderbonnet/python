def awake(time):
    print (">>>>debug : awake function called")
    if 0 < time <= 7 :
        print(" I am sleeping ")
        return False
    else :
        print(" I am awake ")
        return True

def sleep(time) :
    return Not awake(time)
        

def eatMeal(time) :
    print (">>>debug : eat meal called")
    if ( 2 <= time <= 3 ):
        print( "scrumptious sneaky snack")
        return True
    if ( 8 <= time <= 9 ):
        print(" yummy breakfast ")
        return True
    elif ( 12 <= time <= 13 ):
        print(" awesome lunch ")
        return True
    elif ( 18 <= time <= 19 ):
        print(" delicious dinner " )
        return True
    else:
        return False
        

def useUmbrella(weather) :
    if weather == "sunny" :
        print ( "Please don't forget your umbrella")
        return True
    elif weather == "rainy" :
        print ("Don't get wet. Use your umbrella")
        return True
    else :
        print ("No need to take your umbrella")
        return False

#weather = "snowy"
#useUmbrella(weather)

# awake(6)
# awake(8)
# eatMeal(9)
# eatMeal(12)

t = 1
#if awake(t) and eatMeal(t):
if eatMeal(t) and awake(t):
    print ("time to study!")
else:
    print ("still snoozing....")





