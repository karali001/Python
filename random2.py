import random

def getanswer(answernumber):
    if answernumber==1:
        return"boban guzelmııı"
    elif answernumber ==2:
        return "anun guzelmeeee"
    
    elif answernumber ==3:
        return "atbasssss"
    elif answernumber ==4:
        return"molozzzzzz"
    elif answernumber ==5:
        return"sıgurrrr"
    elif answernumber ==6:
        return"terket haburayı"
    elif answernumber ==7:
        return"koyam saa bı doldı"
    elif answernumber ==8:
        return"haburayı terket"
    elif answernumber ==9:
        return"sıcam kafana"

r = random.randint(1,9)

fortune=getanswer(r)
print(fortune)
    
