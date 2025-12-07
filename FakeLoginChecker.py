# fake login checker
# not real security just practice with if and string compare

user ="admin"   # real website would not do this lol
passw= "1234"

u = input ("username: ")   # everything from input is string
p= input ("password: ")

if u== user :   # check username match
    if p ==passw :         # check password match
        print("login ok")   # both right
    else :
       print("wrong password")   # username right but pass wrong
else :
   print ("wrong username")      # username wrong already
