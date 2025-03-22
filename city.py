## Exercise: Python If Condition
# 1. Using following list of cities per country,
#     ```
#     india = ["mumbai", "banglore", "chennai", "delhi"]
#     pakistan = ["lahore","karachi","islamabad"]
#     bangladesh = ["dhaka", "khulna", "rangpur"]
#     ```
# Write a program that asks user to enter a city name and it should tell which country the city belongs to
india=['mumbai','banglore','chennai','delhi']
pak=['lahore','karachi','islamabad']
bang=['dhaka','khulna','rangpur']
c1=input("Enter the city 1 ")
c2=input("Enter the city 2 ")

if c1 in india and c2  in india:
    print( "both cities aree in India")
elif c1 in pak and c2 in pak:
    print("both cities are in pakistan")
elif c1 in bang and c2 in bang :
    print("both cities are in bangladesh")