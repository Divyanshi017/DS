# 4. Lets say you are running a 5 km race. Write a program that,
#    1. Upon completing each 1 km asks you "are you tired?"
#    2. If you reply "yes" then it should break and print "you didn't finish the race"
#    3. If you reply "no" then it should continue and ask "are you tired" on every km
#    4. If you finish all 5 km then it should print congratulations message
for i in range(5):
    print((i+1)," miles run")
    t=input("Are you tired?"'\n')
    if t=='yes':
        break
if i==4:
    print("Race finished")
else:
    print("You didn't finish the race")