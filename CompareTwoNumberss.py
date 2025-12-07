# compare two numbers
# remember to turn input to int or it compares as string (bad)

a =input("first number: ")
b= input ("second number: ")

a =int(a)   # i always forget these lol
b= int (b)

if a> b :
   print("first number bigger")
elif b >a :
    print("second number bigger")
else :
   print("they equal")   # only happens if same number
