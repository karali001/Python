defkullanıcı="ısılnazboku"
defparola="ahadasıctıamınyum"

kullanıcı=input("kullanıcı adı:")
parola=input("parolanuz:")


if((defkullanıcı==kullanıcı) and (defparola==parola)):
    print("sal kendunu bana")
elif((defkullanıcı!=kullanıcı) and (defparola==parola)):
   print("ısılnaz bokmusun aq kullanıcını bılmeyısun")
elif((defkullanıcı==kullanıcı) and (defparola!=parola)):
    print("sıktır yavsakkkk")
else:
    print(" boka bak devam edeyı")
                  
