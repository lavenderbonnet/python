# 5th July 2019
# Lilac W.
# Testing switch
# Did you know that the bushy end of a cow's tail is also called a switch

def testSwitch() :
    print (" pythons don't need no switch's because they are not cows")


#def NoSwitchInPython(candy) :
 #    switch(candy) :
 #       case "KitKat" :
 #          print ("Lilac's favorite")
 #           break
 #       case "AlmondJoy" :
 #           print ("Dad's favorite")
 #           break
 #       case "Pokey" :
 #           print ("Coral's favorite")
 #           break
 #       default:
 #           print ("We will eat it anyways as it is chocolate!")
 #           break

def SwitchReplacedByIf(candy):
    if candy == "KitKat" :
       print ("Lilac's favorite")
       
    elif candy == "AlmondJoy":
        print ("Dad's favorite")
        
    elif candy == "Pokey" :
        print ("Coral's Favorite")
        
    else:
        print ("We will eat it anyways since it is candy!")
        

testSwitch()
candy = "Hersheys"
SwitchReplacedByIf(candy)    
