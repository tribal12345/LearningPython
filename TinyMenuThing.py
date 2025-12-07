# tiny menu thing
# only basic if, no loops yet so it ends after one choice

print("1 - say hello")
print("2 - show age")
print("3 - quit")   # not real quit just message

choice= input ("choose: ")   # input is string so compare with "1","2","3"

if choice =="1" :
   print("hello there")   # easy
elif choice =="2" :
    age= input ("whats ur age: ")    # dont need int here bc just printing
    print("u are " + age + " years old")
else :
   print("bye")     # default case if not 1 or 2
