# mini quiz
# just if statements and counting score manually

score= 0   # start score, int

q1= input ("capital of france: ")    # dont forget lowercase if checking like this
if q1=="paris" :
   score =score +1    # add 1
else :
   print("nope")    # wrong answer

q2 =input ("2 + 2 = : ")
if q2 == "4" :         # check as string here
    score= score+ 1
else :
    print("wrong again lol")

# need str() to print number score with text
print("your score is " + str(score) )
