# simple grade thing
# note: the input is string so i gotta turn into int or it wont compare right

grade =input ("enter your grade number: ")
grade = int( grade )   # convert or python cries

if grade>= 90 :
   print("thats a A")     # nice
elif grade >=80 :
    print("thats a B")    # still good
elif grade>= 70 :
     print("thats a C")   # okay i guess
elif grade >=60 :
      print("thats a D")
else :
   print("thats fail bro")  # oh no
